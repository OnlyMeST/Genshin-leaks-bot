#Hello bitches

#Libraries and shit
from __future__ import unicode_literals
import telegram
import praw
import logging
import html
import sys
import os
import json
from time import sleep
from datetime import datetime

#Important bs

credentials = {}

credentials["token"] = os.environ.get('5944534549:AAGI8YaTj3_P5YgMy-FMalVbfGUS1VNHneg')
credentials["subreddit"] = os.environ.get('https://www.reddit.com/r/Genshin_Impact_Leaks')
credentials["channel"] = os.environ.get('https://t.me/GenshinImpact_Leakschannel')

token = credentials["token"]
channel = credentials["channel"]
sub = "Genshin_Impact_Leaks"
start_time = datetime.utcnow().timestamp()

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

if credentials["token"] == "":
    raise RuntimeError('Bot token not found')
if credentials["subreddit"] == "":
    raise RuntimeError('Subreddit name not found ')
if credentials["channel"] == "":
    raise RuntimeError('Telegram Channel name not found ')

def prev_submissions():
    try:
        with open('prev_submissions.id', 'r') as f:
            return f.read().strip()
    except:
        return None

def write_submissions(sub_id):
    try:
        with open('prev_submissions.id', 'w') as f:
            f.write(sub_id)
    except:
        log.expection("Error writing sub ID!")

post = False
last_sub_id = prev_submissions()

if not last_sub_id:
    log.info("Latest submission not found, starting all submissions!")
    post = True
else:
    log.info("Last posted submission is {}".format(last_sub_id))

r = praw.Reddit(user_agent="Genshin Impact Leaks",
                client_id=os.environ.get('kLXmbgYfFp_OcaKKmqBGTg'),
                client_secret=os.environ.get('4c33RFT8i2Iub6LEU35w2pV49QGA0g'),
                username=os.environ.get('STDeveloper'),
                password=os.environ.get('ringof666timeup'))
r.read_only = True
subreddit = r.subreddit(sub)

bot = telegram.Bot(token=token)

while True:
    try:
        for submission in subreddit.hot():
            try:
                link = "https://redd.it/{id}".format(id=submission.id)
                if not post and submission.created_utc < start_time:
                    log.info("Skipping {} --- latest submission not found!".format(submission.id))
                    if submission.id == last_sub_id:
                        post = True
                    continue
                image = html.escape(submission.url or '')
                title = html.escape(submission.title or '')
                user = html.escape(submission.author.name or '')

                template = "{title}\n{link}\nby {user}"
                message = template.format(title=title, link=link, user=user)

                log.info("Posting {}".format(link))
                bot.sendPhoto(chat_id=channel, photo=submission.url, caption=message)
                write_submissions(submission.id)
                sleep(600)
            except Exception as e:
                log.exception("Error parsing {}".format(link))
    except Exception as e:
        log.exception("Error fetching new submissions, restarting in 10 secs")
        sleep(10)

