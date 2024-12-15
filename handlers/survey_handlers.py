from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU, surveys 
from database.database import user_progress
from handlers.user_handlers import kb_builder, keyboard

router = Router()

async def survey_question(message: Message, step: int):
    survey = surveys[step]
    await message.answer(survey["question"])

@router.message(lambda message: message.text == 'Пройти опрос')
async def start_survey(message: Message):
    user_progress[message.from_user.id] = {"survey_step": 0}
    await survey_question(message, 0)

@router.message(
    lambda message: message.from_user.id in user_progress and "survey_step" in user_progress[message.from_user.id])
async def handle_survey_answer(message: Message):
    user_id = message.from_user.id
    step = user_progress[user_id]["survey_step"]
    user_progress[user_id].setdefault("survey_answers", []).append(message.text)

    if step + 1 < len(surveys):
        user_progress[user_id]["survey_step"] += 1
        await survey_question(message, user_progress[user_id]["survey_step"])
    else:
        await message.answer("Спасибо за участие!", reply_markup=keyboard)
        # Удаляем данные опроса
        user_progress.pop(user_id, None)