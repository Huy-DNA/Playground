from tkinter import Tk, OptionMenu, Button, Entry, Toplevel, StringVar, mainloop
from tkinter.ttk import Label
from tkinter import messagebox
import sys
from RSA_encrypt import RSA
from RSA_decrypt import decrypt

#data placeholder
accDict = {}
with open("account_login_GUI.txt", "r") as f:
    for line in f:
        key, *val = line.split(sep = "$")
        accDict[key] = [decrypt(val[0]), decrypt(val[2]), decrypt(val[1])] 
#set up workspace
root = Tk()
root.title("Login")
root.geometry("400x300+550+250")
root.resizable(0, 0)
root.iconbitmap(".\\icon.ico")

#function for command
 #Close window
def onClosing(event = ""):
    if messagebox.askokcancel("Close window", "Do you want to close the app?"):
        sys.exit(0)
 #Login
def clickLogin(event = ""):
    accInput = accountEnt.get()
    passInput = passEnt.get()
    if accDict.get(accInput, [None])[0] == passInput:
        messagebox.showinfo("Login", "Login successful!")
        root.destroy()
    else:
        messagebox.showerror("Login", "Login failed")
 #Register section
def clickRegister(event = ""):
    #register workspace setup
    res = Toplevel(root)
    res.title("Register")
    res.geometry("400x300+550+250")
    res.resizable(0, 0)
    res.iconbitmap(".\\icon.ico")

    #widgets
    newAccountName = Label(res, text = "Account name: ")
    newAccountName.place(x = 130, y = 70, anchor = "center")
    password = Label(res, text = "Password: ")
    password.place(x = 144, y = 100, anchor = "center")
    passwordReEnter = Label(res, text = "Re-enter password: ")
    passwordReEnter.place(x = 120, y = 130, anchor = "center")
    recQues = Label(res, text = "Recovery question: ")
    recQues.place(x = 120, y = 160, anchor = "center")
    recAns = Label(res, text = "Answer: ")
    recAns.place(x = 147, y = 190, anchor = "center")
    
    accountEnt = Entry(res)
    accountEnt.place(x = 240, y = 70, anchor = "center")
    passEnt = Entry(res, show = "*")
    passEnt.place(x = 240, y = 100, anchor = "center")
    passwordReEnterEnt = Entry(res, show = "*")
    passwordReEnterEnt.place(x = 240, y = 130, anchor = "center")
    ansEnt = Entry(res)
    ansEnt.place(x = 240, y = 190, anchor = "center")

    #sub function
    def clickRegister_register(event = ""):
        accInput = accountEnt.get()
        passInput = passEnt.get()
        reEnterInput = passwordReEnterEnt.get()
        if accInput == "":
            messagebox.showwarning("Warning", "Enter account name!")
        elif "$" in accInput:
            messagebox.showwarning("Warning", "$ is not allowed in account name!")
        elif accInput in accDict:
             messagebox.showerror("Error", "Account already exists")
        elif passInput == "":
             messagebox.showwarning("Warning", "Enter password!")
        elif passInput != reEnterInput:
            messagebox.showerror("Register", "Re-entered password is different from entered password.")
        else:
            quesInput = ques.get()
            answerInput = ansEnt.get()
            if quesInput == "Choose a recovery question":
                messagebox.showerror("Error", "Choose a recovery question.")
            elif answerInput == "":
                messagebox.showerror("Error", "Enter an answer.")
            else:
                messagebox.showinfo("Registed", "Registered successfully!")
                accDict.update({accInput:[passInput, quesInput, answerInput]})
                with open("account_login_GUI.txt", "a") as f:
                    f.write(f"{accInput}${RSA(passInput)}${RSA(answerInput)}${RSA(quesInput)}\n")
                res.destroy()

    ques = StringVar()
    ques.set("Choose a recovery question")
    quesList = OptionMenu(res, ques, *quiz)
    quesList.place(x = 175, y = 160, anchor = "w")

    registerBut = Button(res, text = "Register", command = clickRegister_register)
    registerBut.place(x = 230, y = 220, anchor = "center")
    
    #Give focus
    accountEnt.focus()

    #Event binding
    registerBut.bind("<Return>", clickRegister_register)
    res.bind("<Alt-KeyPress-F4>", onClosing)
    
    res.grab_set()

 #Forgot password section
