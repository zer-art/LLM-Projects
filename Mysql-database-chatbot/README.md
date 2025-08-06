# MYSQLchatbot

A conversational chatbot interface for querying your MySQL e-commerce database using natural language, powered by LLMs.

## Features

- Chat interface built with Streamlit
- Uses Google Gemini LLM for SQL generation
- Semantic few-shot prompting for better SQL accuracy
- Supports MySQL database queries

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Ecom-chatbot.git
   cd Ecom-chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with:

   ```
   GOOGLE_API_KEY=your_google_api_key
   MYSQL_PASSWORD=your_mysql_password
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

## Usage

- Ask questions about your e-commerce database in natural language.
- The chatbot will generate and execute SQL queries, returning the results conversationally.

## Project Structure

- `app.py` — Streamlit chat interface
- `src/utils.py` — LLM and database chain logic
- `src/few_shorts_queries.py` — Few-shot examples for prompting
- `src/mysql_prompt.py` — Custom prompt templates

---

