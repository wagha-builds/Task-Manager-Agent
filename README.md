# 🤖 LangChain AI Task Manager Agent

A Python-based **AI-powered task manager** that integrates **LangChain**, **Google Gemini**, and **Todoist API** to help users manage their tasks via natural language commands.  
This agent can add tasks, show task lists, and interact with Todoist seamlessly using AI-driven prompts.

---

## 🚀 Features

- 📝 **Add tasks via natural language** commands.  
- 📋 **Show all existing tasks** in a clean bullet list format.  
- 🤖 **AI-powered assistant** using LangChain and Google Gemini LLM.  
- 🔐 **Secure API key management** using environment variables.  
- ⚡ Fully interactive **command-line interface** with real-time conversation history.  

---

## 📂 Project Structure

LangChain-AI-Task-Manager-Agent/
│
├── main.py # Main Python script running the AI agent
├── .env # Environment variables containing API keys
├── README.md # Project documentation
└── requirements.txt # Python dependencies

---

## 🧰 Prerequisites

- Python 3.8+  
- [LangChain](https://www.langchain.com/)  
- [Todoist API Python Client](https://github.com/Doist/todoist-python)  
- Google Gemini API access  
- `python-dotenv` for managing environment variables  

Install dependencies using:

```bash
pip install langchain langchain_google_genai todoist-api-python python-dotenv

