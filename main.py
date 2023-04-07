import streamlit as st
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from pathlib import Path

st.header('Diary Tone')
st.subheader('Positivity')

analyzer = SentimentIntensityAnalyzer()
y_pos = []
y_neg = []
dates = []
for file_path in glob.glob('Diary/*'):
    print(file_path)
    dates.append(Path(file_path).stem)

    with open(file_path, 'r') as f:
        content = f.read()
        score = analyzer.polarity_scores(content)
        y_pos.append(score['pos'])
        y_neg.append(score['neg'])

x = sorted(dates)
figure = px.line(x=x, y=y_pos, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure)

figure = px.line(x=x, y=y_neg, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure)
