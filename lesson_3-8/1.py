class Robot:
    __counter = 0 # видно только внутри класса

    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age
        Robot.__counter += 1
        print('Robot was created')

    def __del__(self):
        Robot.__counter -= 1
        print('Robot was deleted')

    def __setattr__(self, name: str, value):
        self.__dict__[name] = value
        # return super().__setattr__(name, value)

    def get_robots_count():
        return Robot.__counter


r2d2 = Robot(name='R2 D2', age=10)
c3po = Robot(name='C3PO')
# Robot.__counter += 100
# del(r2d2)
print(Robot.get_robots_count())
