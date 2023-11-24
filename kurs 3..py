"""
Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku
"""
import os


def count_words_in(file):
    with open(path) as f:
        content = f.readline()
        words = len(content.split())
    return words


path = r'C:\Users\Maciej\Desktop\myfile.txt'

#if os.path.isfile(path):
#    print(f"{count_words_in(path)}, tyle słów jest w pliku {path}.")

os.path.isfile(path) and print(f"{count_words_in([path])}, tyle słów jest w pliku {path}")

