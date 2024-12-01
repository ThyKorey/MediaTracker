import tkinter as tk # abbreviated to save textspace
from tkinter import filedialog as FileExplorer # Will be used for saving and loading 
from tkinter import ttk # Themed Tkinter
from PIL import Image, ImageTk # used to import images

# Variable
File_Open_Status = False 

def main():
    App = MediaTracker()
    App.mainloop()

class MediaTracker(tk.Tk): # Main Window Part 1: Defining characteristics
    def __init__(self):

        # Starts the TKinter Function
        super().__init__()

        self.geometry("300x210")
        self.resizable(False, False)
        self.title("Media Tracker")
        self.iconbitmap('MediaTracker_Icon.ico') 

        MainWindow = MainWindowFrame(self)
        MainWindow.pack(fill="both", expand= True)

class TopSoftwareWindow: # All Program Logic Here
    def __init__(self):
        self.TopWindow = tk.Toplevel()

class TopAboutWindow: # About Software area
    def __init__(self):
        self.TopWindow = tk.Toplevel()

class MainWindowFrame(ttk.Frame): # Main Window Part 2: The interface
    def __init__(self, parent):
        super().__init__(parent)

        self.image = Image.open("MediaTracker_Image.jpg")
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, image=self.photo)

        self.New_btn = ttk.Button(self, text="Start Software", command=self.CallTopSoftwareWindow)
        self.About_btn = ttk.Button(self, text="About Software", command=self.CallAboutWindow)
        self.Quit_btn = ttk.Button(self, text="Quit Software", command=parent.destroy)

        self.label.pack()    

        self.New_btn.pack(fill= "x")
        self.About_btn.pack(fill= "x")
        self.Quit_btn.pack(fill= "x")

    def CallTopSoftwareWindow(self):

        self.Looper = TopSoftwareWindow()
        self.Looper.TopWindow.mainloop()

    def CallAboutWindow(self):
        self.Looper = TopAboutWindow()        
        self.Looper.TopWindow.mainloop()

main()