import json
import collections


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    with open(file_path, 'r', encoding='utf8') as f:
        data = json.load(f)

    news_list = data['rss']['channel']['items']
    all_words = []
    for row in news_list:
        all_words.append(row['description'].split())
    big_words = []
    for word in all_words:
        for letter in word:
            if len(letter) > word_max_len:
                big_words.append(letter)

    word_count = collections.Counter(big_words)
    top_words = [word for word, count in word_count.most_common(top_words_amt)]
    return (top_words)


if __name__ == '__main__':
    print(read_json('newsafr.json'))

import requests