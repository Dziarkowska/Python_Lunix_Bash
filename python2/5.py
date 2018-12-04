import threading
import random
import time

class Philosophers(threading.Thread):
    running = True

    def __init__(self, name, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = name
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while (self.running):
            time.sleep(random.uniform(3, 13))
            print("%s is hAngry." % self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print("%s swaps forks" % self.name)
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print("%s starts eating " % self.name)
        time.sleep(random.uniform(1, 10))
        print("%s finishes eating and leaves for a nap" % self.name)



forks = [threading.Lock() for n in range(5)]
philosophersNames = ("Aristotle", "Marx", "Voltaire", "Plato", "Nietzsche")

philosophers = [Philosophers(philosophersNames[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

Philosophers.running = True
for p in philosophers:
    p.start()
time.sleep(50)
Philosophers.running = False
print("Now we're on the finish line.")