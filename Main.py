import streamlit as st
from PIL import Image

# Define the header
st.title("Bee Own")

# Create navigation links
nav_links = ["Features", "Pricing", "Contact"]

# Create a sidebar for navigation
selected_page = st.sidebar.radio("Navigation", nav_links)

image1 = Image.open('C:/Users/manoj/OneDrive/Desktop/Test/Blue Apple.jpg')
image2 = Image.open('C:/Users/manoj/OneDrive/Desktop/Test/Green Apple.jpg')
image3 = Image.open('C:/Users/manoj/OneDrive/Desktop/Test/Red Apple.jpg')

# Define the content for each section
if selected_page == "Features":
    st.header("Key Features")
    st.markdown("### Feature 1")
    st.image(image1, width=300)  # Adjust the width as needed
    st.write("Description of feature 1.")

    st.markdown("### Feature 2")
    st.image(image2, width=300)  # Adjust the width as needed
    st.write("Description of feature 2.")

    st.markdown("### Feature 3")
    st.image(image3, width=300)  # Adjust the width as needed
    st.write("Description of feature 3.")

elif selected_page == "Pricing":
    st.header("Pricing Plans")
    st.markdown("### Basic")
    st.write("$9/month")
    st.write("- Feature 1")
    st.write("- Feature 2")
    st.button("Get Started")

    st.markdown("### Pro")
    st.write("$19/month")
    st.write("- Feature 1")
    st.write("- Feature 2")
    st.write("- Feature 3")
    st.button("Get Started", key="pro_button")

elif selected_page == "Contact":
    st.header("Contact Us")
    st.write("If you have any questions, feel free to contact us.")
    st.text_input("Your Name", "")
    st.text_input("Your Email", "")
    st.text_area("Your Message", "")
    st.button("Submit")

# Footer
st.write("&copy; 2023 Your Company Name. All rights reserved.")
