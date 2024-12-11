import tkinter as tk 
from tkinter import filedialog 
from tkinter import ttk 
from PIL import Image, ImageTk 

# tkinter (tk abbreviated to save textspace) is python's builtin GUI handler
# filedialog will be used for saving and loading 
# ttk is Themed Tkinter, used to get a more modern looking button design
# PIL (Python Imaging Library), more accurately Image and ImageTK is used to import images to use in our Tkinter window

Movies = []
TV_Shows = []
Games = []
Music = []
Books = []
Podcasts = []

# Main Window Part 1: Defining characteristics
class MediaTracker(tk.Tk): 
    def __init__(self):

        # Starts the TKinter Function
        super().__init__() 

        # Size for start window
        self.geometry("300x210") 

        # Prevents it from being resizable 
        self.resizable(False, False) 

        # Name of Program
        self.title("Media Tracker") 
        
        # Icon next to Name
        self.iconbitmap('MediaTracker_Icon.ico') 

        # Lets us render the window
        MainWindow = MainWindowFrame(self)
        MainWindow.pack(fill="both", expand= True)
        
# Main Window Part 2: The interface
class MainWindowFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Opens the MediaTracker logo Image
        self.image = Image.open("MediaTracker_Image.jpg")

        # Converts the image into something tkinter can work with
        self.photo = ImageTk.PhotoImage(self.image)

        # puts the image on a empty label
        self.label = tk.Label(self, image=self.photo)

        self.New_btn = ttk.Button(self, text="Start Software", command=self.CallTopSoftwareWindow)
        self.About_btn = ttk.Button(self, text="About Software", command=self.CallAboutWindow)
        self.Quit_btn = ttk.Button(self, text="Quit Software", command=parent.destroy)

        # Using .pack here as the main window just needs to be simple and requires no complex layout
        self.label.pack()

        # (fill= "x") stretches them to cover the entire window
        self.New_btn.pack(fill= "x") 
        self.About_btn.pack(fill= "x")
        self.Quit_btn.pack(fill= "x")

    # Starts the loops for the Toplevel windows

    def CallTopSoftwareWindow(self): 

        self.CallOnWindow = TopSoftwareWindow()

    def CallAboutWindow(self):

        self.CallOnWindow = TopAboutWindow()        


