# 🤖 LangChain AI Task Manager Agent

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Integration-orange)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-purple)
![Todoist API](https://img.shields.io/badge/API-Todoist-red)

A sophisticated, Python-based **AI-powered task manager** that leverages the power of **LangChain**, **Google Gemini 2.5 Flash**, and the **Todoist API**. This intelligent agent allows users to manage their daily tasks entirely through natural language commands via an interactive command-line interface.

---

## 🚀 Features

- 📝 **Natural Language Task Creation:** Tell the AI to add a task in plain English (e.g., "Remind me to buy groceries tomorrow"), and it translates your intent into a structured API call.
- 📋 **Intelligent Task Retrieval:** Ask the assistant to show you your current tasks, and it fetches and formats them into a clean, readable bullet list.
- 🧠 **Context-Aware Conversational Memory:** Built with LangChain's `HumanMessage` and `AIMessage` history lists, allowing the agent to remember context across multi-turn conversations.
- 🛠️ **Custom Tool Binding:** Utilizes LangChain's `@tool` decorator to map LLM reasoning directly to Todoist API Python Client functions.
- 🔐 **Secure Configuration:** Safely manages API keys via `.env` files and the `python-dotenv` library.

---

## 🏗️ How It Works

1. **User Input:** You type a natural language command into the CLI.
2. **LangChain AgentExecutor:** The query, along with the conversation history, is passed to the LangChain Agent Executor.
3. **LLM Reasoning (Gemini):** Google's Gemini-2.5-Flash analyzes the prompt and determines if it needs to invoke a tool (like `add_task` or `show_tasks`).
4. **Tool Execution (Todoist API):** If a tool is invoked, the Python script executes the corresponding Todoist REST API call to fetch or manipulate your actual task list.
5. **Response Generation:** The LLM takes the output of the tool and crafts a conversational, human-friendly response back to you.

---

## 🧰 Tech Stack

- **Python 3.8+**
- **[LangChain](https://www.langchain.com/)** - Orchestration framework for LLMs and Tool Agents.
- **[Google Gemini API](https://aistudio.google.com/)** - Core Large Language Model (`gemini-2.5-flash`).
- **[Todoist API Python Client](https://github.com/Doist/todoist-python)** - For interacting with your actual Todoist account.
- **python-dotenv** - For environment variable management.

---

## 🏁 Getting Started

### 1. Prerequisites
You will need two API keys to run this project:
- **Google Gemini API Key:** Get it from [Google AI Studio](https://aistudio.google.com/).
- **Todoist API Token:** Log into Todoist, go to Settings -> Integrations -> Developer -> API token.

### 2. Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/wagha-builds/Task-Manager-Agent.git
cd Task-Manager-Agent
```

Install the required Python dependencies:
```bash
pip install -r requirements.txt
# Alternatively, if you don't have the requirements file:
# pip install langchain langchain_google_genai todoist-api-python python-dotenv
```

### 3. Environment Setup
Create a `.env` file in the root directory of the project and add your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
TODOIST_API_KEY=your_todoist_api_token_here
```

### 4. Run the Agent
Start the interactive AI task manager:
```bash
python main.py
```

---

## 💻 Usage Examples

Once the script is running, simply type your requests naturally:

**Adding Tasks:**
> **You:** "Hey, can you add a task to review the pull request for the frontend team?"<br>
> **Agent:** "I have added the task 'Review the pull request for the frontend team' to your Todoist."

**Viewing Tasks:**
> **You:** "What do I have on my plate right now?"<br>
> **Agent:** "Here are your current tasks: \n- Buy groceries \n- Review the pull request for the frontend team"

---

## 📂 Project Structure

```text
Task-Manager-Agent/
│
├── main.py              # Main Python script defining tools, prompts, and the execution loop
├── requirements.txt     # List of dependencies
├── .env                 # (Ignored) Environment variables containing API keys
└── README.md            # Project documentation
```

---

## 🤝 Contributing
Contributions are welcome! If you have ideas for new tools (like task deletion, setting due dates, or marking tasks as complete), feel free to fork the repository and submit a Pull Request.

---

## 📜 License
This project is open-source and available under the MIT License.
