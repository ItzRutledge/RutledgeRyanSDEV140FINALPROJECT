from tkinter import *
#THIS IS THE ROOT WINDOW OF RECIPE TO GROCERY LIST
root = Tk()
root.title('Recipe to Store')


#Frame that still needs a borderline with my meal options within
frame = LabelFrame(root, text="Please Select 5 Meals for the Week", bd = 5, padx=5, pady=5)
frame.grid(row=0,column=0,rowspan=50,columnspan=50)

#variables associated with each meal
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()




#Creation of a new window that displays the ingredients needed for each recipe.

def OpenNewWindow():
    NewWindow=Toplevel(root)

    NewWindow.title("Ingredients List")

    NewWindow.geometry("400x400")
    BT1 = Label(NewWindow, text = "1 lb Ground Beef, 12 pack of crunch shells, Lettuce, Tomatoes, Shredded Mexican Cheese.", padx=5,pady=5)
    BT1.grid(row=0, column=0)
    CSF = Label(NewWindow, text="1 lb Chicken Breast, Lo Mein Noodles, 2 Carrots, 1 White Onion, 1 Broccoli Head.", padx=5, pady=5)
    CSF.grid(row=1,column=0)
    HHB = Label(NewWindow, text="1 lb Ground Beef, Hamburger Helper Box", padx=5, pady=5)
    HHB.grid(row=2,column=0)
    HHT = Label(NewWindow, text="1 lb Ground Turkey, Hamburger Helper Box", padx=5, pady=5)
    HHT.grid(row=3,column=0)
    button_quit2 = Button(NewWindow, text="Leave the Ingredients Page.", command= NewWindow.destroy)
    button_quit2.grid(row=4, column=0)
# Attempting to display the recipe if the Checkboxes are selected for each meal variable.
def isChecked():
    if var1.get() == 1:
       BT1()
    elif var1.get() == 0:
       NULL
    if var2.get() == 1:
        CSF()
    elif var2.get() == 0:
       NULL
    if var3.get() == 1:
        HHB()
    elif var3.get() == 0:
       NULL
    if var4.get() == 1:
        HHT()
    elif var4.get() == 0:
       NULL

#Checkboxes for each of the meals available
Beef_Taco = Checkbutton(root, text = "Beef Taco Dinner", variable = var1, onvalue=1, offvalue=0, command=isChecked)
Beef_Taco.grid(row=1, column=0)
Chicken_Stir_Fry = Checkbutton(root, text = "Chicken & Veg Stir Fry", variable = var2, onvalue=1, offvalue=0, command=isChecked)
Chicken_Stir_Fry.grid(row=2, column=0)
Hamburger_HelperB = Checkbutton(root, text = "Hamburger Helper (Beef)", variable = var3, onvalue=1, offvalue=0, command=isChecked)
Hamburger_HelperB.grid(row=3, column=0)
Hamburger_HelperT = Checkbutton(root, text = "Hamburger Helper (Turkey)", variable = var4, onvalue=1, offvalue=0, command=isChecked)
Hamburger_HelperT.grid(row=4, column=0)

#button to exit the root window
button_quit= Button(root, text="Leave the Application.", command= root.destroy)
button_quit.grid(row=6, column=0)
    

#Button that user will click once they have selected 5 meals
mybutton = Button(root, text="View Ingredients", command=OpenNewWindow)
mybutton.grid(row=6,column=3)
root.mainloop()

