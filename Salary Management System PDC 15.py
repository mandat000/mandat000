from tkinter import *

payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Salary Management Systems")


def Exit():
    payroll.destroy()


def Reset():
    EmployeeID.set("")
    CurrentSalary.set("")
    Reference.set("")
    EmployerName.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")


EmployeeID = StringVar()
CurrentSalary = StringVar()
Reference = StringVar()
EmployerName = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
Tax = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()

Tops = Frame(payroll, width=1350, height=50, bd=16, relief=FLAT)
Tops.pack(side=TOP)
LF = Frame(payroll, width=700, height=650, bd=16, relief=RIDGE)
LF.pack(side=LEFT)
RF = Frame(payroll, width=600, height=650, bd=16, relief=RIDGE)
RF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Salary Management System", fg="black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

LeftInsideLF = Frame(LF, width=700, height=100, bd=16, relief=RIDGE)
LeftInsideLF.pack(side=TOP)
LeftInsideLEFT = Frame(LF, width=325, height=400, bd=8, relief=RIDGE)
LeftInsideLEFT.pack(side=LEFT)
LeftInsideREFR = Frame(LF, width=325, height=400, bd=8, relief=RIDGE)
LeftInsideREFR.pack(side=RIGHT)

RightInsideLF = Frame(RF, width=600, height=200, bd=8, relief=RIDGE)
RightInsideLF.pack(side=TOP)
RightInsideLEFT = Frame(RF, width=300, height=400, bd=8, relief=RIDGE)
RightInsideLEFT.pack(side=LEFT)
RightInsideREFR = Frame(RF, width=300, height=400, bd=8, relief=RIDGE)
RightInsideREFR.pack(side=RIGHT)
# -----------------------Left side-------------------------#
lblEmployeeID = Label(LeftInsideLF, font=('arial', 12, 'bold'), text="Employee ID", fg="black", bd=10, anchor='w')
lblEmployeeID.grid(row=0, column=0)
txtEmployeeID = Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg='sky blue',
                      justify='right', textvariable=EmployeeID)
txtEmployeeID.grid(row=0, column=1)
lblCurrentSalary = Label(LeftInsideLF, font=('arial', 12, 'bold'), text="Current Salary", fg="black", bd=10, anchor='w')
lblCurrentSalary.grid(row=1, column=0)
txtCurrentSalary = Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg='sky blue',
                         justify='right', textvariable=CurrentSalary)
txtCurrentSalary.grid(row=1, column=1)

lblReference = Label(LeftInsideLF, font=('arial', 12, 'bold'), text="Reference", fg="black", bd=10, anchor='w')
lblReference.grid(row=2, column=0)
txtReference = Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg='sky blue',
                     justify='right', textvariable=Reference)
txtReference.grid(row=2, column=1)

lblEmployerName = Label(LeftInsideLF, font=('arial', 12, 'bold'), text="Employer Name ", fg="black", bd=10, anchor='w')
lblEmployerName.grid(row=3, column=0)
txtEmployerName = Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54, bg='sky blue',
                        justify='right', textvariable=EmployerName)
txtEmployerName.grid(row=3, column=1)

# ==============

lblBasicSalary = Label(LeftInsideLEFT, font=('arial', 12, 'bold'), text="Basic Salary", fg="black", bd=10, anchor='w')
lblBasicSalary.grid(row=3, column=0)
txtBasicSalary = Entry(LeftInsideLEFT, font=('arial', 12, 'bold'), bd=14, width=18, bg='sky blue',
                       justify='right', textvariable=BasicSalary)
txtBasicSalary.grid(row=3, column=1)

lblOverTime = Label(LeftInsideLEFT, font=('arial', 12, 'bold'), text="Over Time", fg="black", bd=10, anchor='w')
lblOverTime.grid(row=4, column=0)
txtOverTime = Entry(LeftInsideLEFT, font=('arial', 12, 'bold'), bd=14, width=18, bg='sky blue',
                    justify='right', textvariable=OverTime)
txtOverTime.grid(row=4, column=1)

lblGrossPay = Label(LeftInsideLEFT, font=('arial', 12, 'bold'), text="Gross Pay", fg="black", bd=10, anchor='w')
lblGrossPay.grid(row=5, column=0)
txtGrossPay = Entry(LeftInsideLEFT, font=('arial', 12, 'bold'), bd=14, width=18, bg='sky blue',
                    justify='right', textvariable=GrossPay)
txtGrossPay.grid(row=5, column=1)
# =====================================LeftInsideREFR==========================#
lblTax = Label(LeftInsideREFR, font=('arial', 12, 'bold'), text="Tax", fg="black", bd=10, anchor='w')
lblTax.grid(row=2, column=0)
txtTax = Entry(LeftInsideREFR, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
               justify='right', textvariable=Tax)
