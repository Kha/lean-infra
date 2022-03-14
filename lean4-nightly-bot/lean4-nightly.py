#!/usr/bin/env python3

import os
import sys
import datetime
import re

import tweepy
from github import Github

def main():
    client = tweepy.Client(consumer_key=os.getenv("CONSUMER_KEY"),
                           consumer_secret=os.getenv("CONSUMER_SECRET"),
                           access_token=os.getenv("ACCESS_TOKEN"),
                           access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))
    r = Github().get_repo("leanprover/lean4-nightly").get_releases()[0]
    d = datetime.date.today().isoformat()
    if r.tag_name.endswith(d):
        lines = r.body.splitlines()[1:]
        lines = lines[:lines.index("*Full commit log*")]
        body = "\n".join(lines).strip()
        prev = None
        for bullet in re.split(r"^\* ", body, flags=re.MULTILINE):
            if bullet:
                limit = 280 - 10  # for unclear reasons
                LINK_LEN = 23
                if not prev:
                    limit -= 23 + len("\n\n")
                if len(bullet) >= limit:
                    bullet = bullet[:limit - len(" [...]")] + " [...]"
                if not prev:
                    bullet += "\n\n" + r.html_url
                resp = client.create_tweet(text=bullet, in_reply_to_tweet_id=prev)
                prev = resp.data['id']

if __name__ == '__main__':
    main()
