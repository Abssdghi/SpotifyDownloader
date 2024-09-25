import telebot, Spotify_download

def link_to_id(link):    
    link=link[::-1]
    result = ""
    for i in link:
        if (i == "/") and (len(result) != 0):
            return result[::-1]
        result+=i


token = "BOT_TOKEN"
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: True)
def spotify_bot(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Send Spotify music link! ")
        return
    try:
        song_info = Spotify_download.get_song_info(link_to_id(message.text))
        if (song_info['success'] == True) and (song_info['statusCode'] == 200):
            cover_caption = f"{song_info['metadata']['title']} by {song_info['metadata']['artists']}\nAlbum: {song_info['metadata']['album']}\nRelease Date: {song_info['metadata']['releaseDate']}"
            bot.send_photo(chat_id=message.chat.id, photo=song_info['metadata']['cover'], caption=cover_caption)
            bot.send_audio(chat_id=message.chat.id, audio=Spotify_download.link_to_mp3(song_info['link']))
        else:
            bot.send_message(message.chat.id, f'ERROR:\n{song_info}\nTry again!')
    except Exception as e:
        bot.send_message(message.chat.id, f'ERROR:\n{e}\nTry again!')

if __name__ == '__main__':
    print("i'm alive!")
    bot.polling(none_stop=True)
