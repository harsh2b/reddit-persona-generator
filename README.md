# Reddit Persona Generator

This application generates a user persona based on their Reddit activity. It scrapes a user's recent comments and posts, then uses a Large Language Model (LLM) to analyze the data and create a detailed user persona.

This project includes two main components:
1.  A command-line interface (CLI) to generate a persona and save it to a `.txt` file.
2.  A web-based application built with Streamlit for a more interactive experience.

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <your-repository-url>
cd reddit-persona-generator
```

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

This project requires API keys for both Reddit and Groq (the LLM provider).

#### For the Command-Line App (`main.py`):

Create a file named `.env` in the root of the `reddit_persona_generator` directory and add your API keys in the following format:

```
PRAW_CLIENT_ID="your_reddit_client_id"
PRAW_CLIENT_SECRET="your_reddit_client_secret"
PRAW_USER_AGENT="your_reddit_user_agent"
GROQ_API_KEY="your_groq_api_key"
```

#### For the Streamlit App (`app.py`):

Create a file named `secrets.toml` inside the `.streamlit` directory. Add your credentials like this:

```toml
# .streamlit/secrets.toml

[praw]
client_id = "your_reddit_client_id"
client_secret = "your_reddit_client_secret"
user_agent = "your_reddit_user_agent"

[groq]
api_key = "your_groq_api_key"
```

## How to Execute the Code

You can run either the command-line script or the Streamlit web application.

### Running the Command-Line Script

To generate a persona for a Reddit user, run `main.py`:

```bash
python main.py
```

The script will prompt you to enter the URL of the Reddit user's profile. After processing, it will print the persona to the console and save it as a `.txt` file (e.g., `username_persona.txt`).

### Running the Streamlit Web Application

To launch the web interface, use the following Streamlit command:

```bash
streamlit run app.py
```

This will open the application in your web browser. You can then enter a Reddit user URL in the input field and click "Generate Persona" to see the results. You will also have an option to download the generated persona as a `.txt` file.
