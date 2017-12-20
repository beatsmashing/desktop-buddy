import tkinter as tk

class gameButton(tk.Button):
    def __init__(self,*args,**kwargs):
        super(gameButton,self).__init__()

        self.root=args[0]

        self.configure(text=kwargs["text"])
        
        self.configure(fg=kwargs["fg"],
                       activeforeground=kwargs["fg"])

        try:
            self.configure(command=kwargs["command"])
        except KeyError:
            pass

        self.configure(relief="flat",cursor="hand2")
        self.bind("<Enter>",self.hover)
        self.bind("<Leave>",self.leave)

        self.old=kwargs["bg"]
        self.dark=self.darken(self.old)

        self.configure(bg=self.old,activebackground=self.dark,
                       bd=1,relief="solid")

    def getRGB(self,h):
        it=tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
        return it

    def getHex(self,h):
        it='#%02x%02x%02x' % h
        return it

    def darken(self,h):
        currentHex=self.old.replace("#","")
        currentRGB=self.getRGB(currentHex)
        
        currentR=currentRGB[0]
        currentG=currentRGB[1]
        currentB=currentRGB[2]
        if currentR>30:
            newR=round(currentR-30)
        else:
            newR=0
        if currentG>30:
            newG=round(currentG-30)
        else:
            newG=0
        if currentB>30:
            newB=round(currentB-30)
        else:
            newB=0

        newRGB=(newR,newG,newB)

        newHex=self.getHex(newRGB)
        return newHex

    def hover(self,event):
        self.configure(bg=self.dark)

    def leave(self,event):
        self.configure(bg=self.old)
