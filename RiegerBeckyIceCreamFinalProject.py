import tkinter as tk
from tkinter import messagebox
def open_next_window(choice):
    if choice == "Dine In":
        # Open another window for Dine In
        selections=tk.Toplevel()
        selections.title("We All Scream For Ice Cream!")

    elif choice == "Carry Out":
        # Open another window for Carry Out
        selections=tk.Toplevel()
        selections.title("We All Scream For Ice Cream!")        

def button_clicked(choice):
    # Display a popup message
    result = messagebox.askokcancel("Confirmation", f"You picked: {choice}. Proceed?")
    if result:
        open_next_window(choice)
    else:
        # Return to the previous window
        print("Canceled")
#root title
root = tk.Tk()
root.title("We All Scream For Ice Cream!")

#Root title label
title = tk.Label (root, text = "Welcome to Kevin's Creamy Confections!", font=('Arial 20 bold'), bg='white', fg='light blue')
#placement
title.grid(row=0,columnspan=2, sticky=tk.W+tk.E)

#selections title
selections=tk.Toplevel()
selections.title("We All Scream For Ice Cream!")

#set the root window size
root.geometry('640x480+300+300')
root.resizable(False, False)

#set the selections window size
selections.geometry('640x480+300+300')
selections.resizable(False, False)

#order label
orderLabel=tk.Label(root, text="To start an order please choose one of the following", font=('Arial 12 bold'))
#placement of order label
orderLabel.grid(row=3, column=0, sticky=tk.W+tk.E)


# Create buttons
button_dine_in = tk.Button(root, text="Dine In", command=lambda: button_clicked("Dine In"))
button_carry_out = tk.Button(root, text="Carry Out", command=lambda: button_clicked("Carry Out"))
#place buttons
button_dine_in.grid(row=10,column=0, sticky=tk.W+tk.E)
button_carry_out.grid(row=12,column=0,sticky=tk.W+tk.E)

root.mainloop()

        
