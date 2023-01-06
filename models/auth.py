from typing import TypedDict, Union
from .base import ObservableModel


class User(TypedDict):
    username: str


class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.current_user: Union[User, None] = None

    def login(self, user: User) -> None:
        self.is_logged_in = True
        self.current_user = user
        self.trigger_event("auth_changed")

    def logout(self) -> None:
        self.is_logged_in = False
        self.current_user = None
        self.trigger_event("auth_changed")
