from tkinter import *
import tkinter as tk
import math


def main():
    def choice():
        restart = input("\nTry Again? 😎 (y/n): ")
        if restart.lower() == "y":
            main()
        else:
            print("\nThank You For Using The Calculator.... (ツ)")
            return

    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    print("\n-------------------------------------------------")
    print("            🤓   CALCULATOR ++  🤓            ")
    print("-------------------------------------------------")
    while True:
        A = input("\nEnter The 1st Number: - ")
        B = input("Enter The 2nd Number: - ")
        if A.isdigit() and B.isdigit():
            num1 = float(A)
            num2 = float(B)
        elif isfloat(A) == True and isfloat(B) == True:
            num1 = float(A)
            num2 = float(B)
        else:
            print("\nSorry, You Can Enter Only A Integer or A Decimal Number... (▱˘︹˘▱)")
            continue

        screen = tk.Tk()
        screen.title('Calculator ++')
        screen.iconbitmap(r'calculator.ico')
        screen.geometry("320x400")
        screen.configure(bg='sky blue')

        def add():
            print("\n", num1, "+", num2, "=", num1 + num2)
            screen.withdraw()
            choice()

        def sub():
            print("\n", num1, "-", num2, "=", num1 - num2)
            screen.withdraw()
            choice()

        def mult():
            print("\n", num1, "×", num2, "=", num1 * num2)
            screen.withdraw()
            choice()

        def div():
            if num2 == 0.0:
                print("\nZeroDivisionError..Cant Divide By Zero... Undefined... (▱˘︹˘▱)")
                screen.withdraw()
                choice()
            else:
                print("\n", num1, "/", num2, "=", num1 / num2)
                screen.withdraw()
                choice()

        def rem():
            if num2 == 0.0:
                print("\nZeroDivisionError..Cant Divide By Zero... Undefined... (▱˘︹˘▱)")
                screen.withdraw()
                choice()
            else:
                print("\nRemainder Of", num1, "/", num2, "is", num1 % num2)
                screen.withdraw()
                choice()

        def sq():
            if num1 == 0.0 and num2 == 0.0:
                print("\nZero power Zero is Undefined... (▱˘︹˘▱) ")
                screen.withdraw()
                choice()
            else:
                print("\n", num1, "^", num2, "=", num1 ** num2)
                screen.withdraw()
                choice()

        def sqroot():
            print("\nThe Sqaure Root Of The First Number =", math.sqrt(num1))
            print("The Sqaure Root Of The Second Number =", math.sqrt(num2))
            screen.withdraw()
            choice()

        def fac():
            num3 = int(num1)
            num4 = int(num2)
            print("\nDecimal Numbers Can't Have A Factorial... So By Taking Only The Integer Part : - ")
            print("\nThe Factorial Of The First Number (", num3, ") = ", math.factorial(num3))
            print("The Factorial Of The Second Number (", num4, ") = ", math.factorial(num4))
            screen.withdraw()
            choice()

        def logcalc():
            print("\nThe Log Of The First Number (", num1, ") = ", math.log(num1))
            print("The Log Root Of The Second Number (", num2, ") = ", math.log(num2))
            screen.withdraw()
            choice()

        addition = Button(screen, text="+", command=add)
        addition.config(font=('Trebuchet MS', 20), highlightbackground="#FF00FF", bg="white", fg="black", padx=7,
                        pady=7)
        addition.place(x=20, y=44)

        subtract = Button(screen, text="-", command=sub)
        subtract.config(font=('Trebuchet MS', 20), highlightbackground="#12A006", bg="white", fg="black", padx=7,
                        pady=7)
        subtract.place(x=20, y=167)

        multiply = Button(screen, text="×", command=mult)
        multiply.config(font=('Trebuchet MS', 20), highlightbackground="#5F3434", bg="white", fg="black", padx=7,
                        pady=7)
        multiply.place(x=20, y=300)

        divide = Button(screen, text="÷", command=div)
        divide.config(font=('Trebuchet MS', 20), highlightbackground="#FFF703", bg="white", fg="black", padx=7, pady=7)
        divide.place(x=120, y=44)

        remain = Button(screen, text="%", command=rem)
        remain.config(font=('Trebuchet MS', 20), highlightbackground="#4F03FF", bg="white", fg="black", padx=7, pady=7)
        remain.place(x=120, y=167)

        square = Button(screen, text="x^2", command=sq)
        square.config(font=('Trebuchet MS', 20), highlightbackground="#FF031E", bg="white", fg="black", padx=7, pady=7)
        square.place(x=110, y=300)

        squareroot = Button(screen, text="√", command=sqroot)
        squareroot.config(font=('Trebuchet MS', 20), highlightbackground="#8E8E8E", bg="white", fg="black", padx=7,
                          pady=7)
        squareroot.place(x=230, y=44)

        factorial = Button(screen, text="Factorial", command=fac)
        factorial.config(font=('Trebuchet MS', 20), highlightbackground="#02FCC3", bg="white", fg="black", padx=7,
                         pady=7, width=4)
        factorial.place(x=210, y=170)

        log = Button(screen, text="log", command=logcalc)
        log.config(font=('Trebuchet MS', 20), highlightbackground="#FC9602", bg="white", fg="black", padx=7, pady=7)
        log.place(x=220, y=297)

        screen.mainloop()
