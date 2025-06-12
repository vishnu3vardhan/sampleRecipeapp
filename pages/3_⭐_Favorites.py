import streamlit as st
from utils.recipe_utils import load_recipes

st.title("⭐ Your Favorite Recipes")

if "favorites" not in st.session_state:
    st.session_state.favorites = []

recipes = load_recipes()

for r in recipes:
    if st.button(f"❤️ Add to favorites: {r['name']}"):
        if r not in st.session_state.favorites:
            st.session_state.favorites.append(r)

if st.session_state.favorites:
    st.header("Your Favorites")
    for r in st.session_state.favorites:
        st.subheader(r["name"])
        st.markdown("**Ingredients:** " + ", ".join(r["ingredients"]))
        st.markdown("**Instructions:**")
        st.markdown(r["instructions"])
        st.divider()
else:
    st.info("You haven’t added any favorites yet.")
