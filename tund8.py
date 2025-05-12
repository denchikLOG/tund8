import tkinter as tk
from tkinter import messagebox
import funktsioonid as f

kontaktid = f.loe_kontaktid_failist()
def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        f.lisa_kontakt(kontaktid, nimi, telefon, email)
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Edu", "Kontakt lisatud.")
        nimi_entry.delete(0, 'end')
        telefon_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad", "Täida kõik väljad.")

def otsi_kontakti_gui():
    nimi = nimi_entry.get()
    tulemused = f.otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt = tulemused[0]
        otsingu_viide.set(kontakt["nimi"])

        nimi_entry.delete(0, 'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0, 'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0, 'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0", "end")
        tekstikast.insert("end", f"Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakti ei leitud.")

def kustuta_kontakt_gui():
    nimi = nimi_entry.get()
    if f.kustuta_kontakt(kontaktid, nimi):
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakti ei leitud.")

def sorteeri_gui():
    kontaktid_sorted = f.sorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")

def muuda_kontakt_gui():
    vana_nimi = otsingu_viide.get()
    uus_nimi = nimi_entry.get()
    uus_telefon = telefon_entry.get()
    uus_email = email_entry.get()

    if vana_nimi and uus_nimi and uus_telefon and uus_email:
        õnnestus = f.muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            f.salvesta_kontaktid_faili(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks.")
    else:
        messagebox.showwarning("Puuduvad andmed", "Palun täida kõik väljad.")


aken = tk.Tk()
aken.title("Telefoniraamat")
# Sisestusväljad
otsingu_viide = tk.StringVar()
otsingu_viide.set("")
tk.Label(aken, text="Nimi:").pack()
nimi_entry = tk.Entry(aken)
nimi_entry.pack()

tk.Label(aken, text="Telefon:").pack()
telefon_entry = tk.Entry(aken)
telefon_entry.pack()

tk.Label(aken, text="Email:").pack()
email_entry = tk.Entry(aken)
email_entry.pack()

nuppude_rida = tk.Frame(aken)
nuppude_rida.pack(pady=5)

tk.Button(nuppude_rida, text="Lisa kontakt", command=lisa_kontakt).pack(side="left",pady=5)
tk.Button(nuppude_rida, text="Kuva kontaktid", command=kuva_kontaktid).pack(side="left")
tk.Button(nuppude_rida, text="Otsi kontakti", command=otsi_kontakti_gui).pack(side="left")
tk.Button(nuppude_rida, text="Kustuta kontakt", command=kustuta_kontakt_gui).pack(side="left")
tk.Button(nuppude_rida, text="Sorteeri (nime järgi)", command=sorteeri_gui).pack(side="left")
tk.Button(nuppude_rida, text="Muuda kontakt", command=muuda_kontakt_gui).pack(side="left")
tk.Button(nuppude_rida, text="Lisa fail", command=lisa_fail_gui).pack(side="left")
tekstikast = tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)

aken.mainloop()