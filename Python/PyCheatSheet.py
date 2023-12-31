   # modules - short lowercase
    # class names - Cap Words
    # variables and function names - lowercase_with_underscores
    # constants - CAPS_WITH_UDERSCORES
    # python keywords names - end with underscore_
    # spaces before and after operators and commas
    # avoid having space inside brackets

    #'from module import *' should be avoided
    # should be one statement per line  
Num1 = 1
Num2 = 2
Num3 = 3
Int1 = 4
Int2 = 5
Int3 = 6
Lst1 = [1,2,3]

######################### Basic Operations ############################

def Function():             #Creates a new function which can be called upon
    intA = int(1)              #Creates a variable which is set as an interger
    strB = str(1)              #Creates a string variable
    boolC = bool(True)          #Creates a boolean variable
    floatD = float(3.14)        #Creates a float variable

    print(strB)              #Outputs the brackets contents
    userinput = int(input("Please input a value"))#takes the users input and assigns it a variable


    if intA == 1: #if the statement is true it will run the contents
        pass 
    elif strB == "1": #runs contents if the statement is true and the last one was false
        pass
    else: #Runs if none of the statements are 
        pass 

    for i in range(0,20,2): #loops from 0 to 20 by a step of 2 eg. 0,2,4,6
        pass

    while intA == 1: #loops until the statement is false
        intA += 1
        break #end the loop instantly
        continue #jumps to the top without finishing previous loop

######################## Basic List Operations #################################

    listE = [1,2,3,4,5] #creates a list of 5 items from 1 to 5
    listF = listE[0:4:2] #makes a new list of items 0 to 3 in listE with step 2
    listG = [i**2 for i in range(9) if i%2 == 0] 
    #Creates a list using i from 0 to 8 according to the mathematical notation, only adding the item if it produces a true if statement  
    
    if 1 in listE: #checks to see if 1 is in the list
        pass
    if all([i > 5 for i in listE]): #only runs the code if all items are under 5
        pass
    if any([i % 2 == 0 for i in listE]): #only runs the code if there's an even item
        pass

    for v in enumerate(listE): #runs with v being (i,nums[i])
        pass

    list(range(5,10,2)) #creates a list of values 
    listE.count(1) #Counts the amount of 1's in the list
    listE.append(6) #adds item 6 to the end of the list
    listE.extend(listF)#Used for append each value from an iterable
    listE.insert(0,10) # inserts 10 into th first position
    listE.remove(Int1) #removes the first instance of the value in the list
    listE.sort() #sorts the list from lowest to highest value
    listE.sort(reverse = True) #sorts highest to lowest
    listE.reverse() #Reverses List
    sorted(listE, key=Function) # sorts the list, via the functions return values 
    zip(listE,listF) #creates a list of tuples of (listE[i],listF[i])

###################### Error Handling Operations #############################

    try: #runs contents and watches for errors
        raise ValueError("invalid value inputted") #raises an error
    except(ZeroDivisionError,ValueError): #if either of these errors popup the contents are run
        pass
    else: #runs if no exception is found
        pass
    finally: #runs this with or without error
        pass

    assert 1+1 == 3 #if the statement is false an AssertionError is given

##################### File Handling Operations ###############################

    fileF = open("filename.txt","r+") #opens a file to be read("r") or written("w") to
                                      #r+ does both read and write
    cont = fileF.read()  #assigns a variable to the contents of the file
    cont = fileF.read(4) #reads the next 4 characters
    cont = fileF.readline() #assigns the variable the contents of the next line
    fileF.readlines()   #creates a list where each item is a line
    
    fileF.write("...") #overwrites a file and all the following text
                       #if assigned to a variable, displays amount of characters
    fileF.writelines(listE) #writes each item of a list on a seperate line    

    fileF.tell() #returns the current position in the file

    fileF.close() #closes the opened file

