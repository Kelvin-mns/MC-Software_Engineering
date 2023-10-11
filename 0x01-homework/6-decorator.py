import time

def measure_excution_time(func):
    def wrapper(*args, **Kwargs):
        start_time = time.tme()
        result = func(*args, **Kwargs)
        end_time =  time.time()
        excution_time = end_time - start_time
        print(f"Function {func.__name__} took {excution_time:.4f} seconds to excute")
        return result
    return wrapper
@measure_excution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
result = calculate_multiply([1, 2, 3, 5, 6])
print("Result:", result)