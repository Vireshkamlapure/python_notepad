from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    file = TextArea.get(1.0,END)
    if not file.strip():
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0 ,END)
    else:
        result = messagebox.askyesnocancel("Save Dialog Box","Do you want to save your file")
        if result==True:
            file = asksaveasfilename(defaultextension = '.txt',filetypes=[('Text File','*.txt'),('All files','*.*')])
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            root.title("Untitled - Notepad")
            TextArea.delete(1.0,END)
        elif result==False:
            root.title("Untitled - Notepad")
            TextArea.delete(1.0,END)
    
    #delete function will delete data from first line zero character to end of file 


def openFile():
    global file 
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files" , "*.*" ),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        print("File Opened")

def saveFile():
    global file 
    if (file==None):
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files" , "*.*" ),("Text Documents","*.txt")])

        if(file==""):
            file=None
        else:
            #Save as a new file 
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        #save the file 
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        print("Existing File Saved")

def saveFileAs():
    global file
    file = asksaveasfilename(defaultextension = '.txt',filetypes=[('Text File','*.txt'),('All files','*.*')])
    f = open(file,"w")
    f.write(TextArea.get(1.0,END))
    root.title(os.path.basename(file)+ " - Notepad")
    print("File Saved-AS")
    f.close()

def quitApp():
    file = TextArea.get(1.0,END)
    if not file.strip():
        quit()
    else:
        result = messagebox.askyesnocancel("Save Dialog Box","Do you want to save your file")
        if result==True:
            file = asksaveasfilename(defaultextension = '.txt',filetypes=[('Text File','*.txt'),('All files','*.*')])
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            root.title(os.path.basename(file)+ " - Notepad")
        elif result==False:
            quit()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad","Notepad by Viresh Kamlapure \n Its PWP microproject")

if __name__ == '__main__':
    #Basic tkinter setup 
    root  = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("500x488")

    #Add TextArea 
    TextArea = Text(root,font="lucida 13 ")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    #Menubar 
    MenuBar = Menu(root)

    #File Menu starts 
    FileMenu = Menu(MenuBar,tearoff=0)
    # For open new file 
    FileMenu.add_command(label="New",command=newFile)
    #For open aldready existing file 
    FileMenu.add_command(label="Open",command=openFile)
    # For save the current file 
    FileMenu.add_command(label="Save",command=saveFile)

    # For save the current file 
    FileMenu.add_command(label="Save As",command=saveFileAs)
    FileMenu.add_separator()
    #For quit app 
    FileMenu.add_command(label="Exit",command= quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #File Menu Ends 

    #Edit Menu starts 
    EditMenu = Menu(MenuBar,tearoff=0)
    #For feature of cut, copy , paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    #Edit Menu Ends 

    #Help Menu starts
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    #Help Menu ends

    root.config(menu=MenuBar)

    #Adding Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()