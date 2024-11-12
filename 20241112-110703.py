import telebot
from pytube import YouTube

# Replace with your Telegram bot token
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a song name or a voice message to play music.")

@bot.message_handler(content_types=['text', 'voice'])
def handle_message(message):
    if message.content_type == 'text':
        query = message.text
    elif message.content_type == 'voice':
        # Process voice message to text using a speech-to-text service (e.g., Google Speech-to-Text)
        query = process_voice_message(message.voice.file_id)

    try:
        # Search and download the audio stream
        yt = YouTube(f"https://www.youtube.com/results?search_query={query}")
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename='temp.mp3')

        # Send the audio file to the user
        with open('temp.mp3', 'rb') as f:
            bot.send_voice(message.chat.id, f)
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

# Start the bot
bot.polling()