# Software Window class
class TopSoftwareWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.resizable(False, False)
        self.title("Software Window")
        self.iconbitmap('MediaTracker_Icon.ico')

        # Everything that appears on this window
        # Binding the Enter key to append the list so the user doesn't have to click new entry every time
        self.Entry_Field = ttk.Entry(self)
        self.Entry_Field.bind("<Return>", lambda event: self.addtolist())

        self.Text_List = tk.Listbox(self)
        self.Text_List.bind("<Delete>", lambda event: self.removefromlist())

        self.New_Entry_Btn = ttk.Button(self, text="New Entry", command=self.addtolist)
        self.Remove_Entry_Btn = ttk.Button(self, text="Delete Entry", command=self.removefromlist)
       
        self.Category_Dropdown = ttk.Combobox(self, state="readonly", values=["Movies", "TV Shows", "Games", "Music", "Books", "Podcasts"])
        self.Category_Dropdown.set("Movies")
        self.Category_Dropdown.bind("<<ComboboxSelected>>", lambda event: self.CategorySelected())

        self.Save_File_Btn = ttk.Button(self, text="Save File")
        self.Load_File_Btn = ttk.Button(self, text="Load File")
        self.Quit_Btn = ttk.Button(self, text="Quit", command=self.destroy)

        # Using .place to manually place the assets across the window as the window is unresizeable to the user

        self.Entry_Field.place(x= 0, y= 3, width= 720)
        
        self.New_Entry_Btn.place(x= 722, y= 0)

        self.Text_List.place(x= 0, y= 25, width= 620, height= 570)
        self.Category_Dropdown.place(x=621, y=25, width= 99)

        self.Remove_Entry_Btn.place(x=722, y= 25)

        self.Save_File_Btn.place(x= 621, y= 495, width= 178)
        self.Load_File_Btn.place(x= 621, y= 520, width= 178)
        self.Quit_Btn.place(x= 621, y= 570, width= 178)

    def addtolist(self):
        global Movies
        global TV_Shows
        global Games
        global Music
        global Books
        global Podcasts
        
        text = self.Entry_Field.get()

        if text:
            Cate_Selection = self.Category_Dropdown.get()
            if Cate_Selection == "Movies":
                Movies.append(text)
            elif Cate_Selection == "TV Shows":
                TV_Shows.append(text)
            elif Cate_Selection == "Games":
                Games.append(text)
            elif Cate_Selection == "Music":
                Music.append(text)
            elif Cate_Selection == "Books":
                Music.append(text)
            elif Cate_Selection == "Podcasts":
                Podcasts.append(text)

            self.Text_List.insert(tk.END, text)
            self.Entry_Field.delete(0, tk.END)

    def removefromlist(self):
        global Movies
        global TV_Shows
        global Games
        global Music
        global Books
        global Podcasts

        Selection = self.Text_List.curselection()
        Cate_Selected = self.Category_Dropdown.get()

        if Cate_Selected == "Movies":
            for i in range(len(Movies)):
                if Selection == Movies[i]:
                    Movies.pop(i)
                    break

        elif Cate_Selected == "TV Shows":
            for i in range(len(TV_Shows)):
                if Selection == TV_Shows[i]:
                    TV_Shows.pop(i)
                    break

        elif Cate_Selected == "Games":
            for i in range(len(Games)):
                if Selection == Games[i]:
                    Games.pop(i)
                    break

        elif Cate_Selected == "Music":
            for i in range(len(Music)):
                if Selection == Music[i]:
                    Music.pop(i)
                    break

        elif Cate_Selected == "Books":
            for i in range(len(Books)):
                if Selection == Books[i]:
                    Books.pop(i)
                    break

        elif Cate_Selected == "Podcasts":
            for i in range(len(Podcasts)):
                if Selection == Podcasts[i]:
                    Podcasts.pop(i)
                    break

        self.Text_List.delete(Selection)

    def CategorySelected(self):
        global Movies
        global TV_Shows
        global Games
        global Music
        global Books
        global Podcasts

        Cate_Selection = self.Category_Dropdown.get()
        if Cate_Selection == "Movies":
            Movies.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(Movies)):
                self.Text_List.insert(tk.END, Movies[i])

        elif Cate_Selection == "TV Shows":
            TV_Shows.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(TV_Shows)):
                self.Text_List.insert(tk.END, TV_Shows[i])

        elif Cate_Selection == "Games":
            Games.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(Games)):
                self.Text_List.insert(tk.END, Games[i])

        elif Cate_Selection == "Music":
            Music.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(Music)):
                self.Text_List.insert(tk.END, Music[i])
        
        elif Cate_Selection == "Books":
            Books.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(Books)):
                self.Text_List.insert(tk.END, Books[i])
        
        elif Cate_Selection == "Podcasts":
            Podcasts.sort()
            self.Text_List.delete(0, tk.END)
            for i in range(len(Podcasts)):
                self.Text_List.insert(tk.END, Podcasts[i])


# About Software class
class TopAboutWindow(tk.Toplevel): 
    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.resizable(False, False)
        self.title("About Window")
        self.iconbitmap('MediaTracker_Icon.ico')

        # Opens the MediaTracker logo Image
        self.image = Image.open("MediaTracker_Image_Vertical.jpg") 

        # Converts the image into something tkinter can work with
        self.photo = ImageTk.PhotoImage(self.image)

        # puts the image on a empty label
        self.img_label = tk.Label(self, image=self.photo)

        self.label1 = ttk.Label(self, text="Korey Bibie 2024")
        self.label2 = ttk.Label(self, text="This program was designed to help those who")
        self.label3 = ttk.Label(self, text="struggle like I do keeping track of Media")

        self.img_label.pack(side= "top")
        
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label1.pack(side="top")



def main():
    App = MediaTracker()
    # Lets the program loop so it can open and run
    App.mainloop() 

main()
