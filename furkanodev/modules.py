# modules.py
import string
from collections import Counter

def info():
    print("Ad: Furkan")
    print("Soyad: Savaş")
    print("Öğrenci Numarası: 211213074")
    print("Python > all")

def is_letter(character):
    return character.isalpha()

def to_lowercase(letter):
    return letter.lower() if letter.isupper() else letter

def text_frequency_analysis(text):
    text = ''.join(filter(is_letter, text.lower()))
    char_count = Counter(text)
    total_chars = sum(char_count.values())
    return {char: count / total_chars for char, count in char_count.items()}

    
    