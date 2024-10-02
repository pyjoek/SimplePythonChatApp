import time
import threading

def pp():
    for i in range(10):
        print(i)
        time.sleep(1)

threading.Thread(target=pp).start()

name = input("Enter your name: ")
print(f"Your name is {name}")
