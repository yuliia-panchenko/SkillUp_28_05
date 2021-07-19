my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class MyList:
    def __init__(self, *args) -> None:
        self.my_list = args

    def __str__(self) -> str:
        output = str(self.my_list)
        output = "".join(['[', output[1:-1], ']'])
        return output

    def __len__(self):
        return len(self.my_list)


example = MyList(*my_list)

print(example)
print(len(example))


class String:
    def __init__(self, *args) -> None:
        self.text = "".join[args]

    def __str__(self) -> str:
        return self.text


text = "Hello"