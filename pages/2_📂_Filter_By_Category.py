import streamlit as st
from utils.recipe_utils import load_recipes

st.set_page_config(page_title="Filter by Category", layout="centered")
st.title("📂 Filter Recipes by Category")

recipes = load_recipes()
categories = sorted(set(r.get("category", "Uncategorized") for r in recipes))

# Get category count for better UX
category_counts = {cat: sum(1 for r in recipes if r.get("category", "Uncategorized") == cat) for cat in categories}
category_labels = [f"{cat} ({category_counts[cat]})" for cat in categories]
category_map = dict(zip(category_labels, categories))

# Restore selected category if coming from home
default = None
if "selected_category" in st.session_state:
    default = categories.index(st.session_state["selected_category"])
    del st.session_state["selected_category"]

choice_label = st.selectbox("Select a category", category_labels, index=default if default is not None else 0)
choice = category_map[choice_label]

# Init favorites
if "favorites" not in st.session_state:
    st.session_state["favorites"] = []

st.markdown("---")
filtered = [r for r in recipes if r.get("category", "Uncategorized") == choice]
for r in filtered:
    st.subheader(r["name"])

    if "just_added_recipe" in st.session_state and r["name"] == st.session_state["just_added_recipe"]["name"]:
        st.markdown("🆕 *Recently Added!*")

    st.markdown("**Ingredients:** " + ", ".join(r["ingredients"]))
    st.markdown("**Instructions:**")
    st.markdown(r["instructions"])

    if st.button(f"⭐ Favorite '{r['name']}'", key=r["name"]):
        if r["name"] not in st.session_state["favorites"]:
            st.session_state["favorites"].append(r["name"])
            st.success(f"✅ Added '{r['name']}' to favorites")
        else:
            st.info(f"ℹ️ '{r['name']}' is already in favorites")

    st.divider()
