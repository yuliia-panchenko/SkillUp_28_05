# LIFO
# процедурный подход

# stack = []
#
#
# def push(value):
#     stack.append(value)
#
#
# def pop():
#     value = stack[-1]
#     del stack[-1]
#     return value
#
#
# push(10)
# push(20)
# push(30)
# print(stack)
# a = pop()
#
# print(a)
# print(stack)

class Stack:
    def __init__(self):
        self.__stack_list = []

    @property
    def data(self):
        return self.__stack_list

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        try:
            value = self.__stack_list[-1]
            del self.__stack_list[-1]
            return value
        except IndexError:
            return None

    def __str__(self):
        return str(self.__stack_list)

class AdvancedStack(Stack):

    # def __init__(self):
    #     super().__init__()

    def __len__(self):

        return len(self.data)


stack_1 = AdvancedStack()
stack_2 = Stack()

stack_1.push(1)
stack_1.push(2)
stack_1.push(3)

stack_2.push(10)
stack_2.push(20)
stack_2.push(30)

stack_1.pop()

print(stack_1)
print(stack_2)
print(len(stack_1))
