# Thread-safe job scheduler with a concurrency limit N. This is the most-reported Pure question.
# Semaphore(N) + worker threads pulling from a Queue.
# Then extend: how do you shut it down cleanly? (Sentinel values, or an Event flag checked in the loop.)

# 2 Design :
# Worker Pool Version (no semaphore) — this is how executors and thread pools are commonly implemented.
# Semaphore Version — start, say, 10 worker threads but use Semaphore(2) so that only 2 jobs execute concurrently


import threading
import time
import queue




class JobScheduler:
    def __init__(self, n):
        self.semaphore = threading.Semaphore(n)
        self.q = queue.Queue()
    def submit(self, work_time):
        # with self.semaphore:
        self.q.put(work_time)
        time.sleep(work_time)
        print("appended: ", work_time)

    def worker(self):
        with self.semaphore:
            while True:
                print("Worker started: ")
                wait_time = self.q.get()
                if wait_time == -1:
                    print("ending the worker thread")
                    break
                time.sleep(wait_time)
                print("worker completed: ", wait_time)


    def shutdown(self, worker_count):
        '''
        Called throguh main thread only
        :return: None
        '''
        for i in range(worker_count):
            self.q.put(-1)



js = JobScheduler(2)
work_time = [1,2,3,4]
threads = []


for wt in work_time:
    t = threading.Thread(target=js.submit, args=[wt])
    t.start()
    threads.append(t)

worker_count = 5
for i in range(worker_count):
    t2 = threading.Thread(target=js.worker)
    t2.start()
    # threads.append(t2)

for t in threads:
    t.join()

js.shutdown(worker_count)
print("MAIN THREAD ENDED ")




