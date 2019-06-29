import argparse

verbose = False

runewords = {
"dummyDoppelt": ["Tir","Tir","Vex"],
"dummyGross": ["tir","sol","eTh"],
"dummyUmUmUm": ["um","um","um"],
"Ancient's Pledge": ["Ral","Ort","Tal"],
"Beast": ["Ber","Tir","Um","Mal","Lum"],
"Black": ["Thul","Io","Nef"],
"Bone": ["Sol","Um","Um"],
"Bramble": ["Ral","Ohm","Sur","Eth"],
"Brand": ["Jah","Lo","Mal","Gul"],
"Breath of the Dying": ["Vex","Hel","El","Eld","Zod","Eth"],
"Call to Arms": ["Amn","Ral","Mal","Ist","Ohm"],
"Chains of Honor": ["Dol","Um","Ber","Ist"],
"Chaos": ["Fal","Ohm","Um"],
"Crescent Moon": ["Shael","Um","Tir"],
"Death": ["Hel","El","Vex","Ort","Gul"],
"Delirium": ["Lem","Ist","Io"],
"Destruction": ["Vex","Lo","Ber","Jah","Ko"],
"Doom": ["Hel","Ohm","Um","Lo","Cham"],
"Dragon": ["Sur","Lo","Sol"],
"Dream": ["Io","Jah","Pul"],
"Duress": ["Shael","Um","Thul"],
"Edge": ["Tir","Tal","Amn"],
"Enigma": ["Jah","Ith","Ber"],
"Enlightenment": ["Pul","Ral","Sol"],
"Eternity": ["Amn","Ber","Ist","Sol","Sur"],
"Exile": ["Vex","Ohm","Ist","Dol"],
"Faith": ["Ohm","Jah","Lem","Eld"],
"Famine": ["Fal","Ohm","Ort","Jah"],
"Fortitude": ["El","Sol","Dol","Lo"],
"Fury": ["Jah","Gul","Eth"],
"Gloom": ["Fal","Um","Pul"],
"Grief": ["Eth","Tir","Lo","Mal","Ral"],
"Hand of Justice": ["Sur","Cham","Amn","Lo"],
"Harmony": ["Tir","Ith","Sol","Ko"],
"Heart of the Oak": ["Ko","Vex","Pul","Thul"],
"Holy Thunder": ["Eth","Ral","Ort","Tal"],
"Honor": ["Amn","El","Ith","Tir","Sol"],
"Ice": ["Amn","Shael","Jah","Lo"],
"Infinity": ["Ber","Mal","Ber","Ist"],
"Insight": ["Ral","Tir","Tal","Sol"],
"King's Grace": ["Amn","Ral","Thul" ],
"Kingslayer": ["Mal","Um","Gul","Fal"],
"Last Wish": ["Jah","Mal","Jah","Sur","Jah","Ber"],
"Lawbringer": ["Amn","Lem","Ko"],
"Leaf": ["Tir","Ral"],
"Lionheart": ["Hel","Lum","Fal"],
"Lore": ["Ort","Sol"],
"Malice": ["Ith","El","Eth" ],
"Melody": ["Shael","Ko","Nef"],
"Memory": ["Lum","Io","Sol","Eth"],
"Myth": ["Hel","Amn","Nef"],
"Nadir": ["Nef","Tir"],
"Oath": ["Shael","Pul","Mal","Lum"],
"Obedience": ["Hel","Ko","Thul","Eth","Fal"],
"Passion": ["Dol","Ort","Eld","Lem"],
"Peace": ["Shael","Thul","Amn"],
"Phoenix": ["Vex","Vex","Lo","Jah"],
"Pride": ["Cham","Sur","Io","Lo"],
"Principle": ["Ral","Gul","Eld"],
"Prudence": ["Mal","Tir"],
"Radiance": ["Nef","Sol","Ith"],
"Rain": ["Ort","Mal","Ith"],
"Rhyme": ["Shael","Eth"],
"Rift": ["Hel","Ko","Lem","Gul"],
"Sanctuary": ["Ko","Ko","Mal"],
"Silence": ["Dol","Eld","Hel","Ist","Tir","Vex" ],
"Smoke": ["Nef","Lum"],
"Spirit": ["Tal","Thul","Ort","Amn"],
"Splendor": ["Eth","Lum"],
"Stealth": ["Tal","Eth"],
"Steel": ["Tir","El"],
"Stone": ["Shael","Um","Pul","Lum"],
"Strength": ["Amn","Tir"],
"Treachery": ["Shael","Thul","Lem"],
"Venom": ["Tal","Dol","Mal"],
"Voice of Reason": ["Lem","Ko","El","Eld"],
"Wealth": ["Lem","Ko","Tir"],
"White": ["Dol","Io"],
"Wind": ["Sur","El"],
"Wrath": ["Pul","Lum","Ber","Mal"],
"Zephyr": ["Ort","Eth"]
}

def findRuneworts(runes):
    runesLower = [r.lower() for r in runes]
    if verbose:
        print "stash: " + str(runesLower)
    foundWords = []
    for name,letters in runewords.iteritems():
        lettersLower = [l.lower() for l in letters]
        result =  all(elem in runesLower for elem in lettersLower) #and all(elem in lettersLower for elem in runesLower)
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
    if verbose:
        print "*"*50
    for rw in possibleRuneWords:
        print rw + ": " + str(runewords[rw])
