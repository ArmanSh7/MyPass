from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas( width=200, height=200)

#Main Image
lockImg = PhotoImage(file='./asset/logo.png')
canvas.create_image(100, 100, image=lockImg)
canvas.grid(column=1, row=0)


#Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Website EditText(Input box)
websiteinput = Entry(width=35)
websiteinput.focus()
print(websiteinput.get())
websiteinput.grid(column=1, row=1, columnspan=2)

#Email/username label
email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)


#Email EditText(Input box)
emailinput = Entry(width=35)
emailinput.grid(column=1, row=2, columnspan=2)
emailinput.insert(0, "Arman.shahriari7@gmail.com")
#Password label
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Password EditText(Input box)
PassInput = Entry(width=35)
PassInput.grid(column=1, row=3, columnspan=2)
# it checks wether fields that user enetered are correct,
# if it was it saves a data in a file
def save():
    confirmed =confirm()
    if confirmed:
        website = websiteinput.get()
        new_data = {
            website: {
                "email": emailinput.get(),
                "password": PassInput.get()
            }
        }
        try:
            with open("./passwords/pass.json", "r") as passwordFile:
                # load function turns json to python dictionary
                #reading old data
                passes = json.load(passwordFile)
        except FileNotFoundError:
            with open("./passwords/pass.json", "w") as passwordFile:
                # saving updated data
                json.dump(new_data, passwordFile, indent=5)
        else:
            # updating old password file
            passes.update(new_data)
            with open("./passwords/pass.json", "w") as passwordFile:
                # saving updated data
                json.dump(passes, passwordFile, indent=5)
        finally:
                PassInput.delete(0, END)
                websiteinput.delete(0, END)
# it confirms wether user input are valid or not
def confirm():
    if(len(websiteinput.get())==0 or len(emailinput.get())==0 or len(PassInput.get())==0):
        messagebox.showerror(title="Incorrect input" , message="Please fill all the fields!")
        return False;
    return messagebox.askokcancel(title={websiteinput.get()},
                                  message=f'Please confrirm the below informartion\nEmail: '
                                   f'{emailinput.get()}\nPassword:{PassInput.get()}')
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    PassInput.insert(0, password)
    #it copies password to clipboard for user to use it
    pyperclip.copy(password)

def search():
    websiteName=websiteinput.get()
    try:
        with open("./passwords/pass.json", "r") as passwordFile:
            # load function turns json to python dictionary
            # reading old data
            passes = json.load(passwordFile)
    except FileNotFoundError:
        messagebox.showerror(title="No records", message="There are no records in our database")
    else:
        if websiteName in passes:
            messagebox.showinfo(title=websiteName,
                                message=f'The password is {passes[websiteName]["password"]}\n'
                                f'The email:{passes[websiteName]["email"]}')
        else:
            messagebox.showerror(title="Does not exist", message="Please check the company name!")
        return;

# add password Button
addbutton = Button(width=36, text="add Password", command=save)
addbutton.grid(column=1, row=4, columnspan=2)

# generate password Button
generateButton = Button(text="Generate Password", command=generate_password)
generateButton.grid(column=3, row=3,padx = 5, pady=5)

# generate password Button
searchButton = Button(text="Search",  width=15, command=search)
searchButton.grid(column=3, row=1,padx = 5, pady=5)

window.mainloop()
