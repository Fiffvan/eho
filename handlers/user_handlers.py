from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from database.database import user_progress

# Инициализируем роутер уровня модуля
router = Router()

kb_builder = ReplyKeyboardBuilder()
kb_builder.row(KeyboardButton(text='Пройти опрос'), KeyboardButton(text='Пройти викторину 1'),
               KeyboardButton(text='Пройти викторину 2'), width=3)
keyboard = kb_builder.as_markup(resize_keyboard=True)


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет! Нажмите кнопку, чтобы пройти опрос или викторину.', reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)