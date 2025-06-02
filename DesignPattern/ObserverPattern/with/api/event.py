subscriber = dict()

def subscribe(event_type, fn):
    if event_type not in subscriber:
        subscriber[event_type] = []
    subscriber[event_type].append(fn)
    print(subscriber)

def post_event(event_type, data):
    if event_type not in subscriber:
        return
    for fn in subscriber[event_type]:
        fn(data)
