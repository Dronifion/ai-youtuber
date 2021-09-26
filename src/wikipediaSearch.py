import wikipedia as wiki

while True:
    myInput = input("Question: ")
    print(wiki.summary(str(myInput)))