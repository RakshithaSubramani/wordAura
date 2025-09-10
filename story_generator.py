import google.generativeai as genai
import pandas as pd
import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv


load_dotenv()
API_KEY=os.getenv('GEMINI_API_KEY')
if not API_KEY:
    st.error("GEMINI_API_KEY not found in .env file. Please add it.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Database setup
def init_db():
    conn = sqlite3.connect('stories.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stories
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  prompt TEXT NOT NULL,
                  genre TEXT,
                  length INTEGER,
                  story TEXT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Save a generated story to DB
def save_story(prompt, genre, length, story):
    conn = sqlite3.connect('stories.db')
    c = conn.cursor()
    c.execute("INSERT INTO stories (prompt, genre, length, story) VALUES (?, ?, ?, ?)",
              (prompt, genre, length, story))
    conn.commit()
    conn.close()

# Load all stories from DB as a DataFrame
@st.cache_data  # Cache for better performance
def load_stories():
    conn = sqlite3.connect('stories.db')
    df = pd.read_sql_query("SELECT * FROM stories ORDER BY timestamp DESC", conn)
    conn.close()
    return df

# Function to generate a story using Gemini
def generate_story(enhanced_prompt, max_tokens):
    try:
        response = model.generate_content(
            enhanced_prompt,
            generation_config={"max_output_tokens": max_tokens}
        )
        return response.text
    except Exception as e:
        return f"Error generating story: {str(e)}"

# Initialize DB on app start
init_db()

# Streamlit UI
st.title("AI-Powered Story Generator")
st.write("Enter a story idea and let the AI craft a tale for you! Stories are saved automatically.")

# Tabs for Generate and History
tab1, tab2 = st.tabs(["Generate Story", "Story History"])

with tab1:
    # User inputs
    user_prompt = st.text_input("Enter your story idea (e.g., 'A pirate adventure on a haunted ship'):", "")
    genre = st.selectbox("Choose a genre (optional):", ["None", "Sci-Fi", "Fantasy", "Mystery", "Horror", "Adventure"])
    length = st.slider("Story length (words, approximate):", 100, 1000, 300)

    # Generate button
    if st.button("Generate Story"):
        if user_prompt:
            # Enhance prompt with genre and length
            enhanced_prompt = f"Write a story (around {length} words) based on: {user_prompt}"
            if genre != "None":
                enhanced_prompt = f"Write a {genre.lower()} story (around {length} words) based on: {user_prompt}"
            
            with st.spinner("Crafting your story..."):
                story = generate_story(enhanced_prompt, max_tokens=length * 2)  # Rough token estimate
                st.subheader("Your Generated Story")
                st.write(story)
                
                # Save to DB
                save_story(user_prompt, genre, length, story)
                st.success("Story saved to history!")
        else:
            st.error("Please enter a story idea.")

with tab2:
    stories_df = load_stories()
    if not stories_df.empty:
        st.subheader("Your Story History")
        st.dataframe(stories_df)  # Interactive table
    else:
        st.info("No stories saved yet. Generate one to see it here!")