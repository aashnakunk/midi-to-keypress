from pynput.keyboard import Controller, Key
import mido
import time

keyboard = Controller()
pressed_notes = set()
held_keys = set()
jumping = False  # Tracks if space is currently held

# Note-to-key mappings
note_to_key = {
    59: Key.left,   # B
    60: Key.down,   # C
    61: Key.up,     # C#
    62: Key.right   # D
}

# Chord → Jump
jump_chord = frozenset([60, 64, 67])  # C major chord
jump_key = Key.space

def is_jump_chord(notes):
    return jump_chord.issubset(notes)

with mido.open_input() as inport:
    print("dino controller")
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            pressed_notes.add(msg.note)

            # Handle movement keys
            if msg.note in note_to_key:
                direction = note_to_key[msg.note]
                if direction not in held_keys:
                    print(f"hold key: {direction}")
                    keyboard.press(direction)
                    held_keys.add(direction)

            if is_jump_chord(pressed_notes) and not jumping:
                print("starting long jump")
                keyboard.press(jump_key)
                jumping = True

        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            if msg.note in pressed_notes:
                pressed_notes.remove(msg.note)

            if msg.note in note_to_key:
                direction = note_to_key[msg.note]
                if direction in held_keys:
                    print(f"key release: {direction}")
                    keyboard.release(direction)
                    held_keys.remove(direction)

            # Handle jump release
            if not is_jump_chord(pressed_notes) and jumping:
                print("LONG Jump END")
                keyboard.release(jump_key)
                jumping = False
