import tkinter as tk

root = tk.Tk()
root.title("Hello wold")
root.geometry("300x400")
root.configure(bg = 'grey')


#Functions
num_string = ''
out = '0'
operations = []
first = True
OPERATORS = ['+', '-', '*', '/']
ALLNUMBERS = '0123456789'



def show(x):
  global num_string, out, operations
  if x == '':
    print('Ac clicked')
    num_string = ''
    operations = []
    out = '0'
    screen.configure(text = '')
    
  elif x in ALLNUMBERS:
    num_string += x
    # out = num_string
    screen.configure(text = num_string)
    
  elif x in OPERATORS:
    add_operator(x)
    
  elif x == '=':
    calculate()
    print(operations)
    print(out)
  

def add_operator(op):
  global operations, num_string
  operations.append(num_string)
  screen.configure(text = op)
  num_string = ''
  operations.append(op)

def math(num1, operator, num2):
  print('num1: ', num1)
  print('num2: ', num2)
  if operator == '+':
    return int(num1) + int(num2)
  elif operator == '-':
    return int(num1) - int(num2)
  elif operator == '*':
    return int(num1) * int(num2)
  elif operator == '/':
    return int(num1) / int(num2)

def calculate():
  global operations, num_string, first, out
  operations.append(num_string)
  if first == True:
    if len(operations) >= 3:
      out = math(operations[0], operations[1], operations[2])  
      operations[0] = out
      screen.configure(text = out)
    first = False
  else:
    print(operations,  'not first')
    operations[0] = out
    out = math(operations[0], operations[-2], operations[-1])
    screen.configure(text = out)
  

def combine(num):
  global num_string
  num_string += num
  out = num_string
  


#Buttons:        NUMBERS

ZERO = tk.Button(root, 
                 text = '0', 
                 activebackground = 'green',
                 command = lambda: show('0')
                 )
ZERO.place(x = 30, y = 270, 
           width = 100, height = 50)

ONE = tk.Button(root, 
                 text = '1', 
                 activebackground = 'green',
                 command = lambda: show('1')
                 )
ONE.place(x = 30, y = 220, 
           width = 50, height = 50)
TWO = tk.Button(root, 
                 text = '2', 
                 activebackground = 'green',
                 command = lambda: show('2')
                 )
TWO.place(x = 80, y = 220, 
           width = 50, height = 50)
THREE = tk.Button(root, 
                 text = '3', 
                 activebackground = 'green',
                 command = lambda: show('3')
                 )
THREE.place(x = 130, y = 220, 
           width = 50, height = 50)
FOUR = tk.Button(root, 
                 text = '4', 
                 activebackground = 'green',
                 command = lambda: show('4')
                 )
FOUR.place(x = 30, y = 170, 
           width = 50, height = 50)
FIVE = tk.Button(root, 
                 text = '5', 
                 activebackground = 'green',
                 command = lambda: show('5')
                 )
FIVE.place(x = 80, y = 170, 
           width = 50, height = 50)
SIX = tk.Button(root, 
                 text = '6', 
                 activebackground = 'green',
                 command = lambda: show('6')
                 )
SIX.place(x = 130, y = 170, 
           width = 50, height = 50)
SEVEN = tk.Button(root, 
                 text = '7', 
                 activebackground = 'green',
                 command = lambda: show('7')
                 )
SEVEN.place(x = 30, y = 120, 
           width = 50, height = 50)
EIGHT = tk.Button(root, 
                 text = '8', 
                 activebackground = 'green',
                 command = lambda: show('8')
                 )
EIGHT.place(x = 80, y = 120, 
           width = 50, height = 50)
NINE = tk.Button(root, 
                 text = '9', 
                 activebackground = 'green',
                 command = lambda: show('9')
                 )
NINE.place(x = 130, y = 120, 
           width = 50, height = 50)

DECIMAL = tk.Button(root,
                   text = '.',
                   activebackground = 'purple',
                   command = lambda: show('.')
                   )
DECIMAL.place(x = 130, y = 270,
             width = 50, height = 50)

#Buttons:          SYMBOLS

AC = tk.Button(root,
              text = 'AC',
              activebackground = 'red',
              command = lambda: show(''))
AC.place(x = 30, y = 70,
         width = 150, height = 50)

EQUALS = tk.Button(root,
                   text = '=',
                   activebackground = 'orange',
                   command = lambda: show('=')
                  )
EQUALS.place(x = 180, y = 270,
            width = 50, height = 50)

PLUS = tk.Button(root, 
                text = '+',
                activebackground = 'blue',
                command = lambda: show('+')
                )
PLUS.place(x = 180, y = 220,
          width = 50, height = 50)

MINUS = tk.Button(root,
                 text = '-',
                 activebackground = 'blue',
                 command = lambda: show('-')
                 )
MINUS.place(x = 180, y = 170,
           width = 50, height = 50)

MULT = tk.Button(root,
                text = '*',
                activebackground = 'blue',
                command = lambda: show('*')
                )
MULT.place(x = 180, y = 120,
          width = 50, height = 50)

DIVISION = tk.Button(root,
                    text = '/',
                    activebackground = 'blue',
                    command = lambda: show('/')
                    )
DIVISION.place(x = 180, y = 70,
              width = 50, height = 50)

  


#Display
screen = tk.Label(root,
                  text = '',
                  bg = 'black',
                  fg = 'white',
                  anchor = 'e')
screen.place(x = 30, y = 10,
             width = 200, height = 60)









tk.mainloop()
