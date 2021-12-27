import csv
import pandas as pd
import plotly.graph_objects as pg
import plotly_express as px

data = pd.read_csv("data.csv")
studentID = data.loc[data["student_id"]=="TRL_abc"]

print(studentID.groupby("level")["attempt"].mean())

fig = pg.Figure(pg.Bar(
    x=studentID.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h",
))
fig.show()