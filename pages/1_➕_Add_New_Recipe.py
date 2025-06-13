import streamlit as st
from utils.recipe_utils import load_recipes, save_recipes

st.set_page_config(page_title="Add New Recipe", layout="centered")
st.title("➕ Add a New Recipe")

name = st.text_input("Recipe name")
category = st.text_input("Category (e.g., Breakfast, Lunch, Snack)")
ingredients = st.text_area("Ingredients (comma-separated)")
instructions = st.text_area("Instructions")

recipes = load_recipes()
existing_names = [r["name"].lower() for r in recipes]

if st.button("✅ Add Recipe"):
    if name and ingredients and instructions:
        if name.lower() in existing_names:
            st.error("⚠️ A recipe with this name already exists.")
        else:
            new_recipe = {
                "name": name.strip(),
                "category": category.strip() if category else "Uncategorized",
                "ingredients": [i.strip() for i in ingredients.split(",")],
                "instructions": instructions.strip()
            }
            recipes.append(new_recipe)
            save_recipes(recipes)

            # Store just-added recipe in session to show on HOME
            st.session_state["just_added_recipe"] = new_recipe

            st.success(f"🎉 '{name}' added successfully!")

            # Optional: View on Home
            if st.button("👀 View on Home"):
                st.switch_page("HOME.py")
    else:
        st.warning("Please fill in all fields.")
