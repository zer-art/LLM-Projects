# LLM-Projects

<img src="https://imgs.search.brave.com/gfqte3HT4C1YJT0AtKRexIPRTIsgvGmzEPoZj4D4LS4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG5p/Lmljb25zY291dC5j/b20vaWxsdXN0cmF0/aW9uL3ByZW1pdW0v/dGh1bWIvYWktcm9i/b3QtZG9pbmctdHJh/aW5pbmctaWxsdXN0/cmF0aW9uLWRvd25s/b2FkLWluLXN2Zy1w/bmctZ2lmLWZpbGUt/Zm9ybWF0cy0tZWR1/Y2F0aW9uYWwtYW5k/LWxhcmdlLWxhbmd1/YWdlLW1vZGVsLXBh/Y2stc2NpZW5jZS10/ZWNobm9sb2d5LWls/bHVzdHJhdGlvbnMt/MTIzNDYxNTcucG5n" alt = "LLM img">

This repository contains a collection of projects leveraging Large Language Models (LLMs) for various applications. Each subdirectory is a standalone project with its own codebase, dependencies, and documentation. Below is an overview of each project:

## Ai-Grammer-Tutor
An AI-powered grammar tutor that helps users improve their grammar skills. It features a Python backend and a simple frontend for user interaction.
- **Backend:** Python (main.py, src/)
- **Frontend:** HTML, CSS, JavaScript (frontend/)
- **Usage:** Run `main.py` to start the backend server. Open `frontend/index.html` in a browser for the UI.

## Mysql-database-chatbot
A chatbot interface for interacting with MySQL databases using natural language queries. It translates user questions into SQL and fetches results from the database.
- **Backend:** Python (app.py, src/)
- **Database:** SQL scripts for setup (database/)
- **Usage:** Run `app.py` to start the chatbot server. Ensure MySQL is running and the database is set up using the provided SQL script.

## News-Research-Analysis
An application for researching and analyzing news articles using LLMs and retrieval-augmented generation (RAG) techniques.
- **Backend:** Python (app.py, src/)
- **Data:** Vector store for semantic search (vectorstore.pkl)
- **Usage:** Run `app.py` to start the analysis tool. Add news data to the vector store for improved results.

## Restautant-Name-And-Menu-Gen
Generates creative restaurant names and menu items using LLMs, based on cuisine and style inputs.
- **Backend:** Python (app.py, src/)
- **Data:** Text files for cuisines and styles (data/)
- **Usage:** Run `app.py` and provide cuisine/style inputs to generate names and menus.

---

## How to Use
1. Clone the repository: `git clone <repo-url>`
2. Navigate to the desired project directory.
3. Follow the instructions in each project's README.md for setup and usage.

## Requirements
Each project has its own `requirements.txt` or `pyproject.toml`. Install dependencies using `pip install -r requirements.txt` or `pip install .` as needed.

## License
See individual project directories for license information.
