#!/usr/bin/python3

import threading
import random
import os
import time

mutex = threading.Lock()

birthday = list(open('happy_Birthday.txt').read().rstrip())


def colored_dot(color):
    if color == 'red':
        return f'\033[91m•\033[0m'
    if color == 'green':
        return f'\033[92m•\033[0m'
    if color == 'yellow':
        return f'\033[93m•\033[0m'
    if color == 'blue':
        return f'\033[94m•\033[0m'


def lights(color, indexes):
    off = True
    while True:
        for index in indexes:
            birthday[index] = colored_dot(color) if off else '•'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(birthday))
        mutex.release()

        off = not off

        time.sleep(random.uniform(.5, 1.5))


yellow = []
red = []
green = []
blue = []
for i, c in enumerate(birthday):
    if c == 'Y':
        yellow.append(i)
        birthday[i] = '•'
for i, c in enumerate(birthday):
    if c == 'R':
        red.append(i)
        birthday[i] = '•'
for i, c in enumerate(birthday):
    if c == 'G':
        green.append(i)
        birthday[i] = '•'
for i, c in enumerate(birthday):
    if c == 'B':
        blue.append(i)
        birthday[i] = '•'

ty = threading.Thread(target=lights, args=('yellow', yellow))
tr = threading.Thread(target=lights, args=('red', red))
tg = threading.Thread(target=lights, args=('green', green))
tb = threading.Thread(target=lights, args=('blue', blue))

for t in [ty, tr, tg, tb]:
    t.start()
for t in [ty, tr, tg, tb]:
    t.join()
