import os
import pyttsx3
import PyPDF2
import logging

logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

speed_dict = {
    "slow": 100,
    "normal": 150,
    "fast": 200}


def speak_text(engine, text, print=False):
    if print:
        print(text)
    engine.say(text)
    engine.runAndWait()


class AudioBook:
    def __init__(self, speed="normal"):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", speed_dict[speed])
        
    def create_json_book(self, pdf_file_path, password=None):
        
        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError("File not found!")
        
        if not pdf_file_path.endswith(".pdf"):
            raise ValueError("File must be a pdf!")
        
        book_dict = {}
        with open(pdf_file_path, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            if pdfReader.isEncrypted:
                logging.info("File is encrypted, trying to decrypt...")
                pdfReader.decrypt(password)
            pages = pdfReader.numPages
            for num in range(0, pages):
                pageObj = pdfReader.getPage(num)
                text = pageObj.extractText()
                book_dict[num] = text
        return book_dict, pages
    
    def save_audio(self, pdf_file_path, password=None):
        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError("File not found!")
        
        if not pdf_file_path.endswith(".pdf"):
            raise ValueError("File must be a pdf!")
        
        with open(pdf_file_path, "rb") as fp:
            basename = os.path.basename(pdf_file_path).split(".")[0]
            os.makedirs(basename, exist_ok=True)
            logging.info('Saving audio files in folder: {}'.format(basename))
            pdfReader = PyPDF2.PdfFileReader(fp)
            if pdfReader.isEncrypted:
                logging.info("File is encrypted, trying to decrypt...")
                pdfReader.decrypt(password)
            pages = pdfReader.numPages
            for num in range(0, pages):
                pageObj = pdfReader.getPage(num)
                text = pageObj.extractText()
                self.engine.save_to_file(text, os.path.join(basename, basename + "_" + (str(num) + ".mp3")))
                self.engine.runAndWait()
                
    def read_book(self, pdf_file_path, password=None):
        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError("File not found!")
        
        if not pdf_file_path.endswith(".pdf"):
            raise ValueError("File must be a pdf!")
        
        with open(pdf_file_path, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            if pdfReader.isEncrypted:
                logging.info("File is encrypted, trying to decrypt...")
                pdfReader.decrypt(password)
            pages = pdfReader.numPages
            speak_text(self.engine, f"The book has total {str(pages)} pages!")
            speak_text(self.engine, "Please enter the page number: ")
            start_page = int(input("Please enter the page number: ")) - 1
            reading = True
            while reading:
                if start_page > pages or start_page < 0:
                    speak_text(self.engine, "Invalid page number!")
                    speak_text(self.engine, f"The book has total {str(pages)} pages!")
                    start_page = int(input("Please enter the page number: "))

                speak_text(self.engine, f"Reading page {str(start_page+1)}")
                pageObj = pdfReader.getPage(start_page)
                pageText = pageObj.extractText()
                speak_text(self.engine, pageText)

                user_input = input("Please Select an option: \n 1. Type 'r' to read again: \n 2. Type 'p' to read previous page\n 3. Type 'n' to read next page\n 4. Type 'q' to quit:\n 5. Type page number to read that page:\n")
                if user_input == "r":
                    speak_text(self.engine, f"Reading page {str(start_page+1)}")
                    continue
                elif user_input == "p":
                    speak_text(self.engine, "Reading previous page")
                    start_page -= 1
                    continue
                elif user_input == "n":
                    speak_text(self.engine, "Reading next page")
                    start_page += 1
                    continue
                elif user_input == "q":
                    speak_text(self.engine, "Quitting the book!")
                    break
                elif user_input.isnumeric():
                    start_page = int(user_input) - 1
                else:
                    user_input = input("Please Select an option: \n 1. Type 'r' to read again: \n 2. Type 'p' to read previous page\n 3. Type 'n' to read next page\n 4. Type 'q' to quit:\n 5. Type page number to read that page:\n")
                    continue
