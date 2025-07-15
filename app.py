import streamlit as st
import praw
from reddit_scraper import user_name_extraction, scrape_user_data
from persona_generator import generate_persona

st.title("Reddit Persona Generator")

url = st.text_input("Enter a Reddit user URL")

if st.button("Generate Persona"):
    if url:
        try:
            username = user_name_extraction(url)
            st.write(f"Generating persona for: {username}")

            reddit = praw.Reddit(
                client_id=st.secrets["praw"]["client_id"],
                client_secret=st.secrets["praw"]["client_secret"],
                user_agent=st.secrets["praw"]["user_agent"],
            )

            user_data = scrape_user_data(reddit, username)
            persona = generate_persona(user_data, st.secrets["groq"]["api_key"])

            st.subheader("Generated Persona")
            st.write(persona)

            st.download_button(
                label="Download Persona as TXT",
                data=persona,
                file_name=f"{username}_persona.txt",
                mime="text/plain"
            )

        except ValueError as e:
            st.error(e)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a URL.")
