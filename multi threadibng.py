from time import *
from threading import *
class greet(Thread):
    def run(self):
        for i in range (5):
            print("hello")
            sleep(1)
class welcome(Thread):
    def run(self):
        for i in range (5):
            print("welcome")
            sleep(1)
a = greet()
b = welcome()
a.start()
sleep(0.2)
b.start()
a.join()
b.join()
print('have a nice day')
