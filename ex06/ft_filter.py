def ft_filter(s, n):
    words = s.split()

    for word in words:
        if len(word) > n:
            print(word, end=" ")
