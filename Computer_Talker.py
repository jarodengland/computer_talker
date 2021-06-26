import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
running=True

while(running):
    words = input('Say something for the computer to say \n')
    if words=="exit":
        running=False
    speaker.Speak(words)
