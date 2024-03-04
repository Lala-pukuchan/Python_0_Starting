import time


def ft_tqdm(lst: range) -> None:
    """This function is a generator that takes a range and returns
    the elements of the range."""
    total = len(lst)
    start = time.time()
    for i, v in enumerate(lst, start=1):
        percentage = (i / total) * 100
        print(f"\r{percentage:.1f}% |", end="")
        block = int(percentage / 2)
        for _ in range(block):
            print("█", end="")
        for _ in range(50 - block):
            print(" ", end="")
        now = time.time()
        seconds = round(now - start, 2)
        if seconds == 0:
            seconds = 0.01
        speed = round(i / seconds, 2)
        estimation = round(seconds / i * total - seconds, 2)
        print(f"| {i}/{total} [ {seconds}<{estimation}, {speed}it/s]", end="")
        yield v


if __name__ == "__main__":
    for elem in ft_tqdm(range(333)):
        time.sleep(0.005)
