import streamlit as st
import random
from PIL import Image
from utils.recipe_utils import load_recipes

st.set_page_config(page_title="Random Recipe Recommender", layout="centered")
st.title("🍲 Random Recipe Recommender")
st.markdown("Click the button to get a surprise recipe!")

image = Image.open("assets/food.jpg")
st.image(image, use_container_width=True)

recipes = load_recipes()

if st.button("Show me a recipe!"):
    recipe = random.choice(recipes)
    st.subheader(recipe["name"])
    st.markdown("**Ingredients:**")
    for item in recipe["ingredients"]:
        st.markdown(f"- {item}")
    st.markdown("**Instructions:**")
    st.write(recipe["instructions"])
