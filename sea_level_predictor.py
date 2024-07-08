from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('C:/Users/SHALINI SINGH/Desktop/VS Code_Program/Sea_Level_Predictor/epa-sea-level.csv')
def draw_plot():
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    res1=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1=np.arange(df['Year'].min(),2051,1)
    y1=res1.intercept+res1.slope*x1
    plt.plot(x1,y1,'green')
    plt.show()
    
    dfn=df[df['Year']>=2000]
    plt.scatter(dfn['Year'],dfn['CSIRO Adjusted Sea Level'])
    res2=linregress(dfn['Year'],dfn['CSIRO Adjusted Sea Level'])
    x2=np.arange(dfn['Year'].min(),2051,1)
    y2=res2.intercept+res2.slope*x2
    plt.plot(x2,y2,"yellow")
    plt.show()
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (Inches)")
    plt.title("Sea Level Predictor")
    plt.savefig("Sea-Level-predictor.png")
        

draw_plot()
