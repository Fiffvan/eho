LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ эхо-бот для демонстрации работы роутеров!\n\n'
              'Если хотите - можете мне что-нибудь прислать или '
              'отправить команду /help',
    '/help': 'Я просто отправляю вам копию вашего сообщения',
    '/echo': 'Подключен модуль «Эхо-бот».\nЕсли хотите - можете мне что-нибудь прислать',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
'text_echo': 'Вы отправили текст',
    'photo_echo': 'Вы отправили фото',
    'video_echo': 'Вы отправили видео',
    'audio_echo': 'Вы отправили аудио',
    'sticker_echo': 'Вы отправили стикер',
    'video_note_echo': 'Вы отправили видеозаметку',
    'document_echo': 'Вы отправили документ',
    'voice_echo': 'Вы отправили голосовое сообщение',
    'animation_echo': 'Вы отправили анимацию'

}

surveys = [
    {"question": "Часто ли вы опаздываете?", "options": ["Да", "Нет"]},
    {"question": "Вы были отличником в школе?", "options": ["Да", "Нет"]},
    {"question": "Вы занятой человек?", "options": ["Да", "Нет"]}
]

quizs = [
    {"question": "Сколько субъектов в РФ?", "options": ["80", "85", "63"], "correct_otvet": 1},
    {"question": "Столица РФ?", "options": ["Москва", "Брянск",],
     "correct_otvet": 0},
    {"question": 'Кто написал "Горе от ума"?', "options": ["Пушкин", "Грибоедов", "Не знаю"], "correct_otvet": 1}
]

quizs2 = [
    {"question": "Какой спутник у планеты Земля?", "options": ["Луна", "Марс", "Несквик"], "correct_otvet": 0},
    {"question": "Кто создал Linux?",
     "options": ["Линус Торвальдс", "Билл Гейтс", "Павел Дуров"], "correct_otvet": 0},
    {"question": "Кто написал 'Претсупление и наказание'?", "options": ["Достоевский", "Толстой", "Пушкин"], "correct_otvet": 0}
]
