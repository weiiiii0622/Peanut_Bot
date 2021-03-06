from linebot.models import FlexSendMessage

def Flex_MainMenu():
    content = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "Peanut Bot",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 2,
                        "text": "About Me"
                    },
                    {
                        "type": "text",
                        "text": "Hi",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Time",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": "24hr",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                }
                ]
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "二元一次方程式計算器",
                "text": "二元一次方程式計算器"
                },
                "style": "link",
                "height": "md",
                "margin": "5px",
                "position": "relative"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "二階反矩陣生成器",
                "text": "二階反矩陣生成器"
                },
                "style": "link",
                "height": "md",
                "margin": "5px"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "理想平拋模擬器",
                "text": "理想平拋模擬器"
                },
                "style": "link",
                "height": "md",
                "margin": "5px"
            },
            ]
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
    }
    message = FlexSendMessage(alt_text='Flex_MainMenu',contents=content)
    return message