txtTax.grid(row=2, column=1)

lblPension = Label(LeftInsideREFR, font=('arial', 12, 'bold'), text="Pension", fg="black", bd=10, anchor='w')
lblPension.grid(row=3, column=0)
txtPension = Entry(LeftInsideREFR, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                   justify='right', textvariable=Pension)
txtPension.grid(row=3, column=1)

lblStudentLoan = Label(LeftInsideREFR, font=('arial', 12, 'bold'), text="Student Loan ", fg="black", bd=10, anchor='w')
lblStudentLoan.grid(row=4, column=0)
txtStudentLoan = Entry(LeftInsideREFR, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                       justify='right', textvariable=StudentLoan)
txtStudentLoan.grid(row=4, column=1)

lblNIPayment = Label(LeftInsideREFR, font=('arial', 12, 'bold'), text="NIPayment ", fg="black", bd=10, anchor='w')
lblNIPayment.grid(row=5, column=0)
txtNIPayment = Entry(LeftInsideREFR, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                     justify='right', textvariable=NIPayment)
txtNIPayment.grid(row=5, column=1)
# =================================
# -----------------------Right side-------------------------#
lblPostCode = Label(RightInsideLF, font=('arial', 12, 'bold'), text="Post Code", fg="black", bd=10, anchor='w')
lblPostCode.grid(row=0, column=0)
txtPostCode = Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=46, bg='sky blue',
                    justify='right', textvariable=PostCode)
txtPostCode.grid(row=0, column=1)
lblGender = Label(RightInsideLF, font=('arial', 12, 'bold'), text="Gender", fg="black", bd=10,
                  anchor='w')
lblGender.grid(row=1, column=0)
txtGender = Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=46, bg='sky blue',
                  justify='right', textvariable=Gender)
txtGender.grid(row=1, column=1)
# ---------------------------------Right inner side-------------------#
lblPayDate = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="Pay Date", fg="black", bd=10, anchor='w')
lblPayDate.grid(row=0, column=0)
txtPayDate = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                   justify='right', textvariable=PayDate)
txtPayDate.grid(row=0, column=1)

lblTaxPeriod = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="Tax Period", fg="black", bd=10, anchor='w')
lblTaxPeriod.grid(row=1, column=0)
txtTaxPeriod = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                     justify='right', textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1, column=1)

lblNINumber = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="NI Number ", fg="black", bd=10, anchor='w')
lblNINumber.grid(row=2, column=0)
txtNINumber = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                    justify='right', textvariable=NINumber)
txtNINumber.grid(row=2, column=1)

lblNICode = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="NI Code ", fg="black", bd=10, anchor='w')
lblNICode.grid(row=3, column=0)
txtNICode = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                  justify='right', textvariable=NICode)
txtNICode.grid(row=3, column=1)

lblTaxablePay = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="Taxable Pay ", fg="black", bd=10, anchor='w')
lblTaxablePay.grid(row=4, column=0)
txtTaxablePay = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                      justify='right', textvariable=TaxablePay)
txtTaxablePay.grid(row=4, column=1)

lblPensionablePay = Label(RightInsideLEFT, font=('arial', 12, 'bold'), text="Pensionable Pay ", fg="black", bd=10,
                          anchor='w')
lblPensionablePay.grid(row=5, column=0)
txtPensionablePay = Entry(RightInsideLEFT, font=('arial', 12, 'bold'), bd=10, width=18, bg='sky blue',
                          justify='right', textvariable=PensionablePay)
txtPensionablePay.grid(row=5, column=1)

btnSalaryPayment = Button(RightInsideREFR, padx=8, bd=8, fg="black", font=('arial', 14, 'bold'), width=14,
                          text="Salary Payment", bg="Sky blue").grid(row=0, column=0)

btnResetSystem = Button(RightInsideREFR, padx=8, bd=8, fg="black", font=('arial', 14, 'bold'), width=14,
                        text="Reset System", bg="Sky blue", command=Reset).grid(row=1, column=0)

btnPayReference = Button(RightInsideREFR, padx=8, bd=8, fg="black", font=('arial', 14, 'bold'), width=14,
                         text="Pay Reference", bg="Sky blue").grid(row=2, column=0)

btnPayCode = Button(RightInsideREFR, padx=8, bd=8, fg="black", font=('arial', 14, 'bold'), width=14,
                    text="Pay Code", bg="Sky blue").grid(row=3, column=0)

btnExit = Button(RightInsideREFR, padx=8, bd=8, fg="black", font=('arial', 14, 'bold'), width=14,
                 text="Exit", bg="Sky blue", command=Exit).grid(row=4, column=0)
payroll.mainloop()
