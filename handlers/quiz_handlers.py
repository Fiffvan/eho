from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU, quizs, quizs2 
from database.database import user_progress
from handlers.user_handlers import kb_builder, keyboard

router = Router()

async def quiz_question(message: Message, step: int, quiz_list):
    quiz = quiz_list[step]
    kb = ReplyKeyboardBuilder().row(*(KeyboardButton(text=opt) for opt in quiz["options"])).as_markup(
        resize_keyboard=True)
    await message.answer(quiz["question"], reply_markup=kb)


@router.message(lambda message: message.text == 'Пройти викторину 1')
async def start_quiz_1(message: Message):
    user_progress[message.from_user.id] = {"quiz_step": 0, "correct_answers": 0, "current_quiz": 'quiz1'}
    await quiz_question(message, 0, quizs)

@router.message(lambda message: message.text == 'Пройти викторину 2')
async def start_quiz_2(message: Message):
    user_progress[message.from_user.id] = {"quiz_step": 0, "correct_answers": 0, "current_quiz": 'quiz2'}
    await quiz_question(message, 0, quizs2)

@router.message(
    lambda message: message.from_user.id in user_progress and ("quiz_step" in user_progress[message.from_user.id]))
async def handle_quiz_answer(message: Message):
    user_id = message.from_user.id
    step = user_progress[user_id]["quiz_step"]

    if user_progress[user_id]["current_quiz"] == 'quiz1':
        quiz_list = quizs
    else:
        quiz_list = quizs2

    correct_option = quiz_list[step]["options"][quiz_list[step]["correct_otvet"]]

    if message.text == correct_option:
        user_progress[user_id]["correct_answers"] += 1
        await message.answer("Правильно")
    else:
        await message.answer(f"Неправильно! Правильный ответ: {correct_option}")

    if step + 1 < len(quiz_list):
        user_progress[user_id]["quiz_step"] += 1
        await quiz_question(message, user_progress[user_id]["quiz_step"], quiz_list)
    else:
        correct_count = user_progress[user_id]["correct_answers"]
        await message.answer(f"Викторина завершилась. У вас {correct_count} правильных ответов из 3.", reply_markup=keyboard)
        # Удаляем данные викторины
        user_progress.pop(user_id, None)

if __name__ == '__main__':
    dp.run_polling(bot)