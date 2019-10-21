import tkinter as tk
from tkinter import *
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
root= Tk()
data = pd.read_csv("MOCK_DATA.csv")
df = pd.DataFrame(data)
kick = df[["kick"]]
a = df[["a"]]
b = df[["b"]]
c = df[["a"]]
d = df[["d"]]
e = df[["e"]]
f = df[["f"]]
g = df[["g"]]
def data_plot_A():
    top = Toplevel() 
    top.title('Python')
    figure3 = plt.Figure(figsize=(5,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(kick,a, color = 'g')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.legend() 
    top.mainloop() 
Kick_n_A = Button(root, text = 'Kick and A', bd = '5', command = data_plot_A)

Kick_n_A.pack()

root.mainloop()