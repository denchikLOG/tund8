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
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def solve_quadratic():
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        c=float(entry_c.get())
        if a==0:
            messagebox.showerror("Ошибка","Коэффициент 'a' не может быть равен 0!")
            return
        discriminant=b**2-4*a*c
        if discriminant>0:
            x1=(-b+np.sqrt(discriminant))/(2*a)
            x2=(-b-np.sqrt(discriminant))/(2*a)
            solution_label.config(text=f"Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif discriminant==0:
            x=-b/(2*a)
            solution_label.config(text=f"Единственный корень: x = {x:.2f}")
        else:
            solution_label.config(text="Нет действительных корней.")
    except ValueError:
        messagebox.showerror("Ошибка ввода","Введите корректные значения для коэффициентов.")
def plot_graph():
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        c=float(entry_c.get())
        if a==0:
            messagebox.showerror("Ошибка","Коэффициент 'a' не может быть равен 0!")
            return
        x=np.linspace(-10,10,400)
        y=a*x**2+b*x+c
        fig,ax=plt.subplots()
        ax.plot(x,y,label=f'{a}x² + {b}x + {c}')
        ax.axhline(0,color='black',linewidth=1)
        ax.axvline(0,color='black',linewidth=1)
        ax.legend()
        canvas=FigureCanvasTkAgg(fig,master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except ValueError:
        messagebox.showerror("Ошибка ввода","Введите корректные значения для коэффициентов.")
def check_empty_fields():
    if not entry_a.get() or not entry_b.get() or not entry_c.get():
        if not entry_a.get():
            entry_a.config(bg="red")
        else:
            entry_a.config(bg="white")
        if not entry_b.get():
            entry_b.config(bg="red")
        else:
            entry_b.config(bg="white")
        if not entry_c.get():
            entry_c.config(bg="red")
        else:
            entry_c.config(bg="white")
        return False
    return True
window=tk.Tk()
window.title("Решение квадратного уравнения")
label_a=tk.Label(window,text="a:")
label_a.pack(padx=10,pady=5)
entry_a=tk.Entry(window)
entry_a.pack(padx=10,pady=5)
label_b=tk.Label(window,text="b:")
label_b.pack(padx=10,pady=5)
entry_b=tk.Entry(window)
entry_b.pack(padx=10,pady=5)
label_c=tk.Label(window,text="c:")
label_c.pack(padx=10,pady=5)
entry_c=tk.Entry(window)
entry_c.pack(padx=10,pady=5)
solve_button=tk.Button(window,text="Решить",command=lambda:[check_empty_fields(),solve_quadratic()])
solve_button.pack(padx=10,pady=10)
solution_label=tk.Label(window,text="")
solution_label.pack(padx=10,pady=5)
plot_button=tk.Button(window,text="График",command=plot_graph)
plot_button.pack(padx=10,pady=10)
window.mainloop()