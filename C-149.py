# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:02:01 2022

@author: Mannan
"""

from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("300x300")
root.config(bg="aqua")

label1=Label(root)

def randomnumber():
    list1=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    print(list1)
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26)
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    random_alph1=list1[random_no1]
    random_alph2=list1[random_no2]
    random_alph3=list1[random_no3]
    random_alph4=list1[random_no4]
    random_alph5=list1[random_no5]
    label1["text"]=random_alph1+random_alph2+random_alph3+random_alph4+random_alph5
btn1 = Button(root)
btn1=Button(root, text="Generate Random Word ", bg= "green", fg="black", command=randomnumber())
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()
    