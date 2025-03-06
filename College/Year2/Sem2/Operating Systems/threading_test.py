import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
    datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    logging.info("Main : before running thread")
    for i in range(10):
        x = threading.Thread(target=thread_function, args=(i,))
        x.start()
    logging.info("Main : wait for the thread to finish")
    # x.join() joins x so it runs sequentially with the main thread
    # i.e. the main thread will wait until the worker thread has completed
    # x.join()
    logging.info("Main : all done")
