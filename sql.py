from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import pymysql
import sqlite3
from langchain.chains import create_sql_query_chain

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCx5DAM5VTvRqYwsyQWTaq9FB-GmLNkeys"

con = sqlite3.connect('university.db')
c = con.cursor()

db = SQLDatabase.from_uri(f"sqlite:///university.db")

db.run("SELECT * FROM instructor LIMIT 10")

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0)
chain = create_sql_query_chain(llm, db)

from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db)
db_chain = write_query | execute_query


from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, removing string 'SQLQuery:', and SQL result, answer the user question.
    
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer:
 """
)

answer = answer_prompt | llm | StrOutputParser()
chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    | answer
    
)
user_input = input()
input_data = {"question": user_input}

chain.invoke(input_data)
