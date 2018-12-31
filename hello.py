name = "Kobus Printa"
print(f"my name is {name} third letter in name is {name[2]}")

i = 28
print(f"i is {i}") 

f = 2.8 
print(f"f is {f}")

b = True 
print(f"b is {b}")

n = None
print(f"the value of n is {n}")

coordinates = (10.0, 20.0)
print(f"these are the coordinates {coordinates} second coordinate is {coordinates[1]}")

mylist = ["Alice", "Bob", "John"]
print(f"this is a python list {mylist} the second name in list is {mylist[1]}")
print(f"the first letter in first name in list is {mylist[0][0]}")


# items in the set are unique. does not order by entry. test whether value is in set or not
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
s.add(1)
print(f"this is a set {s}")

# dictionaries; associates key to value
ages = {"Susan": 22, "Alex": 27}
ages["Kwasiba"] = 30  # adding john to ages dictionary
ages["Susan"] += 1   # increment alice age by 1
print(f"printing dictionory ages {ages}")



#name = input()
#print(f"the name entered is {name}")

# if statements
if name == "ulrich":
    print(f"Good morning boss {name}")
elif name == "delano":
    print(f"entering psuedo name {name}")
else:
    print(f"Hello other person {name}")

# loops
for i in range(5):
    print(f"for loop range: {i}")

for name in mylist:
    print(f"for loop mylist: {name}")

# functions
def add(x):
    return x + x

# loop from 0 to 9, something squared is somenthing. get the something values from format i, square(i).
for i in range(10):
    print("{} plus {} is {}".format(i,i, add(i)))

# call an external function
from myFunction import square
print(f"calling myFunction.square {square(12)}")

# classes
# create new type point like string. 
# init means when create new point object self what new info do i need x,y.
 
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = point(3, 5)
print(f"class point x is {p.x}")
print(f"class point y is {p.y}")


