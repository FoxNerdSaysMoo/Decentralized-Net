from threading import Thread, activeCount


class ThreadHandler:
    def __init__(self, maxthreads):
        self.maxthreads = maxthreads
    def on_ping(self, request, target):
        if activeCount() < self.maxthreads:
            thread = Thread(target=target, args=[request])
            thread.start()
            print(activeCount())
        else:
            print("MaxThreads reached: please wait")