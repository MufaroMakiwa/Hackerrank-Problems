def workbook(n, k, arr):
    page = 1
    special = 0

    for i in range(n):
        problems = arr[i]
        problem = 1

        while problems > 0:
            if problem <= page <= problem + min(problem, k) - 1:
                special += 1
        
            problem += k
            problems -= k
            page += 1

    return special

print(workbook(5, 3, [4,2,6,1,10]))
