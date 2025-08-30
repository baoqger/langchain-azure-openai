import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.messages import HumanMessage, SystemMessage


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

    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]

    message_stream = model. stream(messages)
    print("".join(chunk.content for chunk in message_stream))

if __name__ == '__main__': 
    main()