from openai import OpenAI
from dotenv import load_dotenv
import datetime

load_dotenv()

class TextToSpeech:
    
    def __init__(self):
        self.client = OpenAI()
        
    def tts(self, input):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=input
        )
        
        filename = os.path.join("./audios/", datetime.date.today().strftime('%Y-%m-%d') + ".mp3")
        response.stream_to_file(filename)
    
    def test(self):
        input = """
        In this week's tech and AI news roundup, we've got some major developments to cover, starting with a significant move in the AI industry. Mustafa Suleyman, a co-founder of Google DeepMind, has made a surprising career shift by joining Microsoft as the CEO of Microsoft AI. This move is particularly noteworthy given Suleyman's history with Google and his recent venture, Inflection AI, known for creating the advanced chatbot, Piie. Microsoft's strategic hire comes amidst a heated race between Google and Microsoft to dominate the AI sector. In a related development, Microsoft has agreed to pay Inflection AI $650 million to hire its staff, a move speculated to cushion the blow for Inflection's investors and possibly avoid anti-trust scrutiny.

        From Nvidia's GTC conference, a major announcement was the unveiling of the next-gen Blackwell GPU, promising up to a 30 times performance increase for AI inference tasks. This development is set to revolutionize the efficiency and cost-effectiveness of training large language models. Nvidia also introduced Groot, a new AI platform for humanoid robots, and emphasized the importance of digital twins in AI development, including the ambitious Earth 2 project for simulating and visualizing weather and climate.

        Elon Musk has made headlines by open-sourcing Grok 1, the largest open-source model to date, under the Apache 2.0 license, allowing for wide-ranging commercial and non-commercial use. This move could significantly impact AI development and accessibility.

        In other news, Apple is reportedly exploring a partnership with Google for a Gemini-powered feature on iPhones, a surprising turn given Apple's history of in-house development. This development raises questions about Apple's position in the generative AI race and its strategy moving forward.

        Stability AI, known for Stable Diffusion, faces challenges as key researchers depart amidst speculation about the company's future. This shift could impact the landscape of AI development and open-source models.

        Mid Journey has updated its terms and conditions, highlighting the legal responsibilities of users in creating AI-generated content, a move that contrasts with other companies' more supportive stances on copyright issues.

        Lastly, the AI community is abuzz with speculation about OpenAI's secretive new project, Voice Engine, following a trademark filing. This project is anticipated to significantly advance voice recognition and generation technology, potentially setting a new standard for AI-powered personal assistants.

        Stay tuned for more updates in the rapidly evolving world of technology and artificial intelligence.
        """
        
        self.tts(input)

if __name__ == "__main__":
    client = TextToSpeech()
    client.test()