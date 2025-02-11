def kwargsAcceptFun(**kwargs):
    """
    This function accepts an arbitrary number of named arguments and prints them.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    kwargsAcceptFun(name="Alice", age=25, city="New York")
