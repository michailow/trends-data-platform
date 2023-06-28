import numpy as np
import pandas as pd



import plotly.express as px
def createGraphics():
    df = pd.read_csv("../../data/stocks.csv")

    fig = px.line(df, x='Date', 
                  y='Close', 
                  color='Ticker', 
                  title="Stock Market Performance for the Last 3 Months")
    fig.write_html("yourfile.html") 