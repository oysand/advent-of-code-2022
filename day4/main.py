def first_task():
    f = open("input.txt")
    contained_pairs = 0
    for line in f:
        elf_pair = line.strip()
        elf1, elf2 = elf_pair.split(",")
        elf1_lower_str, elf1_upper_str = elf1.split("-")
        elf2_lower_str, elf2_upper_str = elf2.split("-")
        elf1_lower = int(elf1_lower_str)
        elf1_upper = int(elf1_upper_str)
        elf2_lower = int(elf2_lower_str)
        elf2_upper = int(elf2_upper_str)
        if elf1_lower >= elf2_lower and elf1_upper <= elf2_upper:
            contained_pairs += 1
            continue

        if elf2_lower >= elf1_lower and elf2_upper <= elf1_upper:
            contained_pairs += 1

    print(contained_pairs)


def second_task():
    f = open("input.txt")
    overlapping_pairs = 0
    for line in f:
        elf_pair = line.strip()
        elf1, elf2 = elf_pair.split(",")
        elf1_lower_str, elf1_upper_str = elf1.split("-")
        elf2_lower_str, elf2_upper_str = elf2.split("-")
        elf1_lower = int(elf1_lower_str)
        elf1_upper = int(elf1_upper_str)
        elf2_lower = int(elf2_lower_str)
        elf2_upper = int(elf2_upper_str)

        if (elf1_lower < elf2_lower and elf1_upper < elf2_lower) or (
            elf2_lower < elf1_lower and elf2_upper < elf1_lower
        ):
            continue
        else:
            overlapping_pairs += 1

        # if elf1_lower >= elf2_lower and elf1_upper <= elf2_upper:
        #     overlapping_pairs += 1
        #     continue

        # if elf2_lower >= elf1_lower and elf2_upper <= elf1_upper:
        #     overlapping_pairs += 1

    print(overlapping_pairs)


if __name__ == "__main__":
    # first_task()
    second_task()
