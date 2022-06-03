from multiprocessing.sharedctypes import Value
import pandas as pd
import plotly.figure_factory as pff
import random as r
import statistics as st
df = pd.read_csv('data.csv')
temp = df['temp'].tolist()

fd =[]
def sampling():
    data = []
    for i in range(0,100):
        rp = r.randint(0,len(temp)-1)
        v = temp[rp]
        data.append(v)
    mean = st.mean(data)
    fd.append(mean)

for i in range(0,1000):
    sampling()
graph = pff.create_distplot([fd],['Gpa'], show_hist = False)
graph.show()


