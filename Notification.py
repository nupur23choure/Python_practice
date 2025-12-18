class Notification:
    def method_send(self):
        pass
    
class Email(Notification):
    def method_send(self):
        print("Sending email notification")

class Whatsapp(Notification):
    def method_send(self):
        print("Sending Whatsapp notification")

class SMS(Notification):
    def method_send(self):
        print("Sending SMS notification")

note = [Email(), Whatsapp(), SMS()]
for n in note:
    n.method_send()    
