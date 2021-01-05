#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
# Coded with ❤️ by Neranjana Prasad (@NandiyaLive)


from instaloader import Instaloader
import shutil
import glob
import os
from telegram import Bot
from flask import Flask

bot = Bot(token="1390442245:AAE0gsdbzA7BMau5DgMVfU_hHwLorJOt_dw")
chat_id = "pabllovit"
user_ids = ["carlos", "beyonce","badgalriri"]
src_dir = "/storage/emulated/0/botinstagram"
USER = "privad0dix"
PASSWORD = "ladygaga"

app = Flask(__name__)

L = Instaloader(dirname_pattern=src_dir, download_comments=False,
                download_video_thumbnails=False, save_metadata=False, download_geotags=True, compress_json=True, post_metadata_txt_pattern=None, storyitem_metadata_txt_pattern=None)


@app.route('/download', methods=['GET', 'POST'])
def job():
    try:
        L.download_stories(userids=user_ids)

        for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
            bot.send_photo(chat_id, photo=open(jpgfile, 'rb'))

        for vidfile in glob.iglob(os.path.join(src_dir, "*.mp4")):
            bot.send_video(chat_id, video=open(vidfile, 'rb'))

        try:
            shutil.rmtree(src_dir)
        except Exception:
            pass
        return 'Download Success'

    except:
        L.login(USER, PASSWORD)
        job()
