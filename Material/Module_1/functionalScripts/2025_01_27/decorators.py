# Closure Concept

# def outerFunction (messageArgument):
#     # message = messageArgument
#     def innerFunction ():
#         print (messageArgument)
#     return innerFunction

# if __name__ == '__main__':
#     firstFunction = outerFunction ('Hello World')
#     firstFunction ()

### Decorators

# def decoratorFunction (originalFunction):
#     def wrapperFunction (*args, **kwargs):
#         print (f'Wrapper function executed this before {originalFunction.__name__}')
#         return originalFunction (*args, **kwargs)
#     return wrapperFunction

# @decoratorFunction
# def displayInformation (name, age):
#     print (f'Display information for {name} and {age}')

# @decoratorFunction
# def displayFunction ():
#     print ('This is a display function')

# displayInformation ('Peter Parker', 23)
# displayFunction ()
# decoratorDisplay = decoratorFunction (displayFunction)
# decoratorDisplay ()

### Class and Objects with Decorators

class Decorator (object):
    def __init__ (self, originalFunction):
        self.originalFunction = originalFunction

    def __call__ (self, *args, **kwargs):
        print (f'Call method executed this before {self.originalFunction.__name__}')
        return self.originalFunction (*args, **kwargs)

@Decorator
def displayFunction ():
    print ('Generic Display Function')

@Decorator
def displayInformation (name, age):
    print (f'Display information with {name} and {age}')

displayFunction ()
displayInformation ('Johnny Silverhand', 50)