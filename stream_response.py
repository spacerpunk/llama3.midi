import ollama
import speech_recognition as sr

model = 'llama3.2:latest'
messages = []
# Roles
USER = 'user'
ASSISTANT = 'assistant'

constant =  "You are a helpful agent that only responds with a single JSON object for MIDI. Do not provide explanations or other text outside of the JSON object. If you need to provide an explanation, generate an appropriate response in JSON format. "
example = "the exact response of the JSON File shoud be in this format [{'event':'note_on', 'note':'60', 'velocity':64, 'time':0.5}]. "
end = "Please respond with only a single JSON object and no additional text."

def add_history(content, role):
    messages.append({'role': role, 'content': content})

def chat(message):
    add_history(message, USER)
    response = ollama.chat(model=model, messages=messages, stream=True)
    complete_message = ''
    for line in response:
        complete_message += line['message']['content']
        print(line['message']['content'], end='', flush=True)
    add_history(complete_message, ASSISTANT)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nTalk: ')
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginze_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling

        try:
            # using google speech recognition
            voice = r.recognize_google(audio_text)
            print("Text: "+ voice)
            if voice.lower() == 'exit':
                break
            else:
                chat(voice)
        except:
            print("Sorry, I did not get that")
