from re import split
import textstat
from nltk.corpus import words
from transformers import pipeline

nlp = pipeline("fill-mask")

def makeEasy(paragraph):
    wordList = split('[^a-zA-Z]', paragraph)
    for word in wordList:
        if word in words.words() and int(textstat.difficult_words(word)) == 1:
            preds = nlp(paragraph.replace(word,'<mask>'))
            new_paragraphs = []
            ease_levels = []
            for p in preds:
                w=str(nlp.tokenizer.decode([p['token']])).strip()
                s = paragraph.replace(word,w)
                e= float(textstat.flesch_reading_ease(s))
                if w in words.words() and e>=0:
                    s = paragraph.replace(word,w )
                    new_paragraphs.append(s)
                    ease_levels.append(e)
            if len(new_paragraphs)>0:
                paragraph=new_paragraphs[ease_levels.index(max(ease_levels))]
    return paragraph

paragraph="How to get to the top of that mountain???"
#print(paragraph.replace("mountain","aaaa"))
print(makeEasy(paragraph))