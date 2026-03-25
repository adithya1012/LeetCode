from collections import defaultdict, deque

class EventQueue:
    def __init__(self):
        self.handler = defaultdict(list)
        self.queue = deque([])

    def subscribe(self, event, handler_function):
        self.handler[event].append(handler_function)

    def publisher(self, event, data):
        self.queue.append([event, data])

    def process(self):
        while self.queue:
            event, data = self.queue.popleft()
            for funct in self.handler[event]:
                funct(data)


def Login(data):
    print("[AUTH] Login Successful:", data["name"] )

def Welcome_email(data):
    print("[EMAIL] Email Sent to:", data["email"])


if __name__ == "__main__":
    eventq = EventQueue()
    eventq.subscribe("Login", Login)
    eventq.subscribe("Login", Welcome_email)
    eventq.subscribe("Welcome", Welcome_email)

    data = {
        "name" : "ABC",
        "email": "test@gmail.com"
    }
    data1 = {
        "email": "test1@gmail.com"
    }

    eventq.publisher("Login", data)
    eventq.publisher("Welcome", data1)
    eventq.process()




