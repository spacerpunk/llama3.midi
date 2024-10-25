import requests
import json
import speech_recognition as sr
import asyncio
from ollama import AsyncClient

USER = 'user'
ASSISTANT = 'assistant'

def add_history(content, role):
    messages.append({'role': role, 'content': content})

def runLlama():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginze_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling
    
        try:
            # using google speech recognition
            voice = r.recognize_google(audio_text)
            print("Text: "+ voice)
        except:
            print("Sorry, I did not get that")

    # API endpoint
    url = "http://localhost:11434/api/chat"

    # PROMPT

    prompt = voice

    async def chat():
        """
        Stream a chat from Llama using the AsyncClient.
        """
        message = {
            "role": "user",
            "content": prompt
        }
        async for part in await AsyncClient().chat(
            model="llama3", messages=[message], stream=True
        ):
            print(part["message"]["content"], end="", flush=True)


    asyncio.run(chat())

     # Initialize recognizer class (for recognizing the speech)


for a in range(15):
    runLlama()