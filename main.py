import re
import string

from pathlib import Path


def read_text_file(f: str | Path) -> str:
    file = Path(f)
    with file.open("r", encoding="utf-8") as stream:
        return stream.read()


def split_words(w: str) -> list[str]:
    words = re.split(r"\s+", w.strip())
    return [word for word in words if word]


def total_words(w: str) -> int:
    return len(split_words(w))


def count_words(w: str) -> dict[str, int]:
    data = {}
    for word in split_words(w.lower()):
        if word not in data.keys():
            data[word] = 0
        elif word in data.keys():
            data[word] += 1
    return data


def count_letters(w: str) -> dict[str, int]:
    data = {}
    text = w.lower()
    for letter in string.ascii_lowercase:
        if letter not in data:
            data[letter] = 0
        for t in text:
            if t == letter:
                data[letter] += 1
    return data


def main() -> str:
    filepath = "books/frankenstein.txt"
    text = read_text_file(filepath)
    twords = total_words(text)
    cwords = count_words(text)
    cletters = count_letters(text)
    print("Total words: ", twords)
    print("Number of times 'monster' mentioned: ", cwords["monster"])
    print("Frequency of letter occurence: ", cletters)
    return text


if __name__ == "__main__":
    main()
