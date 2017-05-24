# -*- coding: utf-8 -*-
import vk
import os
import telebot
from telebot import types

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot('350195599:AAEJ-5wyPdVVGMd45eps91nFavtoey3Bla0')
session = vk.Session()
api = vk.API(session)


@bot.inline_handler(lambda query: 'vk.com' in query.query)
def query_text(inline_query):
    try:
        if 'wall' in inline_query.query:
            urldata = inline_query.query.split('wall')
            wallpost = api.wall.getById(posts=urldata)
            result = 1
            gifs = []
            if wallpost[0]['attachments']:
                for attach in wallpost[0]['attachments']:
                    if 'doc' in attach:
                        if attach['doc']['ext'] == 'gif' or '.gif' in attach['doc']['title']:
                            gifs.append(types.InlineQueryResultGif(gif_url=attach['doc']['url'],
                                                                   thumb_url=attach['doc']['thumb_s'],
                                                                   id=str(result)))
                            result = result + 1

                bot.answer_inline_query(inline_query.id, gifs)
    except Exception as e:
        print(e)


bot.polling(none_stop=True)
