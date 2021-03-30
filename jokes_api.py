import json
import re
import random


def generate_jokes():
    joke_list = []
    match = re.compile(r'\d{1,2}\.')

    with open('jokes.txt', 'r') as file:
        answer = True
        while answer:
            question = file.readline()
            answer = file.readline()
            question = re.sub(match, "", question)
            joke = {
                "question": question.strip(),
                "answer": answer.strip()
            }
            joke_list.append(joke)

    with open('jokes.json', 'w') as file:
        json.dump(joke_list, file)


with open('jokes.json', 'r') as file:
    joke_list = json.load(file)


def get_random_joke():
    joke = random.choice(joke_list)
    return joke["question"], joke["answer"]
