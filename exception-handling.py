#Exception Handling
# not handling exception is dangerous because it creates vulnerability in the code

# Example 1
# while True:
#     try: 
#         age = int(input('Enter your age'))
#         print(f"Your age is: {age}")
#         break
#     except ValueError:
#         print("invalid number, enter a number ")


# Example 2
def divide(a , b):
    try:
        result = a / b
        print(f"result: {result}")
    except ZeroDivisionError:
        print("Division by zero is not allowed")


divide(3,0)