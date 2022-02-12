import plotly.figure_factory as ff
import pandas as pd
import csv
import scipy

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()],["Name"],show_hist=False)
fig.show()
