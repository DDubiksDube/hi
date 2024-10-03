#create a random number for the maths
import time
import random

def run():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print(x)
    print("*")
    print(y)
    answer = x*y
    input = input()
    time.sleep(5)
    print("done!")
    print(answer)
    if input == answer:
        print("congrats!")
    time.sleep(1)
    run()


run()