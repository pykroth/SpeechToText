import speech_recognition as sr
import pyttsx3

#intialize the recognizer
r=sr.Recognizer()

def record_text():
    #loop in case of errors
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=.2)

                audio2=r.listen(source2)

                MyText = r.recognize_google(audio2)

        except sr.RequestError as e:
            print("Could not request results;")
            
        except sr.UnknownValueError:
            print("unknown error occured")
            
def output_text(text):
    f=open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return
    
while(1):
    text=record_text()
    output_text(text)
        
    print("Wrote Text")