

def data(word):

    try:
        with open(word, 'r', encoding='latin1') as f:
            text = f.read()
            print("Data loaded")
        return text
    except FileNotFoundError:
        print("Data not loaded")
        return None
    
   
def cleaned_words():
    
    text = data('../data/aceventura.txt')
    for word in text.split():
        cleaned_word = ''.join(char for char in word if char.isalnum())
        print(cleaned_word.lower()) 

def top3wordcount():
    text = data('../data/aceventura.txt')
    word_count = {}
    for lines in text:
        words = lines.split()

        for word in words:
            word = word.lower().strip('.,!?;"()[]')
            word_count[word] = word_count.get(word, 0) + 1


    top3 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
    
    print("Top 3 most frequent words:")
    for word, count in top3:
        print(f"{word}: {count} times") 
    

    return word_count



    
    
data('../data/aceventura.txt')

cleaned_words()
print(top3wordcount())

