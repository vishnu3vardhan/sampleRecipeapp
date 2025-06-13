import streamlit as st
from utils.recipe_utils import load_recipes

st.set_page_config(page_title="Search Recipes", layout="centered")
st.title("🔍 Search Recipes")

# Load and prepare
recipes = load_recipes()

if "favorites" not in st.session_state:
    st.session_state["favorites"] = []

def highlight(text, query):
    """Bold the matched query in text."""
    return text.replace(query, f"**{query}**") if query.lower() in text.lower() else text

query = st.text_input("Search by recipe name or ingredients:")

if query:
    query_lower = query.lower()
    results = []

    for recipe in recipes:
        name_match = query_lower in recipe["name"].lower()
        ingredient_match = any(query_lower in ing.lower() for ing in recipe["ingredients"])
        
        if name_match or ingredient_match:
            results.append(recipe)

    if results:
        st.success(f"🔎 Found {len(results)} recipe(s) matching: **{query}**")
        for r in results:
            with st.expander(f"📄 {r['name']}"):
                st.markdown("**Ingredients:**")
                highlighted_ingredients = [highlight(i, query) for i in r["ingredients"]]
                st.markdown("\n".join(f"- {i}" for i in highlighted_ingredients))

                st.markdown("**Instructions:**")
                st.markdown(highlight(r["instructions"], query))

                # Favorite toggle
                if r["name"] in st.session_state["favorites"]:
                    if st.button(f"❌ Remove from Favorites: {r['name']}", key=f"remove_{r['name']}"):
                        st.session_state["favorites"].remove(r["name"])
                        st.success(f"Removed '{r['name']}' from favorites")
                else:
                    if st.button(f"⭐ Add to Favorites: {r['name']}", key=f"add_{r['name']}"):
                        st.session_state["favorites"].append(r["name"])
                        st.success(f"Added '{r['name']}' to favorites")
    else:
        st.warning("No matching recipes found. Try another term.")
else:
    st.info("Start typing to search for recipes...")
