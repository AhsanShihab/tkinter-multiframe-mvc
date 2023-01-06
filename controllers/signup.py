from models.main import Model
from models.auth import User
from views.main import View


class SignUpController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signup_btn.config(command=self.signup)
        self.frame.signin_btn.config(command=self.signin)

    def signin(self) -> None:
        self.view.switch("signin")

    def signup(self) -> None:
        data = {
            "fullname": self.frame.fullname_input.get(),
            "username": self.frame.username_input.get(),
            "password": self.frame.password_input.get(),
            "has_agreed": self.frame.has_agreed.get(),
        }
        print(data)
        user: User = {"username": data["username"]}
        self.model.auth.login(user)
        self.clear_form()
        
    
    def clear_form(self) -> None:
        fullname = self.frame.fullname_input.get()
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        self.frame.fullname_input.delete(0, last=len(fullname))
        self.frame.fullname_input.focus()
        self.frame.username_input.delete(0, last=len(username))
        self.frame.password_input.delete(0, last=len(password))

        self.frame.has_agreed.set(False)
