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




if __name__ == "__main__":
    
    DicOfWords = create_dictionary()
    print(DicOfWords[110])
    
