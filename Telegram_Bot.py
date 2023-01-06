#Hello bitches

#Libraries and shit
from __future__ import unicode_literals
import telegram
import requests
import praw
import html
import os
from time import sleep
from datetime import datetime

print("We got here")

#Important bs

credentials = {}

credentials["token"] ="5944534549:AAGI8YaTj3_P5YgMy-FMalVbfGUS1VNHneg"
credentials["subreddit"] = "https://reddit.com/r/Genshin_impact_leaks"
credentials["channel"] = "https://t.me/genshinimpact_leakschannel"
token = credentials["token"]
channel = credentials["channel"]
sub = "Genshin_Impact_Leaks"
start_time = datetime.utcnow().timestamp()

print("and now here")

r = praw.Reddit(user_agent="Genshin Impact Leaks",
                client_id="kLXmbgYfFp_OcaKKmqBGTg",
                client_secret="4c33RFT8i2Iub6LEU35w2pV49QGA0g",
                username="STDeveloper",
                password="ringof666timeup")
r.read_only = True
subreddit = r.subreddit(sub)

bot = telegram.Bot(token=token)

print("gonna end soon")


def post_to_telegram():
  try:
    for submission in subreddit.hot():
      image = html.escape(submission.url or '')
      title = html.escape(submission.title or '')
      link = "https://redd.it/{id}".format(id=submission.id)
      template = "{title}\n\n Channel: @Genshinimpact_leakschannel"
      message = template.format(title=title, link=link)
      r = requests.get('https://api.telegram.org/bot{}/sendPhoto'.format(
        token),
                       json={
                         "chat_id": channel,
                         "photo": image,
                         "caption": message
                       })
      if r.ok:
        bot.sendPhoto(chat_id=channel, photo=image, caption=message)
        print("Posted. Check your channel")
        #sleep(600)
  except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)

while True:
  post_to_telegram()
