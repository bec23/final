#Becky Rieger
#program for Kevin's Creamy Confections that allows customers to place orders
#last updated 5/9/2024

#import of needed add-ons
import re
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# def on submit, messagebox verifying user wants to submit, then closes program.
def on_submit():
    response = messagebox.askquestion("Submit", "Are you sure you want to submit?")  # messagebox
    if response == 'yes':
        root.destroy()  # This will close the window
    else:
        return  # This will just close the message box and return to the window


# validate name
def validate_input(char):
    # Allow only alphanumeric characters and space
    return re.match(r'^[a-zA-Z0-9 ]*$', char) is not None


def on_validate(P):
    if validate_input(P):
        return True
    else:
        return False


#pop up message confirming choice, then opening another window
def button_clicked(choice):
    # Display a popup message
    result = messagebox.askokcancel("Confirmation", f"You picked: {choice}. Proceed?")
    if result:
        open_next_window(choice)  # to open second window
    else:
        # Return to the previous window
        return


#def open second window
def open_next_window(choice):
    #if dine in picked
    if choice == "Dine In":
        # Open another window for Dine In
        root2 = tk.Toplevel()
        root2.title("We All Scream For Ice Cream!")
        # set the selections window size
        root2.geometry('800x700+400+400')
        root2.resizable(False, False)
        # label for second window
        options_title = tk.Label(root2, text="You picked Dine In, now let's create your creamy confection!",
                                 font='Arial 18 bold',
                                 bg='light blue', fg='gray')
        options_title.grid(row=0, columnspan=2, sticky=tk.W + tk.E)  # placement

        # Load sundae image
        image_path2 = "images/sundae.jpg"
        image2 = Image.open(image_path2)
        photo2 = ImageTk.PhotoImage(image2)

        # Label widget to display the image
        label2 = tk.Label(root2, image=photo2)
        label2.image = photo2  # Keep a reference to avoid garbage collection
        label2.grid(row=1, column=0)  # Placement on window

        #label to enter name
        name_label = tk.Label(root2, text='Please enter your name', font='Arial 11 bold')
        name_label.grid(row=2, column=0, sticky=tk.W, pady=1, padx=1)  # placement

        #text box for name
        entry_var = tk.StringVar()
        entry = tk.Entry(root2, validate="key", validatecommand=(root.register(on_validate), "%P"),
                         textvariable=entry_var)
        entry.grid(row=3, column=0, sticky=tk.W)  # placement

        #label to chose size
        size_label = tk.Label(root2, text='Please choose a size', font='Arial 11 bold')
        size_label.grid(row=4, column=0, sticky=tk.W, pady=1, padx=1)  # placement
        #list of scoop options
        scoop_options = ["1 scoop", "2 scoops", "3 scoops"]

        # variable to store the selected scoop
        scoop_var = tk.StringVar()
        scoop_var.set(scoop_options[0])  # Set the default value

        # the dropdown menu of size
        scoop_menu = tk.OptionMenu(root2, scoop_var, *scoop_options)
        scoop_menu.grid(row=5, column=0, sticky=tk.W)  # placement

        #label to chose type
        type_label = tk.Label(root2, text='Please choose a type', font='Arial 11 bold')
        type_label.grid(row=8, column=0, sticky=tk.W, pady=5, padx=5)  # placement
        # Create a list of scoop options
        type_options = ["cone", "sundae"]

        #variable to store the selected type
        type_var = tk.StringVar()
        type_var.set(type_options[0])  # Set the default value

        #dropdown menu of type
        type_menu = tk.OptionMenu(root2, type_var, *type_options)
        type_menu.grid(row=9, column=0, sticky=tk.W)  # placement

        #toppings label
        toppings_label = tk.Label(root2, text='Please choose your unlimited toppings', font='Arial 11 bold')
        toppings_label.grid(row=12, column=0, sticky=tk.W, pady=1, padx=1)  # placement

        #variables to store checkboxes
        var1 = tk.StringVar()
        var2 = tk.StringVar()
        var3 = tk.StringVar()
        var4 = tk.StringVar()
        var5 = tk.StringVar()
        var6 = tk.StringVar()
        var7 = tk.StringVar()
        var8 = tk.StringVar()
        var9 = tk.StringVar()

        # Create checkboxes for each topping
        c1 = tk.Checkbutton(root2, text="Nuts", variable=var1, onvalue=1, offvalue=0)
        c2 = tk.Checkbutton(root2, text="Chocolate syrup", variable=var2, onvalue=1, offvalue=0)
        c3 = tk.Checkbutton(root2, text="Strawberry syrup", variable=var3, onvalue=1, offvalue=0)
        c4 = tk.Checkbutton(root2, text="Pineapple syrup", variable=var4, onvalue=1, offvalue=0)
        c5 = tk.Checkbutton(root2, text="Whip cream", variable=var5, onvalue=1, offvalue=0)
        c6 = tk.Checkbutton(root2, text="Sprinkles", variable=var6, onvalue=1, offvalue=0)
        c7 = tk.Checkbutton(root2, text="Sugar cookies", variable=var7, onvalue=1, offvalue=0)
        c8 = tk.Checkbutton(root2, text="Bananas", variable=var8, onvalue=1, offvalue=0)
        c9 = tk.Checkbutton(root2, text="Cherry", variable=var9, onvalue=1, offvalue=0)

        #placement of checkboxes
        c1.grid(row=13, column=0, sticky=tk.W)
        c2.grid(row=14, column=0, sticky=tk.W)
        c3.grid(row=15, column=0, sticky=tk.W)
        c4.grid(row=16, column=0, sticky=tk.W)
        c5.grid(row=17, column=0, sticky=tk.W)
        c6.grid(row=18, column=0, sticky=tk.W)
        c7.grid(row=19, column=0, sticky=tk.W)
        c8.grid(row=20, column=0, sticky=tk.W)
        c9.grid(row=21, column=0, sticky=tk.W)

        # review label
        review_submit_label = tk.Label(root2, text='Please review your order, if everything looks correct press submit',
                                       bg='light yellow', font='Arial 12 bold')
        review_submit_label.grid(row=18, column=1, sticky=tk.W + tk.E, pady=5, padx=5)  # placement
        # review button
        review_submit_button = tk.Button(root2, text='Submit', bg='yellow', command=on_submit)
        review_submit_button.grid(row=19, column=1, sticky=tk.W)  # placement

    elif choice == "Carry Out":
        # Open another window for Dine In
        root2 = tk.Toplevel()
        root2.title("We All Scream For Ice Cream!")
        # set the selections window size
        root2.geometry('800x700+400+400')
        root2.resizable(False, False)
        # label for second window
        options_title = tk.Label(root2, text="You picked Carry Out, now let's create your creamy confection!",
                                 font='Arial 18 bold',
                                 bg='light blue', fg='gray')
        options_title.grid(row=0, columnspan=2, sticky=tk.W + tk.E)  # placement

        # Load sundae image
        image_path2 = "images/sundae.jpg"
        image2 = Image.open(image_path2)
        photo2 = ImageTk.PhotoImage(image2)

        # Label widget to display the image
        label2 = tk.Label(root2, image=photo2)
        label2.image = photo2  # Keep a reference to avoid garbage collection
        label2.grid(row=1, column=0)  # placement

        # label to enter name
        name_label = tk.Label(root2, text='Please enter your name', font='Arial 11 bold')
        name_label.grid(row=2, column=0, sticky=tk.W, pady=1, padx=1)  # placement

        entry_var = tk.StringVar()
        entry = tk.Entry(root2, validate="key", validatecommand=(root.register(on_validate), "%P"),
                         textvariable=entry_var)
        entry.grid(row=3, column=0, sticky=tk.W)  # placement

        # label to chose size
        size_label = tk.Label(root2, text='Please choose a size', font='Arial 11 bold')
        size_label.grid(row=4, column=0, sticky=tk.W, pady=1, padx=1)  # placement
        #list of scoop options
        scoop_options = ["1 scoop", "2 scoops", "3 scoops"]

        # variable to store the selected scoop
        scoop_var = tk.StringVar()
        scoop_var.set(scoop_options[0])  # Set the default value

        # dropdown menu of size
        scoop_menu = tk.OptionMenu(root2, scoop_var, *scoop_options)
        scoop_menu.grid(row=5, column=0, sticky=tk.W)  # placement

        # label to chose type
        type_label = tk.Label(root2, text='Please choose a type', font='Arial 11 bold')
        type_label.grid(row=8, column=0, sticky=tk.W, pady=5, padx=5)  # placement
        # list of scoop options
        type_options = ["cone", "sundae"]

        # variable to store the selected type
        type_var = tk.StringVar()
        type_var.set(type_options[0])  # Set the default value

        # dropdown menu of type
        type_menu = tk.OptionMenu(root2, type_var, *type_options)
        type_menu.grid(row=9, column=0, sticky=tk.W)  # placement

        # toppings label
        toppings_label = tk.Label(root2, text='Please choose your unlimited toppings', font='Arial 11 bold')
        toppings_label.grid(row=12, column=0, sticky=tk.W, pady=1, padx=1)  # placement

        # variables to store checkboxes
        var1 = tk.StringVar()
        var2 = tk.StringVar()
        var3 = tk.StringVar()
        var4 = tk.StringVar()
        var5 = tk.StringVar()
        var6 = tk.StringVar()
        var7 = tk.StringVar()
        var8 = tk.StringVar()
        var9 = tk.StringVar()

        # checkboxes for each topping
        c1 = tk.Checkbutton(root2, text="Nuts", variable=var1, onvalue=1, offvalue=0)
        c2 = tk.Checkbutton(root2, text="Chocolate syrup", variable=var2, onvalue=1, offvalue=0)
        c3 = tk.Checkbutton(root2, text="Strawberry syrup", variable=var3, onvalue=1, offvalue=0)
        c4 = tk.Checkbutton(root2, text="Pineapple syrup", variable=var4, onvalue=1, offvalue=0)
        c5 = tk.Checkbutton(root2, text="Whip cream", variable=var5, onvalue=1, offvalue=0)
        c6 = tk.Checkbutton(root2, text="Sprinkles", variable=var6, onvalue=1, offvalue=0)
        c7 = tk.Checkbutton(root2, text="Sugar cookies", variable=var7, onvalue=1, offvalue=0)
        c8 = tk.Checkbutton(root2, text="Bananas", variable=var8, onvalue=1, offvalue=0)
        c9 = tk.Checkbutton(root2, text="Cherry", variable=var9, onvalue=1, offvalue=0)

        # placement of checkboxes
        c1.grid(row=13, column=0, sticky=tk.W)
        c2.grid(row=14, column=0, sticky=tk.W)
        c3.grid(row=15, column=0, sticky=tk.W)
        c4.grid(row=16, column=0, sticky=tk.W)
        c5.grid(row=17, column=0, sticky=tk.W)
        c6.grid(row=18, column=0, sticky=tk.W)
        c7.grid(row=19, column=0, sticky=tk.W)
        c8.grid(row=20, column=0, sticky=tk.W)
        c9.grid(row=21, column=0, sticky=tk.W)

        # review label
        review_submit_label = tk.Label(root2, text='Please review your order, if everything looks correct press submit',
                                       bg='light yellow', font='Arial 12 bold')
        review_submit_label.grid(row=18, column=1, sticky=tk.W + tk.E, pady=5, padx=5)  # placement
        # review button
        review_submit_button = tk.Button(root2, text='Submit', bg='yellow', command=on_submit)
        review_submit_button.grid(row=19, column=1, sticky=tk.W)  # placement


# root title
root = tk.Tk()
root.title("We All Scream For Ice Cream!")

# Root title label
title = tk.Label(root, text="Welcome to Kevin's Creamy Confections!", font='Arial 20 bold', bg='white',
                 fg='light blue')
# placement
title.grid(row=0, columnspan=1)

# Load ice cream image
image_path = "images/icecream.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Label widget to display the image
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection
label.grid(row=3, column=0)  # Placement

# set the root window size
root.geometry("560x340+250+250")
root.resizable(False, False)

# order label
orderLabel = tk.Label(root, text="To start an order please choose one of the following", font='Arial 12 bold')
# placement of order label
orderLabel.grid(row=5, column=0, sticky=tk.W + tk.E)  # placement

# Create dine in and carry out buttons
button_dine_in = tk.Button(root, text="Dine In", command=lambda: button_clicked("Dine In"))
button_carry_out = tk.Button(root, text="Carry Out", command=lambda: button_clicked("Carry Out"))
# place buttons
button_dine_in.grid(row=10, column=0, padx=10, pady=10)
button_carry_out.grid(row=11, column=0, padx=15)

root.mainloop()
