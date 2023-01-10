import customtkinter
import math
from sympy import *


#Sets apearance to dark mode, colo theme to dark-blue
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

number_config = False
#Sets the root window
root = customtkinter.CTk()
root.geometry('1000x500')
root.iconbitmap(r'favicon.ico')

#Sets root title
root.title("Calculator")

#initiazes frame object
frame = customtkinter.CTkFrame(master=root)
frame.place(relwidth=1.0, relheight=1.0)

#create output windows
output_text = customtkinter.CTkTextbox(master=root)
output_text.place(x=10, y=10, relwidth=.3, relheight=0.09)


#Assign numbers to their respected buttons
def number_config(number):
  output_text.insert("end", text=str(number))

for i in range(10):
    locals()[f'number_config_{i}'] = lambda i=i: number_config(i)



def negative_config(n):
    return -n

def number_config_period():
  output_text.insert("end", text=".")

def number_config_plus():
  output_text.insert("end", text="+")
  
def number_config_difference():
  output_text.insert("end", text="-")
  

def number_config_product():
  output_text.insert("end", text="X")

def number_config_quotient():
  output_text.insert("end", text="/")

def number_config_pi():
  output_text.insert("end", text=str(math.pi))

def number_config_sqrt():
  output_text.insert("end", text=sqrt)

def number_config_negative():
  output_text.insert("end", text="(-)")



#Sum, Difference, Quotient, square root, Product Logic, and input num ^2, allows for negative integers.
def get_entrybox():
    a = output_text.get(1.0, "end")
    a = "0" + a
    if "+" in a:
        operand = "+"
        parts = a.split(operand)
        left_side = parts[0]
        right_side = parts[1]
        print(left_side, right_side)
        left_sum = float(left_side)
        right_sum = float(right_side)
        sum = (left_sum + right_sum)
        output_text.delete(1.0, "end")
        output_text.insert(1.0, text=sum)
        if sum == 42:
          output_text.delete(1.0, "end")
          output_text.insert(1.0, text=" oh, 42, The meaning of the universe!")
    elif "-" in a:
        result = eval(a)
        output_text.delete(1.0, "end")
        output_text.insert(1.0, text=result)
    elif "X" in a:
        operand = "X"
        parts = a.split(operand)
        left_side2 = parts[0]
        right_side2 = parts[1]
        print(left_side2, right_side2)
        left_product = float(left_side2)
        right_product = float(right_side2)
        product = (left_product * right_product)
        output_text.delete(1.0, "end")
        output_text.insert(1.0, text=product)
        
    elif "/" in a:
      operand = "/"
      parts = a.split(operand)
      left_side3 = parts[0]
      right_side3 = parts[1]
      print(left_side3, right_side3)
    try:
      left_quotient = int(left_side3)
      right_quotient = int(right_side3)
      quotient = (left_quotient / right_quotient)
      output_text.delete(1.0, "end")
      output_text.insert(1.0, text=quotient)
    except ZeroDivisionError:
      output_text.delete(1.0, "end")
      output_text.insert(1.0, text="cannot divide by zero")
    
    
    
#Define square root, squared

def square_root():
    get_number = output_text.get(1.0, "end")
    sqrt = math.sqrt(int(get_number))
    output_text.delete(1.0, "end")
    output_text.insert(1.0, text=sqrt)

def squared():
    get_number = output_text.get(1.0, "end")
    squared = float(get_number) * float(get_number)
    output_text.delete(1.0, "end")
    output_text.insert(1.0, text=squared)




  
  
#creat and place all Button widgets
button_1 = customtkinter.CTkButton(master=frame, text="1", command=number_config_1)
button_1.place(y=100, x=10)

button_2 = customtkinter.CTkButton(master=frame, text="2", command=number_config_2)
button_2.place(y=100, x=160)

button_3 = customtkinter.CTkButton(master=frame, text="3", command=number_config_3)
button_3.place(y=100, x=310)

button_4 = customtkinter.CTkButton(master=frame, text="4", command=number_config_4)
button_4.place(y=150, x=10)

button_5 = customtkinter.CTkButton(master=frame, text="5", command=number_config_5)
button_5.place(y=150, x=160)

button_6 = customtkinter.CTkButton(master=frame, text="6", command=number_config_6)
button_6.place(y=150, x=310)

button_7 = customtkinter.CTkButton(master=frame, text="7", command=number_config_7)
button_7.place(y=200, x=10)

button_8 = customtkinter.CTkButton(master=frame, text="8", command=number_config_8)
button_8.place(y=200, x=160)

button_9 = customtkinter.CTkButton(master=frame, text="9", command=number_config_9)
button_9.place(y=200, x=310)

button_0 = customtkinter.CTkButton(master=frame, text="0", command=number_config_0)
button_0.place(y=250, x=160, relwidth=.2898)

button_Period = customtkinter.CTkButton(master=frame, text=".", command=number_config_period)
button_Period.place(y=250, x=10)

button_equals = customtkinter.CTkButton(master=frame, text="=", command=get_entrybox)
button_equals.place(y=300, x=10, relwidth=0.4398, relheight=.3)

button_Divide = customtkinter.CTkButton(master=frame, text="/", command=number_config_quotient)  
button_Divide.place(y=100, x=460)

button_X = customtkinter.CTkButton(master=frame, text="X", command=number_config_product)
button_X.place(y=150, x=460)

button_minus = customtkinter.CTkButton(master=frame, text="-", command=number_config_difference)
button_minus.place(y=200, x=460)

button_add = customtkinter.CTkButton(master=frame, text="+", command=number_config_plus)
button_add.place(y=250, x=460, relheight=.4)

button_pi = customtkinter.CTkButton(master=frame, text="Pi", command=number_config_pi)
button_pi.place(y=150, x=610)

button_sqrt = customtkinter.CTkButton(master=frame, text="2√", command=square_root)
button_sqrt.place(y=200, x=610)

button_x2 = customtkinter.CTkButton(master=frame, text="X²", command=squared)
button_x2.place(y=250, x=610)



#Deletes contents of text widget
def delete():
  print("Deleted Current Opperations")
  output_text.delete(1.0, "end")

button_clr = customtkinter.CTkButton(master=frame, text="Clear", command=delete)
button_clr.place(y=100, x=610)


root.mainloop()


