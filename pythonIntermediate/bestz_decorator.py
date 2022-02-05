
# Decorated function without Parameter
# def display_info(function):
#     def inner():
#         print("Executing", function.__name__, "function")
#         function()
#         print("Finished", function.__name__, "function")
#     return inner

# @display_info
# def printer():
#     print("Hello School")

# printer()

def bestz_print(msg):
    print(msg)

# Decorated Function With parameter
# def smart_divide(function):
#     def inner(a, b):
#         print("Dividing", a, "by", b)
#         if b == 0:
#             return "Cannot divide by 0!"
#         return function(a, b)
#     return inner

# @smart_divide
# def divide(a, b):
#     return a / b


# def percentage(function):
#     def inner(args):
#         bestz_print("%" * 30)
#         function(args)
#         bestz_print("%" * 30)
#     return inner

# def star(function):
#     def inner(args):
#         bestz_print("*" * 30)
#         function(args)
#         bestz_print("*" * 30)
#     return inner


# @star
# @percentage
# def printer(message):
#     bestz_print(message)

# printer("Decorator Is Magical")



