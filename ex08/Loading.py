def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, v in enumerate(lst, start=1):
        percentage = (i / total) * 100
        print(f"\r[{percentage:.1f}% | {i}/{total}]", end="")
        yield v
