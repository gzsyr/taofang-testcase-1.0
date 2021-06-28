import inspect

from page_object.base_page.app import App


class TestBase:
    app = None
    shouye = None

    def setup_class(self):
        print("setup_class")
        if self.app is None:
            self.app = App()

            # self.shouye = self.app.openapp().main()  # self.app.start().main()
            # print('&&&&&&&' + inspect.stack()[1].filename)
            # print(self.shouye)
        else:
            print("app: " + self.app)

    def teardown_class(self):
        self.app.stop()
        print("teardown_class")

    def setup_method(self):
        print("setup_method")
        if self.shouye is None:
            self.shouye = self.app.openapp().main()
            print("self.shouye is None")
        else:
            print("self.shouye not None")

    def teardown_method(self):
        print(self.shouye)
        self.app.closeapp()
        print(self.shouye)
        print("teardown_method")