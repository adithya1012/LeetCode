# Bounded buffer / producer-consumer — first with queue.Queue, then your own with Condition.

# Queue:

import threading
import queue
import time


# q = queue.Queue()

# class Prod_Consumer:
#     def __init__(self):
#         self.q = queue.Queue(maxsize=1)
#
#     def producer(self, n):
#         # while True:
#         print("Putting :", n)
#         time.sleep(n)
#         self.q.put(n)
#         # print("OUT OF PRODUCER", n)
#
#     def consumer(self):
#         while True:
#             n = self.q.get()
#             print("Getting :", n)
#             time.sleep(0.1)
#             self.q.task_done()
#         print("OUT OF CONSUMER")
#
# pc = Prod_Consumer()
#
# t1c = threading.Thread(target=pc.consumer, daemon=True)
# # t2c = threading.Thread(target=pc.consumer, daemon=False)
# # t3c = threading.Thread(target=pc.consumer, daemon=False)
# t1p = threading.Thread(target=pc.producer, args=[3])
# t2p = threading.Thread(target=pc.producer, args=[5], )
# t3p = threading.Thread(target=pc.producer, args=[10])
#
#
# t1p.start()
# t2p.start()
# t3p.start()
# t1c.start()
# # t2c.start()
# # t3c.start()
#
# # t1p.join()
# # t2p.join()
# # t3p.join()
# # t1c.join()
# # t2c.join()
# # t3c.join()
#
# print("ALL COMPLETED")


class Prod_Consumer:
    def __init__(self):
        self.condition = threading.Condition()
        self.q = []
        self.cap = 1

    def producer(self, n):
        with self.condition:
            while len(self.q) >= self.cap:
                print("producer waiting: ", n, self.q)
                self.condition.wait()
            print("producer: ", n)
            self.q.append(n)
            self.condition.notify_all()

    def consumer(self):
        while True:
            with self.condition:
                while not self.q:
                    print("consumer waiting: ")
                    self.condition.wait()

                n = self.q.pop(0)
                if n is None:
                    break
                time.sleep(n)
                print("consumer: ", n)
                self.condition.notify_all()
        print("CONSUMER EXITED")


pc = Prod_Consumer()
threading.Thread(target=pc.producer, args=[3]).start()
threading.Thread(target=pc.producer, args=[5]).start()
threading.Thread(target=pc.producer, args=[10]).start()

c = threading.Thread(target=pc.consumer)

threading.Thread(target=pc.producer, args=[None]).start()

c.start()
c.join()

print("All completed")





