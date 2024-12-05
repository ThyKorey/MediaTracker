import tkinter as tk # abbreviated to save textspace
from tkinter import filedialog as FileExplorer # Will be used for saving and loading 
from tkinter import ttk # Themed Tkinter
from PIL import Image, ImageTk # used to import images

def main():
    App = MediaTracker()
    App.mainloop() # Lets the program loop so it can open and run

class MediaTracker(tk.Tk): # Main Window Part 1: Defining characteristics
    def __init__(self):
        super().__init__() # Starts the TKinter Function

        self.geometry("300x210") # Size for start window
        self.resizable(False, False) # Prevents it from being resizable 
        self.title("Media Tracker") # Name of Program
        self.iconbitmap('MediaTracker_Icon.ico') # Icon next to Name

        MainWindow = MainWindowFrame(self)
        MainWindow.pack(fill="both", expand= True) # Lets us render the window

class TopSoftwareWindow: # Software Window area
    def __init__(self):
        self.SoftwareWindow = tk.Toplevel()
        self.SoftwareWindow.geometry("800x600")
        self.SoftwareWindow.resizable(False, False)
        self.SoftwareWindow.title("Software Window")
        self.SoftwareWindow.iconbitmap('MediaTracker_Icon.ico') 

class TopAboutWindow: # About Software area
    def __init__(self):
        self.AboutWindow = tk.Toplevel()
        self.AboutWindow.geometry("300x200")
        self.AboutWindow.resizable(False, False)
        self.AboutWindow.title("About Window")
        self.AboutWindow.iconbitmap('MediaTracker_Icon.ico') 

class MainWindowFrame(ttk.Frame): # Main Window Part 2: The interface
    def __init__(self, parent):
        super().__init__(parent)

        self.image = Image.open("MediaTracker_Image.jpg") # Opens the MediaTracker logo Image
        self.photo = ImageTk.PhotoImage(self.image) # Converts the image into something tkinter can work with

        self.label = tk.Label(self, image=self.photo) # puts the image on a empty label

        self.New_btn = ttk.Button(self, text="Start Software", command=self.CallTopSoftwareWindow)
        self.About_btn = ttk.Button(self, text="About Software", command=self.CallAboutWindow)
        self.Quit_btn = ttk.Button(self, text="Quit Software", command=parent.destroy)

        # packs them so they appear on the window

        self.label.pack()
        self.New_btn.pack(fill= "x") # (fill= "x") stretches them to cover the entire window
        self.About_btn.pack(fill= "x")
        self.Quit_btn.pack(fill= "x")

    # Starts the loops for the Toplevel windows

    def CallTopSoftwareWindow(self): 

        self.Looper = TopSoftwareWindow()
        self.Looper.SoftwareWindow.mainloop()

    def CallAboutWindow(self):
        self.Looper = TopAboutWindow()        
        self.Looper.AboutWindow.mainloop()

main()

