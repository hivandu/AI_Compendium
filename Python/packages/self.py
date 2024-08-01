'''
Author: Hivan Du
mail: doo@hivan.me
LastEditors: Hivan Du
LastEditTime: 2024-08-01 16:02:12
'''
# My.py

# Define Class
class MyException():
    pass

# Define function
def func():
    print("I'm a function inside the module.")

# Define variables 
myStr = 'iloveyou'

name = __name__
print(f'__name__: {name}')

if __name__ == '__main__':
	  print('The code in this location will only run if the current script is run directly.')