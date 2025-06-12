import streamlit as st
from utils.recipe_utils import load_recipes

st.title("📂 Filter Recipes by Category")
recipes = load_recipes()

categories = sorted(set(r.get("category", "Uncategorized") for r in recipes))
choice = st.selectbox("Select category", categories)

for r in recipes:
    if r.get("category", "Uncategorized") == choice:
        st.subheader(r["name"])
        st.markdown("**Ingredients:** " + ", ".join(r["ingredients"]))
        st.markdown("**Instructions:**")
        st.markdown(r["instructions"])
        st.divider()
