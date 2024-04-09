#Imports for functions and GUI
import random
from tkinter import *
import array

on = False # For form toggle

#Clears all entries and inserts random numbers (for testing and showcasing)
def populate():
    #Creates a seed based on current time, and generates numbers for each entry
    random.seed(version=2)
    f1 = random.randrange(2,10,1)
    f2 = random.randrange(1,100,1)
    f3 = random.randrange(1,100,1)
    f4 = random.randrange(1,100,1)

    #Deletes all current entries
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

    #Replaces all entries with the previously generated numbers
    e1.insert(0,f1)
    e2.insert(0,f2)
    e3.insert(0,f3)
    e4.insert(0,f4)
    return

#Final Calculation
def Calculate():
    try:
        if on:
            calc = (float(e2.get()) + float(e3.get()) + float(e4.get()))*int(e1.get())
            ans.delete(0,END)
            ans.insert(END,calc)  
        else:
            calc = (float(e2.get()) + float(e3.get()) + float(e4.get()))
            ans.delete(0,END)
            ans.insert(END,calc)
    except ValueError:
        sub = Toplevel(master)
        sub.geometry('300x100')
        sub.configure(bg="#E6DBD0")
        Label(sub, text='Something is wrong with your inputs!', fg='red').pack()
        Button(sub, text="OK", command=sub.destroy, bg="#439775", activebackground="grey").pack()
        return   
    
#Transmission Delay Calculation
def Trans():

    #Calculation for Transmission by user input
    def TCalc():

        result = 0 #Preperation for loop

        #Calculates Transmission speed using temp, and stores in results
        try: #Catches non float inputs and notifies user
            for x in range(len(rate)-1):
                temp = float(size.get())/float(rate[x].get())
                result = result + temp
        except ValueError: 
            sub2 = Toplevel(master)
            sub2.geometry('300x100')
            sub2.configure(bg="#E6DBD0")
            Label(sub2, text='There is an issue with your inputs!', fg='red').pack()
            Button(sub2, text="OK", command=sub2.destroy, bg="#439775", activebackground="grey").pack()
            return

        #returning result for user and cleanup
        e3.delete(0,END)    
        e3.insert(END,result)
        sub.destroy()

    #Creating and configuring subwindow
    sub = Toplevel(master)
    sub.geometry('600x300')
    sub.configure(bg="#E6DBD0")

    #finding amount of links used, and setting label
    size = Entry(sub)
    size.grid(row=0, column=1)
    Label(sub, text='Packet Size:').grid(row=0, column=0)

    #preparing array for loop for links
    try: #Ensures links are filled in before finishing the more "..." window
        l = int(e1.get())
    except:
        sub.destroy()
        sub2 = Toplevel(master)
        sub2.geometry('300x100')
        sub2.configure(bg="#E6DBD0")
        Label(sub2, text='Must include number of links to use "..."', fg='red').pack()
        Button(sub2, text="OK", command=sub2.destroy, bg="#439775", activebackground="grey").pack()
        return

    rate = [l]
    
    #Creats N enties for N links
    for x in range(l):
        rate.insert(x, Entry(sub))
        rate[x].grid(row=x, column=4)
        Label(sub, text='Rate of ').grid(row=x, column=2, sticky=E)
        Label(sub, text=x+1).grid(row=x, column=3)

    #creating button to initiate calculation (for when after user is finished inputting)
    savet = Button(sub, text="Enter", command=TCalc, bg="#439775", activebackground="grey")
    savet.grid(row=l+1, column =3)

