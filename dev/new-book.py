# Routine to add a new book 

# TODO: add input checking

title = input("book title: ").lower()
numChapters = int(input("number of chapters (numerical answers only): "))
chapterList = range(numChapters)

for chapter in range(numChapters):

    numSections = int(input("How many sections are in chapter " + str(chapter + 1) + "? "))
    sectionList = list(range(1, numSections))

    for section in range(numSections):
        
        numProblems = int(input("How many problems are in section " + str(section + 1) + "? "))
        problemList = list(range(1, numProblems))
        sectionList[section] = problemList

    chapterList[chapter] = sectionList
    