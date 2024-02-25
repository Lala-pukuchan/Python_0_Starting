import subprocess


def run_test(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))


if __name__ == "__main__":
    print("$> python filterstring.py 'Hello the World' 4")
    run_test(
        [
            "python3",
            "filterstring.py",
            "Hello the World",
            "4",
        ]
    )
    print("$> python filterstring.py 'Hello the World' 99")
    run_test(
        [
            "python3",
            "filterstring.py",
            "Hello the World",
            "99",
        ]
    )
    print("$> python filterstring.py 'Hello the World'")
    run_test(
        [
            "python3",
            "filterstring.py",
            "Hello the World",
        ]
    )
    print("$> python filterstring.py")
    run_test(
        [
            "python3",
            "filterstring.py",
        ]
    )
