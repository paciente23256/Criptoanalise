#!/usr/bin/python3

"""
    vigenere.py - Vigenere tool, can use statistical analysis to guess keys of varying length for enciphered text

    Options:
        --encrypt - enable encryption mode
        --decrypt - enable decryption mode
        --preserve-spacing - preserve the spacing of the input in the output
        --key - specify the encryption key
        --spacing - specify the output spacing
        --guess - attempt to guess the encryption key by statistical analysis

    Todo:
        - Implement n-gram analysis to improve accuracy of key guesses
        - Perform frequency analysis of deciphered text to improve accuracy of key guesses
    Future:
        - Add support for multiple languages
        - Include standard deviations for each letter frequency
        - Get better numbers for frequency analysis
"""

import argparse
import re
import string
from itertools import cycle

def buildSubStrings(string, seperation): # Build all substrings required to analyse the polyalphabetic cipher
    return [string[i::seperation] for i in range(seperation)]

def frequencyAnalysis(string): # Normalised frequency analysis
    freq = [0] * 26

    for c in string:
        freq[ord(c) - ord('A')] += 1

    total = sum(freq)

    for i in range(0, len(freq)):
        freq[i] /= (float(total) / 100)

    return freq

def initialiseParser():
    parser = argparse.ArgumentParser(description = "Encrypt or decrpyt a string using the Caesar Cipher")

    parser.add_argument("--encrypt", "--enc", "-e", help = "encryption mode (default)", action = "store_true")
    parser.add_argument("--decrypt", "--dec", "-d", help = "decryption mode", action = "store_true")
    parser.add_argument("--preserve-spacing", "--preserve", "-p", help = "use same spacing as the input text", action = "store_true", dest = "preserveSpacing")
    parser.add_argument("--key", "-k", help = "encryption key for vigenere cipher", type = str)
    parser.add_argument("--spacing", "-s", help = "specify the spacing in output", type = int)
    parser.add_argument("--guess", "-g", help = "Attempt to guess the most likely key value", action = "store_true")

    return parser

def scoreCalculator(frequencyAnalysis, shift): # Calculates a weighted score for a given shift value
    englishFrequencies = [  8.167, 1.492, 2.782,
                            4.253, 12.702, 2.228,
                            2.015, 6.094, 6.966,
                            0.153, 0.772, 4.025,
                            2.406, 6.749, 7.507,
                            1.929, 0.095, 5.987,
                            6.327, 9.056, 2.758,
                            0.978, 2.360, 0.150,
                            1.974, 0.074 ]

    score = 0

    for index in range(0, 26):
        shiftIndex = (index + shift) % 26
        score += abs(frequencyAnalysis[index] - englishFrequencies[shiftIndex])

    return score / 26

def shiftCalculator(frequencyAnalysis): # Calculates the most likely shift value for a substring by comparing weighted scores of different shift values
    bestGuess = ''
    bestGuessScore = float('inf')

    for shift in range(1, 27):
        score = scoreCalculator(frequencyAnalysis, shift)

        if score < bestGuessScore:
            bestGuessScore = score
            bestGuess = chr(ord('Z') - shift + 1)

    return bestGuess

def stringPrepare(string, preserveSpacing): # Strip all non alphabetic characters from a string and convert to upper case
    if preserveSpacing == True:
        regex = '[^A-Z\s]'
    else:
        regex = '[^A-Z]'

    return re.compile(regex).sub('', string).upper()

def vigenere(plaintext, key, encrypt):
    alphabet = string.ascii_uppercase
    output = ''
    shift = 1

    if encrypt == False:
        shift = -1

    for x, y in zip(stringPrepare(plaintext, False).upper(), cycle(key.upper())):
        output += alphabet[(alphabet.index(x) + alphabet.index(y) * shift) % 26]

    return output

def main():
    parser = initialiseParser()
    args = parser.parse_args()
    rawText = stringPrepare(str.upper(input('')), True)
    strippedText = stringPrepare(rawText, False)

    if args.decrypt or args.encrypt:
        if(args.key != None):
            output = vigenere(strippedText, args.key, args.encrypt)
        else:
            print("Error: No key given!")
    elif args.guess:
        maxGuess = 30 if len(strippedText) > 30 else len(strippedText)
        keyList = list()

        for guess in range(2, maxGuess):
            substringList = buildSubStrings(strippedText, guess)
            frequencyAnalysisList = list()
            key = ''

            for subString in substringList:
                frequencyAnalysisList.append(frequencyAnalysis(subString))

            for frequency in frequencyAnalysisList:
                key += shiftCalculator(frequency)

            keyList.append(key)

        bestGuess = ''
        bestGuessScore = float('inf')

        for key in keyList:
            score = scoreCalculator(frequencyAnalysis(str.upper(vigenere(strippedText, key, False))), 0)

            if score < bestGuessScore:
                bestGuessScore = score
                bestGuess = key

        print("Best key guess: %s\nAttepting decryption..." % bestGuess)
        output = vigenere(strippedText, bestGuess, False)

    if args.preserveSpacing:
        for x in range(0, len(rawText)):
            if rawText[x] == ' ':
                output = output[:x] + ' ' + output[x:] # Reinsert the stripped spaces back into the output
    elif args.spacing:
        if args.spacing > 0:
            output = ' '.join([output[i:i + args.spacing] for i in range(0, len(output), args.spacing)])

    print(output)

if __name__ == "__main__":
    main()