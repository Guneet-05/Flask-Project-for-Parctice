from logging import *

def my_logger(origfunc):
    basicConfig(filename='{}.log'.format(origfunc.__name__), level=INFO)

    def wrapper(*args,**kwargs):
        info(f'Ran with args: {args} and kwargs: {kwargs}')
        return origfunc(*args,**kwargs)
    
    return wrapper

@my_logger
def display():
    print("I am a display method")

@my_logger
def display_details(name,age):
    print(f"Name: {name} and Age: {age}")


display()
display_details("Guneet",23)