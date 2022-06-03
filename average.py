from multiprocessing.sharedctypes import Value
from numpy import average
import pandas as pd
import plotly.figure_factory as pff
import random as r
import statistics as st
df = pd.read_csv('newdata.csv')
avg = df['average'].tolist()

fd = []
def sampling():
    data = []
    for i in range(0,100):
        rp = r.randint(0,len(avg)-1)
        v = avg[rp]
        data.append(v)
    mean = st.mean(data)
    fd.append(mean)

for i in range(0,1000):
    sampling()
    
graph = pff.create_distplot([fd],['Gpa'], show_hist = False)
graph.show()