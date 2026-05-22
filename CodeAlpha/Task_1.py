import tkinter as tk
import random

# Words list
words = ["apple", "tiger", "chair", "robot", "plant"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []
max_wrong = 6
wrong_guesses = 0

# Window setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x500")

# Labels
word_label = tk.Label(root, text=" ".join(guessed_word), font=("Arial", 20))
word_label.pack(pady=20)

lives_label = tk.Label(root, text="❤️ Lives: " + "♥" * max_wrong, font=("Arial", 14))
lives_label.pack()

message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.pack(pady=10)

# Update display
def update_display():
    word_label.config(text=" ".join(guessed_word))
    lives_label.config(text="❤️ Lives: " + "♥" * (max_wrong - wrong_guesses))

# Check win/lose
def check_game():
    if "_" not in guessed_word:
        message_label.config(text="🎉 You Win!")
        disable_buttons()
    elif wrong_guesses >= max_wrong:
        message_label.config(text="💀 You Lose! Word: " + word)
        disable_buttons()

# Disable all buttons
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Letter guess function
def guess_letter(letter):
    global wrong_guesses

    if letter in guessed_letters:
        message_label.config(text="⚠️ Already guessed!")
        return

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        message_label.config(text="✅ Correct!")
    else:
        wrong_guesses += 1
        message_label.config(text="❌ Wrong!")

    update_display()
    check_game()

# Letter buttons
buttons = []
frame = tk.Frame(root)
frame.pack()

for letter in "abcdefghijklmnopqrstuvwxyz":
    btn = tk.Button(frame, text=letter.upper(), width=4,
                    command=lambda l=letter: guess_letter(l))
    btn.pack(side="left", padx=2, pady=2)
    buttons.append(btn)

# Full word guess
def guess_word():
    global wrong_guesses
    guess = entry.get().lower()

    if guess == word:
        for i in range(len(word)):
            guessed_word[i] = word[i]
        message_label.config(text="🎉 Correct Word!")
    else:
        wrong_guesses += 1
        message_label.config(text="❌ Wrong Word!")

    entry.delete(0, tk.END)
    update_display()
    check_game()

entry = tk.Entry(root)
entry.pack(pady=10)

guess_btn = tk.Button(root, text="Guess Word", command=guess_word)
guess_btn.pack()

# Start GUI loop
root.mainloop()