from tkinter import *
import time
import pickle
import sys,os
from os import path
from wakeonlan import send_magic_packet
from pygame import mixer



def inf():
    from tkinter import messagebox
    messagebox.showinfo("showinfo", "Requirements\n"
                                    "* Ethernet connection."
                                    "\n"
                                    "* A peer to peer network between two or more computers."
                                    "\n"
                                    "* The computer must be in either sleep or hibernation mode for this to work."
                                    "\n"
                                    "* Windows Configuration.\n"
                                    "* Bios Configuration\n"
                                    "* IP Address - Mac Address\n")
data_save_control={}
def My_data_Load():
    global data_save_control
    try:
        with open('.\data\data_save_control_w.pkl', 'rb') as f:
            data_save_control = pickle.load(f)
        #     ****for one file****
        # bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
        # path_to_data = path.join(bundle_dir, 'data', 'data_save_control_w.pkl')

    except:
        pass
    return data_save_control
My_data_Load()

main_tikinter=Tk()
# main_tikinter.iconbitmap(default="./data/favicon.ico")
# main_tikinter.title("")

#-------------Main Geometri--------------------
main_tikinter.geometry("160x200+1870+850")
main_tikinter.minsize(170,230)
main_tikinter.maxsize(170,250)

notification=Label(main_tikinter,text="")
def WOL():
    global notification
    notification.destroy()
    try:
        send_magic_packet(str(mac), ip_address=str(ip), port=int(port))
        notification = Label(main_tikinter, text="Your PC turning on!", fg="gray22", font="Helvetica 10")
        notification.place(rely=0.76, relx=0.18)
        mixer.init()
        mixer.music.load('./data/OK.wav')
        mixer.music.play()
        time.sleep(0.3)
    except:
        notification = Label(main_tikinter, text="Unsuccessful \ncheck to setting!", fg="gray22", font="Helvetica 10")
        notification.place(rely=0.76, relx=0.21)

turning_on_button=Button(main_tikinter)
setting_button=Button(main_tikinter)
main_menu = Button(main_tikinter)

def Main_menu():
    global main_menu

    info.place_forget()
    label_mac_adress.place_forget()
    label_ip.place_forget()
    label_port.place_forget()
    buton_save.place_forget()
    main_menu.place_forget()
    main_menu.place_forget()
    mac_adress.place_forget()
    ip_adress.place_forget()
    port_number.place_forget()
    buton_save.place_forget()
    turning_on_button.place(rely=0.25, relx=0.28)
    setting_button.place(rely=0.55, relx=0.28)
main_menu.destroy()
def clear_text(event):
    event.widget.delete(0, "end")
def save_fonc():
    global mac
    global ip
    global port

    mac=mac_adress.get()
    ip=ip_adress.get()
    port= port_number.get()
    data_save_control["Save_Data"] = {
        "mac": mac,
        "ip": ip,
        "port": port}
    def My_data_Save():
        with open('./data/data_save_control_w.pkl', 'wb') as f:
            pickle.dump(data_save_control, f)

    My_data_Save()

def Setting():
    global notification
    global setting_button
    notification.place_forget()
    setting_button.place_forget()
    turning_on_button.place_forget()
    main_menu.place(rely=0.02, relx=0.03)
    info.place(rely=0.02, relx=0.65)
    label_mac_adress.place(rely=0.175, relx=0.02)
    mac_adress.place(rely=0.26, relx=0.03)
    label_ip.place(rely=0.37, relx=0.02)
    ip_adress.place(rely=0.46, relx=0.03)
    label_port.place(rely=0.565, relx=0.02)
    port_number.place(rely=0.65, relx=0.03)
    buton_save.place(rely=0.76, relx=0.50)
My_data_Load()

took_mac = data_save_control['Save_Data']['mac']
took_ip = data_save_control['Save_Data']['ip']
took_port = data_save_control['Save_Data']['port']

label_mac_adress = Label(main_tikinter, text="Mac Adress", fg="gray22", font="Helvetica 9")
mac_adress=Entry(main_tikinter,width=15)

label_ip= Label(main_tikinter, text="Ip Adress", fg="gray22", font="Helvetica 9")
ip_adress=Entry(main_tikinter,width=15)

label_port= Label(main_tikinter, text="Port numbers", fg="gray22", font="Helvetica 9")
port_number=Entry(main_tikinter,width=15)

if len(took_mac) == 0:
    mac_adress.insert(0, "ff.ff.ff.ff.ff.ff")
    mac_adress.bind("<FocusIn>", clear_text)
else:
    mac_adress.insert(0, took_mac)
if len(took_ip) == 0:
    ip_adress.insert(0, "00-00-00-00-00-00")
    ip_adress.bind("<FocusIn>", clear_text)
else:
    ip_adress.insert(0, took_ip)
if len(took_port) == 0:
    port_number.insert(0, "Usually 9")
    port_number.bind("<FocusIn>", clear_text)
else:
    port_number.insert(0, took_port)

buton_save=Button(main_tikinter,text="Save",width=6,fg="gray22",borderwidth=3, relief="ridge",font="Helvetica 11",highlightbackground="#ABCBE3",command=save_fonc)

turning_on_button=Button(main_tikinter, text="Turn On",width=7,height=4,borderwidth=3, relief="ridge",fg="gray22",font="Helvetica 11",highlightbackground="#ABCBE3", compound=TOP,command=WOL)#bg"arkaplan",width=7,height=5
turning_on_button.place(rely=0.25, relx=0.28)

setting_button=Button(main_tikinter, text="Setting",width=7,height=2,borderwidth=3, relief="ridge",fg="gray22",font="Helvetica 11",highlightbackground="#ABCBE3", compound=TOP,command=Setting)#bg"arkaplan",width=7,height=5
setting_button.place(rely=0.55, relx=0.28)

main_menu=Button(main_tikinter, text="Main Menu",width=9,height=1,fg="gray22",borderwidth=3, relief="ridge",font="Helvetica 11",highlightbackground="#ABCBE3",command=Main_menu)#bg"arkaplan",width=7,height=5
info=Button(main_tikinter, text="info",width=3,height=1,fg="gray22",borderwidth=3, relief="ridge",font="Helvetica 11",command=inf)

mac=mac_adress.get()
ip=ip_adress.get()
port= port_number.get()
main_tikinter.mainloop()