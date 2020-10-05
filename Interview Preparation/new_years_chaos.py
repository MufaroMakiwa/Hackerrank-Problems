def minimumBribes(q):

    def swaps(seq_, bribes):
        """
        Yield the possible swaps that can occur in a sequence

        :param bribes: bribes so far for each person
        :param seq_: list of integers before swapping
        :yield: all the possible swaps from the sequence
        """

        for i in range(len(seq_) - 1):

            if bribes[seq_[i+1]] < 2:

                # add one to the person's bribes
                bribes_updated = dict(bribes)
                bribes_updated[seq_[i+1]] += 1

                yield seq_[:i] + [seq_[i + 1]] + [seq_[i]] + seq_[i + 2:], bribes_updated

    initial = [i + 1 for i in range(len(q))]
    agenda = [(initial, {i: 0 for i in initial})]
    seen = {tuple(initial)}
    parents = {}

    while agenda and tuple(q) not in seen:
        current = agenda.pop(0)
        seq = current[0]

        for swap in swaps(seq, dict(current[1])):
            tup_swap = tuple(swap[0])

            if tup_swap not in seen:
                agenda.append(swap)
                seen.add(tup_swap)
                parents[tup_swap] = seq

    if tuple(q) not in seen:
        return "Too chaotic"

    path = [q]

    while initial not in path:
        parent = parents[tuple(path[-1])]
        path.append(parent)

    return list(reversed(path))


if __name__ == '__main__':
    arr = [2, 1, 5, 3, 4]
    b = minimumBribes(arr)
    print(b)