# Musical Scale

A small Python command-line tool for generating major and natural minor scales, along with their diatonic triads.

## Features

- Major and natural minor scales
- Diatonic triads labeled as major, minor, or diminished
- Optional ANSI colors, with automatic terminal detection
- No third-party Python dependencies

## Requirements

- Python 3
- Git, if cloning the repository from the command line

## Quick Start

```bash
git clone https://github.com/willian20091/Musical_scale.git
cd Musical_scale
python3 musical_scale.py --help
```

If your system uses `python` to launch Python 3, replace `python3` with `python` in the commands below.

## Usage

```text
python3 musical_scale.py --scale {major,natural-minor} NOTE [--color {auto,always,never}]
```

The supported root notes are `C`, `D`, `E`, `F`, `G`, `A`, and `B`. Input is case-insensitive. Accidentals are generated as needed in the scale, but roots with accidentals are not accepted.

Examples:

```bash
python3 musical_scale.py --scale major C
python3 musical_scale.py --scale natural-minor C
```

The original shortcuts remain available:

```bash
python3 musical_scale.py --major C
python3 musical_scale.py --natural_minor C
```

`--natural-minor` is also accepted as a shortcut. Run `python3 musical_scale.py --help` for the complete option list.

## Output

The output includes the interval pattern, scale notes, and a harmonized triad for each scale degree. `W` means whole tone; `H` means semitone. In chord names, no suffix means major, `m` means minor, and `dim` means diminished.

### C Major

```text
MUSICAL SCALE
C major scale
Intervals (W=whole tone, H=semitone): W-W-H-W-W-W-H
Notes:     C - D - E - F - G - A - B
Chords:    C - Dm - Em - F - G - Am - Bdim
Legend:    cyan major | magenta minor | yellow diminished
```

### C Natural Minor

```text
MUSICAL SCALE
C natural minor scale
Intervals (W=whole tone, H=semitone): W-H-W-W-H-W-W
Notes:     C - D - Eb - F - G - Ab - Bb
Chords:    Cm - Ddim - Eb - Fm - Gm - Ab - Bb
Legend:    cyan major | magenta minor | yellow diminished
```

## Colors

Colors are enabled automatically when output is sent to an interactive terminal. `NO_COLOR` disables automatic color when that environment variable is set.

Use `--color` to control color output:

- `auto` (default): color only in an interactive terminal
- `always`: force ANSI colors, including when output is redirected
- `never`: disable colors

Major-scale output uses cyan and natural-minor output uses magenta. Chords use cyan for major, magenta for minor, and yellow for diminished.

## Scope

The current version generates major and natural minor scales. Harmonic and melodic minor scales are not yet implemented.