#################### Dictionary Handling Operations ##########################

    ages = {"Alfie":20, "Jasmine":20, "Tom":32} #Dictoinary variable type
    ages["Alfie"] #Returns the value associated (20)
    ages.get("Jasmine", "...") #Returns value associated or returns "..."  by default
    ages["Athena"] = 22 #Adds a new variable to the dictionary
    ages.pop("Tom") #Removes the key and value

    ages.update(ages) #adds the key value pairs from ages to ages 
    ages.keys() #gives a readable output for all the keys in a dictionary
    ages.values() #gives a readable output for all values
    ages.items() #gives readable output for keys and values

################### String Functions ########################################
    
    str_1 = "Hello " + "World" #Outputs "Hello World" as 1 string
    str_1[0] #Outputs the first character of the string
    str_1[6:8:2] #Outputs everything between chr 6 to 8 in a step of 2. 

    var_1 = 1
    print(f"Variable : {var_1}") #f strings allow variables to be apart of the string
    print("{1}{0}{1}".format("cad","abra")) #prints abracadabra
    print(",".join(["spam", "eggs", "ham"])) #prints "spam, eggs, ham"
    print("Hello ME".replace("ME", "world")) #prints "Hello world"
    print("Hello World".count("l")) #prints 3
    print("This is a sentence.".startswith("This")) #prints "True"
    print("This is a sentence.".endswith("sentence.")) #prints "True"
    print("This is a sentence.".upper()) #prints "THIS IS A SENTENCE."
    print("AN ALL CAPS SENTENCE".lower()) #prints "an all caps sentence"
    print("hello world".capitalize()) #prints " Hello world"
    print("hello world".title()) #prints "Hello World"
    print("spam, eggs, ham".split(", ")) #prints "['spam', 'eggs', 'ham']"
    print("hello   ".rstrip()) #prints "hello", removes leading white space
    print("12345".isdigit()) #prints True if the string is made of numbers only
    print("Hello".isalpha()) #prints True is the string is made of letters only
    print("Hello123".isalnum()) #prints True is string is made of only alphanumeric characters
    print("Hello".center(10,"-")) #prints "--Hello--"
    print("Hello".ljust(10,"-")) #prints "Hello----"
    print("Hello".rjust(10,"-")) #prints "----Hello"

################### Set Functions #############################################
    set_1 = {1,2,3} #Creates a set, in which dulpicate elements cannot exist
    set_2 = {4,5,6}
    set_1.add(4) #Adds 4 to the set
    set_1.remove(1) #Removes 1 from the set
    
    set_1 | set_2 #Set_1 OR Set_2
    set_1 & set_2 #Set_1 AND Set_2
    set_1 - set_2 #Set_1 but not Set_2
    set_1 ^ set_2 #Set_1 XOR set_2

################# Tuple Functions #############################################
    tuple1 =(1,2,3)
    a,b,c = tuple1 #sets a=1 b=2 c=3
    a,*b = tuple1 # *b takes the rest of the tuples values

    a=1 if b>=5 else 10 # a=1 if true, if false, a=10   
################### Numerical Functions #######################################

print(min(1, 2, 3, 4, 0, 2, 1)) #finds the minimum value in a list
print(max([1, 4, 9, 2, 5, 6, 8])) #finds the maximum value in a list
print(abs(-99)) #finds the absolute value 
print(round(99.1234,2)) #round the number to 2dp
print(sum([1, 2, 3, 4, 5])) #sums all the items in the list
 
################ Functional Programming ########################################
def func_1(x):    
    if 1==1:
        return(x) #Returns a value and ends the current function.
    double = (lambda x: 2*x)(5) #creates a simple function with x value 5  
    
    list(map(double,nums)) #map takes a function and applies it to each value in the list 
    list(filter(lambda x: x%2==0, nums)) #filter removes any values which don't hold true to the function 

    yield(x) #used in functions to return multiple values without leaving the loop (used to iterate)

    ### We use decorators to 'decorate' functions (adding extra features)
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
@decor
def print_text():
    print("Hello world!")
print_text()

    ### We can also call functions within themselves, this is called recursion
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))

def function1(*args): # * allows for any number of args, given as a tuple 'args'
    pass
