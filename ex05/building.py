import sys
import string


def building(text):
    """
    Count the number of characters in a text
    and print the number of upper letters, lower letters,
    punctuation marks, spaces and digits.
    """
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for c in text if c.isupper())} upper letters")
    print(f"{sum(1 for c in text if c.islower())} lower letters")
    print(f"{sum(1 for c in text if c in string.punctuation)} "
          f"punctuation marks")
    print(f"{sum(1 for c in text if c.isspace())} spaces")
    print(f"{sum(1 for c in text if c.isdigit())} digits")


def main():
    try:
        text = ""
        if len(sys.argv) > 2:
            raise AssertionError("The number of arguments is not correct")
        elif len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]
        building(text)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
