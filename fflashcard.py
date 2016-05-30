import os, random

done = False

def flashquiz():
    count = 0
    score = 0

    file1 = open('english.txt', 'r')
    file2 = open('french.txt', 'r')

    f1content = file1.readlines()
    f2content = file2.readlines()

    while count < 10:
        os.system('clear')
    
        wordnum = random.randint(0, len(f1content)-1)
    
        print 'Word:', f1content[wordnum], ''
    
        options = [random.randint(0, len(f2content)-1),
            random.randint(0, len(f2content)-1),
            random.randint(0, len(f2content)-1)]
    
        options[random.randint(0, 2)] = wordnum
    
        print '1 -', f2content[options[0]],
        print '2 -', f2content[options[1]],
        print '3 -', f2content[options[2]],
    
        answer = input('\nYour choice: ')
    
        if options[answer-1] == wordnum:
            raw_input('\nCorrect! Hit enter...')
            score = score + 1
        else:
            raw_input('\nWrong! Hit enter...')
    
        count = count + 1
    
    print '\nYour score is:', score

def addwords():
    print "What is the English word to be added?"
    engword = raw_input()
    print "And what is its French equivalent?"
    freword = raw_input()
    print "Adding %r -- and %r." % (engword, freword)

    fh = open("english.txt", "a")
    fh.write("\n" "%r" % engword)
    fh.close
    
    fh = open("french.txt", "a")
    fh.write("\n" "%r" % freword)
    fh.close

while not done:
    print "Welcome to flashcard."
    print "1 - Quiz"
    print "2 - Add words"
    print "3 - Quit"
    
    choice = raw_input("> ")
    if choice == "1":
        flashquiz()
    elif choice == "2":
        addwords()
    elif choice == "3":
        done = True
    else:
        print "Please enter a valid command."
