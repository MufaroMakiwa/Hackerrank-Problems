def countTriplets(arr, r):
    """
    :param arr: Sequence of elements
    :param r: Common ratio
    :return: Number of triplet that form a geometric progression
    """

    log_r_n = {}

    for i in range(len(arr)):
        log = log_base_four_int(arr[i], r)

        if log is not None:
            log_r_n.setdefault(log, [])
            log_r_n[log].append(i)

    count = 0

    for b1 in sorted(log_r_n.keys()):
        if b1 + 1 in log_r_n and b1 + 2 in log_r_n:
            for i in log_r_n[b1]:
                for j in log_r_n[b1 + 1]:
                    for k in log_r_n[b1 + 2]:
                        if i < j < k:
                            count += 1

    return count


def log_base_four_int(num, r, count=0):
    """
    :param r: Base
    :param count: Number of times num has been divided by 4 so far
    :param num: Integer
    :return: Return the log of num to base four is the log is an integer else None
    """

    if int(num) != num:
        return None

    if num == 1:
        return count

    return log_base_four_int(num / r, r, count + 1)


if __name__ == '__main__':
    arr = [1, 2, 1, 2, 4]
    print(countTriplets(arr, 2))