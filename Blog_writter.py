from dotenv import load_dotenv

load_dotenv()


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key = os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(image, prompt):
    response = model.generate_content([image, prompt])
    return response.text


prompt = """
You are an AI blog writer specializing in creating engaging and descriptive blog posts based on images. 
When a user uploads an image, your task is to analyze the visual content, context, 
and elements of the image, and then write a detailed and captivating blog post. 
Your post should reflect a deep understanding of the image, incorporating vivid descriptions, artistic interpretations, 
and any emotional undertones. Please ensure the blog is rich in detail, suitable for a diverse audience interested in art, 
photography, and storytelling. Use a narrative style that brings the image to life, making readers feel connected to the scene or subject depicted in the image.
"""

st.set_page_config("Gemini Model")

st.header("Blog Writter")



up_file = st.file_uploader("Choose image...", type = ["jpg", "jpeg", "png"])

button = st.button("Enter")

if button:

    image = ""
    if up_file is not None:
        image = Image.open(up_file)
        st.image(image, caption = "uploaded image", use_container_width = True)
        result = get_response(image, prompt)
        st.write(result)
    else:
        st.write("Please Upload the image....")