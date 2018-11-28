import plotly.offline as offline
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt
import os

#import matplotlib.pyplot as plt
#inputDataionary = plt.figure()
#inputData= { "A":1 , "B":2}
#data = [go.Bar(x=[inputData.keys()],y=[20, 14, 23])]

def doCommitGraph(inputData) :
        #a = t + (v)
    data = [go.Bar(
            x=tuple(inputData.keys()),
            y=tuple(inputData.values()),marker=dict(
        color='#4F7CAC'
        )
    )]

    layout = go.Layout(title='Number of Commits per Contributor')

    fig = go.Figure(data=data, layout=layout)
    offline.plot(fig)
    os.rename('temp-plot.html', 'commitGraph.html')


def doCodeGraph(inputData) :
        #a = t + (v)
    data = [go.Line(
            x=tuple(inputData.keys()),
            y=tuple(inputData.values()),marker=dict(
        color='#4F7CAC'
        )
    )]

    layout = go.Layout(title='Number of Commits per Contributor')

    fig = go.Figure(data=data, layout=layout)
    offline.plot(fig)
    os.rename('temp-plot.html', 'CodeBase.html')
