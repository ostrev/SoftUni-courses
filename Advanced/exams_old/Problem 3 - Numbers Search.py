def numbers_searching(*args):
    all_list = sorted(args)
    dup_list = []
    dupp = set()
    result = []
    for x in all_list:
        if args.count(x) > 1:
            dupp.add(x)

    dup_list = sorted([x for x in dupp])
    missing = 0
    for i in range(all_list[0], all_list[-1] + 1):
        if i not in args:
            missing = i
    result.append(missing)
    result.append(dup_list)

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
# resu = f'[{"".join([str(s) for s in missing])}, [{", ".join([str(s) for s in sorted(dup_list)])}]]'