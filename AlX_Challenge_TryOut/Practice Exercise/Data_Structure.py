from random import random

fruits = ["apple", "banana", "pineapple", "gripes","mango"]

print(fruits[1])

book = {
        'title': 'Purpose of Life',
        'author':'John C Maxwell',
        'genre': 'growth'
}

print(len(book))

def get_value(d,k):
    for key in d:
        if key == k:
            print(d[key])


get_value(book, 'genre')


books_dic = {
    'book_1' : {
        'title': 'Purpose of Life',
        'author':'John C Maxwell',
        'genre': ''
    }
}


def get_2d_value(data_dic, key_lookup):
    for key in data_dic:
        if key == key_lookup:
            print(data_dic[key])
        else:
            for k in data_dic[key]:
                if k == key_lookup:
                    print(data_dic[key][k])


get_2d_value(books_dic,'author')
