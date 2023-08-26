#!/usr/bin/env python3

class MyString:
    def __init__(self,value):
        if isinstance(value, str):
          self.value = value
        else:
            print("value must be a string")
        
    def is_sentence(self):
        if self.value.endswith("."):
            print("this is a sentence")
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False
        
        
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False
        
    def count_sentences(self):
               # Replace variations of sentence-ending punctuation with a period
        cleaned_value = self.value.replace("?", ".").replace("!", ".")

        # Split the cleaned string using a period as the separator
        sentences = cleaned_value.split(".")

        # Remove empty strings from the list
        valid_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        return len(valid_sentences)
        


answer = MyString("this is a string.")
answer.is_sentence()
