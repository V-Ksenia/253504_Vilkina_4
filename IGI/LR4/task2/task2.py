import re
from inputvalidator import *
from zipfile import ZipFile
from generaltask import GeneralTask

class FileHandler:
    filename_ = r'task2\inputText.txt' 

    @property
    def filename(self):
        return self.filename_
    
    @filename.setter
    def filename(self, filename):
        self.filename_ = filename

    def read_from_file(self):
        f = open(self.filename_, 'r')
        text = f.read()
        return text

    def write_to_file(self, text):
        f = open(self.filename_, 'w')
        f.write(text)
        return
    
class Zipper:  
    @staticmethod
    def zipFile(file_name, zip_file_name):
        with ZipFile(zip_file_name, 'w') as zf:
            zf.write(file_name)

class TextHandler:
    text_ = ""

    @property
    def text(self):
        return self.text_
    
    @text.setter
    def text(self, text):
        self.text_ = text

    def count_sentences(self):
        return self.count_declarative_sentences() + self.count_incentive_sentences() + self.count_interrogative_sentences()

    def count_declarative_sentences(self):
        return len(re.findall(r"\.\W", self.text_))

    def count_interrogative_sentences(self):
        return len(re.findall(r"\?\W", self.text_))

    def count_incentive_sentences(self):
        return len(re.findall(r"!\W", self.text_))
    
    def calculate_sentence_average_length(self):
        sentences_list = re.split(r'\.\W |\?\W |!\W', self.text_)
        word_list = [re.findall(r'\w+', sen) for sen in sentences_list]
        sum_ = 0
        for words in word_list:
            sum_ += sum(len(word) for word in words)
        return sum_/(len(word_list))
    
    def calculate_word_average_length(self):
        words_list = re.findall(r'\w+', self.text_)
        sum_ = 0
        for word in words_list:
            sum_ += len(word)
        return sum_/(len(words_list))
    
    def calculate_smiles_count(self):
        smile_pattern = re.compile(r'[;:]-*[()\[\]]+')
        smiles = re.findall(smile_pattern, self.text_)
        return len(smiles)
    
    def replace_spaces_wcharacter(self, char):
        return re.sub(r" ", char, self.text_)
    
    def find_capital_letter(self):
        return len(re.findall(r"[A-Z]", self.text_))

    def find_lowercase_letter(self):
        return len(re.findall(r"[a-z]", self.text_))
    
    def find_firts_zword_index(self):
        words_list = re.findall(r'\w+', self.text_)
        print(words_list)
        match = re.search(r'[a-yA-Y]*[zZ][a-yA-Y]*', self.text_)
        return match[0], words_list.index(match[0]) + 1

    def remove_awords(self):
        return re.sub(r" [aA][a-zA-Z]*", "", self.text_)
        
    def validate_guid_string(self):
        guid = re.fullmatch(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', self.text_)
        match = re.fullmatch(r'\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}', self.text_)

        if match:
            return 'GUID with brackets'
        if guid:
            return 'GUID without brackets'
            
        return "String isn't in a GUID format"
       

class TaskSecond(GeneralTask):
    @staticmethod
    def __call__():
        file_loader = FileHandler()
        text = file_loader.read_from_file()
        print(text)
        
        text_handler = TextHandler()
        text_handler.text_ = text
        print(f"{text_handler.count_declarative_sentences()}\n{text_handler.count_interrogative_sentences()}\n{text_handler.count_incentive_sentences()}")
        print(text_handler.count_sentences())
        print(text_handler.calculate_sentence_average_length())
        print(text_handler.calculate_word_average_length())
        print(text_handler.calculate_smiles_count())
        c = input("Enter char: ")
        print(text_handler.replace_spaces_wcharacter(c))
        print(text_handler.find_capital_letter(), text_handler.find_lowercase_letter())
        print(text_handler.find_firts_zword_index())
        print(text_handler.remove_awords())

        text_handler.text = "e02fd0e4-00fd-090A-ca30-0d00a0038ba0"
        print(text_handler.validate_guid_string())