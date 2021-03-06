#First - The Purely Random Word Generator
import random

#Function to set the settings of the conlang
def set_values():
    print 'Set Values:\n'
    passval = 0
    while passval == 0:
        phones = raw_input('What phones would you like to use?')
        if phones == 'help':
            print '\nA phone is a distinct speech sound or gesture. Phones are usually either vowels or consonants, but your conlang can have different ones'
            print 'Please try again'
        else:
            phones = list(phones)
            global phones
            passval = 1

    passval = 0
    while passval == 0:
        syllable_types = raw_input('Enter the syllable types. Enter help if you need help.')
        if syllable_types == 'help':
            print 'Please seperate groupings with spaces. E.g CVVC for [consonant][vowedl][vowel][consonant] word \nAn example entry would be something like: CVVC CVC CCCVV VVCC'
        else:
            syllable_types = syllable_types.split()
            global syllable_types
            passval = 1

    passval = 0
    while passval == 0:
        categories = {}
        for key in phones:
            templetters = raw_input('Enter your letters for the category: ' + key + ' or type help if you need help')
            if templetters == 'help':
                print 'Categories are phonological classes defined by enumeration. For example, you might define consonants like this: consonants=bcdfg. This means that every time a consonant is called ConGen will randomely select either b,c,d,f or g. The key here is that order determines probability. The default dropoff is 30%, which means that ConGen runs through each letter and has a 30 percent chance of stopping at every letter.'
            else:
                categories[key] = templetters
                categories[key] = list(categories[key])
                global categories
                passval = 1

    passval = 0
    while passval == 0:
        dropoff = raw_input('Enter the dropoff value on a scale of 1-5 with 5 being the slowest. Enter help if you need help.')
        if dropoff == 'help':
            print 'Dropoff determines how fast the power law declines. The average dropoff value is 30 or 30%. If you have consonants = ptkdgd then when calling a C, P will come up the most, followed by t, k, and so forth'
        else:
            global dropoff
            passval = 1

    print 'Here are your current settings:\n'
    print 'Phones:' + str(phones)
    print 'Syllable_types: ' + str(syllable_types)
    print 'Categories: ' + str(categories)
    print 'Dropoff: ' + str(dropoff)

phones = ['c','v']
syllable_types = ['cvc','vcc']
categories = {'c' : ['w','i','l','l'], 'v' : ['c','h','r','i','s']}
dropoff = 30

#Function to generate a word list or table
def generate():
    syllable_dict = {}
    wordlist = []
    wordnum = input('How many words would you like to generate?')
    wordnum = int(wordnum)

    #runs for every word
    for i in range(wordnum):
        word = []
        
        #runs for every syllable in the word
        for x in range(random.randint(0,3)):
            letters = []
            syllable_type = random.choice(syllable_types)
            syllable_type = list(syllable_type)
            for j in syllable_type:
                letters.append(random.choice(categories[j]))
                word.append(''.join(letters))

'''
while True:
    print '\n1. Set values (word generation parameters)'
    print '2. Generate word list'
    print '3. Exit the program'
    menuchoice = raw_input('\nWhich would you like to do?')
    menuchoice = int(menuchoice)

    if menuchoice == 1:
        set_values()
    elif menuchoice == 2:
        generate()
    elif menuchoice == 3:
        exit()

'''


