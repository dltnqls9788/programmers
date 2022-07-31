def solution1(arr1, arr2):
    return [[arr1[i][j]+arr2[i][j] for j in range(len(arr1))] for i in range(len(arr1))]


def solution2(arr1, arr2):
    return [[c + d for c, d in zip(a,b)] for a, b in zip(arr1,arr2)]