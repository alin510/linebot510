from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('6jhsJV76McRhoXWcGqFqqbqa222b3ndcF5m+02+WHgoG/doSvKiwN2C+WDBqG4jkU5Yhep58oXCoLKxjawWzA3KDKTkRcWnniqIm/iEQnphAKdiwi2HtXhxj5aEXqBrReOeo16RTnAqLo4DUuXeHWQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ce848950f33d123b03d87643069212fe')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if "早安" or "你好"  in msg : 
        r = msg
    else :
        r ＝ '聽不懂?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()