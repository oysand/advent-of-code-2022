def first_task():
    f = open("input.txt")
    duplicate_items = []
    for line in f:
        items_in_rucksack = line.strip()
        duplicate_item = find_duplicate_in_both_sacks(items=items_in_rucksack)
        duplicate_items.append(duplicate_item)

    priorities = []
    for item in duplicate_items:
        priority = convert_item_to_priority(item)
        priorities.append(priority)

    print(sum(priorities))


def find_duplicate_in_both_sacks(items: str):
    first_compartment, second_compartment = (
        items[: len(items) // 2],
        items[len(items) // 2 :],
    )
    if len(first_compartment) != len(second_compartment):
        raise ValueError("The two compartments have different sizes")

    common_item = list(set(first_compartment) & set(second_compartment))
    if len(common_item) != 1:
        raise ValueError("There is more than one singe item")

    return common_item[0]


def convert_item_to_priority(character: str):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


def second_task():
    f = open("input.txt")
    groups = []
    i = 0
    j = 0
    groups.append([])
    for line in f:
        items_in_rucksack = line.strip()
        groups[i].append(items_in_rucksack)
        j += 1
        if j == 3:
            j = 0
            i += 1
            groups.append([])

    priorities = []
    for group in groups:
        if len(group) == 0:
            continue

        common_letter = list(set(group[0]) & set(group[1]) & set(group[2]))
        if len(common_letter) != 1:
            raise ValueError("There are multiple common items")
        priorities.append(convert_item_to_priority(common_letter[0]))
    print(sum(priorities))


if __name__ == "__main__":
    # first_task()
    second_task()
