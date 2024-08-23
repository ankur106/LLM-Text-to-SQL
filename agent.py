import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent

load_dotenv()

uri = f"postgresql://{os.environ['POSTGRES_USERNAME']}:{os.environ['POSTGRES_PASSWORD']}@localhost/LLM_SQL"

db = SQLDatabase.from_uri(uri)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) 
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)


agent_executor.invoke(
    {
        "input": "List all the cities with less than 1 million population"
    }
)