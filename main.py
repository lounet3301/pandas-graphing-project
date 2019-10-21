#Please Run this Command Before running the program
#pip install -r requirements.txt - windows
#pip3 install -r requirements.txt - unix based systems
import pandas as pd
from matplotlib import pyplot as plt
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
def normal_plot():
    plt.plot(kick,a)
    plt.show()
def scatter_plot():
    plt.scatter(kick,a)
    plt.show()
scatter_plot()