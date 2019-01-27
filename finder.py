import argparse

verbose = False

runewords = {"Ancient's Pledge": ["Ral","Ort","Tal"],
"Beast": ["Ber","Tir","Um","Mal","Lum"],
"dummyDoppelt": ["Tir","Tir","Vex"],
"dummyGross": ["tir","sol","eTh"],
"dummyUmUmUm": ["um","um","um"]}

def findRuneworts(runes):
    runesLower = [r.lower() for r in runes]
    if verbose:
        print "stash: " + str(runesLower)
    foundWords = []
    for name,letters in runewords.iteritems():
        lettersLower = [l.lower() for l in letters]
        result =  all(elem in runesLower for elem in lettersLower) and all(elem in lettersLower for elem in runesLower)
        if verbose:
            print "checking " + str(lettersLower) + ": " + str(result)
        if result:
            foundWords.append(name)
    return foundWords

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--runes', nargs='+', help='<Required> List of runes', required=True)
    parser.add_argument('-v','--verbose', help='increase output verbosity', action='store_true')
    args = parser.parse_args()
    runes = args.runes
    verbose = args.verbose
    possibleRuneWords = findRuneworts(runes)
    for rw in possibleRuneWords:
        print rw + ": " + str(runewords[rw])
