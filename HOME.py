import streamlit as st
import random
from PIL import Image
from utils.recipe_utils import load_recipes

st.set_page_config(page_title="🍽️ Random Recipes", layout="centered")

# App header
st.title("👨‍🍳 Random Recipes")
st.markdown("A fresh recipe with every click!")

# Hero image
image = Image.open("assets/food.jpg")
st.image(image, use_container_width=True, caption="Swipe-worthy deliciousness 🍝")

# Load recipes
recipes = load_recipes()

# Initialize session state
if "favorites" not in st.session_state:
    st.session_state["favorites"] = []
if "current_recipe" not in st.session_state:
    st.session_state["current_recipe"] = None

# Prioritize recently added recipe
if "just_added_recipe" in st.session_state:
    st.session_state["current_recipe"] = st.session_state.pop("just_added_recipe")

# Recipe randomizer button
if st.button("🎲 Surprise Me With a Dish!"):
    st.session_state["current_recipe"] = random.choice(recipes)

# Display recipe if selected
recipe = st.session_state.get("current_recipe")

if recipe:
    st.markdown("---")
    st.subheader(f"🍽️ {recipe['name']}")
    st.markdown(f"**📂 Category:** {recipe.get('category', 'Uncategorized')}")

    st.markdown("### 🧂 Ingredients")
    for item in recipe["ingredients"]:
        st.markdown(f"- {item}")

    st.markdown("### 📝 How to Make It")
    st.write(recipe["instructions"])

    # Favorite button
    if st.button("⭐ Save to My Faves"):
        if recipe["name"] not in st.session_state["favorites"]:
            st.session_state["favorites"].append(recipe["name"])
            st.success("✅ Added to your favorite recipes!")
        else:
            st.info("✨ Already in your faves — you're clearly a fan!")

    # Category navigation
    if st.button("🔍 Explore More from This Category"):
        st.session_state["selected_category"] = recipe.get("category", "Uncategorized")
        st.switch_page("pages/2_📂_Filter_By_Category.py")
