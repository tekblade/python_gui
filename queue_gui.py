from tkinter import *
from collections import *
from sys import *
from datetime import *
from time import *
from random import *
from tkinter.messagebox import *
from threading import *

class List1:

        def __init__(self):
                self.listA=[]
                self.listB=[]
                self.listVipA=[]
                self.listVipB=[]
                self.aCount=0
                self.bCount=0
                self.vipACount=0
                self.vipBCount=0

        def addA(self, x):
                self.aCount += 1
                self.listA.append(x + 1)
                

        def addB(self, x):
                self.bCount += 1
                self.listB.append(x + 1)
                

        def addVipA(self, x):
                self.vipACount += 1
                self.listVipA.append(x + 1)
                

        def addVipB(self, x):
                self.vipBCount += 1
                self.listVipB.append(x + 1)
                

        def returnA(self):
                return self.aCount

        def returnB(self):
                return self.bCount

        def returnVipA(self):
                return self.vipACount

        def returnVipB(self):
                return self.vipBCount

        def isEmptyA(self):
                if len(self.listA) == 0:
                        return True
                else:
                        return False

        def isEmptyB(self):
                if len(self.listB) == 0:
                         return True
                else:
                        return False
        
        def isEmptyVipA(self):
                if  len(self.listVipA) == 0:
                        return True
                else:
                        return False

        def isEmptyVipB(self):
                if  len(self.listVipB) == 0:
                        return True
                else:
                        return False

        def allocate(this_object, a):   # function retierves as argument to the specified queue
                b=0
                if a == 1:
                        b=this_object.returnA()
                        this_object.addA(b)
                elif a == 2:
                        b=this_object.returnB()
                        this_object.addB(b)
                elif a == 3:
                        b=this_object.returnVipA()
                        this_object.addVipA(b)
                elif a == 4:
                        b=this_object.returnVipB()
                        this_object.addVipB(b)
                else:
                        pass



class Client():
        list1=List1()

        def __init__(self):
                self.case = 0
 
        
           
                
class ClientA(Client):

        def __init__(self):
                super(ClientA, self).__init__()

class ClientB(Client):

        def __init__(self):
                super(ClientB, self).__init__()

class ClientVipA(Client):

        def __init__(self):
                super(ClientVipA, self).__init__()

class ClientVipB(Client):

        def __init__(self):
                super(ClientVipB, self).__init__()
                
        
                
def checkA():
        global end
        t=Timer(0.001, checkifA)
        t.start()
        if end == 1:
                t.cancel()


def checkB():
        global end
        t=Timer(0.001, checkifB)
        t.start()
        if end == 1:
                t.cancel()
        
        
        
def end(): #######################################################################################################
        global end
        end = 1
        del Client.list1.listA[:]
        del Client.list1.listB[:]
        del Client.list1.listVipA[:]
        del Client.list1.listVipB[:]
        exit(0)

def checkifA():
        sec=0
        while 1:
                if not Client.list1.isEmptyVipA():
                        client=Client.list1.listVipA[0]
                        while sec <= 10:
                                sleep(1)
                                sec += 1
                        if Client.list1.isEmptyVipA():
                                pass                
                        else:
                                if Client.list1.listVipA[0] == client:
                                        showinfo("Skandal", "To skandaliczne Klient Vip A czeka dłużej niż 10 sekund")
                                        sec=0
                                while not Client.list1.isEmptyVipA() and Client.list1.listVipA[0] == client:
                                        pass
                        
                        
                
def checkifB():
        sec=0
        while 1:
                if not Client.list1.isEmptyVipB():
                        client=Client.list1.listVipB[0]
                        while sec <= 10:
                                sleep(1)
                                sec += 1
                        if Client.list1.isEmptyVipB():
                                pass
                        else:
                                if Client.list1.listVipB[0] == client:
                                        showinfo("Skandal", "To skandaliczne Klient Vip B czeka dłużej niż 10 sekund")
                                        sec=0
                                while not Client.list1.isEmptyVipB() and Client.list1.listVipB[0] == client:                                       
                                       pass
                                
                        
                
                        




def radiobutton():
        pool = var.get()
        return pool

def button():
        global clicked
        client = radiobutton()
        if client == 1:
                Client.list1.allocate(client)

        elif client == 2:
                Client.list1.allocate(client)

        elif client == 3:
                Client.list1.allocate(client)

        elif client == 4:
                Client.list1.allocate(client)

        else:
                print('wystąpił błąd')


        varA.set(Client.list1.returnA())
        varB.set(Client.list1.returnB())
        varVipA.set(Client.list1.returnVipA())
        varVipB.set(Client.list1.returnVipB())
        print('Init value ' + str(ClientA.list1.returnA()) + " " + str(ClientB.list1.returnB()) + " " + str(ClientVipA.list1.returnVipA()) + " " + str(ClientVipB.list1.returnVipB()))
        print(ClientA.list1.listA)
        print(ClientB.list1.listB)
        print(ClientVipA.list1.listVipA)
        print(ClientVipB.list1.listVipB)
        if clicked == 0:
                checkB()
                checkA()
                clicked = 1