def function2(food="spam"): # giving a default value, means a value doesnt need to be given.
    pass
def function3(**args): # ** returns a dictionary with name and values
    pass
function3(a=1,b=2,c=3)
def function4(arg:int) -> int: #ensures arg is an int and ensures the output is an int
    '''
    can be accessed through function4.__doc__
    Used to explain what the function does,
    Parameter Information
    Configuration 
    '''


################# Object Orientated Programming ######################
#4 principles:
#1. Inheritence 
#2. Polymorphism
#3. Abstraction
#4. Encapsulation

class Cat: #class is used to create objects 
    'Contents of __doc__'
               ##Functions in the class are known as methods
               ##All methods must have first parameter self
    def __init__(self,colour): # __init__ is a method called when an object is created 
        self.colour = colour
        self._colours = colour # _colours is a semi private variable
        self.__colors = colour # __colors is a private variable, to access outside of the class, use _Cat__colors
    def meow(self):
        passur = self.colour #self sets a value to the attribute of the object
    def __add__(self, other): # There are other 'magic' methods such as __add__ which reassigns +
        return(Cat)
#Types of Magic methods include:
#__add__
#__sub__
#__str__
#__lt__
#__le__
#__eq__


felix = Cat("ginger") #This is an object 
felix.colour #returns the value 'ginger'
felix.meow #runs the meow method for felix attributes
hasattr(felix, meow) #checks to see if object has given attribute
delattr(felix, meow) # deletes attribute

issubclass(sub, sup) #Checks to see if 'sub' is a subclass of 'sup'
isinstance(obj, cls_1) #Checks to see if object is in class of subclass

Cat.__doc__ #Returns class description
Cat.__name__#Returns class name
Cat.__module__#Returnsdule the class came from eg. __main__


class persian(Cat): #having a class as an attribute gives it all the properties of that class
    def __init__(self,colour):
        super.__init__(colour) #super is used to call methods from superclasses

    @classmethod #runs a special case for the class
    def new_meow(cls, meow):
        return cls(meow)
    pass
        
    @staticmethod #like a normal function except it can be called from a class instnace
    def old_meow(meow):
        return(meow)

    @property #Provides a way to customize access to attributes (makes it read only)
    def meow_allowed(self):
        return False

    @meow_allowed.setter #Sets the corresponding property's value 
    def meow_allowed(self, value):
        self.meow_allowed = True

    @meow_allowed.getter #Gets the corresponding property's value
    def meow_allowed(self):
        pass

if __name__ == "__main__": # only runs if the file isnt imported
    pass

############ Data Structures ####################

class Stack: #First in Last Out
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
class Queue: #First in First out
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

#Linked list
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()

#graph
class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

##################### Testing ##################
#run in bash 
#python3 -m pytest <testfile> --cov= <directory>/<file to test> --cov-report html

############# Automatic Doccumentation ##########

#-m pydoc -w <Filename>



# 3rd-party libraries web-based
# Django , CherryPy , Flask , BeautifulSoup
# 3rd-party libraries math-based
# matplotlib , NumPy , SciPy
# 3rd-party libraries game-based
# pygame , Panda3D

############# Importation #######################
    from random import randint as randint
    # import is used to open a library of additional functions
    # from allows for specific functions to be taken out od the library
    # as allows for a new name allocation of the function 

############## sys ##############################
    import sys
    for line in sys.stdin: #Gets inputs from the user 
        sys.stdout.write(line) #Outputs the variable 'line'
        print(line, file = sys.stderr) #outputs 'line' as an error
############### pdb #############################
    import pdb

    pdb.set_trace() # open the pdb command prompt
    #where # tells which line you're on
    #list #shows the line  you're on
    #s - Step, execute until next line
    #n - Next, execute until next line (doesn't step into functions)
    #p - print value of reference or variable.
    #ll - list all lines of current file or function    
    #b num - Break execution at line num
    #c - Continue execution until next breakpoint
    #q - Quit
    #retval #print the return of the last function
    

