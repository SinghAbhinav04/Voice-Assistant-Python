import speech_recognition as sr
import pyttsx3
from openai import OpenAI


#creating an instance of class Recognizer which is an object of speech_recognizer class
recognizer = sr.Recognizer()

#starting text to speech engine
engine = pyttsx3.init()

voices = engine.getProperty("voices")
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.languages}")

desired_voice_index = 33  # Change this index to select a voice
engine.setProperty("voice", voices[desired_voice_index].id)

greeting_text="Hello there, start speaking to test"
engine.say(greeting_text)
engine.runAndWait()

# function to listen to voice commands
def listen_speech():
    while(1):
        try:
            #accessing the microphone
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration=0.5)
                #listening the audio
                audio_input= recognizer.listen(source)
                # audio to text
                text = recognizer.recognize_google(audio_input)
                
                return text.strip().lower()
        
        except sr.UnknownValueError:
            print("Unknown error occurred")
        except sr.RequestError:
            print("Failed to request correctly")
    return

# function to write into the file
def write_text(text):
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

def del_text():
    f=open("output.txt","w")
    f.write("")
    f.close()
    return
       
client = OpenAI(
    # Write your gemini free api key here
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def get_query(text):
    try:
        # Make a request to the Gemini API using the new method
        response = client.chat.completions.create(
            model="gemini-1.5-pro",  # Use the Gemini model
            n=1,  # Number of responses to return
            messages=[

                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"keep your answer short in about 50words or less on {text}"},
            ]
        )

        # Extract the AI's response from the Gemini API's response object
        result = response.choices[0].message.content.strip()
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, I couldn't process your query."


while(True):

    text=listen_speech()
    quit_command=["q","quit","exit","end","bye","tcv","abort"]
    clear_command=["clear", "clear the file", "clean", "clean the file","clear the log", "remove", "remove log"]
    farewell_text="Bye!"
    
    print(text)
    if(text in quit_command):
        engine.say(farewell_text)
        engine.runAndWait()
        break
    elif (text in clear_command):
        engine.say(text)
        engine.runAndWait()
        del_text()
    else:
        result=get_query(text)
        write_text(text)
        write_text(result)
        engine.say(result)
        engine.runAndWait()
        print("written into source")

