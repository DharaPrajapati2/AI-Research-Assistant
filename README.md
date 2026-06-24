# 🤖 AI Research Assistant (LangChain + Gemini + Tools)

An AI-powered research assistant built using Python, LangChain, and Google Gemini.  
It can search the web, fetch Wikipedia information, and generate structured research outputs.

---

## 🚀 Features

- Web search using DuckDuckGo
- Wikipedia information retrieval
- Google Gemini LLM integration
- Structured output using Pydantic
- Tool-based agent system (LangChain tools)
- Save research output to a text file

---

## 🧰 Tech Stack

- Python
- LangChain
- Google Gemini API
- DuckDuckGo Search
- Wikipedia API
- Pydantic

---

## 📁 Project Structure

AI AGENT/
├── main.py              # Main file (LLM + prompt + output)
├── tools.py             # Tools (search, wikipedia, save)
├── test.py              # Testing file
├── .gitignore
├── requirements.txt
└── research_output.txt

---

## ⚙️ How It Works

- User enters a research query
- Gemini processes the query
- Tools are used if required:
  - DuckDuckGo for web search
  - Wikipedia for factual data
- AI generates structured response:
  - Topic
  - Summary
  - Sources
  - Tools used
- Output can be saved to a file

---

## 📌 Future Improvements

- Multi-step autonomous agent
- PDF report generation
- Web UI using Streamlit
- Memory for past queries
- Better citation system

---

## 👨‍💻 Author

Dhara Prajapati  
AI/ML Enthusiast | Python Developer

---

## ⭐ Support

If you like this project, give it a star ⭐ on GitHub
