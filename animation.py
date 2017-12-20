import tkinter as tk
import _thread

class animation(tk.Label):
    def __init__(self,*args,**kwargs):
        super(animation,self).__init__()
        self.root=args[0]
        self.file=kwargs["image"]
        try:
            self.delay=kwargs["delay"]
        except KeyError:
            self.delay=20
        try:
            self.configure(bg=kwargs["bg"])
        except KeyError:
            pass

        _thread.start_new_thread(self.animate,(0,))
        

    def animate(self,y):
        try:
            self.frame=tk.PhotoImage(file=self.file,
                            format="gif -index {}".format(y))
            self.config(image=self.frame)
            self.image=self.frame
            self.root.after(self.delay,self.animate,y+1)
        except Exception:
            self.root.after(self.delay,self.animate,0)

    def update(self,**kwargs):
        self.file=kwargs["image"]
