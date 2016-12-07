#First - The Purely Random Word Generator
#v1.0 based on Zompist's Gen
#import random

#dropoff = "" # Dropoff determines how fast the power law declines. If you have consonants = ptkdgd then when calling a C, P will come up the most, followed by t, k, and so forth
#monosyllables = "" #This tells the program how much of the output should be monosyllables

print 'Settings:'

def generate():
    passval = 0
    while passval == 0:
        phones = raw_input('What phones would you like to use?')
        if phones == 'help':
            print '\nA phone is a distinct speech sound or gesture. Phones are usually either vowels or consonants, but your conlang can have different ones'
            print 'Please try again'
        else:
            phones = list(phones)
            passval = 1

    passval = 0
    while passval == 0:
        syllable_types = raw_input('Enter the syllable types. Enter help if you need help.')
        if syllable_types == 'help':
            print 'Please seperate groupings with spaces. E.g CVVC for [consonant][vowedl][vowel][consonant] word \nAn example entry would be something like: CVVC CVC CCCVV VVCC'
        else:
            syllable_types = syllable_types.split()
            passval = 1

    passval = 0
    while passval == 0:
        categories = raw_input('Enter your categories. Enter help if you need help.')
        if categories == 'help':
            print 'Categories are phonological classes defined by enumeration. For example, you might define consonants like this: consonants=bcdfg. This means that every time a consonant is called ConGen will randomely select either b,c,d,f or g. The key here is that order determines probability. The default dropoff is 30%, which means that ConGen runs through each letter and has a 30 percent chance of stopping at every letter.'
        else:
            categories1 = categories.split()
            categories2 = categories.something

    passval = 0
    while passval == 0:
        dropoff = raw_input('Enter the dropoff value on a scale of 1-5 with 5 being the slowest. Enter help if you need help.')
        if dropoff == 'help':
            print 'Dropoff determines how fast the power law declines. If you have consonants = ptkdgd then when calling a C, P will come up the most, followed by t, k, and so forth'
        else:
            passval = 1
generate()

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

    

#Function to generate a word list or table
def generate():
    wordlist = {}
    wordnum = input('How many words would you like to generate?')
    wordnum = int(wordnum)
    
    for i in range(wordnum):
        word = ''
        syllable_type = random.choice(syllable_types)
        syllable_type = list(syllable_type)
        print syllable_type
        

           
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
