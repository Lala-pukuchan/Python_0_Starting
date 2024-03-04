def ft_filter(s, n):
    """filter string by len"""
    words = s.split()

    filtered_words = [word for word in words if (lambda x: len(x) > n)(word)]
    print(" ".join(filtered_words), end="")
