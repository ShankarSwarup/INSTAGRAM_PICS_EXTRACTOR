from tkinter import *
from tkinter import ttk 
import instaloader

class insta:
    def __init__(self,root):
        self.root=root      
        self.root.title("INSTAGRAM PICS EXTRACTOR")
        self.root.geometry("500x420+300+50")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        title=Label(self.root,text='INSTAGRAM PICS EXTRACTOR',font=("algerian",10),bg="#262626",fg='white').pack(side=TOP,fill=X)

        self.var_handle=StringVar()

        lbl_handle=Label(self.root,text='INSTAGRAM_HANDLE:',font=("times new roman",15),bg='white').place(x=10,y=50)
        txt_handle=Entry(self.root,textvariable=self.var_handle,font=("times new roman",13),bg="#d9fcff").place(x=120,y=80,width=340,height=30)

        btn_download=Button(self.root,text='Download',command=self.download,font=('times new roman',13),bg='red',fg='white').place(x=60,y=120,width=100,height=40)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('times new roman',13),bg='violet',fg='white').place(x=330,y=120,width=100,height=40)


    def download(self):
        d=instaloader.Instaloader()
        d.download_profile(self.var_handle.get(),profile_pic_only=False)

    def clear(self):
        self.var_handle.set('')

root=Tk()
obj=insta(root)
root.mainloop()