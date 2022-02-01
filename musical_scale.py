# -*- coding: utf-8 -*-
#!/usr/bin/python
# 2022 by Willian Ferreira
# Version 0.1 Beta

# Reference: 
# https://www.descomplicandoamusica.com/escala-menor-natural/
# https://www.descomplicandoamusica.com/escala-menor-melodica/ 
# https://www.descomplicandoamusica.com/escala-menor-harmonica/

import sys

def title():
    print("  __  __           _           _    _____           _      ")
    print(" |  \/  |         (_)         | |  / ____|         | |     ")
    print(" | \  / |_   _ ___ _  ___ __ _| | | (___   ___ __ _| | ___ ")
    print(" | |\/| | | | / __| |/ __/ _` | |  \___ \ / __/ _` | |/ _ |")
    print(" | |  | | |_| \__ \ | (_| (_| | |  ____) | (_| (_| | |  __/")
    print(" |_|  |_|\__,_|___/_|\___\__,_|_| |_____/ \___\__,_|_|\___|\n")
    print("Created by William Ferreira - 2022")
    print("Version 0.1 Beta\n")

def help():

    print("Usage: musical_scale.py [-- Scale] [Note]")
    print("     # Scales available: --major, --natural_minor")
    print("     # Notes available: C, D, E, F, G, A, B\n")
    print("Example 1: musical_scale.py --major G")
    print("Example 2: musical_scale.py --natural_minor B\n")

    sys.exit(1)

def convertNoteToNumber(note_, number_ = False):

	notes_numbers = {'C' : 0, 'D' : 2, 'E' : 4, 'F' : 5, 'G' : 7, 'A' : 9, 'B' : 11}
	accidentals_numbers = {'#' : 1, 'b' : -1, 'bb' : -2}
	
	numbers_notes = {}
	for n in notes_numbers:
		numbers_notes[notes_numbers[n]] = n
	
	numbers_accidentals = {}
	for n in accidentals_numbers:
		numbers_accidentals[accidentals_numbers[n]] = n
		
	if number_:
		if note_ in range(12):
			if note_ in numbers_notes.keys():
				return_note = numbers_notes[note_]
				return return_note
			else:
				return_note = numbers_notes[note_ + accidentals_numbers['#']] + numbers_accidentals[1]
				return return_note	
		else:
			return None
		
	elif not number_:

		if note_[0] in notes_numbers.keys():
			if len(note_) == 1:
				return_number = notes_numbers[note_]
			elif len(note_) > 1:
				return_number = notes_numbers[note_[0]] + accidentals_numbers[note_[1:]]
			if return_number < 0:
				return_number = return_number + 12	
			return return_number
			
		else:
			return None

def generateScale(note, scale, return_numbers = False):

    note = convertNoteToNumber(note)

    notes = {
		'sharps' : ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
		'flats' : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
	};

    scales = {
		'--major' : [2, 2, 1, 2, 2, 2],
		'--natural_minor' : [2, 1, 2, 2, 1, 2],
		#'--harmonic_minor' : [2, 1, 2, 2, 1, 3],
		#'--melodic_minor' : [2, 1, 2, 2, 2, 2, 1, -2, -2, -1, -2, -2, -1, -2]
	}

    if scales[scale] == scales['--major']:
        if note in [1, 3, 5, 8, 10]:
            notes_array = notes['flats']
        else:
            notes_array = notes['sharps']
    else:
        if note in [0, 1, 2, 3, 5, 7, 8, 10]:
            notes_array = notes['flats']
        else:
            notes_array = notes['sharps']
    
    return_scale = []	
    start_reference = []
    total = 0
    
    for i in range(len(scales[scale])+1):
    		
            if i < len(scales[scale]):
                total += scales[scale][i]	
                
            start_reference.append(total)

            if i == 0:
                current_note = note
            else:
                current_note = note + start_reference[i - 1]

            if current_note >= len(notes_array):
                current_note = current_note - 12  
            if not return_numbers:
                return_scale.append(notes_array[current_note])    
            elif return_numbers:
                return_scale.append(convertNoteToNumber(notes_array[current_note]))    
            else:
                return None

    return return_scale

def main():

    title()

    try:
        args = sys.argv[1:]
        if not args:
            print("You must inform the note to be generated in the scale.\n Use --help or -h for more information.")
            sys.exit(1)

        if args[0] in ["--natural_minor"] and  args[1] in ["C", "D", "E", "F", "G", "A", "B"]:
            print("{} minor scale".format(args[1]))
            print(generateScale(args[1], args[0]))
            sys.exit(1)
        
        elif args[0] in ["--major"] and args[1] in ["C", "D", "E", "F", "G", "A", "B"]:
            print("{} major scale".format(args[1]))
            print(generateScale(args[1], args[0]))
            sys.exit(1)
        elif args[0] in ["--help", "-h"]:
            help()
        else:
            print("Invalid information. Use --help or -h for more information.")
            sys.exit(1)
    except Exception as e:
        print("Unexpected error identified. Please contact the administrator. Error: {}".format(e))
        sys.exit(1)
    
if __name__ == '__main__':
	main()