############## itertools ########################
    import itertools as it
    #Infinite Iterations:
    it.count(3,2) #increments by 2 from 3 to infinity unless stopped 
    it.cycle("hello") #cycles through lists and strings infinitely 
    it.repeat(7,3) #repeats the number 7 3 times or infinitely with no 3 

    #Combinatoric Iterators:
    it.product("ABCD", repeat=2) #iterates through all of the possibile combinations in the form of tuples
    it.permutations("ABCD",2) #iterates through all of the permutations (moving values, not creating or destroying)
    it.combinations("ABCD",2) #iterates all combinations (perm but order doesnt matter)
    it.combinations_with_replacement("ABCD",2) #combinations but repeat values are allowed
    
    #Normal Iterations
    it.accumulate(range(8)) #iterates through the cummulative values eg, 1,3,6,10,etc
    it.compress("ABCD",[1,0,0,1]) #iterates through "ABCD" only when the list is a 1 eg, AD
    it.takewhile(lambda x: x<5, [1,4,6,5,2]) # Iterates values until the statement is True
    it.dropwhile(lambda x: x<5, [1,4,6,5,2]) # Iterates from the first value to return True   
    it.islice("ABCD",2,None,1) #iterates starting from 2 ending at None with step 1
    it.pairwise("ABCD") #iterates through the pairs AB BC CD
    it.zip_longest("ABCD","XY", fillvalue=".")
############## re #######################
    import re

    r"spam" #Creates a raw string
    r"gr.y" # . matches with any character
    r"^gr.y$" # ^ implies what it starts with $ what it ends with
    r"[aeiou]" # [] provides a way to match only one of a set of characters
    r"[A-Za-z]" # matches a letter of any case
    r"[^A-Z]" # ^ inverts the group. matching everything outside of it
    r"spam(egg)*" # * allows for zero or more repititions of 'egg'
    r"gra(y)+" # + allows one or more repititions
    r"ice(-)?cream" # ? allows zero or one repititions 
    r"abc{1,5}" # {} allows 1 to 5 repititions
    r"gr(a|e)y" # | behaves as an or operator
    r"(.+) \1" # \1 matches expression of group number 1
    r"\d\s\w" #\d is 1 digit, \s is 1 whitespace, \w is one character
    r"\D" #capital versions give the opposite result
    r"\A\Z\b" #\A \z anchors beginning and end of string, \b space or special character at start or end of string
    Re1 = re.compile(r"H..E..") #used to create an rstring object
    Str2 = "H....3"
    Str1 = "Hwllo"
    m1 = Re1.match(Str2) #see if the start of Str2 matches rStr1 at any point
    Re1.search(Str2) #looks to see if rStr1 is anywhere within Str2
    Re1.findall(Str2) #Creates a list of all the instances where rStr1 is in Str2
    Re1.finditer(Str2) #Returns the amount of times rSrt1 appears in Str2
    
    m1.group() #Returns the string matched
    m1.start() #Returns the starting position of the first match
    m1.end() #Returns the end position of the first match
    m1.span() #Returns a tuple of the start and end position of the first match
    Re1.sub(Str1,Str2,count=Int1) #Replaces Int1 instances of matches in Str1 with Str2 
 
############# random ##############################
    import random as rng
    #Integer Random Operators
    rng.randrange(Num1,Num2,Num3) #Randomly selects a number in range (Start,Stop,Step)
    rng.randint(Int1,Int2) #Selects an integer between 1 and 10
    rng.random(Num1,Num2) #Returns Random float in range

    #List Random Operators
    rng.choice(Lst1) #Returns random element from list
    rng.shuffle(Lst1) #Shuffles List
    
    #Distribution Operators
    rng.uniform(Num1,Num2) #Return a value from the uniform distribution
    rng.triangular(Low,High,Mode) #Return a value from the uniform triangle
    rng.betavariate(alpha,beta) #Return a value from the beta distribution
    rng.expovariate(alpha) #Return a value from the exponential distribution
    rng.gammavariate(alpha,beta) #Return a value from the gamma distribution
    rng.gauss(mu,sigma) #Return a value from the normal distribution
    rng.lognormvariate(mu,sigma) #Return a value from the log normal distribution


