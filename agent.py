import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main(): 
    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load environment variables from .env file
    load_dotenv()
    endpoint= os.getenv("PRAZURE_INFERENCE_ENDPOINT")
    credential = os.getenv("AZURE_INFERENCE_CREDENTIAL")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    model = AzureAIChatCompletionsModel(
        endpoint=endpoint,
        credential=credential,
        model=model_deployment,
    )

    # messages = [
    #     SystemMessage(content="Translate the following from English into Italian"),
    #     HumanMessage(content="hi!"),
    # ]

    # message_stream = model.stream(messages)
    # print("".join(chunk.content for chunk in message_stream))
    system_template = "Translate the following into {language}:"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    producer_template = PromptTemplate(
        template="You are an urban poet, your job is to come up \
                verses based on a given topic.\n\
                Here is the topic you have been asked to generate a verse on:\n\
                {topic}",
        input_variables=["topic"],
    )

    parser = StrOutputParser()

    chain = producer_template | model | parser

    # response = chain.invoke({"language": "italian", "text": "hi"})

    response = chain.invoke({"topic": "living in a foreign country"})

    print("response: ", response)

if __name__ == '__main__': 
    main()