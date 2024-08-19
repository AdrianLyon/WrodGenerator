class LoginPresenter:
    def __init__(self, view, user_model, main_presenter):
        self.view = view
        self.user_model = user_model
        self.main_presenter = main_presenter

    def on_login(self):
        username, password = self.view.get_credentials()
        if self.user_model.validate_user(username, password):
            self.view.close()
            self.main_presenter.run()
        else:
            self.view.show_error("Invalid username or password")
