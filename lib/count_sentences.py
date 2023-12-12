#!/usr/bin/env python3
class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Input must be a string")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string based on '.', '?', and '!'
        sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self.value) if sentence]
        return len(sentences)