#Propogation Delay Calculation
def Prop():

    #Calculates Propogatation Delay from user inputs
    def PCalc():

        result = 0 #Preperation for loop

        #user input for distance/prop speed added together using temp stored in result
        try: #Catches non float inputs and notifies user
            for x in range(len(distance)-1):
                temp = float(distance[x].get())/float(speed[x].get())
                result = result + temp
        except ValueError:
            sub2 = Toplevel(master)
            sub2.geometry('300x100')
            sub2.configure(bg="#E6DBD0")
            Label(sub2, text='There is an issue with your inputs!', fg='red').pack()
            Button(sub2, text="OK", command=sub2.destroy, bg="#439775", activebackground="grey").pack()
            return


        #Returning that data to the user and exiting SubWindow
        e4.delete(0,END)    
        e4.insert(END,result)
        sub.destroy()

    #Creating and configuring subwindow
    sub = Toplevel(master)
    sub.geometry('600x300')
    sub.configure(bg="#E6DBD0")

    #preparing array for loop for links

    try: # Ensures link entry is filled in before finishing the more "..." window
        l = int(e1.get())
    except:
        sub.destroy()
        sub2 = Toplevel(master)
        sub2.geometry('300x100')
        sub2.configure(bg="#E6DBD0")
        Label(sub2, text='Must include number of links to use "..."', fg='red').pack()
        Button(sub2, text="OK", command=sub2.destroy, bg="#439775", activebackground="grey").pack()
        return

    distance = [l]
    speed = [l]
    
    #Creats N enties for N links, and storing entries in array distance and speed
    for x in range(l):

        distance.insert(x, Entry(sub))
        speed.insert(x, Entry(sub))

        distance[x].grid(row=x, column=2)
        speed[x].grid(row=x, column=5)

        Label(sub, text='Length of ').grid(row=x, column=0, sticky=E)
        Label(sub, text=x+1).grid(row=x, column=1)

        Label(sub, text='Prop rate of ').grid(row=x, column=3, sticky=E)
        Label(sub, text=x+1).grid(row=x, column=4)

    #Button to initiate calculation (for when user is finished inputing)
    save = Button(sub, text="Enter", command=PCalc, bg="#439775", activebackground="grey")
    save.grid(row=l+1, column=4)

def Toggle():
    global on

    if on:
        on=False
        togLable.configure(text = 'Custom \n (Links will not be \nused in calculation)')
        moreTran.place(x=410, y=95)
        moreProp.place(x=410, y=145)
    else:
        on=True
        togLable.configure(text = 'L(Trans+Proc+Prop)')
        moreTran.place_forget()
        moreProp.place_forget()


#Creating and setting up main window
master = Tk() 
master.geometry('600x300')
master.configure(bg="#E6DBD0")
master.tk.call('tk', 'scaling', 1)

#Labels for each entry box
master.option_add("*Label*Background", "#E6DBD0")
master.option_add("*Label*Foreground", "#2F3E46")
Label(master, text='# of Links (Required for "..."):').place(x=0,y=0)
Label(master, text='Processing Delay:').place(x=0,y=50)
Label(master, text='Transmission Delay:').place(x=0,y=100)
Label(master, text='Propogation Delay').place(x=0,y=150)
Label(master, text='End to End Delay:').place(x=0,y=200)
togLable = Label(master, text = 'Custom \n (Links will not be \nused in calculation)')
togLable.place(x=522, y=160, anchor=CENTER)

#entry initialization for required inputs
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
ans = Entry(master)
 
#The entry placement for the required inputs
e1.place(x=200,y=0)
e2.place(x=200,y=50)
e3.place(x=200,y=100)
e4.place(x=200,y=150)
ans.place(x=200,y=200)


#Button setup
tog = Button(master, text="Form", command=Toggle, bg="#439775", activebackground="grey")
tog.place(x=500, y=100)

submit = Button(master, text="Calculate", command=Calculate, bg="#439775", activebackground="grey")
submit.place(x=260, y=250)

autoPop = Button(master, text="Auto Populate", command=populate, bg="#98473E", activebackground="grey")
autoPop.place(x=450, y=10)

moreTran = Button(master, text="...", command=Trans, bg="grey", activebackground="grey")
moreTran.place(x=410, y=95)

moreProp = Button(master, text="...", command=Prop, bg="grey", activebackground="grey")
moreProp.place(x=410, y=145)

exitb = Button(master, text="Exit", command=master.destroy, bg="#FF6B6C", activebackground="grey")
exitb.place(x=550, y=250)

#Loops until the window is closed
mainloop()