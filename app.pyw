import os,random
from tkinter import *
from animation import animation as A
from gameButton import gameButton as G

def clickwin(event):
    caller=event.widget
    if caller==root:
        root._offsetx=event.x
        root._offsety=event.y
def dragwin(event):
    caller=event.widget
    if caller==root:
        x=root.winfo_pointerx()-root._offsetx
        y=root.winfo_pointery()-root._offsety
        root.geometry("+{x}+{y}".format(x=x,y=y))

def browse(ftype):
    files=[]
    for file in os.listdir("./pokes/"):
        if file.endswith(ftype):
            f=(os.path.join("./pokes/",file))
            files.append(f)
    return files

def refresh():
    global pic
    pokes=browse(".gif")
    poke=random.choice(pokes)
    pic.update(image=poke)

bg="#a0c1ff"

root=Tk()
root.configure(bg=bg)
root.call('wm', 'attributes', '.', '-topmost', '1')
root.overrideredirect(True)
root.bind("<ButtonPress-1>",clickwin)
root.bind("<B1-Motion>",dragwin)

pokes=browse(".gif")
poke=random.choice(pokes)

f=Frame(bd=1,relief=RAISED)
f.grid()

pic=A(f,image=poke,bg=bg)
pic.grid(row=0,column=0,padx=10,pady=10)

b=G(f,text="Refresh",bg=bg,fg="black",command=refresh)
b.grid(row=1,column=0,padx=10,pady=10,sticky="nesw")

b=G(f,text="Close",bg=bg,fg="black",command=root.destroy)
b.grid(row=1,column=1,padx=10,pady=10,sticky="nesw")

root.mainloop()
