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




if __name__ == "__main__":
    
    DicOfWords = create_dictionary()
    Dic_sorted = words_sorted_by_word_height(DicOfWords)
    for key in Dic_sorted.keys():
        print(key,  " " , len(Dic_sorted[key]))

