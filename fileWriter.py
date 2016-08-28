import csv
import os

    #counts number of characters
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

    #creates csv
with open("/Users/michael/Desktop/counttrain.csv", "w") as csvfile:
    charset = "abcdefghijklmnopqrstuvwxyz"
    writer = csv.writer(csvfile)
    writer.writerow(charset)

    #iterates through files in folder
    for filename in os.listdir("/Users/michael/Desktop/wikitrain"):
        if filename != ".DS_Store":
            print(filename)
            #opens text file
            with open("/Users/michael/Desktop/wikitrain/"+filename, "r") as f:
                text = f.read()
                #populates a list with character percentages then writes to csv
                list = []
                for x in charset:
                    percent = round(100 * count_char(text, x) / len(text), 2)
                    list.append(percent)
                if "_en" in filename:
                    list.append("english")
                elif "_de" in filename:
                    list.append("german")
                elif "_it" in filename:
                    list.append("italian")
                elif "_es" in filename:
                    list.append("spanish")
                elif "_fr" in filename:
                    list.append("french")
                list.append(filename)
                writer.writerow(list)

with open("/Users/michael/Desktop/counttest.csv", "w") as csvfile:
    charset = "abcdefghijklmnopqrstuvwxyz"
    writer = csv.writer(csvfile)
    writer.writerow(charset)

    #iterates through files in folder
    for filename in os.listdir("/Users/michael/Desktop/wikitest"):
        if filename != ".DS_Store":
            print(filename)
            #opens text file
            with open("/Users/michael/Desktop/wikitest/"+filename, "r") as f:
                text = f.read()
                #populates a list with character percentages then writes to csv
                list = []
                for x in charset:
                    percent = round(100 * count_char(text, x) / len(text), 2)
                    list.append(percent)
                if "_en" in filename:
                    list.append("english")
                elif "_de" in filename:
                    list.append("german")
                elif "_it" in filename:
                    list.append("italian")
                elif "_es" in filename:
                    list.append("spanish")
                elif "_fr" in filename:
                    list.append("french")
                list.append(filename)
                writer.writerow(list)