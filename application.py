import os
from dotenv import load_dotenv
from flask import Flask, request
from bot import Bot


module_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(module_path, '.env'))

app = Flask(__name__)
app.debug = True

fb_verify_token = os.environ.get('FACEBOOK_VERIFY_TOKEN')
fb_page_access_token = os.environ.get('FACEBOOK_PAGE_TOKEN')
bot = Bot(fb_page_access_token)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == fb_verify_token:
            return request.args.get('hub.challenge')
        raise ValueError('FACEBOOK_VERIFY_TOKEN does not match.')
    elif request.method == 'POST':
        print(request.get_json(force=True))
        bot.handle(request.get_json(force=True))
    return ''


if __name__ == '__main__':
    app.run()