def firstbutton():
        
        random = randint(1, 2)
        if random == 1: 
                if not Client.list1.isEmptyVipA():
                        windowCountA = Client.list1.listVipA.pop(0)
                        windowTypeA = "Vip A: "
                elif not Client.list1.isEmptyVipB():
                        windowCountA = Client.list1.listVipB.pop(0)
                        windowTypeA = "Vip B: "
                elif not Client.list1.isEmptyA():
                        windowCountA = Client.list1.listA.pop(0)
                        windowTypeA = "A: "
                elif not Client.list1.isEmptyB():
                        windowCountA = Client.list1.listB.pop(0)
                        windowTypeA = "B: "
                else:
                        windowCountA = ""
                        windowTypeA = "Empty lists"
        else:
                if not Client.list1.isEmptyVipB():
                        windowCountA = Client.list1.listVipB.pop(0)
                        windowTypeA = "Vip B: "
                elif not Client.list1.isEmptyVipA():
                        windowCountA = Client.list1.listVipA.pop(0)
                        windowTypeA = "Vip A: "
                elif not Client.list1.isEmptyB():
                        windowCountA = Client.list1.listB.pop(0)
                        windowTypeA = "B: "
                elif not Client.list1.isEmptyA():
                        windowCountA = Client.list1.listA.pop(0)
                        windowTypeA = "A: "
                else:
                        windowCountA = ""
                        windowTypeA = "Empty lists"
                
                        

        a = windowTypeA + str(windowCountA)
        firstWindow.set(a)

def secoundbutton():

        random = randint(1, 2)
        if random == 1:
                if not Client.list1.isEmptyVipA():
                        windowCountB = Client.list1.listVipA.pop(0)
                        windowTypeB = "Vip A: "
                elif not Client.list1.isEmptyVipB():
                        windowCountB = Client.list1.listVipB.pop(0)
                        windowTypeB = "Vip B: "
                elif not Client.list1.isEmptyA():
                        windowCountB = Client.list1.listA.pop(0)
                        windowTypeB = "A: "
                elif not Client.list1.isEmptyB():
                        windowCountB = Client.list1.listB.pop(0)
                        windowTypeB = "B: "
                else:
                        windowCountB = ""
                        windowTypeB = "Empty lists"
        else:
                if not Client.list1.isEmptyVipB():
                        windowCountB = Client.list1.listVipB.pop(0)
                        windowTypeB = "Vip B: "
                elif not Client.list1.isEmptyVipA():
                        windowCountB = Client.list1.listVipA.pop(0)
                        windowTypeB = "Vip A: "
                elif not Client.list1.isEmptyB():
                        windowCountB = Client.list1.listB.pop(0)
                        windowTypeB = "B: "
                elif not Client.list1.isEmptyA():
                        windowCountB = Client.list1.listA.pop(0)
                        windowTypeB = "A: "
                else:
                        windowCountB = ""
                        windowTypeB = "Empty lists"
                
                
      
                

        b = windowTypeB + str(windowCountB)
        secoundWindow.set(b)
        
def thirdbutton():

        if random == 1:
                if not Client.list1.isEmptyVipA():
                        windowCountC = Client.list1.listVipA.pop(0)
                        windowTypeC = "Vip A: "
                elif not Client.list1.isEmptyVipB():
                        windowCountC = Client.list1.listVipB.pop(0)
                        windowTypeC = "Vip B: "
                elif not Client.list1.isEmptyA():
                        windowCountC = Client.list1.listA.pop(0)
                        windowTypeC = "A: "
                elif not Client.list1.isEmptyB():
                        windowCountC = Client.list1.listB.pop(0)
                        windowTypeC = "B: "
                else:
                        windowCountC = ""
                        windowTypeC = "Empty lists"
        else:
                if not Client.list1.isEmptyVipB():
                        windowCountC = Client.list1.listVipB.pop(0)
                        windowTypeC = "Vip B: "
                elif not Client.list1.isEmptyVipA():
                        windowCountC = Client.list1.listVipA.pop(0)
                        windowTypeC = "Vip A: "
                elif not Client.list1.isEmptyB():
                        windowCountC = Client.list1.listB.pop(0)
                        windowTypeC = "B: "
                elif not Client.list1.isEmptyA():
                        windowCountC = Client.list1.listA.pop(0)
                        windowTypeC = "A: "
                else:
                        windowCountC = ""
                        windowTypeC = "Empty lists"
                
        
                
                
        c = windowTypeC + str(windowCountC)
        thirdWindow.set(c)
        

