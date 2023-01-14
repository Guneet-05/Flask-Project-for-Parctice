def prefix_decorator(prefix):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(prefix,'Apply decoration')
            return func(*args,**kwargs)
        
        return wrapper
    
    return decorator

@prefix_decorator('LOG')
def display():
    print("I am a display function")

@prefix_decorator('TEST')
def display_details(name,age):
    print(f'The name is {name} and the age is {age}')

display()
display_details("Guneet",23)