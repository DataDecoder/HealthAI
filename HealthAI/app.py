import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Setup
st.set_page_config(page_title="AI Dietician", page_icon="🥗")
st.title("Your AI Dietician")
st.subheader("Get healthy, personalized recipe suggestions using Gemini AI!")

# User Inputs
ingredients = st.text_input("Ingredients (comma-separated):")
diet = st.selectbox("Diet Preference:", ["Vegetarian", "Vegan", "Low Carb", "Gluten-Free", "Any"])
cuisine = st.text_input("Preferred Cuisine (e.g., Indian, Italian, Fusion):")

# Generate Recipe
if st.button("Get Recipe") and ingredients:
    with st.spinner("Talking to Gemini Chef..."):
        try:
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            prompt = (
                f"Suggest a healthy {diet.lower()} recipe using these ingredients: {ingredients}. "
                f"Make it in {cuisine if cuisine else 'any'} style. Include preparation steps and a health tip."
            )
            response = model.generate_content(prompt)
            st.markdown("### Your Recipe")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")

