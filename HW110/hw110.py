import pandas as pd 
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects  as go

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()
population_mean=statistics.mean(data)
stdev=statistics.stdev(data)
print(stdev)

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    figure=ff.create_distplot([df],
    ["temp"],
    show_hist=False)
    figure.add_trace(go.Scatter(
        x=[mean,mean],
        y=[0,1],
        mode="lines",
        name="MEAN"))
    figure.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_figure(mean_list)
    mean=statistics.mean(mean_list)
    print("Mean of sampling distribution is"+ mean)
setup()

def stdev():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_figure(mean_list)
    stdev=statistics.stdev(mean_list)
    print("stdev of sampling distribution is"+ stdev)
stdev()


