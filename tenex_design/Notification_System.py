from abc import ABC, abstractmethod
from enum import Enum


class Channel(Enum):
    EMAIL = "email"
    SMS = "sms"


class Notification(ABC):

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def get_recepient(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

class Email(Notification):
    def __init__(self, name, email, content):
        self.email = email
        self.name = name
        self.content = content

    def get_channel(self):
        return Channel.EMAIL

    def get_content(self):
        return self.content

    def get_recepient(self):
        return self.email


class SMS(Notification):
    def __init__(self, name, ph, content):
        self.ph = ph
        self.name = name
        self.content = content

    def get_channel(self):
        return Channel.EMAIL

    def get_content(self):
        return self.content

    def get_recepient(self):
        return self.ph

class NotificationSender(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        pass

class EmailNotificationSender(NotificationSender):
    def send(self, notification: Notification):
        print("Sending and email to : ", notification.get_recepient(), "contnet", notification.get_content())

class SMSNotificationSender(NotificationSender):
    def send(self, notification: Notification):
        print("Sending and SMS to : ", notification.get_recepient(), "contnet", notification.get_content())



class DefaultNotificationSenderFactory:
    def __init__(self):
        email_sender = EmailNotificationSender()
        sms_sender = SMSNotificationSender()

        self.send_map = {
            Channel.EMAIL : email_sender,
            Channel.SMS: sms_sender,
        }

    def get_sender(self, channel:Channel):
        return self.send_map.get(channel, None)

class NotificationDispatcher:
    def __init__(self, dns: DefaultNotificationSenderFactory):
        self.dns = dns

    def dispatch(self, notifiation: Notification):
        channel = notifiation.get_channel()
        sender = self.dns.get_sender(channel)
        if sender:
            sender.send(notifiation)
        else:
            print("Unsupported Sending channel ")


def main():
    dnf = DefaultNotificationSenderFactory()
    dispatch = NotificationDispatcher(dnf)

    email = Email("ABC", "test@email.com", "**** Email Body ****")
    dispatch.dispatch(email)



main()





