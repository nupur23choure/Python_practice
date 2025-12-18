# data abstratction
from abc import ABC, abstractmethod

class LoginSystem:
    @abstractmethod
    def login(self, username):
           self.username = username

class GmailLogin(LoginSystem):
    def login(self, username):
        print(f"Gmail for {username} logged in successfullly.")

class NumberLogin(LoginSystem):
    def login(self, username):
        print(f"Number for {username} logged in successfullly.")

email = GmailLogin()
email.login("user1")
number = NumberLogin()
number.login("user2")
