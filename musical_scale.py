# -*- coding: utf-8 -*-
#!/usr/bin/python
# 2022 by Willian Ferreira
# Version 0.2

# Reference: 
# https://www.descomplicandoamusica.com/escala-menor-natural/
# https://www.descomplicandoamusica.com/escala-menor-melodica/ 
# https://www.descomplicandoamusica.com/escala-menor-harmonica/

import argparse
import os
import sys

VERSION = "0.2"
NOTES = ("C", "D", "E", "F", "G", "A", "B")
ANSI_COLORS = {
    "bold": "\033[1m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "yellow": "\033[33m",
    "reset": "\033[0m",
}


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate major and natural minor scales.",
        epilog=(
            "Examples:\n"
            "  python musical_scale.py --scale major C\n"
            "  python musical_scale.py --scale natural-minor C"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    scale_options = parser.add_mutually_exclusive_group()
    scale_options.add_argument(
        "--scale",
        choices=("major", "natural-minor", "natural_minor"),
        help="scale type",
    )
    scale_options.add_argument(
        "--major", dest="scale", action="store_const", const="major",
        help="shortcut for --scale major",
    )
    scale_options.add_argument(
        "--natural-minor", "--natural_minor", dest="scale",
        action="store_const", const="natural-minor",
        help="shortcut for --scale natural-minor",
    )
    parser.add_argument(
        "note", nargs="?", type=str.upper, choices=NOTES,
        help="root note (C, D, E, F, G, A, or B)",
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + VERSION
    )
    parser.add_argument(
        "--color", choices=("auto", "always", "never"), default="auto",
        help="color output: auto for terminals, always, or never",
    )
    return parser


def style(text, color, enabled, bold=False):
    if not enabled:
        return text

    prefix = ANSI_COLORS[color]
    if bold:
        prefix = ANSI_COLORS["bold"] + prefix
    return prefix + text + ANSI_COLORS["reset"]


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


def generateTriads(scale_notes):
    chord_qualities = {
        (4, 7): "",
        (3, 7): "m",
        (3, 6): "dim",
    }
    chords = []

    for degree, root_note in enumerate(scale_notes):
        root_number = convertNoteToNumber(root_note)
        third_number = convertNoteToNumber(scale_notes[(degree + 2) % 7])
        fifth_number = convertNoteToNumber(scale_notes[(degree + 4) % 7])
        intervals = (
            (third_number - root_number) % 12,
            (fifth_number - root_number) % 12,
        )
        chords.append(root_note + chord_qualities[intervals])

    return chords


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.scale is None:
        parser.error("specify a scale with --scale, --major, or --natural-minor")
    if args.note is None:
        parser.error("specify the root note")

    scale_name = args.scale.replace("_", "-")
    scale_key = "--major" if scale_name == "major" else "--natural_minor"
    scale_notes = generateScale(args.note, scale_key)
    scale_chords = generateTriads(scale_notes)
    label = "major" if scale_name == "major" else "natural minor"
    formula = "W-W-H-W-W-W-H" if scale_name == "major" else "W-H-W-W-H-W-W"
    color_enabled = args.color == "always" or (
        args.color == "auto"
        and sys.stdout.isatty()
        and "NO_COLOR" not in os.environ
    )
    scale_color = "cyan" if scale_name == "major" else "magenta"
    colored_chords = []
    for chord in scale_chords:
        if chord.endswith("dim"):
            chord_color = "yellow"
        elif chord.endswith("m"):
            chord_color = "magenta"
        else:
            chord_color = "cyan"
        colored_chords.append(style(chord, chord_color, color_enabled, bold=True))

    print(style("MUSICAL SCALE", "bold", color_enabled))
    print(style("{} {} scale".format(args.note, label), scale_color, color_enabled, bold=True))
    print("Intervals (W=whole tone, H=semitone): {}".format(
        style(formula, scale_color, color_enabled)
    ))
    print("Notes:     " + style(" - ".join(scale_notes), scale_color, color_enabled))
    print("Chords:    " + " - ".join(colored_chords))
    print("Legend:    {} major | {} minor | {} diminished".format(
        style("cyan", "cyan", color_enabled),
        style("magenta", "magenta", color_enabled),
        style("yellow", "yellow", color_enabled),
    ))
    return 0
    
if __name__ == '__main__':
    sys.exit(main())