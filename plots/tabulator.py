import panel as pn
def create_tabulator(data, height=600, width=600):
    # Drop the column you want to exclude
        data = data.drop(columns=['Unnamed: 0','track_id'])
    # Create the Tabulator widget with the modified DataFrame
        tabulator = pn.widgets.Tabulator(data, height=height, width=width, buttons={'Print': "<i class='fa fa-print'></i>"})
        # Create a Panel app to display the Bokeh plot
        app = pn.Column(
            f"# Spotify Dataset",
            tabulator,
            )
        return app