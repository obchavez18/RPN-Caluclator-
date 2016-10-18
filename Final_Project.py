from Tkinter import *
import math
'''Import Tkinter and math module'''

master = Tk()
e=Entry(master)
l = Label(master, text='RPN CALCULATOR')
l.grid(row=0, columnspan=2)
e.grid(row=0, columnspan = 7)
'''create the GUI containg the ENTRY slot'''

def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval=' Objet tpe connot be converted to float'
    return retval        
#---------------------------CODE for the core functions----------------------#
def op():
    '''Takes and stores the first input'''
    global n1
    try:
        n1=e.get()
        n1=safe_float(n1)
        e.delete(0,END)
    except:
        e.insert(0,'MATH ERROR')
    
def addequals():
    '''It takes the second input, and then adds
       it with the first input, and returns the total value'''
    try:
        n2=e.get()
        n2=safe_float(n2)
        e.delete(0,END)
        v=(n1+n2)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(v))

def subequals():
    '''It takes the second input, and then subtracts
       it with the first input, and reutrns the total value'''
    try:
        n2=e.get()
        n2=safe_float(n2)
        e.delete(0,END)
        v=(n1-n2)
    except:
        e.insert(0, 'MATH ERROR')
    else:
        e.insert(0,str(v))

def mulequals():
    '''It takes the second input, and then mulitplies
     it with the first input, and returns the total value'''
    try:
        n2=e.get()
        n2=safe_float(n2)
        e.delete(0,END)
        v=(n1*n2)
    except:
        e.insert(0, 'MATH ERROR')
    else:
        e.insert(0,str(v))

def divequals():
    '''It takes the second input, and then divides
       it with the first input, and returns the total value'''
    try:
        n2=e.get()
        n2=safe_float(n2)
        e.delete(0,END)
        v=(n1/n2)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(v))

def modequals():
    '''It takes teh second input, and then modules
       it with the first input, and returns the total value'''
    try:
        n2=e.get()
        n2=safe_float(n2)
        e.delete(0,END)
        v=(n1%n2)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(v))


#---------------------------CODE for the miscellaneous functions-------------#



def sqt():
    '''It takes the first input and returns the square root of the given input''' 
    n1 = e.get()
    e.delete(0, END)
    n1= safe_float(n1)
    try:
        n= math.sqrt(n1)
    except:
        e. insert(0,'MATH ERROR')
    else:
        e.insert(0,str(n))
    

def s():
    '''It takes the first input and returns the sine of the given input'''
    n1=e.get()
    e.delete(0,END)
    n1= safe_float(n1)
    try:
        n= math.sin(n1)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(n))

def c():
    '''It takes the first input and returns the cose of the given input'''
    n1= e.get()
    e.delete(0,END)
    n1= safe_float(n1)
    try:
        n = math.cos(n1)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0, str(n))

def t():
    '''It takes the first input and returns the tangent of the given input'''
    n1= e.get()
    e.delete(0,END)
    n1=safe_float(n1)
    try:
        n=math.cos(n1)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0, str(n))

def pie():
    '''reutrns the value of pie'''
    n= math.pi
    e.insert(0, str(n))

def ex():
    '''returns the value of e'''
    n = math.e
    e.insert(0, str(n))

def lug():
    '''It takes the first input and returns the log10 of the given input'''
    n1=e.get()
    e.delete(0,END)
    n1 = safe_float(n1)
    try:
        n = math.log10(n1)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(n))

def pow2():
    '''It takes the first input and returns the power of second degree of the given input'''
    n1=e.get()
    e.delete(0,END)
    n1=safe_float(n1)
    try:
        n = math.pow(n1,2)
    except:
        e.insert(0,'MATH ERROR')
    else:
        e.insert(0,str(n))

def pm():
    '''It takes the first input and returns *-1 value of the given input '''
    n1=e.get()
    e.delete(0,END)
    n1= safe_float(n1)
    if n1 <0:
        n=n1*(-1)
    elif n1>0:
        n=n1*(-1)
    else:
        pass
    try:
        e.insert(0,str(n))
    except:
        e.insert(0,'0')


'''The assignment of the buttons with its functions and locations'''    
#-----------------ROW #0 BUTTON----------------------------------------------#
bop=Button(master, text='ENTER', width=12, command=op).grid(row=0, column=4)
        

#------------------ROW #1 BUTTONS--------------------------------------------#
    
bc= Button(master, text=('clear'), width = 10, command= lambda:e.delete(0,END)).grid(row=1, column=0)
b7 = Button(master, text="7", width=10, command=lambda:(e.insert(END,'7'))).grid(row=1, column=1)
b8 = Button(master, text="8", width=10, command=lambda:(e.insert(END,'8'))).grid(row=1, column=2)
b9 = Button(master, text="9", width=10, command=lambda:(e.insert(END,'9'))).grid(row=1, column=3)
bmule=Button(master, text='x', width=10, command = mulequals).grid(row=1, column=4)

#--------------------ROW #2 BUTTONS------------------------------------------#
bsqt=Button(master, text='sqrt', width= 10, command =sqt).grid(row=2, column=0)
b4 = Button(master, text="4", width=10, command=lambda:(e.insert(END,'4'))).grid(row=2, column=1)
b5 = Button(master, text="5", width=10, command=lambda:(e.insert(END,'5'))).grid(row=2, column=2)
b6 = Button(master, text="6", width=10, command=lambda:(e.insert(END,'6'))).grid(row=2, column=3)
bdive=Button(master, text='/', width =10, command=divequals).grid(row=2, column=4)

#---------------------ROW #3 BUTTONS------------------------------------------#
bpie=Button(master, text='pi', width=10, command= pie).grid(row=3, column=0)
b1 = Button(master, text="1", width=10, command=lambda:(e.insert(END,'1'))).grid(row=3, column=1)
b2 = Button(master, text="2", width=10, command=lambda:(e.insert(END,'2'))).grid(row=3, column=2)
b3 = Button(master, text="3", width=10, command=lambda:(e.insert(END,'3'))).grid(row=3, column=3)
bpluse=Button(master, text='+', width=10, command = addequals). grid(row=3, column=4)

#--------------------ROW #4 BUTTONS------------------------------------------3
bex=Button(master, text='e', width = 10, command= ex).grid(row=4, column=0)
bsin=Button(master, text ='sin', width =10, command= s).grid(row=4, column=1)
bcos=Button(master, text='cos', width = 10, command =c).grid(row=4, column=2)
btan=Button(master, text='tan', width = 10, command = t).grid(row=4, column=3)
bsube=Button(master,text='-', width =10, command=subequals).grid(row=4, column=4)

#---------------------ROW #5 BUTTONS------------------------------------------#
bpow2=Button(master, text='pow2', width =10, command = pow2).grid(row=5, column=0)
b0 = Button(master, text="0", width=10, command=lambda:(e.insert(END,'0'))).grid(row=5, column=1)
blug=Button(master, text = 'log10', width =10, command=lug).grid(row=5, column=2)
bpm=Button(master, text='+/-', width=10, command= pm).grid(row=5, column=3)
bmedo=Button(master, text='%',width=10,command=modequals).grid(row=5,column=4)

#------------------------MAINLOOP-----------------------------------------------#
master.mainloop()
