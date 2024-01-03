
# Spotify Data Visualization Project with Panel : VIZIFY

## Overview

This project aims at analyzing Spotify's data and predicting the genre of the music title. The webapp uses bokeh and panel for data visuallization, and fastapi for web embedding.

## Installation

To run VIZIFY, follow these steps:

1. Open the project in an IDE then Create and activate a conda virtual environment:
   ```bash
   conda create -n venv python=3.6 -y 
   conda activate venv
   ```

2. Install the required packages using the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application using [uvicorn](https://www.uvicorn.org/):
   ```bash
   uvicorn main:app --reload
   ```

4. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to access the home page.

## Dashboards

Vizify offers the following dashboards:

1. **Home Page**: Navigate to the home page to get an overview of the application.

2. **Dashboard 1 - Exploratory Dashboard**: Explore the Spotify tracks dataset with various filters and visualizations. Uncover patterns, trends, and details of top songs, artists, and genres.

    - Access: [http://127.0.0.1:8000/dash1](http://127.0.0.1:8000/dash1)
      

3. **Dashboard 2 - Genre Prediction Dashboard**: Predict and understand the genre of a track using machine learning models. Interact with predictions and discover the magic behind the music.

    - Access: [http://127.0.0.1:8000/dash2](http://127.0.0.1:8000/dash2)


## Meet the Team

Vizify is brought to you by our enthusiastic duo:

- [**Eya Sahli**](https://www.linkedin.com/in/eya-sahli-5ab205174/)

- [**Nour ElHouda Ben Ali**](https://www.linkedin.com/in/nour-elhouda-ben-ali-b01982195/)

## Contact

For inquiries or support, feel free to reach out to us:

- Eya Sahli: [eya.sahli@dauphine.eu](mailto:eya.sahli@dauphine.eu)
- Nour ElHouda Ben Ali : [nour-el-houda.ben-ali@dauphine.eu](mailto:nour-el-houda.ben-ali@dauphine.eu)

## Additional Information

- Dataset Source: [https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
