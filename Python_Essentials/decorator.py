def decorator_function(original_function):
    def wrapper_function(*args,**kwargs): #*args and **kwargs are used so that the function can take N number of 
        # Positional arguments
        print("Some extra functionality")
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("I am a display method")


@decorator_function
def display_info(name,age):
    print(f"The name is {name} and the age is {age}")

display()
display_info("Guneet",23)