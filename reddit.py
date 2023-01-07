
import os

from dotenv import load_dotenv
import praw

load_dotenv()

def authenticate():
    return praw.Reddit("Genshin leaks", user_agent="Genshin Leaks bot")


def get_posts(reddit):
    posts = reddit.subreddit(os.getenv('sub')).new(limit=20)
    return list(posts)


def main():
    reddit = authenticate()
    subs = get_posts(reddit)
    x = subs[0]
    import pprint
    pprint.pprint(x.url)


if __name__ == '__main__':
    main()
