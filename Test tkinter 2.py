import tkinter as tk
#imports
class App(tk.Tk):#base class
    def __init__(self):
        super().__init__()#gets tk.Tk attributes (makes into a window
        self.terminate = False
        self.show = False
        #variables
        self.title =("login Menu")
        self.geometry("250x125")
        #sets up window information
        self.submit_button = tk.Button(self,text="submit",command=lambda:self.returnData())
        self.submit_button.grid(padx=0,pady=0,column=1,row=4,columnspan=1,rowspan=1,sticky="e")
        #sets up and places submit button
        #
        self.show_password_button = tk.Button(self,text="show password", command = lambda:self.changeEntry())
        self.show_password_button.grid(padx=0,pady=0,column=0,row=3,columnspan=1,rowspan=1,sticky="w")
        #sets up and places show password button
class Login(App):#login screen class
    def __init__(self):
        super().__init__()#gets all objects from class "App"
        self.Username_Label = tk.Label(self,text="Username:")
        self.Username_Label.grid(padx=0,pady=0,column=0,row=0,columnspan=1,rowspan=1,sticky="w")
        self.Username_entry = tk.Entry(self)
        self.Username_entry.grid(padx=0,pady=0,column=1,row=0,columnspan=1,rowspan=1,sticky="e")
        #sets up Username label and entry feild
        #
        self.Password_Label = tk.Label(self,text="Password:")
        self.Password_Label.grid(padx=0,pady=0,column=0,row=1,columnspan=1,rowspan=1,sticky="w")
        self.Password_entry = tk.Entry(self,show="*")
        self.Password_entry.grid(padx=0,pady=0,column=1,row=1,columnspan=1,rowspan=1,sticky="e")
        #sets up password label and entry feild
    def changeEntry(self):#called by show password button
        if self.show == False:#if password is currently hidden
            self.Password_entry.config(show="")#show password
            self.show_password_button.config(text="hide password")#change button text
            self.show = True #inform of the change
        elif self.show == True: #if password is currently shown
            self.Password_entry.config(show="*")#hide password
            self.show_password_button.config(text="show password")#change button text
            self.show = False#inform of change
    def returnData(self):#called by submit button
        self.Username = self.Username_entry.get()
        self.Password=self.Password_entry.get()
        #gets username and password from entry data to class objects
        self.destroy()#destroys frame
    def getData(self):#called externally
        try:
            if self.Password!= "":
                if self.Username!= "":
        #testing for username and password to exist and be real strings
                    return(self.Username,self.Password)#returns username and password
            return("","")
        except:
            return("","")
class Create(App):#create account screen class
    def __init__(self):
        super().__init__()
        self.Username_Label = tk.Label(self,text="Username:")
        self.Username_Label.grid(padx=0,pady=0,column=0,row=0,columnspan=1,rowspan=1,sticky="w")
        self.Username_entry = tk.Entry(self)
        self.Username_entry.grid(padx=0,pady=0,column=1,row=0,columnspan=1,rowspan=1,sticky="e")
        #
        #
        #
        #
        self.Password_Label = tk.Label(self,text="Password:")
        self.Password_Label.grid(padx=0,pady=0,column=0,row=1,columnspan=1,rowspan=1,sticky="w")
        self.Password_entry = tk.Entry(self,show="*")
        self.Password_entry.grid(padx=0,pady=0,column=1,row=1,columnspan=1,rowspan=1,sticky="e")
        #
        #repeat of what's in the login class
        self.Password_confirm_Label = tk.Label(self,text="Password Confirm:")
        self.Password_confirm_Label.grid(padx=0,pady=0,column=0,row=2,columnspan=1,rowspan=1,sticky="w")
        self.Password_confirm_entry = tk.Entry(self,show="*")
        self.Password_confirm_entry.grid(padx=0,pady=0,column=1,row=2,columnspan=1,rowspan=1,sticky="e")
        #adds a password confirm label and entry
    def changeEntry(self):#called by show password button
        if self.show == False:
                self.Password_entry.config(show="")
                self.Password_confirm_entry.config(show="")
                self.show_password_button.config(text="hide password")
                self.show = True
        elif self.show == True:
            self.Password_entry.config(show="*")
            self.Password_confirm_entry.config(show="*")
            self.show_password_button.config(text="show password")
            self.show = False
        #repeat of what's in login screen class except the addition of password_confirm_entry conforming to the same changes
    def returnData(self):#called by submit button
        self.Username=self.Username_entry.get()
        self.Password=self.Password_entry.get()
        self.Password_confirm=self.Password_confirm_entry.get()
        self.destroy()
        #repeat of what's in login screen class execpt the addition of Password_confirm
    def getData(self):#called externally
        return(self.Username,self.Password,self.Password_confirm)
    #repeat of what's in login screen class execpt that addition of Password_confirm
if __name__== "__main__":#if this program is run on its own
    TestWindow=Login() #creates login window
    TestWindow.mainloop() #maintans window
    Username,Password = TestWindow.getData()#gets entry data
    print(Username)#test
    print(Password)#test
    TestWindow_two=Create()#creates create account window
    TestWindow_two.mainloop()#maintains window
    Username,Password,Password_confirm=TestWindow_two.getData()#gets entry data
    print(Username)#test
    print(Password)#test
    print(Password_confirm)#test
