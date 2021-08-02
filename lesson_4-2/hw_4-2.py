# Реализовать 2 вида Стека с применением классов.
# Метод push каждого из них будет работать следующим образом:
# Принимает только числа.
# Если число до 50 - засыпаем на 1 секунду (использовать time.sleep()).
# Если число после 50 - засыпаем на 2 секунды.
# Нужно создать 2 объекта этого стека и используя random.randint() добавить в каждый из них по 10 значений.
# Реализовать Асинхронный стек с теми же условиями.
# Значения от randint() получем из генератора.
# Использование исключений обязательно!

from time import sleep
from random import randint
import asyncio


class Stack:
    def __init__(self):
        self.__stack_list = []

    @property
    def stack_content(self):
        return self.__stack_list

    def push(self, value):
        try:
            new_value = int(value)
            if new_value <= 50:
                sleep(1)
            else:
                sleep(2)
            self.__stack_list.append(new_value)
        except ValueError:
            print('Use only integers')

    def pop(self):
        try:
            value = self.__stack_list[-1]
            del self.__stack_list[-1]
            return value
        except IndexError:
            return None

    def __str__(self):
        return str(self.__stack_list)


class AsyncStack(Stack):

    async def push(self, value):
        try:
            new_value = int(value)
            self.stack_content.append(new_value)
            if new_value <= 50:
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(2)
        except ValueError:
            print('Use only integers')


def generator(n):
    """Generator of random numbers in range n"""
    for i in range(n):
        yield randint(1, 100)


def main():
    number_stacks = 2
    number_element = 10
    stack_sync = [Stack() for i in range(number_stacks)]
    for stack in stack_sync:
        [stack.push(k) for k in generator(number_element) for stack in stack_sync]
        print('Synchronous stack:', stack)
        print('=' * 25)

    stack_async = [AsyncStack() for i in range(number_stacks)]
    tasks = [as_stack.push(k) for k in generator(number_element) for as_stack in stack_async]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    for as_stack in stack_async:
        print('Asynchronous stack:', as_stack)
        print('=' * 25)


if __name__ == '__main__':
    main()
