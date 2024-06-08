from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import OpenAI

class LangChainClient:
    def __init__(self, bedrock_client):
        self.bedrock_client = bedrock_client
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                Context: {context}
                Question: {question}
                Answer:
            """
        )
        self.llm = OpenAI(
            bedrock_client=bedrock_client,
            model_name='your-bedrock-model'
        )
        self.llm_chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def generate_response(self, context, question):
        return self.llm_chain.run({"context": context, "question": question})

# Example usage
lang_chain_client = LangChainClient(bedrock_client)
context = "\n".join(doc[1] for doc in relevant_docs)
response = lang_chain_client.generate_response(context, user_query)
print(response)
