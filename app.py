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
    st.caption("Distribution of popularity scores across all tracks. The logarithmic scale on the y-axis highlights the rarity of highly popular tracks.")

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
    st.caption("This scatter plot shows the relationship between the emotional intensity and mood (0=Sad, 1=Happy) of tracks, colored by loudness. It reveals clusters of tracks with similar audio characteristics and highlights how loudness varies across different energy and mood levels.")

if st.checkbox("Show audio features correlation matrix"):
    st.write("How four key audio features relate to one another.")
    matrix_fig = px.scatter_matrix(
        data.sample(1000, random_state=42),
        dimensions=['danceability', 'loudness', 'valence', 'energy'],
        labels={'danceability': 'Danceability',
                'loudness': 'Loud(dB)',
                'valence': 'Mood',
                'energy': 'Intensity'},
        opacity=0.4,
        template="plotly_dark",
        color_discrete_sequence=['#1DB954'],
    )
    matrix_fig.update_xaxes(gridcolor="#222222")
    matrix_fig.update_yaxes(gridcolor="#222222")
    matrix_fig.update_layout(height=700)
    st.plotly_chart(matrix_fig, width='stretch')
    st.markdown("""
Loudness and intensity move together  they cluster tightly. Mood (valence) floats 
free of every other feature, showing that happy and sad songs exist at every level 
of energy or loudness.

Danceability is mostly independent but has a slight positive correlation with intensity, 
indicating that more energetic tracks tend to be more danceable.

Even though loudness correlates with all other features, when you upload a track to 
Spotify, the loudness is automatically adjusted to fit a standard level, so it doesn't 
affect the track's popularity or how listeners perceive its energy or mood.
""")