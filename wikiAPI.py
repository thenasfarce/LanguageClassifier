import wikipedia
import string

articleListTrain = ["Facebook","Twitter","George W. Bush","Donald Trump"]
articleListTest = ["Martin Luther", "IBM", "Google", "Radiohead", "Ronald Reagan", "Tumblr"]
languageList = ["en","fr","es","it","de"]

for lang in languageList:
    wikipedia.set_lang(lang)
    print(lang)

    for page in articleListTrain:
        content = wikipedia.page(page).content
        content = content.lower()
        translator = str.maketrans({key: None for key in string.punctuation})
        content = content.translate(str.maketrans(translator))
        with open("/Users/michael/Desktop/wikitrain/"+page+"_"+lang+".txt", "w") as f:
            f.write(content)
    for page in articleListTest:
        content = wikipedia.page(page).content
        content = content.lower()
        translator = str.maketrans({key: None for key in string.punctuation})
        content = content.translate(str.maketrans(translator))
        with open("/Users/michael/Desktop/wikitest/"+page+"_"+lang+".txt", "w") as f:
            f.write(content)

