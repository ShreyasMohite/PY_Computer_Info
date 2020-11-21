from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import threading
import json
import socket
import getpass
from urllib.request import urlopen

class Computer:
    def __init__(self,root):
        self.root=root
        self.root.title("Computer Information")
        self.root.geometry("500x405")
        self.root.iconbitmap("logo591.ico")
        self.root.resizable(0,0)

    


#=================================================================================#

        def clear():
            
            text.delete("1.0","end")

        def searchs():
            try:
                with open("C:/TEMP/computer_info.txt","w") as f:
                    username=getpass.getuser()
                    hostname=socket.gethostname()
                    machine_ip=socket.gethostbyname(hostname)
                    machine_address=socket.gethostbyaddr(machine_ip)
                    
                    url="http://ipinfo.io/json"
                    response=urlopen(url)
                    
                    data=json.load(response) 


                    information=f"""
Username        : {username}
Hostname        : {hostname}
Machine Ip      : {machine_ip}
Wifi Address   : {machine_address[0]}
public              : {data['ip']}
city                  : {data['city']}
state                : {data['region']}
Country           : {data['country']}


                                
"""
                    f.write(information)
                    
                
                with open("C:/TEMP/computer_info.txt","r") as f:
                    text.insert("end",f.read())

                
            except Exception as e:
                tkinter.messagebox.showerror("Error","Network Error Please Turn internet connection ON")

        def thread_search():
            t1=threading.Thread(target=searchs)
            t1.start()
                

#==================================================================================#
        def on_enter1(e):
            but_search['background']="black"
            but_search['foreground']="cyan"
  
        def on_leave1(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

#==================================================================================#
        mainframe=Frame(self.root,width=500,height=405,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=100,bd=3,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=297,bd=3,relief="ridge")
        secondframe.place(x=0,y=100)

#================================firstframe===================================================#

        lab_frame=LabelFrame(firstframe,width=488,height=95,text="COMPUTER INFORMATION",bg="#89b0ae",fg="white")
        lab_frame.place(x=0,y=0)
#==============================================================================================#


        but_search=Button(lab_frame,width=13,text="Extract Information",font=('times new roman',12),cursor="hand2",command=thread_search)
        but_search.place(x=50,y=30)
        but_search.bind("<Enter>",on_enter1)
        but_search.bind("<Leave>",on_leave1)

        but_clear=Button(lab_frame,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=300,y=30)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=============================================================================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=15,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Computer(root)
    root.mainloop()