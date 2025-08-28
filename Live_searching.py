import keyboard
import os

words = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Papaya", "Apricot"]
search_term = ""

print("Start typing to search (press ESC to quit):")

while True:
    key = keyboard.read_event()

    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'esc':
            break
        elif key.name == 'backspace':
            search_term = search_term[:-1]
        elif len(key.name) == 1:  # normal letters
            search_term += key.name

        # Clear the screen (cross-platform)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Display results
        print(f"Search: {search_term}")
        matches = [word for word in words if search_term.lower() in word.lower()]
        print("Matches:", matches if matches else "No matches found.")
