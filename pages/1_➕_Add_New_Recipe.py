import streamlit as st
from utils.recipe_utils import load_recipes, save_recipes

st.title("➕ Add a New Recipe")

name = st.text_input("Recipe name")
category = st.text_input("Category (e.g., Breakfast, Lunch, Snack)")
ingredients = st.text_area("Ingredients (comma-separated)")
instructions = st.text_area("Instructions")

if st.button("Add Recipe"):
    if name and ingredients and instructions:
        recipes = load_recipes()
        new_recipe = {
            "name": name,
            "category": category if category else "Uncategorized",
            "ingredients": [i.strip() for i in ingredients.split(",")],
            "instructions": instructions
        }
        recipes.append(new_recipe)
        save_recipes(recipes)
        st.success("Recipe added successfully!")
    else:
        st.warning("Please fill in all fields.")
