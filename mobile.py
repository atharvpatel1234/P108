import plotly.figure_factory as ff
import pandas as pd 
import csv

df=pd.read_csv("Data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Average"],)
fig.show()
 
