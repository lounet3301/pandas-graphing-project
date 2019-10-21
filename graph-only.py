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