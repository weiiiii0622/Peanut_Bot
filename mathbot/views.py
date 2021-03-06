from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .models import User

import re

from .flex_msg import Flex_MainMenu
from .equation import two_var_equation, inverse_matrix, HorizontalThrow

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
                if len(User.objects.filter(user = event.source.user_id)) == 0:
                    User.objects.get_or_create(
					    user = event.source.user_id,
				    )
                    user_status = User.objects.filter(user = event.source.user_id)[0].status
                else:
                    user_status = User.objects.filter(user = event.source.user_id)[0].status

                if user_status == "Waiting":
                    if event.message.type == "text":
                        user_msg = event.message.text
                        
                        if user_msg == "選單":
                            message.append(Flex_MainMenu())
                            line_bot_api.reply_message(event.reply_token, message)
                        
                        elif user_msg == "二元一次方程式計算器":
                            User.objects.filter(user = event.source.user_id).update(status = "TwoVar")
                            text = "請輸入一組二元一次方程式\n範例：\n2x+3y=5\n4x+5y=1"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                        
                        elif user_msg == "二階反矩陣生成器":
                            User.objects.filter(user = event.source.user_id).update(status = "InverseMatrix")
                            text = "請輸入一組二階矩陣\n範例：\n2 5\n6 3"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                        
                        elif user_msg == "理想平拋模擬器":
                            User.objects.filter(user = event.source.user_id).update(status = "HorizontalThrow")
                            text = "請輸入一組『初速/高度』來求\n飛行時間(sec)和水平飛行距離(m)\n範例：25/100\n(g=10m/s^2)"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))

                        else:
                            line_bot_api.reply_message( 
                                event.reply_token,
                                TextSendMessage(text="我還不夠聰明，我聽不懂！")
                            )
                    return HttpResponse()
                
                else:
                    user_msg = event.message.text
                    if user_status == "TwoVar":
                        try:
                            text = two_var_equation(user_msg)
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                        except:
                            text = "輸入格式有誤，請重新再試"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                    elif user_status == "InverseMatrix":
                        try:
                            text = inverse_matrix(user_msg)
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                        except:
                            text = "輸入格式有誤，請重新再試"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                    elif user_status == "HorizontalThrow":
                        try:
                            text = HorizontalThrow(user_msg)
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
                        except:
                            text = "輸入格式有誤，請重新再試"
                            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))


                    User.objects.filter(user = event.source.user_id).update(status = "Waiting")
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