from custom_words import shuffled_answers

title = 'Firt Meet uPCI Hang(man) Time!'
prompt = "Tebak Huruf atau kata: "

def answerer():
    answer = shuffled_answers.popitem()
    word = answer[0].upper()
    hint = answer[1]['hint']
    return word, hint


def play(word, hint):
    guessed = False
    first_hint = True
    guessed_letters = []
    guessed_words = []
    word_completion = ""
    tries = 6
    counter = len(word.split())
    holder = word.split()

    while counter > 0:
        word_completion += "_" * len(holder[0]) + "\n"
        counter -= 1
        holder.pop(0)
    print(f"\n{title}")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
        guess = input(prompt).upper()
        print("\n\n")

        reguess = f"'{guess}' sudah di tebak."
        wrong = f"'{guess}' BUKAN huruf yang di dalam kata. \nBoleh minta petunjuk, tetapi akan dikenakan denda."
        right = f"Sungguh hoki...'{guess}' merupakan huruf dalam kata"

        if len(guess) == 1 and guess.isalpha(): # Letter guessing
            if guess in guessed_letters:
                print(reguess)
            elif guess not in word:
                print(wrong)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(right)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif guess == '?':
            tries -= 1
            if first_hint == True: 
                print("Dendanya adalah ANGGOTA BADAN!\n")
                first_hint = False
            print("Petunjuknya adalah:")
            print(hint)
        elif len(guess) == len(word) and guess.isalpha(): # Full word guessing
            if guess in guessed_words:
                print(reguess)
            if guess != word:
                print(f"Ha! Usaha yang bagus, '{guess}' bukanlah kata yang tepat. Mungkin lebih baik tebak menggunakan huruf, lebih mudah.")
            else:
                guessed = True
                word_completion = word
        else:
            print("\nBukan tebakan yang valid. Itu jelas bukan tebakan yang valid. Tolong, ini serius.")
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print(f"MENANG | Muantap bosqu")
    else:
        print(f"KALAH | Better luck next time!")



def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |     \\O/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |     \\O
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |       \\
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def main():
    # try:
        answer, hint = answerer()
        play(answer, hint)
        while input("Maen lagi? (Y/N) ").upper() == "Y":
            answer, hint = answerer()
            play(answer, hint)
    # except:
    #     print("\n\nOh no, there are no more words!\n\n")

if __name__ == "__main__":
    main()
