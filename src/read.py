import PyPDF2
import pyttsx3

def voicePDF():
    with open(r'C:\Users\gusta\Projetos\IA-MODEL\src\teorico.pdf', 'rb') as path:
        pdfReader = PyPDF2.PdfReader(path)

        speak = pyttsx3.init()
        for page_num in range(len(pdfReader.pages)):
            if page_num > 5:
                page = pdfReader.pages[page_num]
                text = page.extract_text()
                if text:
                    print("f\nReading Page {page_num + 1}:\n")
                    print(text)
                    speak.say(text)
                    speak.runAndWait()
        speak.stop()
    print("Fim")