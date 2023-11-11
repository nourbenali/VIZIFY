import panel as pn
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, ColumnDataSource
#Scatter Plot
def create_scatter_plot(data,x_col,y_col):
    title = f"{x_col} vs. {y_col}"
    p = figure(width=500, height=500, title=title)
    # Add a circle renderer with a size, color, and alpha
    p.circle(data[x_col], data[y_col], size=5, color="#53A687", alpha=0.5)
    # Set the axis labels as legend labels
    p.xaxis.axis_label = x_col
    p.yaxis.axis_label = y_col
    app = pn.Column(
        f"# Spotify Scatter Plot",
        p,
        )
    return app