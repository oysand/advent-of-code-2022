def remove_oldest_value(values: list) -> list:
    remaining_values = []
    for i in range(len(values) - 1):
        remaining_values.append(values[i + 1])

    return remaining_values


def check_if_uniqueue(elements: list):
    return len(elements) == len(set(elements))


def first_task(file_name):
    f = open(file_name)
    for line in f:
        i = 1
        potential_markers = []
        for character in line:
            potential_markers.append(character)

            if len(potential_markers) >= 14:
                if check_if_uniqueue(potential_markers):
                    print(i)
                    break

                potential_markers = remove_oldest_value(potential_markers)
            i += 1


if __name__ == "__main__":
    file_name = "input.txt"
    first_task(file_name=file_name)
