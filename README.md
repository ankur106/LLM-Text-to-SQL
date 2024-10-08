# LLM-Text-to-SQL

#### Here are the different approaches used to solve the problem

1. SQl chain
- Here llm is used to create sql query first and then through python pipe/chain the query is passed to sql database tool and finally llm sumarizes whatever outcome of the query.

- We are passing SQL schema by default and the result can be optimized via passing example queries. 

- Or event we can send most relevant k queries in context via similarity search.

2. SQL Agent

- Langchain agentic approach can be more robust as it can regerate query and execute it if there is an execution error. 

for example here it solved the error via adding state first when state was not available in state table
![SQL Agent](/Data/sql_agent.png)

3. If infrastructure is on aws [reference](https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-to-sql-solution-generating-complex-queries-self-correcting-and-querying-diverse-data-sources/)

- similar thing can be done on aws with glue(ETL) for metadata extraction, opensearch for similarity search, Bedrock and Athena for query execution.
![SQL Agent](/Data/aws.png)
