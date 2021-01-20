import time
import datetime
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Salary Management System")
root.geometry('1350x650+0+0')
root.configure(background="Gray")

Tops = Frame(root, width=1350, height=50, bd=10, bg="Gray",relief=RIDGE)
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, bg="Gray", relief=RIDGE)
f1.pack(side=BOTTOM)
f2 = Frame(root, width=300, height=700, bd=8, bg="Gray")
f2.pack(side=RIGHT)

fla = Frame(f1, width=600, height=200, bd=8, bg="Gray")
fla.pack(side=TOP)
flb = Frame(f1, width=300, height=600, bd=8, bg="Gray", relief=RIDGE)
flb.pack(side=TOP)

lblinfo = Label(Tops, font=('arial', 45, 'bold'), text="Salary Management System", bd=10, fg="Black")
lblinfo.grid(row=0, column=0)


def exit():
    exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit the system")
    if exit > 0:
        root.destroy()
        return


def reset():
    EmployeeID.set("")
    Gender.set("")
    BasicSalary.set("")
    # wageshour.set("")
    Payable.set("")
    Taxable.set("")
    FinalPayable.set("")
    GrossPayable.set("")
    OverTimeBonus.set("")
    Employer.set("")
    Position.set("")
    txtpayslip1.delete("1.0", END)
    txtpayslip2.delete("1.0", END)




def enterinfo():
    txtpayslip1.delete("2.0", END)
    txtpayslip1.insert(END, "\t\tGeneral\n\n")
    txtpayslip1.insert(END, "EmployeeID :\t\t" + EmployeeID.get() + "\n\n")
    txtpayslip1.insert(END, "Gender :\t\t" + Gender.get() + "\n\n")
    txtpayslip1.insert(END, "Employee Name :\t\t" + Employer.get() + "\n\n")
    txtpayslip1.insert(END, "Position :\t\t" + Position.get() + "\n\n")
    txtpayslip1.insert(END, "Basic Salary :\t\t" + BasicSalary.get() + "\n\n")
    txtpayslip1.insert(END, "FinalPay :\t\t" + FinalPayable.get() + "\n\n")
    # txtpayslip.insert(END, "Wages per hour :\t\t" + wageshour.get() + "\n\n")
    txtpayslip1.insert(END, "Tax Paid :\t\t" + Taxable.get() + "\n\n")
    txtpayslip1.insert(END, "Payable :\t\t" + Payable.get() + "\n\n")

def weeklywages():
    txtpayslip1.delete("1.0", END)
    basicsalary = float(BasicSalary.get())
    # wagesperhours = float(wageshour.get())

    paydue = basicsalary  # * wagesperhours
    paymentdue = "$", str('%.2f' % paydue)
    Payable.set(paymentdue)

    tax = paydue * 0.1
    taxable = "$", str('%.2f' % tax)
    Taxable.set(taxable)

    FinalPay = paydue - tax
    FinalPays = "$", str('%.2f' % FinalPay)
    FinalPayable.set(FinalPays)

    if basicsalary > 40:
        overtimehours = (basicsalary - 40)  # + wagesperhours * 1.5
        overtime = "$", str('%.2f' % overtimehours)
        OverTimeBonus.set(overtime)
    elif basicsalary <= 40:
        overtimepay = (basicsalary - 40)  # + wagesperhours * 1.5
        overtimehrs = "$", str('%.2f' % overtimepay)
        OverTimeBonus.set(overtimehrs)
    return


# =============================== Variables ========================================================
EmployeeID = StringVar()
Gender = StringVar()
BasicSalary = StringVar()
wageshour = StringVar()
Payable = StringVar()
Taxable = StringVar()
FinalPayable = StringVar()
GrossPayable = StringVar()
OverTimeBonus = StringVar()
Employer = StringVar()
Position = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

# ================================ Label Widget =================================================

lblEmployeeID = Label(fla, text="Employee ID", font=('arial', 16, 'bold'), bd=20, fg="black", bg='gray').grid(
    row=0, column=0)
#lblGender = Label(fla, text="Gender", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(row=0,
                                                                                                    #column=2)
#lblEmployer = Label(fla, text="Employer Name", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(
    #row=1,
    ##column=0)
#lblPosition = Label(fla, text="Position", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(row=1,
                                                                                                         #column=2)
#lblBasicSalary = Label(fla, text="Basis Salary", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(
    #row=2, column=0)
#lblHourlyRate = Label(fla, text="Hourly Rate", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(
    #row=2, column=2)
#lblTax = Label(fla, text="Tax", font=('arial', 16, 'bold'), bd=20, anchor='w', fg="black", bg="gray").grid(row=3,
                                                                                                           #column=0)
#lblOverTime = Label(fla, text="OverTime", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(row=3,
                                                                                                         #column=2)
#lblGrossPay = Label(fla, text="GrossPay", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(row=4,
                                                                                                         #column=0)
#lblFinalPay = Label(fla, text="Final Pay", font=('arial', 16, 'bold'), bd=20, fg="black", bg="gray").grid(row=4,
                                                                                                         # column=2)

# =============================== Entry Widget =================================================

etxEployeeID = Entry(fla, textvariable=EmployeeID, font=('arial', 16, 'bold'), bd=10, width=22, justify='left')
etxEployeeID.grid(row=0, column=1)

#etxGender = Entry(fla, textvariable=Gender, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxGender.grid(row=0, column=3)

#etxemployer = Entry(fla, textvariable=Employer, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxemployer.grid(row=1, column=1)

#etxBasicSalary = Entry(fla, textvariable=BasicSalary, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxBasicSalary.grid(row=2, column=1)

#etxwagesperhours = Entry(fla, textvariable=wageshour, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxwagesperhours.grid(row=2, column=3)

#etxPosition = Entry(fla, textvariable=Position, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxPosition.grid(row=1, column=3)

#etxgrosspay = Entry(fla, textvariable=Payable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxgrosspay.grid(row=4, column=1)

#etxFinalPay = Entry(fla, textvariable=FinalPayable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxFinalPay.grid(row=4, column=3)

#etxtax = Entry(fla, textvariable=Taxable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxtax.grid(row=3, column=1)

#etxovertime = Entry(fla, textvariable=OverTimeBonus, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
#etxovertime.grid(row=3, column=3)

# =============================== Text Widget ============================================================

payslip = Label(fla, textvariable=DateOfOrder, font=('arial', 23, 'bold'), fg="red", bg="powder blue").grid(row=0,
                                                                                                           column=2)
txtpayslip1 = Text(fla, height=25, width=40, bd=10, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
txtpayslip1.grid(row=1, column=2)

txtpayslip2 = Text(fla, height=25, width=40, bd=10, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
txtpayslip2.grid(row=1, column=1)


# =============================== buttons ===============================================================

btnsalary = Button(flb, text='Weekly Salary', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, fg="red",
                   bg="powder blue", command=weeklywages).grid(row=0, column=0)

btnreset = Button(flb, text='Reset', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, command=reset,
                  fg="red", bg="powder blue").grid(row=0, column=1)

btnpayslip = Button(flb, text='View', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14,
                    command=enterinfo, fg="red", bg="powder blue").grid(row=0, column=2)

btnexit = Button(flb, text='Exit System', padx=16, pady=16, bd=8, font=('arial', 16, 'bold'), width=14, command=exit,
                 fg="red", bg="powder blue").grid(row=0, column=3)

root.mainloop()
