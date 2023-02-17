class Credentials:

    def __init__(self, token=None, openaikey=None):

        self.token = token
        self.openaikey = openaikey

        if token is None:
            self.token = 'ваш секретный ключ' #в кавычки нужно подставить свой токен из личного кабинета Dadata
            self.openaikey = 'ваш секретный ключ' #сюда нужно подставить свой секретный ключ OpenAI

