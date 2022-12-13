import math


def get_stacks(file_name):
    f = open(file_name)
    bucket_placement = []
    should_brake = False
    for line in f:
        # stripped_line = line.strip()
        # if len(stacks) == 0:
        # number_of_stacks = int(len(line) / 3)
        # stacks = [[]] * number_of_stacks
        # bucket_placement = [0] * number_of_stacks
        # print(number_of_stacks)

        i = 0
        bucket_number = 0
        bucket_placement = []
        for character in line:
            if character.isnumeric():
                should_brake = True
                bucket_placement.append(i)
                bucket_number += 1
            i += 1

        if should_brake:
            break

    number_of_stacks = bucket_number
    stacks = []
    for i in range(number_of_stacks):
        stacks.append([])
    # stacks = [[]] * number_of_stacks
    f = open(file_name)
    should_brake = False
    for line in f:
        for character in line:
            if character.isnumeric():
                should_brake = True

        if should_brake:
            break

        for i in range(number_of_stacks):
            bucket_item = line[bucket_placement[i]]
            if bucket_item.isalpha():
                stacks[i].append(bucket_item)

    for i in range(number_of_stacks):
        stacks[i].reverse()

    return stacks, number_of_stacks


def move_stacks(number_to_move: int, from_stack: int, to_stack: int, stacks: list):
    # print(f"Move: {number_to_move}")
    # print(f"From: {from_stack}")
    # print(f"To: {to_stack}")
    for i in range(number_to_move):
        object_to_move = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(object_to_move)

    return stacks


def first_task(file_name):
    stacks, number_of_stacks = get_stacks(file_name=file_name)
    print(stacks)
    f = open(file_name)
    instructions_begun = False
    for line in f:
        if line == "\n":
            instructions_begun = True
            continue
        if not instructions_begun:
            continue
        number_to_move = 0
        from_stack = 0
        to_stack = 0
        number = 0
        first_number = ""
        on_first_number = False
        for character in line:

            if on_first_number:
                if character.isnumeric():
                    first_number += character
                else:
                    on_first_number = False
                    number_to_move = int(first_number)
                    print(f"Move: {number_to_move}")
                    number += 1
            else:
                if character.isnumeric():
                    if number == 0:
                        on_first_number = True
                        first_number += character
                        # print(f"Move: {number_to_move}")
                        # number += 1
                    elif number == 1:
                        from_stack = int(character)
                        print(f"From: {from_stack}")
                        number += 1
                    elif number == 2:
                        to_stack = int(character)
                        print(f"To: {to_stack}")
                        number += 1
                    else:
                        print(number)
                        raise ValueError

        stacks = move_stacks(
            number_to_move=number_to_move,
            from_stack=from_stack,
            to_stack=to_stack,
            stacks=stacks,
        )

    # print(stacks)
    result = ""
    for i in range(number_of_stacks):
        result += stacks[i].pop()
    print(result)


def move_stacks_9001(number_to_move: int, from_stack: int, to_stack: int, stacks: list):
    objects_to_move = []
    for i in range(number_to_move):
        object_to_move = stacks[from_stack - 1].pop()
        objects_to_move.append(object_to_move)

    for i in range(number_to_move):
        stacks[to_stack - 1].append(objects_to_move.pop())

    return stacks


def second_task(file_name):
    stacks, number_of_stacks = get_stacks(file_name=file_name)
    print(stacks)
    f = open(file_name)
    instructions_begun = False
    for line in f:
        if line == "\n":
            instructions_begun = True
            continue
        if not instructions_begun:
            continue
        number_to_move = 0
        from_stack = 0
        to_stack = 0
        number = 0
        first_number = ""
        on_first_number = False
        for character in line:

            if on_first_number:
                if character.isnumeric():
                    first_number += character
                else:
                    on_first_number = False
                    number_to_move = int(first_number)
                    print(f"Move: {number_to_move}")
                    number += 1
            else:
                if character.isnumeric():
                    if number == 0:
                        on_first_number = True
                        first_number += character
                        # print(f"Move: {number_to_move}")
                        # number += 1
                    elif number == 1:
                        from_stack = int(character)
                        print(f"From: {from_stack}")
                        number += 1
                    elif number == 2:
                        to_stack = int(character)
                        print(f"To: {to_stack}")
                        number += 1
                    else:
                        print(number)
                        raise ValueError

        stacks = move_stacks_9001(
            number_to_move=number_to_move,
            from_stack=from_stack,
            to_stack=to_stack,
            stacks=stacks,
        )

    # print(stacks)
    result = ""
    for i in range(number_of_stacks):
        result += stacks[i].pop()
    print(result)


if __name__ == "__main__":
    file_name = "input.txt"
    second_task(file_name=file_name)
