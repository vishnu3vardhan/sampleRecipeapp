import streamlit as st
from utils.recipe_utils import load_recipes

st.title("⭐ Favorite Recipes")

recipes = load_recipes()
if "favorites" not in st.session_state:
    st.session_state["favorites"] = []

# Allow user to favorite/unfavorite
recipe_names = [r["name"] for r in recipes]
selected = st.selectbox("Select a recipe to add/remove from favorites", recipe_names)

if st.button("⭐ Add to Favorites"):
    if selected in st.session_state["favorites"]:
        st.session_state["favorites"].remove(selected)
        st.success(f"❌ Removed '{selected}' from favorites")
    else:
        st.session_state["favorites"].append(selected)
        st.success(f"✅ Added '{selected}' to favorites")

# Clear all button
if st.button("🗑️ Clear All Favorites"):
    st.session_state["favorites"].clear()
    st.info("All favorites cleared.")

st.markdown("---")
st.subheader("Your Favorite Recipes")

if not st.session_state["favorites"]:
    st.info("No favorites yet. You can add one from the home page.")
else:
    for fav in st.session_state["favorites"]:
        recipe = next((r for r in recipes if r["name"] == fav), None)
        if recipe:
            with st.expander(f"🌟 {recipe['name']}"):
                st.markdown("**Ingredients:**")
                st.markdown("\n".join(f"- {i}" for i in recipe["ingredients"]))
                st.markdown("**Instructions:**")
                st.markdown(recipe["instructions"])
