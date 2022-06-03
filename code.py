import pandas as pd
import plotly.figure_factory as pff
df = pd.read_csv('newdata.csv')
mean = df['average'].tolist()
graph = pff.create_distplot([mean],['Gpa'], show_hist = False)
graph.show()