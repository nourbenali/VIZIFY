import panel as pn
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, ColumnDataSource
def plot_top_artists_genre(data, selected_genre):
        # Filter the data for the selected track genre
        selected_data = data[data['track_genre'] == selected_genre]

        # Group the filtered data by the artists and calculate the count of the specified feature for each artist
        artists_data = selected_data.groupby('artists')['track_genre'].count().reset_index()

        # Sort the data by the count of the specified feature in descending order (optional)
        artists_data = artists_data.sort_values(by='track_genre', ascending=False)

        # Select the top 10 artists
        top_10_artists = artists_data.head(10)

        # Create a Bokeh figure
        p = figure(
            width=600,
            height=600,
            #title=f'Top 10 Artists by Track Genre in {selected_genre}',
            x_range=list(top_10_artists['artists']),
            toolbar_location=None,
            tools='hover',
        )

        # Set all bars to green
        color = "#5C4F7E"

        # Plot the count of the specified feature by artist without legend
        p.vbar(x='artists', top='track_genre', source=top_10_artists, width=0.8, color=color)

        # Rotate x-axis labels for better readability
        p.xaxis.major_label_orientation = "vertical"

        # Add labels
        p.xaxis.axis_label = 'Artist'
        p.yaxis.axis_label = 'Count Track Genre'

        # Add hover tool with value formatting
        hover = p.select(dict(type=HoverTool))
        hover.tooltips = [('Count Track Genre', '@track_genre{0.2f}')]

    
        # Create a Panel app to display the Bokeh plot
        app = pn.Column(
            f"# Top 10 Artists By Track Genre in {selected_genre}",
            p,
        )

        return app
