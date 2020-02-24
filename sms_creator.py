def remove():
    text.remove()


def get_count():
    smslength = len(smsstore)
    return smslength


class SMSmessage(object):
    has_been_read = bool
    messageText = str
    from_number = int

    def __init__(self, senders_number, has_been_read=False):
        self.text = text
        self.senders_number = senders_number
        self.has_been_read = has_been_read

    def mark_as_read(self, has_been_read=True):
        self.has_been_read = has_been_read

    SMSstore = []

    def add_sms(self, from_number):
        self.from_number = from_number
        SMSstore.append(self.text)

    def get_message(self):
        self.messageText = input("input message index ")
        if self.message:
            self.has_been_read = True
        return self.messageText

    def get_unread_messages(self, has_been_read=False):
        self.has_been_read = has_been_read
        return self.has_been_read


userChoice = ""

while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        get_message()
    elif userChoice == "send":
        textmessage = input("enter message ")
        SMSstore.append(textmessage)
    elif userChoice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
