import argparse

runewords = {"Ancient's Pledge": ["Ral","Ort","Tal"],
"Beast": ["Ber","Tir","Um","Mal","Lum"],
"dummyDoppelt": ["Tir","Tir","Vex"],
"dummyGross": ["tir", "Um", "eTh"]}

def findRuneworts(runes):
    return ['Spirit']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--runes', nargs='+', help='<Required> List of runes', required=True)

    args = parser.parse_args()
    runes = args.runes

    possibleRuneWords = findRuneworts(runes)
    print possibleRuneWords
