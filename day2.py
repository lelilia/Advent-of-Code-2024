with open("input2", "r") as f:
    reports = f.readlines()


def check_report(report):
    if type(report) == str:
        report = [int(x) for x in report.split()]
    if report[0] > report[1]:
        for i in range(len(report) - 1):
            if not 1 <= report[i] - report[i + 1] <= 3:
                return 0
        return 1
    if report[0] < report[1]:
        for i in range(len(report) - 1):
            if not 1 <= report[i + 1] - report[i] <= 3:
                return 0
        return 1
    return 0


def check_report_dampener(report):
    report = [int(x) for x in report.split()]
    if check_report(report) == 1:
        return 1
    for i in range(len(report)):
        if check_report(report[:i] + report[i + 1 :]) == 1:
            return 1
    return 0


def check_report_dampener1(report, flag=True):
    report = [int(x) for x in report.split()]

    if report[0] > report[1]:
        for i in range(len(report) - 1):
            if not 1 <= report[i] - report[i + 1] <= 3:
                if flag:
                    list_1 = " ".join(
                        [str(x) for x in report[: i + 1] + report[i + 2 :]]
                    )
                    list_2 = " ".join([str(x) for x in report[:i] + report[i + 1 :]])
                    return (
                        1
                        if check_report_dampener(list_1, False)
                        + check_report_dampener(list_2, False)
                        >= 1
                        else 0
                    )
                else:
                    return 0
        return 1
    if report[0] < report[1]:
        for i in range(len(report) - 1):

            if not 1 <= report[i + 1] - report[i] <= 3:
                if flag:

                    list_1 = " ".join(
                        [str(x) for x in report[: i + 1] + report[i + 2 :]]
                    )
                    list_2 = " ".join([str(x) for x in report[:i] + report[i + 1 :]])

                    return (
                        1
                        if check_report_dampener(list_1, False)
                        + check_report_dampener(list_2, False)
                        >= 1
                        else 0
                    )
                else:
                    return 0
        return 1
    return 0


save = 0
save_with_tolerance = 0

for i, report in enumerate(reports):

    save += check_report(report)
    save_with_tolerance += check_report_dampener(report)

print("Part 1:", save)
print("Part 2:", save_with_tolerance)


assert check_report("49 46 47 49 50 57 60 66") == 0
assert check_report("41 40 45 47 49 53") == 0
assert check_report("43 43 44 45 47 50 53 56") == 0
assert check_report("1 2 3 7") == 0
assert check_report("1 2 3 4 5 8") == 1
assert check_report("5 4 3 2 1") == 1

assert check_report_dampener("7 6 4 2 1") == 1
assert check_report_dampener("1 2 7 8 9") == 0
assert check_report_dampener("9 7 6 2 1") == 0
assert (result := check_report_dampener("1 3 2 4 5")) == 1, result
assert check_report_dampener("8 6 4 4 1") == 1
assert check_report_dampener("1 3 6 7 9") == 1

assert check_report_dampener("1 2 3 4 10") == 1

assert check_report("65 68 71 72 71") == 0
assert check_report_dampener("65 68 71 72 71") == 1
assert check_report("31 34 36 37 37") == 0
assert check_report_dampener("31 34 36 37 37") == 1
assert check_report("80 83 84 86 87 90 92 96") == 0
assert check_report_dampener("80 83 84 86 87 90 92 96") == 1
assert check_report("30 33 36 39 45") == 0
assert check_report_dampener("30 33 36 39 45") == 1
assert check_report("21 22 25 23 24") == 0
assert check_report_dampener("21 22 25 23 24") == 1
assert check_report("66 68 69 71 72 71 72 69") == 0
assert check_report_dampener("66 68 69 71 72 71 72 69") == 0
assert check_report("2 3 5 4 4") == 0
assert check_report_dampener("2 3 5 4 4") == 0
assert check_report("77 78 77 79 82 83 86 90") == 0
assert check_report_dampener("77 78 77 79 82 83 86 90") == 0
assert check_report("6 9 10 7 9 12 17") == 0
assert check_report_dampener("6 9 10 7 9 12 17") == 0
assert check_report("25 27 28 28 30 32") == 0
assert check_report_dampener("25 27 28 28 30 32") == 1
assert check_report("61 63 66 68 68 66") == 0
assert check_report_dampener("61 63 66 68 68 66") == 0
assert check_report("51 54 54 57 60 60") == 0
assert check_report_dampener("51 54 54 57 60 60") == 0
assert check_report("50 52 52 53 56 60") == 0
assert check_report_dampener("50 52 52 53 56 60") == 0

assert check_report("73 75 76 76 83") == 0
assert check_report_dampener("73 75 76 76 83") == 0
assert check_report("19 20 24 26 28") == 0
assert check_report_dampener("19 20 24 26 28") == 0
assert check_report("36 38 41 42 45 49 47") == 0
assert check_report_dampener("36 38 41 42 45 49 47") == 1
assert check_report("56 59 63 64 64") == 0
assert check_report_dampener("56 59 63 64 64") == 0
assert check_report("26 29 32 36 40") == 0
assert check_report_dampener("26 29 32 36 40") == 0
assert check_report("70 72 74 75 77 80 84 89") == 0
assert check_report_dampener("70 72 74 75 77 80 84 89") == 0
assert check_report("81 83 88 89 92 95 96") == 0
assert check_report_dampener("81 83 88 89 92 95 96") == 0
assert check_report("79 80 85 87 89 92 93 90") == 0
assert check_report_dampener("79 80 85 87 89 92 93 90") == 0
assert check_report("77 80 85 87 89 92 92") == 0
assert check_report_dampener("77 80 85 87 89 92 92") == 0
assert check_report("29 31 33 38 40 42 46") == 0
assert check_report_dampener("29 31 33 38 40 42 46") == 0
assert check_report("49 52 57 58 59 65") == 0
assert check_report_dampener("49 52 57 58 59 65") == 0
