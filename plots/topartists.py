import panel as pn
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, ColumnDataSource
def plot_top_artists_features(data,feature):
            # Group the data by the artists and calculate the mean of the specified feature for each group
            artists_data = data.groupby('artists')[feature].mean().reset_index()

            # Sort the data by the mean of the specified feature in descending order (optional)
            artists_data = artists_data.sort_values(by=feature, ascending=False)

            # Select the top 10 artists
            top_10_artists = artists_data.head(10)

            # Create a Bokeh figure
            p = figure(
                width=600,
                height=600,
                #title=f'Top 10 Artists by Mean {feature.capitalize()}',
                x_range=list(top_10_artists['artists']),
                toolbar_location=None,
                tools='hover',
            )

            # Set all bars to green
            color = "#5C4F7E"

            # Plot the mean of the specified feature by artist without legend
            p.vbar(x='artists', top=feature, source=top_10_artists, width=0.8, color=color)

            # Rotate x-axis labels for better readability
            p.xaxis.major_label_orientation = "vertical"

            # Add labels
            p.xaxis.axis_label = 'Artists'
            p.yaxis.axis_label = f'Mean {feature.capitalize()}'

            # Add hover tool with value formatting
            hover = p.select(dict(type=HoverTool))
            hover.tooltips = [(f'Mean {feature.capitalize()}', f'@{feature}{{0.2f}}')]

            # Remove legend
            p.legend.visible = False

            # Create a Panel app to display the Bokeh plot
            app = pn.Column(
                f"# Top 10 Artists By {feature.capitalize()}",
                p,
            )

            # Show the Panel app
            return app