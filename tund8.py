from tkinter import *
from tkinter import messagebox
# aken=Tk()
# aken.title("tund8")
# aken.geometry("600x400")
# aken.configure(bg="Lightblue")
# aken.resizable(width=False,height=False)
# aken.iconbitmap("")
# #aken.attributes("-alpha0.9")
# pealkiri=Label(aken,text="Tere tulemast!\n Tund 8 Tkinter",bg=blue,fg=green,font=("Arial",20))

# nupp=Button(aken,text="kliki mind",bg="red",fg="white",font=("Arial",15),command=lambda: messagebox.showinfo("teema 8","Tere tulemast Tkinteri maailma!"))
# nupp.bind("<Button-3>",vajatud)

# sisestus=Entry(aken,bg="white",font=("Arial",15), fg="black")
# sisestus.insert(0,"kirjuta siia tekst")
# sisestus.bind("<FocusIn>",tuhista)#"<FocusOut>"
# sisestus.bind("<Return>",text_to_label)

# pilt=PhotoImage(file="coconut.png").subsample(2, 2)
# pilt_label=Label(aken,image=pilt)

# pealkiri.pack(pady=20)
# nupp.pack(pady=20,side=LEFT)
# sisestus.pack(pady=20,side=LEFT)
# pilt_label.pack(pady=20)
import tkinter as tk
from tkinter import filedialog
import smtplib
from email.message import EmailMessage
import os

def lisa_manus(entry_widget):
    failitee = filedialog.askopenfilename()
    if failitee:
        entry_widget.delete(0, 'end')
        entry_widget.insert(0, failitee)
def saada_kiri():
    saaja = email_entry.get()
    teema = teema_entry.get()
    manus = manus_entry.get()
    sisu = kiri_text.get("1.0", "end")
    msg = EmailMessage()
    msg['Subject'] = teema
    msg['From'] = "deniss.melnikov@gmail.com"
    msg['To'] = saaja
    msg.set_content(sisu)

    if manus and os.path.isfile(manus):
        with open(manus, 'rb') as f:
            failinimi = os.path.basename(manus)
            msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=failinimi)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("deniss.melnikov@gmail.com", "Neegrit2220")
            smtp.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print("Viga saatmisel:", e)
aken = tk.Tk()
aken.title("E-kirja saatmine")
aken.geometry("500x350")

tk.Label(aken, text="EMAIL:", bg="darkgreen", fg="white", width=10).grid(row=0, column=0, sticky='nsew')
tk.Label(aken, text="TEEMA:", bg="darkgreen", fg="white", width=10).grid(row=1, column=0, sticky='nsew')
tk.Label(aken, text="LISA:", bg="darkgreen", fg="white", width=10).grid(row=2, column=0, sticky='nsew')
tk.Label(aken, text="KIRI:", bg="darkgreen", fg="white", width=10).grid(row=3, column=0, sticky='nsew')

email_entry = tk.Entry(aken, width=50)
teema_entry = tk.Entry(aken, width=50)
manus_entry = tk.Entry(aken, width=50)
kiri_text = tk.Text(aken, width=40, height=10)

email_entry.grid(row=0, column=1, padx=5, pady=5)
teema_entry.grid(row=1, column=1, padx=5, pady=5)
manus_entry.grid(row=2, column=1, padx=5, pady=5)
kiri_text.grid(row=3, column=1, padx=5, pady=5)

lisa_btn = tk.Button(aken, text="LISA PILT", bg="darkgreen", fg="white", command=lambda: lisa_manus(manus_entry))
saada_btn = tk.Button(aken, text="SAADA", bg="darkgreen", fg="white", command=saada_kiri)

lisa_btn.grid(row=4, column=0, pady=10)
saada_btn.grid(row=4, column=1, sticky='e', padx=10)

aken.mainloop()
