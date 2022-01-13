import speech_recognition as sr

def Nghe():
    #khoi tao chuc nang nhan biet
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold=2
        #nghe tu micro
        nghe= r.record(source,duration=5)
        #xuat ra van ban
        try:
            viet=r.recognize_google(nghe, language="vi")
        except:
            viet="Toi khong nghe duoc"
    return viet
