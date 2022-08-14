import threading
from time import sleep

#функции, запущеные впаралель через threading.

def func1( a):
    while a > 0:
        sleep(0.5)
        a -= 1
        print('func1 этап   ', a, ';  ')
        sleep(0.5)
def func2( a):
    while a > 0:
        sleep(0.5)
        a -= 1
        print('func2 этап  ', a, ';  ')
        sleep(0.5)
def func3( a):
    while a > 0:
        sleep(0.5)
        a -= 1
        print('func3 этап  ', a, ';  ')
        sleep(0.5)
def func4( a):
    while a > 0:
        sleep(0.5)
        a -= 1
        print('func4 этап  ', a, ';  ')
        sleep(0.5)
def func5( a):
    while a > 0:
        sleep(0.5)
        a -= 1
        print('func5 этап ', a, ';  ')
        sleep(0.5)

f1 = threading.Thread(target=func1,args= (5,))
f2 = threading.Thread(target=func2,args= (5,))
f3 = threading.Thread(target=func3,args= (5,))
f4 = threading.Thread(target=func4,args= (5,))
f5 = threading.Thread(target=func5,args= (5,))

f1.start()
f2.start()
f3.start()
f4.start()
f5.start()

'''
# решение с помощью asyncio:

import asyncio
async def func1(a):
    while a > 0:
        sleep(1)
        a -= 1
        print('func1 этап   ', a, ';  ')
async def func2(a):
    while a > 0:
        sleep(1)
        a -= 1
        print('func2 этап   ', a, ';  ')
async def func3(a):
    while a > 0:
        sleep(1)
        a -= 1
        print('func3 этап   ', a, ';  ')
async def func4(a):
    while a > 0:
        sleep(1)
        a -= 1
        print('func4 этап   ', a, ';  ')
async def func5(a):
    while a > 0:
        sleep(1)
        a -= 1
        print('func5 этап   ', a, ';  ')
async def main():
    asyncio.create_task(func1(5))
    asyncio.create_task(func2(5))
    asyncio.create_task(func3(5))
    asyncio.create_task(func4(5))
    asyncio.create_task(func5(5))
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()

'''



