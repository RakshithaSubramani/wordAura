# AI-Powered Story Generator

A web-based application built with Python, Streamlit, and the Gemini API to generate creative stories based on user prompts, genres, and desired lengths. Stories are saved in a SQLite database and can be viewed in a history tab. The app supports interactive storytelling, allowing users to continue stories with follow-up prompts.

## Features
- Generate stories using the Gemini 1.5 Flash model.
- Customize stories by prompt, genre (Sci-Fi, Fantasy, Mystery, Horror, Adventure), and length (100-1000 words).
- Save stories to a local SQLite database (`stories.db`).
- View story history in an interactive table.
- Unique twist: Continue stories by adding follow-up actions (e.g., "The hero finds a hidden door").

## Prerequisites
- Python 3.9+ (tested with Python 3.11)
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- Git (optional, for version control)

## Setup Instructions
1. **Clone the Repository** (if using Git):
   ```bash
   git clone <your-repo-url>
   cd AI-STORY-GENERATOR


Create a Virtual Environment:
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux


Install Dependencies:
pip install google-generativeai streamlit python-dotenv pandas


Set Up the API Key:

Create a .env file in the project root (C:\Users\91900\Desktop\AI STORY GENERATOR).
Add your Gemini API key:GEMINI_API_KEY=your_key_here


Get your key from Google AI Studio.


Run the App:
streamlit run story_generator.py


Open http://localhost:8501 in a browser (Chrome/Firefox recommended).



Usage

Generate a Story:

Go to the "Generate Story" tab.
Enter a prompt (e.g., "A wizard in a cyberpunk city").
Select a genre (e.g., Sci-Fi) and length (e.g., 300 words).
Click "Generate Story" to see the output.
Optionally, enter a follow-up action (e.g., "The wizard casts a spell") and click "Continue Story".


View History:

Switch to the "Story History" tab.
Click "Refresh History" to see all saved stories in a table.



Troubleshooting

"No stories saved yet" in history tab:
Check stories.db exists in the project folder.
Verify the debug message: "Debug: Loaded X stories from C:\Users\91900\Desktop\AI STORY GENERATOR\stories.db".
Run test_db.py to confirm database contents:python test_db.py


Delete stories.db and restart the app to recreate it if issues persist.


WebSocket error ("Could not establish connection"):
Try a different port: streamlit run story_generator.py --server.port 8502.
Use Chrome/Firefox instead of Edge.
Disable browser extensions (e.g., Copilot in Edge: edge://extensions/).


Invalid distribution warning (e.g., ~cipy):
Delete the broken package:cd C:\Users\91900\AppData\Roaming\Python\Python311\site-packages
rmdir /s ~cipy


Reinstall in the virtual environment: pip install scipy.


Database locked error:
Ensure only one instance of the app is running.
Close other Python processes accessing stories.db.



Project Structure
AI-STORY-GENERATOR/
├── .env              # Gemini API key (not tracked)
├── .gitignore        # Ignored files
├── README.md         # This file
├── story_generator.py # Main Streamlit app
├── test_db.py        # Script to test SQLite database
├── stories.db        # SQLite database (not tracked)
├── venv/             # Virtual environment (not tracked)

Future Enhancements

Add user authentication for personalized story history.
Support image inputs for story inspiration (using Gemini 1.5 Pro).
Export stories as PDF or text files.
Deploy to Streamlit Cloud for online access.

Contributing
Feel free to fork this repo, submit issues, or create pull requests to enhance the app!
