
#a
#"global" inside a function indicates that the variable came from the calling program. and the funnction can use it and change it
# using global variables inside a function is bad practice, because every calling program will have to check if
# it's variables have other names than the global variable, otherwise the function will change the content of the global variable
#in the following code, we'll get an error
"""   x: int = 1
def foo():
    print(x)
    x = 4
foo() """
# this is because python is a very clever language.
#the interpreter goes over the code of the function and finds the "x = 4" sentence, so
#it knows that X is adressed later on, but there is a print(x), before x has a content
#if there was no "x = 4" the python would go out of the function and find the content of x
