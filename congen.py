#First - The Purely Random Word Generator
#v1.0 based on Zompist's Gen
import random

categories = {} #Phonology classes such as C=f,s,d,w if you want your C (consonants) to be f,s,d and w
syllable_types = [] #E.g CVVC for [consonant][vowedl][vowel][consonant] word
dropoff = "" # Dropoff determines how fast the power law declines. If you have consonants = ptkdgd then when calling a C, P will come up the most, followed by t, k, and so forth
monosyllables = "" #This tells the program how much of the output should be monosyllables
