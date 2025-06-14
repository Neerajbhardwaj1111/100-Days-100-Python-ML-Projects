import speech_recognition as sr
import pyttsx3

# Initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return"Sorry, I did not catch that."
        

def parse_command(command):
    nums = [int(s) for s in command.split() if s.isdigit()]

    if len(nums) < 2:
        return "Error: Not enough numbers found in the command."

    if "add" in command or "plus" in command:
        return nums[0] + nums[1]
    elif "subtract" in command or "minus" in command:
        return nums[0] - nums[1]
    elif "multiply" in command or "times" in command:
        return nums[0] * nums[1]
    elif "divide" in command or "by" in command:
        if nums[1] == 0:
            return "Error: Division by zero."
        return nums[0] / nums[1]
    else:
        return "Error: Operation not recognized."


while True:
    command = listen()
    if "exit" in command:
        break
    result = parse_command(command.lower())
    speak(f"The result is {result}")
