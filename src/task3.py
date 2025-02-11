import time

def decorator_1(func):
    """
    A decorator that measures and prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")
        return result
    
    return wrapper

if __name__ == "__main__":
    @decorator_1
    def sample_function():
        time.sleep(1)
        print("Function executed")

    sample_function()
