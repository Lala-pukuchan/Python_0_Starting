def count_in_list(list, string) -> int:
    """count the number of same string in a list"""
    return list.count(string)


if __name__ == "__main__":
    print(count_in_list(["toto", "tata", "toto"], "toto"))
