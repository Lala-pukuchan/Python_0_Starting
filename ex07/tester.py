import subprocess


def run_test(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))


if __name__ == "__main__":
    print("$> python sos.py sos")
    run_test(
        [
            "python3",
            "sos.py",
            "sos",
        ]
    )
    print("$> python sos.py 'h$llo'")
    run_test(
        [
            "python3",
            "sos.py",
            "h$llo",
        ]
    )
