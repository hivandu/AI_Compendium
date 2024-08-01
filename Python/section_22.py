'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2024-08-01 17:54:33
'''

# Magic Methods
# Define a Person
class Person():

    # Constructor method
    def __new__(cls, *args, **kwargs):
        print(args)
        # print(kwargs)
        print(cls)
        return object.__new__(cls)

    # Initialization method
    def __init__(self, name, age, sex):
        print('Triggering initialization method: __init__')
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self, *args, **kwargs):
        print('You called the object as if it were a function.')

    # Destructor method
    def __del__(self):
        print('Triggering destructor method: __del__')

# Instantiate an object
zs = Person('Zhang Sanfeng', 210, 'Male')
print(zs)
zs()