from tkinter import *
import random
root=Tk()
root.title("Project 153")
root.geometry("400x400")
root.configure(background = "maroon")

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.3,anchor=CENTER)

label = Label(root)
label.place(relx=0.5,rely=0.4,anchor=CENTER)

label1=Label(root)

array_3d= [[['1','2','3','4','5','6','7','8','9','0'],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])

def generator() :
    guess = enter_word.get()
    label["text"] = " Guessed Password " + str(guess)
    random1=random.randint(0, 5)
    random2=random.randint(0, 1)
    random3=random.randint(0, 7)
    
    letter1=str(array_3d[0][0][random1])
    letter2=(array_3d[0][1][random2])
    letter3=(array_3d[0][2][random3])
    
    label1["text"] = "Generated Password : "+letter1+ letter2 + letter3
    

btn=Button(root, text="Generate New Password", command = generator)
btn.place(relx = 0.5,rely = 0.5,anchor= CENTER)

label1.place(relx = 0.5,rely = 0.6,anchor= CENTER)

root.mainloop()