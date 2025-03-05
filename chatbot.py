from langchain.chat_models import ChatOpenAI
from langgraph.graph import MessageGraph
from langchain.schema import AIMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize AI Model
llm = ChatOpenAI(model="gpt-4", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))

# Define LangGraph Chatbot
def get_ai_response(messages):
    return llm(messages)

graph = MessageGraph()
graph.add_node("chat", get_ai_response)
graph.set_entry_point("chat")
graph.add_edge("chat", "chat")

conversation = graph.compile()

def chat_with_ai(user_input):
    response = conversation.invoke([HumanMessage(content=user_input)])
    return response.content
