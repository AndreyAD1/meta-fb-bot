from fbmessenger import BaseMessenger


class Bot(BaseMessenger):
    def __init__(self, page_access_token):
        self.page_access_token = page_access_token
        super(Bot, self).__init__(self.page_access_token)

    def message(self, message):
        self.send(
            {'text': 'Received: {}'.format(message['message']['text'])},
            'RESPONSE'
        )

    def delivery(self, message):
        pass

    def read(self, message):
        pass

    def account_linking(self, message):
        pass

    def postback(self, message):
        pass

    def optin(self, message):
        pass

