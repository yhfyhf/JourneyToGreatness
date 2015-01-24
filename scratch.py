def logging_decorator(func):
    def wrapper():
        wrapper.count += 1
        print "The function I modify has been called {0} time(s)".format(wrapper.count)
        func()
    wrapper.count = 0
    return wrapper

def a_function():
    print "I'm a normal function."



    
modified_function = logging_decorator(a_function)
    

modified_function()
modified_function()
modified_function()