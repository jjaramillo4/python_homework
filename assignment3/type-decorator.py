#Task 2
def type_converter(type_of_output):
    def type_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return type_of_output(result)
            except ValueError:
                raise ValueError(f"can't convert {result} to {type_of_output.__name__}")
        return wrapper
    return type_decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen