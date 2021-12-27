import csv
import pandas as pd
import plotly.graph_objects as pg

data = pd.read_csv("data.csv")

print(data.groupby("level")["attempt"].mean())

