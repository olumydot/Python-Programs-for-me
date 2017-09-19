# using decorators makes the initial function loose a lot of its metadata;
# eg when the call function.__name__ that of the decorator comes up when the name of the function should
# same occurs for function.__doc__ the docstring shows for the metadata. Help function for such function is affected
# hence the concept of functools.wraps()
# this properly updates the metadata on wrapped functions
import functools


def noop(f):  # object f is the function to be wrapped.. The object output of the function to be wrapped: 'Helloworld'
    @functools.wraps(f)  # takes the same arguement as the wrapper fxn. inherits the proper attribute from wrapped fxn
    def noop_wrapper():
        return f()
    # print(noop_wrapper)
    # print(f())
    # print(noop_wrapper.__call__)
    return noop_wrapper


@noop  # the object returned from the hello() function is passed unto the noop wrapper
def hello():
    """Print a well known string: 'Hello world!'"""
    print('Hello world!')
    return 'Hello' + 'world'

hello()
print("")
print(hello)
print("")
print(hello())
print(str(hello))
print(repr(hello))
# line-by-line explanation of the action here:


# when hello() is called
# it  prints 'Hello world!' as the print line in the function instructs
# it then takes the returned object: 'Helloworld' and uses it as a parameter for the noop decorator. so f = 'Helloworld'
# this f is passed unto functools.wraps(f) that helps inherit proper attribute from wrapped function hello
# noop is a function factory of sort. next we look at the noop_wrapper function within the noop function
# noop_wrapper doesn't take any arguements.
# what it does is to take the noop function arguement f, in this case 'Helloworld' and returns it as the original fxn
# that is it returns f(). this is the original function hello(). Functions are callable. so are their objects. so this
# is totally legit. This returned function is then stored as the returned value of noop_wrapper. noop returns whatever
# is returned by noop_wrapper. in this case, it returned  the function f() that is hello(). but remember it returns objs
# General paradigm: callable object goes into the wrapper which in turn returns a callable object. Thus when the funt is
# returned, what really is returned it its callable object which here is 'Helloworld'. If in the original hello() method
# the statement line return 'Hel... ..' was not there, then the @noob wrapper returns none.


# when print(hello) is called this is requesting the memory location and the type of object of hello. its a function


# when print(hello()) is called it takes care of the hello() inside the print first. It does all we stated for hello()
# above first. Now recall that the hello() after going into the decorator returns an object. now this print statement
# prints that object