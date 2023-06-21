class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

command = input()
while command != 'Stop':
    word = command.split()
    sender = word[0]
    receiver = word[1]
    content = word[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()
send_emails = [int(s) for s in input().split(', ')]
for i in send_emails:
    emails[i].send()
for email in emails:
    print(email.get_info())
