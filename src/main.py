import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += i ** 2

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__":
    # Task 1
    kwargsAcceptFun(name="Alice", age=30, city="Paris")

    # Task 2
    transformed_data = typeBasedTransformer(num=3, text="World", flag=False, items=(5, 10, 15), mapping={"x": 10, "y": 20})
    print(transformed_data)

    # Task 3
    func()
    funx()
    func()
    funx()
    func()
