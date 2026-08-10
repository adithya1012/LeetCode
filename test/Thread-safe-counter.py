# Thread-safe counter over a stream of inputs. (Your "keep track of count based on input stream" item.)

import threading
import concurrent
import time


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def add(self, n):
        '''
        increase the count variable
        :param n: int
        :return: None
        '''
        with self.lock:
            print(n)
            for i in range(100_000):
                tmp = self.count
                tmp = tmp + n
                time.sleep(0)
                self.count = tmp
                # self.count += n
        print("#", n)


C = Counter()

f3 = threading.Thread(target=C.add, args=[3])
f2 = threading.Thread(target=C.add, args=[2])
f1 = threading.Thread(target=C.add, args=[1])

f2.start()
f3.start()
f1.start()

f1.join()
f3.join()
f2.join()

print(C.count)

