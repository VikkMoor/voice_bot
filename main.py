import telebot

from telebot import types

from config import BOT_TOKEN
from voice import get_voices, generate_audio

bot = telebot.TeleBot(BOT_TOKEN)

voices = get_voices()

user_voice = {}


@bot.message_handler(commands=['start'])
def start_command(message):

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    for voice in voices[:5]:
        keyboard.add(
            types.KeyboardButton(voice.name)
        )

    bot.send_message(
        message.chat.id,
        'Привет! Выбери голос для озвучки 🎤',
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):

    selected_voice = None

    for voice in voices:

        if message.text == voice.name:
            selected_voice = voice

    if selected_voice:

        user_voice[message.chat.id] = {
            'voice_id': selected_voice.voice_id,
            'voice_name': selected_voice.name
        }

        bot.send_message(
            message.chat.id,
            f'Ты выбрала голос: {selected_voice.name}\n'
            f'Теперь отправь текст для озвучки.'
        )

    else:

        if message.chat.id not in user_voice:

            bot.send_message(
                message.chat.id,
                'Сначала выбери голос.'
            )

            return

        voice_id = user_voice[message.chat.id]['voice_id']

        bot.send_message(
            message.chat.id,
            'Генерирую озвучку...'
        )

        output_path = f'generated/{message.chat.id}.mp3'

        generate_audio(
            text=message.text,
            voice_id=voice_id,
            output_path=output_path
        )

        with open(output_path, 'rb') as audio:

            bot.send_audio(
                message.chat.id,
                audio
            )


if __name__ == '__main__':

    print('Бот запущен...')

    bot.infinity_polling()