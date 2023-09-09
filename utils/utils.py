import math
import random


def get_main_words(text: str):
    words = text.split(" ")

    count_words = math.ceil(len(words) / 4)

    count_positive = math.ceil(count_words / 2)
    count_negative = math.ceil(count_words / 2)

    positive = []
    negative = []

    for i in range(count_positive):
        word = random.choice(words)
        positive.append(word)

    for i in range(count_negative):
        word = random.choice(words)
        negative.append(word)

    return positive, negative
