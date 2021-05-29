from tkinter import * 
def click(event):
    text =event.widget.cget("text")
    if text == "x":
        text = "*"
    elif text == "÷":
        text = "/" 
    elif text == "^":
        text = "**"
    global scval
    line = ""
    if text == "=":
        try :
            if scval.get().isdigit():
                value = int(scval.get())
            else :
                value = eval(scval.get())
        
            scval.set(value)
        except :
            scval.set("Err")
        
    elif text == "c" or text == "C":
        scval.set("")

    else:
        scval.set(scval.get()+text)

root =Tk()
root.geometry("320x550")
root.maxsize(320,550)
root.minsize(320,550)
root.title("Caclulator")

scval =StringVar()
screen = Entry(root , textvar=scval ,font="lucida 40 bold", justify=RIGHT, width=10)
screen.pack( ipadx=10, ipady=10 )
f =Frame(root , bg="grey" ,)
f.pack()
for i in range(9,6,-1):
    b=Button(f,text=str(i) , font="lucida 20 bold")     
    b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
    b.bind("<Button-1>" , click)
b=Button(f,text="÷" , font="lucida 20 bold")
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

f1 =Frame(root , bg="grey")
f1.pack()
for i in range(6,3,-1):
    b=Button(f1,text=str(i) , font="lucida 20 bold")     
    b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
    b.bind("<Button-1>" , click)
b=Button(f1,text="x" , font="lucida 20 bold")
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

f2 =Frame(root , bg="grey")
f2.pack()

for i in range(3,0,-1):
    b=Button(f2,text=str(i) , font="lucida 20 bold")     
    b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
    b.bind("<Button-1>" , click)
b=Button(f2,text="-" , font="lucida 20 bold")
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

f3 =Frame(root , bg="grey")
f3.pack()
b=Button(f3,text="^", font="lucida 20 bold")     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

b=Button(f3,text="0", font="lucida 20 bold")     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

b=Button(f3,text=".", font="lucida 20 bold")     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

b=Button(f3,text="+", font="lucida 20 bold")     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

f4 =Frame(root, bg="grey")
f4.pack()

b=Button(f4,text="=", font="lucida 20 bold" , width=10)     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)
b=Button(f4,text="C", font="lucida 20 bold" , width=3)     
b.pack(ipadx=10 , ipady= 10 , padx=10 , pady=10 , side=LEFT)
b.bind("<Button-1>" , click)

root.configure(bg="lightgrey")
root.mainloop()
