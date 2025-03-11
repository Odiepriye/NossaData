import glob
from mrkdwn_analysis import MarkdownAnalyzer

files = sorted(glob.glob("data/*.md"))

def trueString(str):
    return any(char.isalpha() or char.isdigit() for char in str)

def countWords(file):
    with open(file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    words = content.split()
    words = [w for w in words if trueString(w)]
    print(len(words))

for f in files[:-2]:
    # print(MarkdownAnalyzer(f).analyse().get('words')) #Libraries words
    print(MarkdownAnalyzer(f).count_words()) #Libraries words
    countWords(f) #true words