from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def find_keyword_sentence(str):
    icnt = 0
    keyword = ''
    for element in str:
        if element == ' ':
            icnt = icnt+1
    
    if(icnt==1):
        keyword = str
    else:
        text_tokens = word_tokenize(str)
        lectures = [word for word in text_tokens if not word in stopwords.words()]
        #print(lectures)
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(lectures)
        indices = np.argsort(vectorizer.idf_)[::-1]
        features = vectorizer.get_feature_names()
        top_n = 1
        top_features = [features[i] for i in reversed(indices[:top_n])]
        #print(top_features)
        str1=""
        for element in top_features: 
            str1 += element

        keyword = str1
        #print(str1)
        #return str1
    return keyword        
def main():
    print("Enter the sentence:")
    str = input()
    ret = find_keyword_sentence(str)
    print(ret)

if __name__ == '__main__':
    main()        
