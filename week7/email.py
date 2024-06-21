class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


all_mails = []

command = input().split()
while command[0] != 'Stop':
    mail = Email(command[0], command[1], command[2])
    all_mails.append(mail)
    command = input().split()

send_index = list(map(int, input().split(', ')))

for index in send_index:
    all_mails[index].send()

for mail in all_mails:
    print(mail.get_info())
