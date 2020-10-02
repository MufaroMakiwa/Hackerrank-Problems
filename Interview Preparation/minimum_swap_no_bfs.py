def minimumSwaps(arr: list):
    # initialize an index
    index = 0

    # initialize steps counter
    counter = 0

    while index < len(arr):

        # if value at index is index+1, proceed
        if arr[index] == index + 1:
            index += 1
            continue

        else:
            # get the swapping index
            swap_ind = arr[index] - 1

            arr[index], arr[swap_ind] = arr[swap_ind], arr[index]
            counter += 1

    return counter


if __name__ == '__main__':
    with open("test_case.txt", "r") as f:
        file = f.read()

    values = list(map(int, file.rstrip().split()))
    swaps = minimumSwaps(values)
    print(swaps)
