import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv("spotify_tracks.csv")
st.header("Spotify Tracks Analysis")
st.write("Exploring the relationships between audio features and popularity in Spotify tracks.")
if st.checkbox("Show popularity histogram"):
    st.write("Distribution of popularity scores across all tracks.")
    hist_fig = px.histogram(
        data,
        x="popularity",
        nbins=100,
        log_y=True,
        color_discrete_sequence=['#1DB954'],
        title="Hits are exponentially rare",
        template="plotly_dark",
    )
    st.plotly_chart(hist_fig, width='stretch')
    if st.checkbox("Show scatter plot (mood quadrant)"):
        st.write("How energy and mood relate, colored by loudness.")
        scatter_fig = px.scatter(
        data.sample(1000, random_state=30),
        x="energy",
        y="valence",
        labels={'energy': 'Intensity', 'valence': 'Mood', 'loudness': 'Loud(dB)'},
        color="loudness",
        hover_name="track_name",
        hover_data=["artists", "album_name"],
        opacity=0.4,
        title="<b>Energy × Mood</b><br><sub>1,000 sampled tracks · Spotify dataset</sub>",
        template="plotly_dark",
        color_continuous_scale="Viridis",
    )
        scatter_fig.update_xaxes(gridcolor="#222222")
        scatter_fig.update_yaxes(gridcolor="#222222")
        st.plotly_chart(scatter_fig, width='stretch')
