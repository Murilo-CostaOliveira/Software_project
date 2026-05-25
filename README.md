# App_Project

RENDER URL:https://spotify-charts-nso4.onrender.com

## PT

Este projeto é um dashboard web interativo construído com Streamlit e Plotly Express para explorar um conjunto de dados com características de áudio de aproximadamente 114.000 músicas do Spotify.
Cada música no dataset possui métricas extraídas pelo algoritmo de análise de áudio do Spotify, entre elas: intensidade emocional (energy), volume médio em decibéis (loudness), positividade musical (valence — de triste a feliz), dançabilidade, tempo (BPM), acústica e popularidade.

### Funcionalidades do aplicativo

- **Histograma de popularidade (escala logarítmica):** mostra a distribuição dos scores de popularidade entre todas as faixas, evidenciando a raridade de uma música se tornar viral.
- **Gráfico de dispersão "mood quadrant":** mapa de intensidade × humor das músicas, colorido por volume. Revela como o universo musical se distribui entre os polos calmo/intenso e triste/feliz.
- **Matriz de correlação de características de áudio:** matriz de gráficos de dispersão comparando quatro features-chave (dançabilidade, volume, humor e intensidade), revelando padrões como a forte correlação entre volume e intensidade, e a independência do humor em relação às outras métricas.

Cada gráfico é acompanhado de uma análise interpretativa abaixo, comentando os principais padrões encontrados.

### Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/Murilo-CostaOliveira/Software_project.git
cd Software_project

# Crie e ative o ambiente virtual
python -m venv spotify_env
spotify_env\Scripts\activate   # Windows
# source spotify_env/bin/activate   # macOS/Linux

# Instale as dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
```

O app abrirá automaticamente em `http://localhost:8501`.


## ENG

This project is an interactive web dashboard built with **Streamlit** and **Plotly Express** to explore a dataset of audio features from approximately 114,000 Spotify tracks spanning 114 different genres.

Each track in the dataset comes with metrics extracted by Spotify's audio analysis algorithm, including: emotional intensity (energy), average loudness in decibels, musical positivity (valence — from sad to happy), danceability, tempo (BPM), acousticness, and popularity.

### App features

- **Popularity histogram (log scale):** shows the distribution of popularity scores across all tracks, highlighting how rare it is for a song to go viral.
- **"Mood quadrant" scatter plot:** maps energy × valence, colored by loudness. Reveals how the musical universe spreads across the calm/intense and sad/happy poles.
- **Audio features correlation matrix:** scatter matrix comparing four key features (danceability, loudness, valence, energy), revealing patterns such as the strong correlation between loudness and intensity, and the independence of mood from the other metrics.

Each chart is accompanied by an interpretive analysis discussing the main patterns found in the data.

### How to run locally

```bash
# Clone the repository
git clone https://github.com/Murilo-CostaOliveira/Software_project.git
cd Software_project

# Create and activate the virtual environment
python -m venv spotify_env
spotify_env\Scripts\activate   # Windows
# source spotify_env/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

## Built with

- **Python 3.14**
- **Streamlit** — web framework
- **Pandas** — data manipulation
- **Plotly Express** — interactive visualizations

## Data Source

Spotify Tracks Dataset, originally compiled by [maharshipandya](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset). ~114,000 tracks across 114 genres with full audio features.