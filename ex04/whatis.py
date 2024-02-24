import sys


def main():
    try:
        if len(sys.argv) == 1:
            print("")
            exit(0)
        assert len(sys.argv) == 2, "more than one argument is provided"
        val = int(sys.argv[1])
        if val % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError:", "argument is not an integer")


if __name__ == "__main__":
    main()
