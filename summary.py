from langchain_openai import ChatOpenAI
from langchain.prompts import ChatMessagePromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from get_youtube_transcript import get_transcripts

class ChatModel:
    
    def __init__(self, docs: list[str]):
        model = ChatOpenAI(temperature=0, model_name="gpt-4-turbo-preview")
        prompt = self._get_prompt()
        self.docs_string: str = "\n\n".join(docs)
        self.chain = (
            prompt
            | model
            | StrOutputParser()
        )

    def _get_prompt(self):
        system_message_template = (
            """
            You are a professional news reporter that reads provided documents on this weeks latest AI developments and summarizes them in a concise text suitable for a one to two minute news segment. 
            Please base your response entirely on the given documents, focusing on key details, facts, and breakthroughs. Do not add any additional information or speculation.
            """
        )
        human_message_template = (
            """
            INPUT DOCUMENTS: 
            {documents}
            """
        )
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_message_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_message_template)

        return ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    def get_response(self):
        return self.chain.invoke("\n\n".join(self.docs_string))


if __name__ == "__main__":
    docs = []
    docs.append(get_transcripts())
    
    chat_model = ChatModel(docs)
    response = chat_model.get_response()
    print(response)