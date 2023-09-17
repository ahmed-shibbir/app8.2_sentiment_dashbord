""" This app creates a dashboard with positivity and negativity
scores.
"""

import streamlit as st
import nltk
import re
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

# nltk.download('vader_lexicon')

# from platform import python_version
# python_version()


# Extract file paths using glob library
filepaths = glob.glob("diary/*.txt")
# print(filepaths)

#  Making a list of dates
# dates = []
#
# for path in filepaths:
#     date = path[-14:-4]
#     # print(date)
#     dates.append(date)

dates = [path.strip(".txt").strip("diary/") for path in filepaths]

print(dates)


# Making lists of positivity and negativity scores by a function

def get_scores(filepaths):
    positivity = []
    negativity = []
    for path in filepaths:
        with open(path, "r") as file:
            content = file.read()
            # print(content)
            analyzer = SentimentIntensityAnalyzer()
            scores = analyzer.polarity_scores(content)
            # print(scores)
            positivity.append(scores["pos"])
            # print(positivity)

            negativity.append(scores["neg"])
            # print(negativity)
    return positivity, negativity


# Calling the function to get positivity and negativity lists
positivity, negativity = get_scores(filepaths=filepaths)
# print(positivity)
# print(negativity)

# Adding title to the streamlit dashboard
st.title("Diary Tone")

# st.text("Positivity")

# Display bold and bigger text
# st.markdown("<span style='font-size:24px'><b>Positivity</b></span>", unsafe_allow_html=True)
st.subheader("Positivity")

# Creating a figure for positivity line chart
figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity Scores"})

# Displaying the figure in streamlit app.
st.plotly_chart(figure)

# st.text("Negativity")
# Display bold and bigger text
# st.markdown("<span style='font-size:24px'><b>Negativity</b></span>", unsafe_allow_html=True)
st.subheader("Negativity")
# Creating a figure for negativity line chart
figure2 = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity Scores"})

# Displaying the figure in streamlit app.
st.plotly_chart(figure2)
