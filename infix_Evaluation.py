from tkinter import *
from Stack import *
window = Tk()
my_input = StringVar()
my_output =StringVar()
my_operator = ""

def math( top, op1, op2):
    if top == "*":
        return op1 * op2
    elif top == "/":
        return op1 / op2
    elif top == "+":
        return op1 + op2
    elif top == "^":
        return pow(op1,op2)
    elif top == "-":
        return op1 - op2


def infixEvaluation(postfixExpr):
    prec: dict[str, int] = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["-"] = 2
    prec["+"] = 2
    prec["("] = 1

    operand_S = Stack()
    no_S = Stack()
   # tookenlist = postfixExpr.split()
    for tooken in postfixExpr:
        if tooken =="(":
            operand_S.push(tooken)
        elif tooken ==")":
            op = operand_S.pop()
            while op != "(" :
                op2 = no_S.pop()
                op1 = no_S.pop()
                result = math(op, op1,op2)
                no_S.push(int(result))
                op = operand_S.pop()


        elif tooken == "*" or tooken == "/" or tooken == "+" or tooken == "-" or tooken == "(" or tooken == "^":
            while not operand_S.isEmpty() and prec[operand_S.peek()] >= prec[tooken]:
                op = operand_S.pop()
                op2 = no_S.pop()
                op1 = no_S.pop()
                result = math(op, op1, op2)
                no_S.push(int(result))
            operand_S.push(tooken)

        else:
            no_S.push(int(tooken))
    while not operand_S.isEmpty():
        op = operand_S.pop()
        op2 = no_S.pop()
        op1 = no_S.pop()
        result = math(op, op1, op2)
        no_S.push(int(result))


    return no_S.pop()


def convert_to_list(my_operator):
   After =""
   ll=[]
   for i in my_operator:
       if i in "1234567890":
           After += str(i)
       else:
           if (After != ""):
               ll.append(After)
               After=""

           if i=='-' and( len(ll)==0 or ll[len(ll)-1]=='*'or ll[len(ll)-1]=='/'or ll[len(ll)-1]=='-'or ll[len(ll)-1]=='+'or ll[len(ll)-1]=='('):
               After+= str(i)
           else:
               ll.append(str(i))


   if After !="":
       ll.append(str(After))
       After = ""
   return ll

def equalf():
   global my_operator
   result =[]
   result = convert_to_list(my_operator)
   res = infixEvaluation(result)
   my_output.set(res)
   my_operator = res


def concat_op(numbers):
   global my_operator
   my_operator += (str(numbers))
   my_input.set(my_operator)


def ac():
   global my_operator
   my_operator = ""
   my_input.set("")
   my_output.set("")


def clr():
    global my_operator
    my_operator = my_operator[:-1]
    my_input.set(my_operator)




window.geometry("375x200+300+300")

# defining the buttons, text field and label
window.title('calculator')
window.configure(bg='#4A4A4A')
text1 = Entry(window, width=20, textvariable=my_input, font=20,bg='#4A4A4A').grid(row=0, column=0, columnspan=3)
Label(window,  textvariable=my_output, width=12, font=20,bg='#4A4A4A').grid(row=0, column=3, columnspan=2)
Button(window, width=6, text="1", font=20, command=lambda: concat_op('1'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=1, column=0, sticky="w")
Button(window, width=6, text="2", font=20, command=lambda: concat_op('2'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=1, column=1, sticky="w")
Button(window, width=6, text="3", font=20, command=lambda: concat_op('3'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=1, column=2, sticky="w")
Button(window, width=6, text="4", font=20, command=lambda: concat_op('4'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=2, column=0, sticky="w")
Button(window, width=6, text="5", font=20, command=lambda: concat_op('5'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=2, column=1, sticky="w")
Button(window, width=6, text="6", font=20, command=lambda: concat_op('6'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=2, column=2, sticky="w")
Button(window, width=6, text="7", font=20, command=lambda: concat_op('7'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=3, column=0, sticky="w")
Button(window, width=6, text="8", font=20, command=lambda: concat_op('8'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=3, column=1, sticky="w")
Button(window, width=6, text="9", font=20, command=lambda: concat_op('9'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=3, column=2, sticky="w")
Button(window, width=6, text="0", font=20, command=lambda: concat_op('0'),bg='black',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=4, column=1, sticky="w")
Button(window, width=6, text="+", font=20, command=lambda: concat_op('+'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=1, column=3, sticky="w")
Button(window, width=6, text="-", font=20, command=lambda: concat_op('-'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=2, column=3, sticky="w")
Button(window, width=6, text="*", font=20, command=lambda: concat_op('*'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=3, column=3, sticky="w")
Button(window, width=6, text="^", font=20, command=lambda: concat_op('^'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=3, column=4, sticky="w")
Button(window, width=6, text="/", font=20, command=lambda: concat_op('/'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=4, column=3, sticky="w")
Button(window, width=6, text="(", font=20, command=lambda: concat_op('('),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=4, column=0, sticky="w")
Button(window, width=6, text=")", font=20, command=lambda: concat_op(')'),bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=4, column=2, sticky="w")
Button(window, width=6, text="AC", font=20, command=ac,bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=1, column=4, sticky="w")
Button(window, width=6, text="C", font=20, command=clr,bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=2, column=4, sticky="w")
Button(window, width=6, text="=", font=20, command=equalf,bg='#292929',fg='white',activebackground='#4A4A4A',activeforeground='white').grid(row=4, column=4, rowspan=2, sticky="w")

window.mainloop()