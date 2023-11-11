import pandas as pd
import panel as pn
import numpy as np
import bokeh.plotting as bp
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, FactorRange
from bokeh.plotting import figure
from ML.metrics_output import metrics
import joblib
from ML.dataset import X
from ML.feature_importance import plot_feature_importance
from ML.cards import create_recall_card,create_f1_score_card,create_precision_card,create_accuracy_card

loaded_model = joblib.load('ML/Model/catboost.pkl')
importances = loaded_model.get_feature_importance(type='PredictionValuesChange')
feature_importances = pd.Series(importances, index=X.columns).sort_values()
feature_importances = feature_importances.sort_values(ascending=True)

plot=plot_feature_importance(feature_importances)


column_select = pn.widgets.Select(name='Select A Music Genre:', options=list(metrics.keys()),width=180)


@pn.depends(column_select.param.value)
def updatef1score(column):
    f1_score = metrics[column]['f1-score']
    return create_f1_score_card(f1_score)

f1_score_card=updatef1score

@pn.depends(column_select.param.value)
def updateprecision(column):
    precision = metrics[column]['precision']
    return create_precision_card(precision)

precision_card=updateprecision

@pn.depends(column_select.param.value)
def updaterecall(column):
    recall = metrics[column]['recall']
    return create_recall_card(recall)

recall_card=updaterecall

accuracy_card=create_accuracy_card(0.72)

recall_card=updaterecall

sidebar = pn.Column(
    column_select,
    background='#72EB8E',  # Set the background color
    width=200,  # Adjust the width of the sidebar as needed
    margin=(20, 20, 20, 20)  # Set the margin for padding
    )

spacing = pn.Spacer(width=70)
layout = pn.Column(
    pn.Row(sidebar,pn.Spacer(width=80),accuracy_card,spacing,f1_score_card,spacing,precision_card,spacing,recall_card),
    pn.Spacer(height=50),
    pn.Row(plot)

)

layout.servable()