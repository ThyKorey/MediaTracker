import tkinter as tk # abbreviated to save textspace
from tkinter import filedialog as FileExplorer # Will be used for saving and loading 
from tkinter import ttk # Themed Tkinter
from PIL import Image, ImageTk # used to import images



class MediaTracker(tk.Tk): # Main Window Part 1: Defining characteristics
    def __init__(self):
        super().__init__() # Starts the TKinter Function

        self.geometry("300x210") # Size for start window
        self.resizable(False, False) # Prevents it from being resizable 
        self.title("Media Tracker") # Name of Program
        self.iconbitmap('MediaTracker_Icon.ico') # Icon next to Name

        MainWindow = MainWindowFrame(self)
        MainWindow.pack(fill="both", expand= True) # Lets us render the window



class MainWindowFrame(ttk.Frame): # Main Window Part 2: The interface
    def __init__(self, parent):
        super().__init__(parent)

        self.image = Image.open("MediaTracker_Image.jpg") # Opens the MediaTracker logo Image
        self.photo = ImageTk.PhotoImage(self.image) # Converts the image into something tkinter can work with

        self.label = tk.Label(self, image=self.photo) # puts the image on a empty label

        self.New_btn = ttk.Button(self, text="Start Software", command=self.CallTopSoftwareWindow)
        self.About_btn = ttk.Button(self, text="About Software", command=self.CallAboutWindow)
        self.Quit_btn = ttk.Button(self, text="Quit Software", command=parent.destroy)

        # Using .pack here as the main window just needs to be simple and requires no complex layout

        self.label.pack()
        self.New_btn.pack(fill= "x") # (fill= "x") stretches them to cover the entire window
        self.About_btn.pack(fill= "x")
        self.Quit_btn.pack(fill= "x")

    # Starts the loops for the Toplevel windows

    def CallTopSoftwareWindow(self): 

        self.CallOnWindow = TopSoftwareWindow()

    def CallAboutWindow(self):

        self.CallOnWindow = TopAboutWindow()        



class TopSoftwareWindow: # Software Window area
    def __init__(self):
        self = tk.Toplevel()
        self.geometry("800x600")
        self.resizable(False, False)
        self.title("Software Window")
        self.iconbitmap('MediaTracker_Icon.ico') 

        # Everything that appears on this window
        self.Entry_Field = ttk.Entry(self)

        self.Text_List = tk.Listbox(self)
        self.Category_List = tk.Listbox(self)

        self.New_Entry_Btn = ttk.Button(self, text="New Entry")
        self.Save_File_Btn = ttk.Button(self, text="Save File")
        self.Load_File_Btn = ttk.Button(self, text="Load File")
        self.Quit_Btn = ttk.Button(self, text="Quit")

        # Note to self, Replace .pack with .grid more complex layout also tryout .place since windows cant be resized
        self.Entry_Field.place(x= 0, y= 0, width= 724)

        self.New_Entry_Btn.place(x= 725, y= 0)

        self.Text_List.place(x= 0, y= 25, width= 625, height= 570)
        self.Category_List.place(x= 626, y= 25, width= 99, height= 570)

        self.Save_File_Btn.place(x= 725, y= 25)
        self.Load_File_Btn.place(x= 725, y= 50)
        self.Quit_Btn.place(x= 725, y= 570)



class TopAboutWindow: # About Software area
    def __init__(self):
        self = tk.Toplevel()
        self.geometry("300x200")
        self.resizable(False, False)
        self.title("About Window")
        self.iconbitmap('MediaTracker_Icon.ico')

        self.image = Image.open("MediaTracker_Image.jpg") # Opens the MediaTracker logo Image
        self.photo = ImageTk.PhotoImage(self.image) # Converts the image into something tkinter can work with

        self.img_label = tk.Label(self, image=self.photo) # puts the image on a empty label
        self.credit = ttk.Label(self, text="Korey Bibie 2024")
        self.label1 = ttk.Label(self, text="This program was designed to help those who")
        self.label2 = ttk.Label(self, text="struggle like I do keeping track of Media")

        self.img_label.pack(side= "top")
        
        self.label1.pack(side="top")
        self.label2.pack(side="top")

        self.credit.pack(side="top")

def main():
    App = MediaTracker()
    App.mainloop() # Lets the program loop so it can open and run

main()

main()

