import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText  # Return the recognized text
        except sr.RequestError as e:
            print("Could not request results:", e)
        except sr.UnknownValueError:
            print("Unknown error occurred")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = record_text()
    output_text(text)
    print("Wrote Text:", text)
