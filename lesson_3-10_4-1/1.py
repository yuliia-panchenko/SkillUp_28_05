# 1. Create a class to launch rockets
# 2. Rocket have to have delay, countdown
# 3. Rocket have to have launch, countdown, delay function
import sys
import asyncio
import random
from threading import Thread
from time import sleep

class Rocket:

    def __init__(self, rocket_number: int) -> None:
        self.rocket_number = rocket_number
        self.rocket_countdown = self.__random_countdown
        self.rocket_delay = self.__random_delay

    def __repr__(self) -> str:
        return f"Rocket #{self.rocket_number}"

    @property
    def __random_countdown(self):
        return random.randint(3, 10)

    @property
    def __random_delay(self):
        return random.randint(1, 3)

    def countdown(self):
        for i in range(self.rocket_countdown, 0, -1):
            print(f"Rocket #{self.rocket_number} runs in {i} seconds...")
            sleep(1)

    def delay(self):
        print(f"Rocket #{self.rocket_number} has a delay - {self.rocket_delay} seconds")
        sleep(self.rocket_delay)

    def launch(self):
        self.delay()
        self.countdown()
        print(f"Rocket #{self.rocket_number} in the space")


class AsyncRocket:
    def __init__(self, rocket_number):
        self.rocket_number = rocket_number
        self.rocket_countdown = self.__random_countdown
        self.rocket_delay = self.__random_delay

    @property
    def __random_countdown(self):
        return random.randint(3, 10)

    @property
    def __random_delay(self):
        return random.randint(1, 3)

    async def countdown(self):
        for i in range(self.rocket_countdown, 0, -1):
            print("Rocket #{} runs in {} seconds...".format(self.rocket_number, i))
            await asyncio.sleep(1)

    async def delay(self):
        print("Rocket #{} has a delay - {} seconds".format(self.rocket_number, self.rocket_delay))
        await asyncio.sleep(self.rocket_delay)

    def __repr__(self):
        return "Rocket #{}".format(self.rocket_number)

    async def launch(self):
        await self.delay()
        await self.countdown()
        print("Rocket #{} in the space".format(self.rocket_number))


def main():
    N = 5000
    choice = input()

    if choice not in ("sync", "async", "threads"):
        raise ValueError("You can use only sync, async, threads values")

    if choice == "async":
        rockets = [AsyncRocket(rocket_number=i + 1) for i in range(N)]
        tasks = [rocket.launch() for rocket in rockets]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*tasks))
        loop.close()

    elif choice == "threads":
        rockets = [Rocket(rocket_number=i + 1) for i in range(N)]
        rocket_threads = [Thread(target=rocket.launch) for rocket in rockets]

        for t in rocket_threads:
            t.start()
        for t in rocket_threads:
            t.join()
    else:
        rockets = [Rocket(rocket_number=i + 1) for i in range(N)]
        for rocket in rockets:
            rocket.launch()


if __name__ == "__main__":
    main()