end = 0        
clicked = 0
timer = 0
random = 0       
clientA = ClientA()
clientB = ClientB()
clientVipA = ClientVipA()
clientVipB = ClientVipB()
root=Tk()
root.title("Kolejka")
var = IntVar()

varA = IntVar(0)  # liczba osób w kolejce do wyświetlenia w Label
varB = IntVar(0)
varVipA = IntVar(0)
varVipB = IntVar(0)

windowCountA = 0
windowTypeA = "kolejka pusta"
windowCountB = 0
windowTypeB = "kolejka pusta"
windowCountC = 0
windowTypeC = "kolejka pusta"

timer = 0

topframe = Frame(root, width=60)
topframe.pack()
underframe = Frame(root)
underframe.pack(side=BOTTOM)

firstWindow = StringVar()
secoundWindow = StringVar()
thirdWindow = StringVar()
firstWindow.set("okno puste")
secoundWindow.set("okno puste")
thirdWindow.set("okno puste")

R1 = Radiobutton(topframe, text="Client A", variable=var, value=1, command=radiobutton)
R2 = Radiobutton(topframe, text="Client B", variable=var, value=2, command=radiobutton)
R3 = Radiobutton(topframe, text="Client Vip A", variable=var, value=3, command=radiobutton)
R4 = Radiobutton(topframe, text="Client Vip B", variable=var, value=4, command=radiobutton)
B=Button(underframe, text="Przycisk dodający wybraną osobę do kolejki", command=button, width=60)
KK=Button(underframe, text="Zakończ", command=end, width=60, relief=GROOVE)
L = Label(underframe, text="liczba oczekujących osób w poszczególnych kolejkach", fg="red2", bg="blue2", width=60)
LL = Label(underframe)
MM = Label(underframe)
WW = Label(underframe)
BB = Label(underframe)
R1.pack(side=LEFT)
R2.pack(side=LEFT)
R3.pack(side=LEFT)
R4.pack(side=LEFT)
KK.pack(side=BOTTOM)
BB.pack(side=BOTTOM) # przyciski
B1 = Button(BB, text="kolejny do okienka 1", width=20, height=5, relief=GROOVE, command=firstbutton)
B1.grid(row=0, column=0)
B2 = Button(BB, text="kolejny do okienka 2", width=20, height=5, relief=RAISED, command=secoundbutton)
B2.grid(row=0, column=1)
B3 = Button(BB, text="kolejny do okienka 3", width=20, height=5, relief=RIDGE, command=thirdbutton)
B3.grid(row=0, column=2)
WW.pack(side=BOTTOM) # która osoba w okienku
W1 = Label(WW, textvariable=firstWindow, width=20,justify=CENTER, bg="orchid1", height=5)
W1.grid(row=0, column=0)
W2 = Label(WW, textvariable=secoundWindow, width=20, justify=CENTER, bg="tan4", height=5)
W2.grid(row=0, column=1)
W3 = Label(WW, textvariable=thirdWindow, width=20, justify=CENTER, bg="pale green", height=5)
W3.grid(row=0, column=2)
M2 = Label(MM, text="A", width=15,justify=CENTER, bg="thistle1", height=5)
M2.grid(row=0, column=0)
MM.pack(side= BOTTOM) #liczba osób w kolejce
M1 = Label(MM, textvariable=str(varA), width=15,justify=CENTER, bg="thistle1", height=5)
M1.grid(row=0, column=0)
M2 = Label(MM, textvariable=str(varB), width=15,justify=CENTER, bg="red2", height=5)
M2.grid(row=0, column=1)
M3 = Label(MM, textvariable=str(varVipA), width=15,justify=CENTER, bg="OliveDrab1", height=5)
M3.grid(row=0, column=2)
M4 = Label(MM, textvariable=str(varVipB), width=15,justify=CENTER, bg="light slate blue", height=5)
M4.grid(row=0, column=3)
LL.pack(side = BOTTOM) # informacja
L1 = Label(LL, text="A", width=15,justify=CENTER, bg="goldenrod")
L1.grid(row=0, column=0)
L2 = Label(LL, text="B" , width=15, justify=CENTER, bg="SkyBlue2")
L2.grid(row=0, column=1)
L3 = Label(LL, text="VIP A", width=15, justify=CENTER, bg="forest green")
L3.grid(row=0, column=2)
L4 = Label(LL, text="VIP B", width=15, justify=CENTER, bg="LightPink1")
L4.grid(row=0, column=3)
L.pack(side=BOTTOM)

B.pack(side=BOTTOM)
root.mainloop()