def clickForgotPassword(event = ""):
    forgot = Toplevel(root)
    forgot.title("Forgot password")
    forgot.geometry("400x300")
    forgot.resizable(0, 0)
    forgot.iconbitmap(".\\icon.ico")

    #widgets    
    accountName = Label(forgot, text = "Account name: ")
    accountName.place(x = 130, y = 70, anchor = "center")
    recQues= Label(forgot, text = "Recovery question: ")
    recQues.place(x = 120, y = 100, anchor = "center")
    recAns = Label(forgot, text = "Answer: ")
    recAns.place(x = 147, y = 130, anchor = "center")
    
    accountEnt = Entry(forgot)
    accountEnt.place(x = 240, y = 70, anchor = "center")
    ansEnt = Entry(forgot)
    ansEnt.place(x = 240, y = 130, anchor = "center")

    ques = StringVar()
    ques.set("Choose your recovery question")
    quesList = OptionMenu(forgot, ques, *quiz)
    quesList.place(x = 175, y = 100, anchor = "w")

    #sub function
    def accountRecovery(event = ""):
        acc = accountEnt.get()
        if acc == "":
            messagebox.showerror("Account recovery", "Enter an account!")
        elif not acc in accDict:
            messagebox.showerror("Account recovery", f"{acc} doesn't exists!")
        else:
            if accDict[acc][1] != ques.get() or accDict[acc][2] != ansEnt.get():
                messagebox.showerror("Account recovery", "Incorrect recovery question or answer.")
            else:
                messagebox.showinfo("Account recovery", f"{acc}'s password is {accDict[acc][0]}")

    recBut = Button(forgot, text = "Recover account", command = accountRecovery)
    recBut.place(x = 200, y = 160, anchor = "center")

    #give focus
    accountEnt.focus()

    #event binding
    recBut.bind("<Return>", accountRecovery)
    forgot.bind("<Alt-KeyPress-F4>", onClosing)

    forgot.grab_set()
#widgets
titlelb = Label(root, text = "Welcome!", font = (18), foreground = "black")
titlelb.place(x = 200, y = 90, anchor = "center")
accountlb = Label(root, text = "Account name or email: ")
accountlb.place(x = 100, y = 130, anchor = "center")
passlb = Label(root, text = "Password: ")
passlb.place(x = 137, y = 160, anchor = "center")
accountEnt = Entry(root)
accountEnt.place(x = 230, y = 130, anchor = "center")
passEnt = Entry(root, show = "*")
passEnt.place(x = 230, y = 160, anchor = "center")
loginBut = Button(root, text = "Login", command = clickLogin)
loginBut.place(x = 170, y = 220, anchor = "center")
registerBut = Button(root, text = "Register", command = clickRegister)
registerBut.place(x = 230, y = 220, anchor = "center")
forgotPass = Button(root, text = "Forgot password?", command = clickForgotPassword, bd = 0, fg = "#B00857", font = ("TkDefaultFont 10 underline"))
forgotPass.place(x = 240, y = 185, anchor = "center")

#give focus
accountEnt.focus()

#event binding
loginBut.bind("<Return>", clickLogin)
registerBut.bind("<Return>", clickRegister)
forgotPass.bind("<Return>", clickForgotPassword)
root.protocol("WM_DELETE_WINDOW", onClosing)
root.bind("<Alt-KeyPress-F4>", onClosing)

#recovery questions
quiz = ["What's your pet's name?",
"What's your favorite name?",
"What's your favorite food?",
"Favorite programming language?"]
#hold the workspace
mainloop()