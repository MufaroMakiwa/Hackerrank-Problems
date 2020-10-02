def minimumSwaps(arr: list):
    # implement using a BFS algorithm

    def perform_swaps(seq):
        """
        Given a sequence, perform all the possible swaps on the elements in the array
        """

        for i in range(n - 1):
            for j in range(i + 1, n):
                yield seq[:i] + [seq[j]] + seq[i + 1: j] + [seq[i]] + seq[j + 1:]

    def is_sorted(seq) -> bool:
        """
        Return true if a sequence is sorted else false
        """

        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                return False
        else:
            return True

    n = len(arr)

    # init agenda, a list of lists
    agenda = [arr]

    # a set to contain all the sequences used so far
    seen = {tuple(arr)}

    # a dictionary to contain all the parent to child mappings
    parents = {}

    # flag to check if the sorted list has been found
    found = False

    # for each list in agenda, do all the possible swaps and add them to agenda if
    # not there already

    while agenda and not found:
        # take the first element in agenda
        sub_list = agenda.pop(0)

        for swap in perform_swaps(sub_list):
            if tuple(swap) not in seen:

                # assign sub_list as its parent
                parents[tuple(swap)] = sub_list

                # check if the swap is sorted
                if is_sorted(swap):
                    found = True
                    break

                # add it to agenda
                agenda.append(swap)

                # add it to the seen set
                seen.add(tuple(swap))

    # trace the path from the sorted list to the parent, counting the number of swaps
    sorted_arr = sorted(arr)

    path = [sorted_arr]

    while arr not in path:
        parent = parents[tuple(path[-1])]
        path.append(parent)

    return list(reversed(path))


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

    ls = minimumSwaps(arr)
    print(*ls, sep="\n")


