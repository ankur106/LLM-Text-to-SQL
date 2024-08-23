from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
import os

from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
uri = f"postgresql://{os.environ['POSTGRES_USERNAME']}:{os.environ['POSTGRES_PASSWORD']}@localhost/LLM_SQL"

db = SQLDatabase.from_uri(uri)  
context = db.get_context()
# print(context)

# print(db.dialect)
# print(db.get_usable_table_names())

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db)
chain = write_query | execute_query
# response = chain.invoke({"question": "Is there a state table?"})
# print(response)




answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)
# print(answer_prompt)
# print(chain.get_prompts()[0].partial(table_info=context["table_info"]))  # can check prompt passes here

answer = answer_prompt | llm | StrOutputParser()
chain1 = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    
)
# print(chain1 | StrOutputParser())
chain = (chain1 | answer)

response  = chain.invoke({"question": "Give all the rows of city table"})

print(response)