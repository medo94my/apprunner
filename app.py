import tkinter as tk
from tkinter import filedialog, Text,messagebox
import os
Application_name='app runner'.capitalize() 
root =tk.Tk()
root.title(Application_name)

apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt','r')as f:
        tempApps=f.read()
        tempApps=tempApps .split(',')
        apps=[x for x in tempApps if x.split()]
def addApp():
    filename = filedialog.askopenfilename(initialdir='/',title="Select File",
    filetypes=(('executables','*.exe'),('all files',"*.*")))
    if filename != '':
        if filename not in apps:
            listbox.insert(tk.END, filename)
            apps.append(filename)
        else:
            messagebox.showinfo("WARNING", "File Duplicates Found . please choose applicaton only once  ".capitalize())
    else:
        pass

def runApps():
    for app in apps:
        os.startfile(app)
def removeApp():
    msg=messagebox.askyesno("delete file warning ".capitalize(), "Are you sure that you want to delete this application from your list?")
    if msg ==True:
        inderx=OnButtonClick()
        App_name=tk.ANCHOR
        listbox.delete(App_name)
        del apps[inderx[0]]
    else:
        pass
def OnButtonClick():
    selection = listbox.curselection()
    return selection
label=tk.Label(root, text="Welcome to Application Runner",justify=tk.CENTER, font=("Arial Bold", 20))
label.pack()
canvas =tk.Canvas(root, height=700,width=700,bg="#263238" )
canvas.pack()
listbox=tk.Listbox(canvas, bg="#ECEFF1")
listbox.place(relwidth=0.8,relheight=0.8, relx=0.1,rely=0.1)
frame_btn=tk.Frame(root, bg="#455A64")
frame_btn.pack(side=tk.BOTTOM, fill=tk.BOTH)

open_file = tk.Button(frame_btn,padx=10, pady=5, text="Open File",fg='white',bg="#388E3C", command=addApp)
open_file.pack(in_=frame_btn, side=tk.LEFT)
openApps = tk.Button(frame_btn,padx=10, pady=5, text="Run Apps",fg='white',bg="#0288D1", command=runApps)
openApps.pack(in_=frame_btn, side=tk.LEFT)
removeApps = tk.Button(frame_btn,padx=10, pady=5,fg='white',bg="#BF360C", text = "Delete", command = removeApp)  
removeApps.pack(in_=frame_btn, side=tk.LEFT)
for index ,app in enumerate(apps) :
        # label=tk.Label(frame,text=app,bg="gray")
        # label.pack()
        listbox.insert(index,app)
root.mainloop()
with open ('save.txt','w')as f:
    for app in apps:
        f.write(app+',')
