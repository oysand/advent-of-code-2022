if __name__ == "__main__":
    f = open("input.txt")
    number_of_elves = 0
    for line in f:
        if line == "\n":
            number_of_elves += 1

    number_of_elves += 1
    elves = [0] * number_of_elves

    elf_number = 0
    f = open("input.txt")
    for line in f:
        if not line == "\n":
            elves[elf_number] += int(line.strip())
        else:
            elf_number += 1

    max_calories = 0
    second_calories = 0
    third_calories = 0
    for elf_calorie in elves:
        if elf_calorie > max_calories:
            third_calories = second_calories
            second_calories = max_calories
            max_calories = elf_calorie
        elif elf_calorie > second_calories:
            third_calories = second_calories
            second_calories = elf_calorie
        elif elf_calorie > third_calories:
            third_calories = elf_calorie
    print(max_calories + second_calories + third_calories)
