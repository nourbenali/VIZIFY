import pandas as pd
from plots.heatmap import create_heatmap
from plots.topgenres import plot_top_genres
from plots.topartists import plot_top_artists_features
from plots.tabulator import create_tabulator
from plots.topartistsgenre import plot_top_artists_genre
from plots.scatterplot import create_scatter_plot
import panel as pn
def create_dashboard_1_app():
    df = pd.read_csv("data/dataset.csv")
    #Colum Selector : Scatter Plot
    x_column = pn.widgets.Select(name="Scatter Plot X-Axis", options=list(df.columns),width=180,value='danceability')
    y_column = pn.widgets.Select(name="Scatter Plot Y-Axis", options=list(df.columns),width=180,value='popularity')

    @pn.depends(x_column.param.value, y_column.param.value)
    def update_scatter_plot(x_col, y_col):
            return create_scatter_plot(df,x_col,y_col)
    
    
    #Column Selector : Top 10

    column_select_top10 = pn.widgets.Select(name='Select a feature:', options=['popularity', 'danceability', 'energy', 'acousticness','liveness','valence','speechiness','instrumentalness'],width=180)

    @pn.depends(column_select_top10.param.value)
    def update_artists_features(column):
        return plot_top_artists_features(df,column)
    
    @pn.depends(column_select_top10.param.value)
    def update_genres(column):
         return plot_top_genres(df,column)
    
    #Column Select Top 10 Artists By Genre
    
    column_select_genre=pn.widgets.Select(name='Select a feature:', options=list(df['track_genre'].unique()),width=180)
    @pn.depends(column_select_genre.param.value)
    def update_artists_genre(column):
         return plot_top_artists_genre(df,column)
    
    #Creating the figures
    heatmap=create_heatmap(df)
    top_10_artists=update_artists_features
    top_10_genres=update_genres
    tabulator=create_tabulator(df)
    scatter_plot=update_scatter_plot
    top_10_artists_genre=update_artists_genre


    #Dashboard
    sidebar = pn.Column(
        column_select_top10,
        background='#72EB8E',  # Set the background color
        width=200,  # Adjust the width of the sidebar as needed
        margin=(20, 20, 20, 20)  # Set the margin for padding
    )
    sidebar2=pn.Column(
        x_column,
        y_column,
        column_select_genre,
        background='#72EB8E',  # Set the background color
        width=200,  # Adjust the width of the sidebar as needed
        margin=(20, 20, 20, 20)  # Set the margin for padding 
    )

    # Organize the layout using Panel's layout capabilities
    layout = pn.Column(
        pn.Spacer(height=50),
        pn.Spacer(width=300),
        pn.Row(tabulator,heatmap),
        pn.Spacer(height=50),
        pn.Row(sidebar,top_10_artists,top_10_genres),
        pn.Spacer(height=50),
        pn.Row(sidebar2,scatter_plot,top_10_artists_genre),
        pn.Spacer(height=50)
    )

    # Serve the app
    return layout
create_dashboard_1_app().servable()



