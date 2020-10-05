def countTriplets(arr, r):
    right_count = {}
    left_count = {}

    for num in arr:
        right_count.setdefault(num, 0)
        left_count.setdefault(num, 0)
        right_count[num] += 1

    triplets = 0

    for i in range(len(arr)):
        # decrement the count of arr[i] in right_count
        right_count[arr[i]] -= 1

        # get the num prev arr[i] if it was a geometric progression
        prev = arr[i] / r

        # get the num next arr[i] if it was a geometric progression
        next_ = arr[i] * r

        if prev in left_count and next_ in right_count:
            triplets += left_count[prev] * right_count[next_]

        # increment the count of arr[i] in the left_count
        left_count[arr[i]] += 1

    return triplets


if __name__ == '__main__':
    arr = [1 for i in range(100)]
    print(countTriplets(arr, 1))
