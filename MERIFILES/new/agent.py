from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

from devops_tools import read_log_file, count_log_levels, show_docker_containers

#LLM CHAHIYE MUJHE
llm = ChatOllama(
    model = "llama3.2",
    base_url = "http://localhost:11434",
    temperature = 0
)

#TOOLS CHAHIYE MUJHE 
#we could use the langchain framework to make ai tools without having to write hefty codes
#decoratoring and using this 
#i called the function from an another function as we coould import the count log levels in our api
@tool
def analyze_logs(path):
    """ This tool counts the log levels , info and count """
    return count_log_levels(read_log_file(path))

@tool
def get_docker_containers():
    """
    This tool internally run docker commands via subprocess the running and exciteing containers
    """
    return show_docker_containers()


#LLM + Tools  = AI Agent
#now integrate the agent
TOOLS = [analyze_logs, get_docker_containers]
SYSTEM_PROMPT = """
    You are an expert DevOps assistant specializing in log analysis. Use the `analyze_logs(file_path)` 
    tool to parse logs, identify recurring error patterns, and pinpoint root causes.
    ***Task ** Giving me the count of ERROR, WARN, WARNING, INFO  and all the reguired tools used.. Prioritize extracting 
    actionable insights, and ensure all outputs are crisp, clear, and directly to the point.
    You have to ensure the outputs are crisp, clear and to the end points.
    ***Task 2** analyse the docker containers running locally using `get_docker_containers` tool
    """
agent = create_agent(llm,tools = TOOLS, system_prompt = SYSTEM_PROMPT )

question = input("Enter your question for Devops Agent: ")
print("\nThinking...\n")
result =  agent.invoke({"messages": [("user", question)]})

#the last message is the agent;s final answer
print(result["messages"][-1].content)

