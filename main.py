import praw
import telegram
import os

reddit = praw.Reddit(client_id='lWARc9TxLMS3XG04JLbHBw',
                     client_secret='x6l5-ezVxyIE5vNYYqYNnr_pbGOLfw',
                     user_agent='Genshin-Leaks',
                     redirect_uri='http://localhost:8080')

bot = telegram.Bot(token='5944534549:AAGI8YaTj3_P5YgMy-FMalVbfGUS1VNHneg')
chat_id = '1515286332'

subreddit_name = 'Genshin_Impact_Leaks'

last_post_id = ''

while True:
    try:
        # Fetch the newest posts from the subreddit
        subreddit = reddit.subreddit(subreddit_name)
        new_posts = subreddit.new(limit=10)

        # Loop through the new posts and post them to Telegram
        for post in new_posts:
            if post.id != last_post_id:
                if post.url.endswith('.jpg') or post.url.endswith('.jpeg') or post.url.endswith('.png'):
                    bot.send_photo(chat_id=chat_id, photo=post.url, caption=post.title)
                elif post.url.endswith('.gif') or post.url.endswith('.mp4'):
                    bot.send_video(chat_id=chat_id, video=post.url, caption=post.title)
                else:
                    bot.send_message(chat_id=chat_id, text=post.url)

                last_post_id = post.id

        time.sleep(60)

    except Exception as e:
        print(e)
