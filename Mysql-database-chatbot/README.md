# ✨ AI Grammar Tutor

A modern, interactive grammar checker and tutor powered by [Google Gemini](https://deepmind.google/technologies/gemini/) and [LangChain](https://python.langchain.com/).  
Get instant, conversational grammar feedback and explanations—right in your browser!

---

## 🚀 Features

- **Conversational AI Tutor:** Friendly, expert feedback on your sentences and grammar questions.
- **Instant Corrections:** Get clear explanations, corrections, and examples for your writing.
- **Interactive Chat UI:** Practice grammar in a chat-like interface.
- **Powered by Gemini:** Uses Google Gemini via LangChain for high-quality language understanding.
- **Easy to Run:** FastAPI backend, modern JavaScript frontend, and simple setup.

---

## 🖥️ Demo

![AI Grammar Tutor Screenshot](https://user-images.githubusercontent.com/your-github-username/your-screenshot.png) <!-- Replace with your screenshot if available -->

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/grammer.git
cd grammer
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

Create a `.env` file in the root directory:

```
GEMINI_API=your_google_gemini_api_key
```

### 4. Start the Backend

```bash
uvicorn main:app --reload
```

### 5. Open the Frontend

Open `frontend/index.html` in your browser.  
*(Or serve it with a simple HTTP server for local development.)*

---

## 🛠️ Project Structure

```
grammer/
├── main.py                # FastAPI backend
├── src/
│   ├── prompts.py         # AI prompt template
│   └── utils.py           # Grammar checking logic
├── frontend/
│   ├── index.html         # Chat UI
│   ├── index.js           # Frontend logic
│   └── index.css          # Styles
├── requirements.txt
└── .env                   # Your Gemini API key (not committed)
```

---

## 🤖 How It Works

- The **frontend** lets users chat with the AI tutor.
- The **backend** receives user input, builds a prompt, and sends it to Gemini via LangChain.
- The AI responds with corrections, explanations, or answers to grammar questions.
- The frontend displays the AI's response in a chat format.

---

## 📚 Example Usage

```python
from src.utils import GrammarChecker

checker = GrammarChecker("He go to school every day.")
print(checker.check_grammar())
```

---

## 💡 Customization

- **Change the AI prompt:** Edit `src/prompts.py` for a different tutor style.
- **Deploy the backend:** Use any cloud provider that supports FastAPI.
- **Style the frontend:** Tweak `frontend/index.css` for your brand.

---

## 📝 License

MIT License

---

## 🙋‍♂️ Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR.

---

## ⭐️ Show Your Support

If you like this project, please star it on [GitHub](https://github.com/your-username/grammer)!

---