############# NumPy ###############################
    import numpy as np
    #Matrix Creation
    matrix = np.array([ListA,ListB,ListC]) #all lists must be same length
    Mat1 = matrix = np.zeros(Int1,Int2) # Makes Int1 by Int2 matrix full of zeros
    Mat2 = matrix = np.ones(Int1,Int2) # Makes matrix of ones
    matrix = np.linspace(Num1,Num2,Int1) #creates a matrix of equally spaced elements between 'NumA' and 'NumB'
    matrix = np.arrange(Int1).reshape(Int2,Int3) #Iterates through each element of IntA, in formation IntB,IntC matrix
    matrix = np.func1(Mat1) #Applies the function to all elements of MatA
    rg = np.random.default_rng(1) # Used as a random generator
    matrix = rg.randon((2,3)) #Produces random elements between 0-1
    
    Mat1 * Mat2 #Element multiplication
    Mat1 @ Mat2 #Matrix multiplication
    Mat1.sum() #Sums all the elements in the matrix
    Mat1.cumsum()
    Mat1.max(axis=0) #Max of each column
    Mat1.min(axis=1) #Min of each row

    matrix[2,3] #Outputs the element in row 2 column 3
    matrix[0:5,1] #Outputs column 1 in rows 0-4
    matrix[:,2] #Outputs column 2 in all rows
    matrix[2,...] #Outputs same as matrix[2,:,:,:,...]

    for row in matrix: #Iterates through the first axis of the matrix
        pass
    for element in matrix.flat: #iterates through the elements
        pass

    matrix.ndim # Number of dimensions of the array
    matrix.shape # Returns a Tuple with row and column 
    matrix.size # Returns the total number of elements


############# tkinter #############################
    # Used to Create basic window applications easily
    import tkinter as tk

    root = tk.Tk(className='calc') #Creates a new window witht title calc
    root.title("Calculator") #Names the window calculator 

    My_label = tk.Label(root, text = "Hello World") #Creates Label

    My_button = tk.Button(root, text="click me", state="disabled", padx=50, pady=50, fg = "orange", bg ="#ffffff",  command=Function) 
    #Creates a button which isn't clickable, padx,y increases the size of the button
    #command is used to select a function which the button should run when it is pressed
    #fg and bg makes the foreground and background, orange and purple 

    Text_Box = tk.Entry(root, width = 10, height = 10, borderwidth = 10)
    Text_Box.get() #takes the string from the text box
    Text_Box.insert(0, "I AM A TEXT BOX") #adds text to the text box 

    My_label.pack() #Displays it on screen in the first open spot
    My_label.grid(row=0, column=0) #places in a grid order

    My_button.destroy() #Removes the button

    root.mainloop() #Opens the window
    
########### PIL #######################
    #used for image editing and creation 
    import PIL

    New_Image = PIL.Image.new(mode = "RGB", size = (1000,1000))
    # This creates a new png file, Default Black. 

    Old_Image = PIL.Image.open("Path to png file")

    Image_Copy = New_Image.copy()
    #Copies an image

    New_Image.paste(Image_Copy, (100,100))
    #pastes the image onto the newly created one starting on pixel (100,100) 
    
    New_Image.save("Path to png file")
    #Saves the image to a new file location
########### os ########################
    import os
  
    if os.path.exists("Path to file") == True:
        pass
    #checks if a file exists in a given location

########### Flask ##########################
import flask as fl

app = fl.Flask(__name__)  #creates a Flask app object
    
app.run(debug=True, host='0.0.0.0') #runs the app (in debug mode) host is usually local by default, by setting to 0.0.0.0 allows for all traffic

@app.route('/Path', methods=['GET','POST']) #sets an endpoint to the app with specific request methods
@app.route('/Path/<int:num>') #used to collect an integer variable out of the URL
def index(num:int): 
    return('Random Name Generator <br> This is a newline') #displays on page, with html elements also!
    
