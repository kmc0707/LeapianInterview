from statistics import median

from sympy import total_degree
from dataset import data
from word_class import Word

def create_dictionary():
    DicOfWords = {}
    for set in data:
        if set != data[0]:
            word = Word(
            int(set[0]),
            int(set[1]),
            int(set[2]),
            float(set[3]),
            float(set[4]),
            float(set[5]),
            round(float(set[6])),
            set[7]
            )
            DicOfWords[int(set[1])] = word
    return DicOfWords

def words_sorted_by_word_height(DicOfWords):
    array_of_words=DicOfWords.values()
    Dic_sorted = {}
    for word in array_of_words:
        if word.wordHeight in Dic_sorted:
            Dic_sorted[word.wordHeight].append(word)
        else:
            Dic_sorted[word.wordHeight] = [word]
    return Dic_sorted

def words_sorted_by_y_coordinate(DicOfWords,key):
    array_of_words=DicOfWords[key]
    Dic_sorted = {}
    for word in array_of_words:
        if word.wordY in Dic_sorted:
            Dic_sorted[word.wordY].append(word)
        else:
            Dic_sorted[word.wordY] = [word]
    return Dic_sorted


def mmm_y_axis(DicOfWords):
    highest_num = -1
    mode = -1
    total = 0
    mean = -1
    highest = -1
    lowest = -1
    median = -1
    for key in DicOfWords.keys():
        total += len(DicOfWords[key])
        mean += len(DicOfWords[key]) * key
        if len(DicOfWords[key]) > highest_num:
            highest_num = len(DicOfWords[key])
            mode = key
        if key > highest:
            highest = key
        if key < lowest:
            lowest = key
    median = (highest - lowest)/2
    mean = mean/total
    print("meadian: " , median, " mode: ", mode, " mean: ", mean)


def words_sorted_by_y_axis_and_x_axis(DicOfWords):
    for key in DicOfWords.keys():
        DicOfWords[key].sort(key=lambda x: x.wordX)
    return DicOfWords

def mmm_x_axis(DicOfWords):
    for key in DicOfWords.keys():
        total = 0
        mean = -1
        median = -1
        x_array = DicOfWords[key]
        highest = x_array[len(x_array)-1].wordX
        lowest = x_array[0].wordX
        for value in x_array:
            total += 1
            mean += value.wordX
        median = (highest - lowest)/2
        mean = mean/total
        print("y line: " , key, "meadian: " , median, " mean: ", mean)
    
if __name__ == "__main__":
    
    DicOfWords = create_dictionary()
    Dic_sorted = words_sorted_by_word_height(DicOfWords)
    for key in Dic_sorted.keys():
        print(key,  " " , len(Dic_sorted[key]))
    Dic_sorted_y = words_sorted_by_y_coordinate(Dic_sorted,8)
    mmm_y_axis(Dic_sorted_y)
    x = words_sorted_by_y_axis_and_x_axis(Dic_sorted_y)
    mmm_x_axis(x)

