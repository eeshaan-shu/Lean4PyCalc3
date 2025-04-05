import subprocess
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_lean(mode):
    result = subprocess.run(["./build/bin/calc_backend", mode], capture_output=True, text=True)
    return result.stdout.strip()

def display_latex(canvas_frame, latex_str):
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    fig = plt.figure(figsize=(6, 1))
    fig.text(0.5, 0.5, f"${latex_str}$", fontsize=18, ha='center', va='center')
    fig.patch.set_facecolor('white')

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def on_calc(mode):
    output = run_lean(mode)
    display_latex(canvas_frame, output)

root = tk.Tk()
root.title("Symbolic Calculator (Lean 4 + Python)")
root.geometry("700x300")

frame = ttk.Frame(root)
frame.pack(pady=20)

ttk.Label(frame, text="Choose Operation:", font=("Arial", 14)).pack()

btns = ttk.Frame(frame)
btns.pack()

ttk.Button(btns, text="Partial Derivative ∂f/∂x", command=lambda: on_calc("pd")).pack(side=tk.LEFT, padx=10)
ttk.Button(btns, text="Indefinite Integral ∫f dx", command=lambda: on_calc("int")).pack(side=tk.LEFT, padx=10)
ttk.Button(btns, text="Double Integral ∬f dx dy", command=lambda: on_calc("dint")).pack(side=tk.LEFT, padx=10)

canvas_frame = ttk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()
