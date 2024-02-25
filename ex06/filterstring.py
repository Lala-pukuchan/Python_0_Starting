import sys
from ft_filter import ft_filter


def filterstring():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        n = sys.argv[2]
        if s.isdigit():
            raise AssertionError("the arguments are bad")
        if not n.isdigit():
            raise AssertionError("the arguments are bad")
        ft_filter(s, int(n))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    filterstring()
