import sys

morse_code_dict = {
    " ": "/ ",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def sos():
    """This function takes a string as an argument and prints the morse code of the string.
    If the string is not valid, it prints an error message."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        upper_str = sys.argv[1].upper()
        if not upper_str.isalnum():
            raise AssertionError("the arguments are bad")
        i = 0
        for s in upper_str:
            print(morse_code_dict[s], end="")
            i += 1
            if i < len(upper_str):
                print(" ", end="")
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    sos()
