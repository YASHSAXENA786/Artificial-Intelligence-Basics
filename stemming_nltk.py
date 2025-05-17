#PROGRAM TO IMPLEMENT STEMMING FOR A GIVEN SENTENCE USING NLTK
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
#download nltk data
nltk.download('punkt_tab')


import nltk
def stem_sentence(sentence):
  #Tokenize the sentence into words
  words=word_tokenize(sentence)
  #initialize porter stemmer
  stemmer=PorterStemmer()

  #stem each wordin sentence
  stemmed_words=[stemmer.stem(word) for word in words]

  #join the stemmed words back into a sentence
  stemmed_sentence=' '.join(stemmed_words)

  return stemmed_sentence

#example_usage
sentence="Earth is not our belonging, we have borrowed it from our successors."
stemmed_sentence= stem_sentence(sentence)
print("original Sentence: ",sentence)
print("Stemmed Sentence: ",stemmed_sentence)