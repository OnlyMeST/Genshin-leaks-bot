import praw
import telegram
from telegram.ext import Updater, CommandHandler

def fetch_posts(subreddit):
  # Set up the Reddit client
  reddit = praw.Reddit(client_id='HDSU8U37RX-E88ev4hyqtw', client_secret='L8NRPbciXya3-XftyxBjeU0HSebvsA', user_agent='Genshin Leaks bot')

  # Fetch the top posts from the subreddit
  posts = reddit.subreddit(subreddit).new(limit=10)

  return posts

def send_posts(bot, posts, channel_id):
  # Use the bot to send the posts to the specified channel
  for post in posts:
    message = f"{post.title}\nJoin : @Jenshin_Leaks"
    bot.send_message(channel_id, message)

def start(bot, update):
  # Fetch the posts and send them to the channel
  posts = fetch_posts('r/Genshin_Impact_Leaks')
  send_posts(bot, posts, '@Jenshin_Leaks')

def main():
  # Set up the Telegram bot
  bot = telegram.Bot(token='5944534549:AAGI8YaTj3_P5YgMy-FMalVbfGUS1VNHneg')
  updater = Updater(bot=bot)
  handler = CommandHandler('start', start)
  updater.dispatcher.add_handler(handler)
  updater.start_polling()

if __name__ == '__main__':
  main()
