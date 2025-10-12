from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI

load_dotenv()

# Store the api key in a variable.
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

# Ensures the use of AI agent from the user_input (here, it will have the function of adding tasks.)
# A tool is a 'function' which ensures that the LLM will execute the function provided.
# A docstring is required in the function which will check whether it matches the user_input's request.
@tool
def add_task(task, desc=None):
    """Add a new task to the user's task list. Use this when the user wants to add or create a task."""
    todoist.add_task(content=task,
                     description=desc)

@tool
def show_tasks():
    """Show all tasks from Todoist. Use this when the user wants to see their tasks."""
    # Here, the variable below will contain the representation of this results paginator, which we need to extract from.
    results_paginator = todoist.get_tasks()
    tasks=[]
    for task_list in results_paginator:
        # print(task_list)
        for task in task_list:
            # print(task)
            tasks.append(task.content)
    return tasks

tools = [add_task, show_tasks]

# Define the features of the AI agent.
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key=gemini_api_key,
                             temperature=0.3)

# Define the prompts (both user and AI)
# {input} is basically a placeholder, and so the prompt will be constructed dynamically due to the response variable.
system_prompt = """You are a helpful assistant. 
You will help the user add tasks.
You will help the user show existing tasks in a bullet list format.
"""
prompt = ChatPromptTemplate([("system", system_prompt),
                             MessagesPlaceholder("history"),
                             ("user", "{input}"),
                             MessagesPlaceholder("agent_scratchpad"),
                             ])

# | is an or operator in Python, but in LangChain. Here, it means that the prompt will go as the input of the llm.
# chain = prompt | llm | StrOutputParser()

#verbose shows you what the agent is doing/thinking.
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# response = chain.invoke({"input": user_input})

history=[]
while True:
    user_input = input("You: ")
    # Sends the user input and the history to the agent executor to invoke.
    response = agent_executor.invoke({"input": user_input, "history": history})
    print(response["output"])
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response["output"]))
