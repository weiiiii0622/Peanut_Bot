from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

import re

from .flex_msg import Flex_MainMenu
from .equation import two_var_equation

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)



@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            message = []
            if isinstance(event, MessageEvent):

                if event.message.type == "text":
                    user_msg = event.message.text
                    print(re.match(r'-?\d*x[+-]-?\d+y=-?\d*\n-?\d*x[+-]-?\d+y=-?\d*', user_msg))
                    if user_msg == "選單":
                        message.append(Flex_MainMenu())
                        line_bot_api.reply_message(event.reply_token, message)
                    elif user_msg == "二元一次方程式計算器":
                        text = "請輸入一組二元一次方程式\n範例：\n2x+3y=5\n4x+5y=1"
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                    elif user_msg == "反矩陣生成器":
                        text = "請輸入一組矩陣\n範例：\n[2 5\n 6 3]"
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                    elif user_msg == "[2 3\n 5 7]":
                        text = "[-7 3\n 5 -2]"
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                    elif re.match(r'-?\d*x[+-]-?\d+y=-?\d*\n-?\d*x[+-]-?\d+y=-?\d*', user_msg) is not None:
                        text = two_var_equation(user_msg)
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))

                    else:
                        line_bot_api.reply_message( 
                            event.reply_token,
                            TextSendMessage(text=event.message.text)
                        )
                return HttpResponse()
    else:
        return HttpResponseBadRequest()




# line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# @csrf_exempt
# def callback(request):

#     if request.method == 'POST':
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')

#         try:
#             events = parser.parse(body, signature)
#         except InvalidSignatureError:
#             return HttpResponseForbidden()
#         except LineBotApiError:
#             return HttpResponseBadRequest()

#         for event in events:
#             if isinstance(event, MessageEvent):
#                 line_bot_api.reply_message(
#                     event.reply_token,
#                    TextSendMessage(text=event.message.text)
#                 )
#         return HttpResponse()
#     else:
#         return HttpResponseBadRequest()