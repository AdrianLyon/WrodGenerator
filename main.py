from models.document_model import DocumentModel
from models.user_model import UserModel
from views.login_view import LoginView
from presenters.login_presenter import LoginPresenter
from presenters.main_presenter import MainPresenter

def main():
    user_model = UserModel()
    document_model = DocumentModel()

    # Crear el presentador primero, luego la vista
    main_presenter = MainPresenter(document_model)

    login_view = LoginView()
    login_presenter = LoginPresenter(login_view, user_model, main_presenter)

    login_view.set_presenter(login_presenter)
    login_view.run()

if __name__ == "__main__":
    main()
