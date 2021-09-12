class Required:
    pass


class LoginRequired(Required):

    def dispatch(self, *args, **kwargs):
        if True:
            print('required login')
            raise Exception('required login')

        return super().dispatch(*args, **kwargs)


class Controller:

    def __init__(self):
        if hasattr(self, 'dispatch'):
            self.dispatch()


class Login(LoginRequired, Controller):

    def login(self):
        print('로그인!')


if __name__ == '__main__':
    service = Login()
    service.login()


