import tkinter as tk
from tkinter import ttk
Title=("Helvetica", 30, "bold")
text=("Helvetica", 20, "bold")
bwd=[]
fwd=[]

class Website(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        stack = tk.Frame(self) 
        stack.pack(fill = "both", expand = True) 
        stack.grid_rowconfigure(0, weight = 1)
        stack.grid_columnconfigure(0, weight = 1)
        
        self.frames = {} 
        for F in (StartPage, Page1, Page2,Page3,Page4,Page5): 
            frame = F(stack, self)
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew")  
        self.frames[StartPage].tkraise()
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        l=(StartPage, Page1, Page2,Page3,Page4,Page5)
        for i in range(len(l)):
                if l[i]==page:
                    x = l[i-1]
                    bwd.append(self.frames[x])
                    fwd.clear()
    def back(self,page):
        if bwd==[]:
            tk.messagebox.showinfo("Error!", "No more pages behind!")
        else:
            l=(StartPage, Page1, Page2,Page3,Page4,Page5)
            for i in range(len(l)):
                if l[i]==page:
                    x = l[i-1]
                    frame = self.frames[x]
                    frame.tkraise()
                    bwd.pop()
                    fwd.append(self.frames[l[i]])
    def front(self,page):
        if fwd==[]:
            tk.messagebox.showinfo("Error!", "No more pages ahead!")
        else:
            l=(StartPage, Page1, Page2,Page3,Page4,Page5)
            for i in range(len(l)):
                if l[i]==page:
                    x = l[i+1]
                    frame = self.frames[x]
                    frame.tkraise()
                    fwd.pop()
                    bwd.append(self.frames[l[i]])
                    
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Haikus", font = ("Helvetica", 45, "bold"))
        label.grid(row=1,column=2)
        body=ttk.Label(self, text='''
        Haikus are a style of Japanese poetry that follow the structure 
        of five syllables in the first line, seven in the second, 
        and five again in the third. They are beautifully crafted
        concise works of art with a minimalistic approach to poetry.
        Since they are so short, every word carries immense weight.''',font=text)
        body.grid(row=2, column=2)
        backS= ttk.Button(self, text ="<<",
            command = lambda:tk.messagebox.showinfo("Error!", "No more pages behind!"))
        backS.grid(row = 0, column = 0)
        frontS = ttk.Button(self, text =">>",
                            command = lambda:controller.front(StartPage))
        frontS.grid(row = 0, column = 1)
        n = ttk.Button(self, text ="The Old Pond",
                            command = lambda:controller.show_frame(Page1))
        n.place(x=750,y=300)
                 
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text =
        '''“The Old Pond” by Matsuo Bashō"
        
            An old silent pond

            A frog jumps into the pond—

            Splash! Silence again''', font = Title,)        
        label1.grid(row = 1, column = 3)
        back1 = ttk.Button(self, text ="<<",
                           command = lambda:controller.back(Page1))
        back1.grid(row = 0, column = 0)
        front1 = ttk.Button(self, text =">>",
                            command = lambda : controller.front(Page1))
        front1.grid(row = 0, column = 1)
        n = ttk.Button(self, text ="A World of Dew",
                            command = lambda : controller.show_frame(Page2))
        n.place(x=750,y=300)
class Page2(tk.Frame):
     
    def __init__(self, parent, controller):         
        tk.Frame.__init__(self, parent)
        label2 = ttk.Label(self, text =
        '''“A World of Dew” by Kobayashi Issa
        
            A world of dew,

            And within every dewdrop

            A world of struggle.''', font = Title)
            
        label2.grid(row = 1, column = 3)
        back2 = ttk.Button(self, text ="<<",
                           command =lambda : controller.back(Page2))
        back2.grid(row = 0, column = 0)
        front2 = ttk.Button(self, text =">>",
                            command = lambda : controller.front(Page2))
        front2.grid(row = 0, column = 1)
        n = ttk.Button(self, text ="Lighting One Candle",
                            command = lambda:controller.show_frame(Page3))
        n.place(x=750,y=300)
   
class Page3(tk.Frame):
     
    def __init__(self, parent, controller):         
        tk.Frame.__init__(self, parent)
        label3 = ttk.Label(self, text =
        '''“Lighting One Candle” by Yosa Buson

            The light of a candle

            Is transferred to another candle—

            Spring twilight''', font = Title)
            
        label3.grid(row = 1, column = 3)
        back3 = ttk.Button(self, text ="<<",
                           command = lambda : controller.back(Page3))
        back3.grid(row = 0, column = 0)
        front3 = ttk.Button(self, text =">>",
                            command = lambda : controller.front(Page3))
        front3.grid(row = 0, column = 1)
        n= ttk.Button(self, text ="A Poppy Blooms",
                            command = lambda:controller.show_frame(Page4))
        n.place(x=750,y=300)
  
class Page4(tk.Frame):
     
    def __init__(self, parent, controller):         
        tk.Frame.__init__(self, parent)
        label4 = ttk.Label(self, text =
        '''“A Poppy Blooms” by Katsushika Hokusai

            I write, erase, rewrite

            Erase again, and then

            A poppy blooms.''', font = Title)
            
        label4.grid(row = 1, column = 3)
        back4 = ttk.Button(self, text ="<<",
                           command = lambda : controller.back(Page4))
        back4.grid(row = 0, column = 0)
        front4 = ttk.Button(self, text =">>",
                            command = lambda : controller.front(Page4))
        front4.grid(row = 0, column = 1)
        n = ttk.Button(self, text ="Over the Wintry",
                            command = lambda:controller.show_frame(Page5))
        n.place(x=750,y=300)
        
class Page5(tk.Frame):
    
    def __init__(self, parent, controller):       
        tk.Frame.__init__(self, parent)
        label5 = ttk.Label(self, text =
        '''“Over the Wintry” by Natsume Sōseki

            Over the wintry

            Forest, winds howl in rage

            With no leaves to blow.''', font = Title)
        
        label5.grid(row = 1, column = 3)
        back5 = ttk.Button(self, text ="<<",
                           command = lambda : controller.back(Page5))    
        back5.grid(row = 0, column = 0)
        front5 = ttk.Button(self, text =">>",
            command = lambda:tk.messagebox.showinfo("Error!", "No more pages ahead!"))
        front5.grid(row = 0, column = 1)

window = Website()
window.geometry("950x550")
window.title("Poetry")
window.mainloop()



