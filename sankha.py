import tkinter as tk
import customtkinter as ctk
ctk.set_appearance_mode("dark")

col = ['#FEFEFE','#FF781F']
root = ctk.CTk()
root.title("Calculator")
root.geometry("348x373")
root.resizable(0, 0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = tk.StringVar()

main = ctk.CTkFrame(root)
main.pack()

inp_frame = ctk.CTkEntry(main, textvariable=input_text,justify = tk.RIGHT,height=50,corner_radius=25,text_color=col[0],
                         font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
inp_frame.grid(row = 0,column = 0,pady = 1,padx = 1,columnspan = 3,sticky = "ew")

clear = ctk.CTkButton(main ,text="C",cursor = "hand2", command = lambda: bt_clear(),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
clear.grid(row = 0,column =3 )

seven = ctk.CTkButton(main, text = "7", cursor = "hand2", command = lambda: btn_click(7),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = ctk.CTkButton(main, text = "8", cursor = "hand2", command = lambda: btn_click(8),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = ctk.CTkButton(main, text = "9", cursor = "hand2", command = lambda: btn_click(9),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
 
divide = ctk.CTkButton(main, text = "/",  cursor = "hand2", command = lambda: btn_click("/"),height=50,corner_radius=25,width=50,
                        fg_color=col[0],bg_color="transparent",text_color=col[1],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
divide.grid(row = 1, column = 3, padx = 1, pady = 1)

four = ctk.CTkButton(main, text = "4", cursor = "hand2", command = lambda: btn_click(4),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = ctk.CTkButton(main, text = "5", cursor = "hand2", command = lambda: btn_click(5),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = ctk.CTkButton(main, text = "6", cursor = "hand2", command = lambda: btn_click(6),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
 
mul = ctk.CTkButton(main, text = "*",  cursor = "hand2", command = lambda: btn_click("*"),height=50,corner_radius=25,width=50,
                        fg_color=col[0],bg_color="transparent",text_color=col[1],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
mul.grid(row = 2, column = 3, padx = 1, pady = 1)

one = ctk.CTkButton(main, text = "1", cursor = "hand2", command = lambda: btn_click(1),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = ctk.CTkButton(main, text = "2", cursor = "hand2", command = lambda: btn_click(2),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = ctk.CTkButton(main, text = "3", cursor = "hand2", command = lambda: btn_click(3),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
 
sub = ctk.CTkButton(main, text = "-",  cursor = "hand2", command = lambda: btn_click("-"),height=50,corner_radius=25,width=50,
                        fg_color=col[0],bg_color="transparent",text_color=col[1],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
sub.grid(row = 3, column = 3, padx = 1, pady = 1)

zero = ctk.CTkButton(main, text = "0", cursor = "hand2", command = lambda: btn_click(0),height=50,corner_radius=25,width=50,
                        fg_color=col[1],bg_color="transparent",text_color=col[0],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
zero.grid(row = 4, column = 1, padx = 1, pady = 1)
 
point = ctk.CTkButton(main, text = ".", cursor = "hand2", command = lambda: btn_click("."),height=50,corner_radius=25,width=50,
                        fg_color=col[0],bg_color="transparent",text_color=col[1],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
point.grid(row = 4, column = 0, padx = 1, pady = 1)
 
equal = ctk.CTkButton(main, text = "=", cursor = "hand2", command = lambda: bt_equal(),height=50,corner_radius=25,width=50,
                        fg_color=col[0],bg_color="transparent",text_color=col[1],
                        font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
equal.grid(row = 4, column = 2, padx = 1, pady = 1)
 
sum = ctk.CTkButton(main, text = "+",  cursor = "hand2", command = lambda: btn_click("+"),height=50,corner_radius=25,width=50,
                    fg_color=col[0],bg_color="transparent",text_color=col[1],
                    font=ctk.CTkFont(family = "Arial",size=20,weight = "bold"))
sum.grid(row = 4, column = 3, padx = 1, pady = 1)

for widget in main.winfo_children():
    widget.grid_configure(padx=15,pady=15)

root.mainloop()