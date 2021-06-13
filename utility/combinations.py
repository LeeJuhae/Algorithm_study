def generate(arr: list, r: int, idx: int, ele: list, comb: list) -> list:
    if r == len(ele):
        comb.append(ele)
    elif idx != len(arr):
        generate(arr, r, idx + 1, ele, comb)
        generate(arr, r, idx + 1, ele + [arr[idx]], comb)
    return comb


def combinations(arr: list, r: int) -> list:
    return generate(arr, r, 0, [], [])


arr = [1, 1, 2, 3, 4]
for i in range(1, len(arr) + 1):
    print(combinations(arr, i))
