import streamlit as st
from utils.recipe_utils import load_recipes

st.title("🔍 Search Recipes")
recipes = load_recipes()

query = st.text_input("Search by name or ingredient")
if query:
    results = []
    for recipe in recipes:
        if query.lower() in recipe["name"].lower() or any(query.lower() in ing.lower() for ing in recipe["ingredients"]):
            results.append(recipe)
    
    if results:
        for r in results:
            st.subheader(r["name"])
            st.markdown("**Ingredients:**")
            st.markdown(", ".join(r["ingredients"]))
            st.markdown("**Instructions:**")
            st.markdown(r["instructions"])
            st.divider()
    else:
        st.warning("No matching recipes found.")