fl.request.method() #used to see which method is being used
fl.request.args.get()
fl.redirect('http://www.google.com') #redirects to a different webpage
fl.url_for("index") #returns a URL inbuilt page based on function name
     
    #type: mysql+pymysql:// 
    #user:pass : root:password
    #location: @localhost:3306
    #exact db: /world
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/world' #databses from mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #in-built databases into the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') #private as database is added through console
    #all used to add a databse to the webpage

fl.render_template('index.html' name='John') #used to display html file

################## flask_sqlalchemy
import flask_sqlalchemy as fl_sql

db = fl_sql.SQLAlchemy(app) #creates a database object

class Family(db.Model): #functions as a table in a database
    id = db.Column(db.Integer, primary_key=True)
    fam_name = db.Column(db.String(30), nullable=False)
    people = db.relationship('Person',backref='familybr') #used to define relationships between tables
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Athena")
    alive = db.Column(db.Boolean, nullable=False)
    fam_id = db.Column(db.Integer,db.ForeignKey('family.id'), nullable=False) #sets up a foreign key with the family db
    
new_fam = Family(fam_name='Martin') #create new family object 
db.session.add(new_fam) #add new record to db
db.session.commit() #commit changes

new_person = Person(first_name='Athena',alive=True, familybr=new_fam)
db.session.add(new_person)
db.session.commit()

all_people = Person.query.all() #return a list of all people as objects of type Person
first_person = Person.query.first() #return the first entry in the table
johns = Person.query.filter_by(first_name="John").all() #filters all result with first name John
person_with_id_1 = Person.query.get(1) #returns person with id 1
person_in_order = Person.query.order_by(Person.name.desc()).all() #order by Person name in descending order
first_2_people = Person.query.limit(2).all() #returns first 2 people
number_of_people = Person.query.count() #returns number of people in db

#Updating records
first_person = Person.query.first()
first_person.first_name = "New name"
db.session.commit()

#Deleting records
person_to_delete = Person.query.first()
db.session.delete(person_to_delete)
db.session.commit()

############ wtforms ##################
import flask_wtf as fwtf
import wtforms as wt
import wtforms.validators as wtv
class PersonForm(fwtf.FlaskForm): #Creates a form
    name = wt.StringField("Name: ") #creates a string input field
    age = wt.IntegerField("Age: ",validators=[wtv.DataRequired(),wtv.Length(min=2,max=10)]) #validators are used to check the field follows rules
    hair_col = wt.SelectField("Breed: ",choices=[('Brown','Brown'),('Blonde','Blonde')]) #sleectfield stores the first word chosen, and displays the second to the user as the choice
    username = wt.StringField("username")
    submit = wt.SubmitField("Submit")

#Validation Methods
    def validate_usernamer(self,username): 
        if username.data.lower() == 'admin':
            raise wtv.ValidationError("Can't use admin as username")
        
class checkAdmin:
    def __init__(self, message=None):
        if not message:
            message = 'please choose another username'
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() =='admin':
            raise wtv.ValidationError(self.message)

###### Flask_testing
import flask_testing as ft

class TestBase(ft.TestCase): #Setup up mock app for testing

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///testdata.sqlite', #uses test db
            DEBUG=True,
            WTF_CSFR_ENABLED=False) #turns off secret key and 
        
        return app
    
    def setup(self):
        db.create_all()

        #Test data
        test_person = Person('Athena',True)
        db.session.add(test_person)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self): 
        response = self.client.get(fl.url_for('index'))
        self.assertEqual(response.status_code,200) #tests get req to index route, status code = 200 if running properly
        self.assertIn('checks if this is in the page',response.data.decode()) #checks to see if the text is in the page

class TestCrud(TestBase):

    def test_person_form_post(self):
        response = self.client.post(fl.url_for('person_form_method'), data = dict(first_name='Athena',alive=True))
        
        obj1 = Person.query.filter_by(name='Athena').first()
        self.assertEqual(obj1.name, 'Athena') #see's if object has been created with the name




Function() #Calls the function