import glob
from mrkdwn_analysis import MarkdownAnalyzer

files = sorted(glob.glob("data/*.md"))
topics = [ "Climate Risk Management", "Water Risk Management", "Scope 1", "Scope 2", "Health", "Employees", "Forests"]
data = {}
paragraphs = []

for f in files[:-1]:
    fileParagraphs = MarkdownAnalyzer(f).identify_paragraphs().get('Paragraph')
    paragraphs.extend(fileParagraphs)
    # print(len(fileParagraphs))
# print(len(paragraphs))

for p in paragraphs:
    for topic in topics:
        if topic in p: 
            data[topic] = p

print(f"There are {len(data.values())} relevant paragraphs.")
for key,value in data.items():
    print(f"""  Topic: {key}  
    Paragraph: {value}""")