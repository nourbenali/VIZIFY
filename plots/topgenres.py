import panel as pn
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColorBar, LinearColorMapper, HoverTool, ColumnDataSource
def plot_top_genres(data,feature):
        # Group the data by the track genres and calculate the mean of the specified feature for each group
        genre_data = data.groupby('track_genre')[feature].mean().reset_index()

        # Sort the data by the mean of the specified feature in descending order (optional)
        genre_data = genre_data.sort_values(by=feature, ascending=False)

        # Select the top 10 track genres
        top_10_genres = genre_data.head(10)

        # Create a Bokeh figure
        p = figure(
            width=600,
            height=600,
            #title=f'Top 10 Genres by Mean {feature.capitalize()}',
            y_range=list(top_10_genres['track_genre'][::-1]),  # Invert y-axis for higher values at the top
            toolbar_location=None,
            tools='hover',
        )

        # Create a ColumnDataSource
        source = ColumnDataSource(top_10_genres)
        
        #Set All Colors To Green
        color = "#5C4F7E"

        # Plot the mean of the specified feature by genre
        p.hbar(y='track_genre', right=feature, source=source, height=0.8, color=color, legend_field='track_genre')

        # Add labels
        p.xaxis.axis_label = f'Mean {feature.capitalize()}'
        p.yaxis.axis_label = 'Genre'

        # Add hover tool with value formatting
        hover = p.select(dict(type=HoverTool))
        hover.tooltips = [(f'Mean {feature.capitalize()}', f'@{feature}{{0.2f}}')]

     

        # Create a Panel app to display the Bokeh plot
        app = pn.Column(
            f"# Top 10 Genres By {feature.capitalize()}",
            p,
        )

        # Show the Panel app
        return app