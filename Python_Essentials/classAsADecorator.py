class decorator_class:

    def __init__(self,originalFunc) -> None:
        self.originalFunc = originalFunc
    
    def __call__(self,*args,**kwargs):
        print("Decoration added")
        self.originalFunc(*args,**kwargs)


@decorator_class
def display():
    print("This is a display method")

@decorator_class
def display_info(name,age):
    print(f"The name is {name} and the age is {age}")

display()
display_info("Guneet",23)