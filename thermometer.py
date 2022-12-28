from tkinter import*



class th():
    def __init__(self,f1,title,bg_color,house_color,init_temp):
        self.f1=f1
        self.title=title
        self.bg_color=bg_color
        self.house_color=house_color
        self.init_temp=init_temp
        

        self.frame=LabelFrame(f1,text=self.title,width=500,height=300,bg=self.bg_color)
        self.spin_temp=IntVar()
        self.spin_temp.set(init_temp)
        self.spin_box=Spinbox(
            self.frame,
            from_=0,
            to=100,
            textvariable=self.spin_temp,
            wrap=True,width=5,
            command=self.change)
        self.spin_box.place(x=20,y=140)

        self.houses=[]
        self.cn()
        self.ch()
        self.change()
    

    def g(self,r,c):
        self.frame.grid(row=r,column=c)

    def cn(self):
        for i in range(0,100,20):
            Label(self.frame,text=i,font=('',8),bg=self.bg_color).place(x=50,y=113-i)
        for i in range(0,100,20):
            Label(self.frame,text=i,font=('',8),bg=self.bg_color).place(x=20,y=113-i)


    def ch(self):
        for i in range(100):
            l=Label(self.frame,bg=self.house_color) 
            self.houses.append(l)
            l.place(x=42,y=100-i)

    def change(self):
        temp=int(self.spin_box.get())
        for i in range(100):
            if i<temp:
                self.houses[i].config(bg=self.house_color)
            elif i>temp:
                self.houses[i].config(bg="gray")
