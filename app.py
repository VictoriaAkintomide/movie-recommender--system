import streamlit as st  #imports the streamlit library and framework
from PIL import Image  #used to display images on streamlit
import movie_recommender_system  #movie_recommender_system.py ran my rec system

#title
st.title("Movie Recommender System")

img = Image.open("figures/movies.jpg")
st.image(img, caption="Movies")

#header
st.header("TOP 10 Similar Movies Recommender System")
st.subheader("The Movie Release date should not be later than August 2018")
#ask user for input
movie_name = st.text_input("Enter your Movie")
test = st.button("Search for similar movies")


st.dataframe(movie_recommender_system.get_movie_recommendation(movie_name))
st.success("Finished") #shows the green Finished banner