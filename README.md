# 🎹 MIDI to Keyboard Mapper

Map MIDI notes and chords to keyboard keys using Python.

Use your MIDI keyboard to control games, apps, or anything that responds to key presses.

(Tested for fun with Chrome Dino and Pac-Man)

---

## Usage

pip install mido python-rtmidi pynput
python midi_controller.py


Edit note_to_key and jump_chord in the script to customize mappings:

Edit `note_to_key` and `jump_chord` in the script to customize mappings.

For example:


note_to_key = {
    60: Key.up,       # C note → Up arrow
    62: Key.down,     # D note → Down arrow
    64: Key.left,     # E note → Left arrow
    65: Key.right     # F note → Right arrow
}

jump_chord = frozenset([60, 64, 67])  # C major chord → Spacebar (jump)
jump_key = Key.space
You can map any MIDI note number (0–127) to any key from pynput.keyboard.Key or even characters like 'a', 'z', etc.

Made by Aashna Kunkolienker


