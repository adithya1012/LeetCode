
import threading
import time
#
#
# def hello(i):
#     print("THREAD name:", i)
#     time.sleep(i)
#     print("THREAD COMPLETED:", i)
#     print("---------------------")
#
#
#
# t1 = threading.Thread(target=hello, args=[1])
# t2 = threading.Thread(target=hello, args=[3])
# t1.start()
# t2.start()
# t2.join()
# # t1.join()
# print("HELLO ALL COMPLETED")


import concurrent.futures

# def hello(i):
    # print("THREAD name:", i)
    # time.sleep(i)
    # print("THREAD COMPLETED:", i)
    # print("---------------------")
    # return "THREAD COMPLETED:" + str(i)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(hello, 1)
#     f2 = executor.submit(hello, 10)
#     print(f2.result())
    # print(f2.result()) # if you want the f2 to complete before main thread.
    # concurrent.futures.wait([f1, f2]) # if you want to wait both of them.
    # print("ALL COMPELETED")


    # result = executor.map(hello, [4,3,2,1]) # result will have the same order which we have given
    # for i in result:
    #     print(i)



# executor = concurrent.futures.ThreadPoolExecutor()
#
# f1 = executor.submit(hello, 1)
# f2 = executor.submit(hello, 10)
# print(f1.result())
# print("******************")




# import threading, time, random
#
# counter = 0
# lock = threading.Lock()
# def increment():
#     global counter
#     for _ in range(100_000):
#         # with lock:
#         tmp = counter
#         time.sleep(0)
#         counter = tmp + 1
#             # counter += 1
#
# ts = [threading.Thread(target=increment) for _ in range(4)]
# [t.start() for t in ts]
# [t.join() for t in ts]
# print(counter)









# class BoundedBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.items = []
#         self.condition = threading.Condition()
#
#     def producer(self, value):
#         with self.condition:
#             while len(self.items) >= self.capacity:
#                 print(f"Producer waiting (buffer full): {self.items}")
#                 self.condition.wait()
#
#
#             self.items.append(value)
#             self.condition.notify()
#             print(f"Producing {value}", self.items)
#
#         # print("PRODUCER OUTSIDE")
#
#     def consumer(self):
#         with self.condition:
#             while not self.items:
#                 print("Consumer waiting (buffer empty)")
#                 self.condition.wait()
#
#             value = self.items.pop(0)
#             print(f"Consumed {value}", self.items)
#
#             self.condition.notify()
#             # return value
#         # print("Consumer OUTSIDE")
#
# buffer = BoundedBuffer(2)
#
# def producer_thread():
#     for i in range(5):
#         time.sleep(0.1)
#         buffer.producer(i)
#
# def consumer_thread():
#     for _ in range(5):
#         time.sleep(0.2)
#         buffer.consumer()
#
# p = threading.Thread(target=producer_thread)
# c = threading.Thread(target=consumer_thread)
#
# p.start()
# c.start()
#
# # p.join()
# # c.join()



# import threading
# import time
#
# sem = threading.Semaphore(2)
#
# def worker(i):
#     print(f"{i} waiting")
#
#     with sem:
#         print(f"{i} entered")
#         time.sleep(3)
#         print(f"{i} leaving")
#
# for i in range(5):
#     threading.Thread(target=worker, args=(i,)).start()


# import threading
# import time
#
# event = threading.Event()
#
# def worker():
#     print("Worker waiting...")
#     event.wait()
#     print("Worker started!")
#
# t1 = threading.Thread(target=worker)
# # t2 = threading.Thread(target=worker).start()
# t1.start()
# # t1.join()
#
# time.sleep(3)
#
# print("Main: Go!")
# event.set()


import threading
import queue
import time

q = queue.Queue()

def worker():
    while True:
        item = q.get()

        print(f"Working on {item}")
        time.sleep(1)

        print(f"Finished {item}")

        q.task_done()

threading.Thread(target=worker, daemon=True).start()

for i in range(5):
    print("Adding to the queue:", i)
    q.put(i)

print("Main waiting...")

q.join()

print("All jobs finished!")


