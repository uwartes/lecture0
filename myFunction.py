# python module

# functions. run this functin when explicitly called. from myFunction import square 
# def main and if __name__ makes sure that only square is run and not all the code in this file
def square(x):
    return x * x

# loop from 0 to 9, something squared is somenthing. get the something values from format i, square(i).
# The main function will run whenever myFunction.py is run e.g. [C:\lecture0>myFunction.py]
def main():
    for i in range(10):
         print("{} squared is {}".format(i, square(i)))

# If this file is run, run main function
if __name__ == "__main__":
    main()