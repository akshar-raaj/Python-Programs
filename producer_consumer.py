from threading import Thread
import time
import random
from Queue import Queue
 
queue = Queue(10)
 
class ProducerThread(Thread):
    #Put limit on num of elements in queue
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num
            time.sleep(random.random())
 
 
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())
 
 
ProducerThread().start()
ConsumerThread().start()
