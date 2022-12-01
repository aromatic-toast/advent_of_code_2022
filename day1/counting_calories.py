# Author: Lesley Miller
# Date: Dec 1, 2022
from collections import Counter

def create_elf_dict(filename):
    """
    Create an elf dict to represent the total calories held by each elf.
    :param filename:
    :return: dict
        a dictionary of elves and their total calories
    """
    with open(filename) as file:
        # initialize dict of elves
        elves = Counter()

        # initialize the elf count
        elf_count = 1
        for calorie in file:
            if not calorie.isspace():
                elves["elf" + str(elf_count)] += int(calorie)
            else:
                # set the calorie count back to empty and increment elf count
                calories = 0
                elf_count += 1
    return elves


def main(num_top_elves):
    # read in the data
    elves = create_elf_dict("input.txt")
    if num_top_elves == 1:
        # return the max calories held by top elf
        print(max(elves.values()))
    if num_top_elves == 3:
        # sort the elves dict
        sorted_elves = sorted(elves, key=elves.get, reverse=True)
        # return max calories held by top 3 elves
        calories = 0
        for key in sorted_elves[0:3]:
            calories += elves[key]
        print(calories)

if __name__ == '__main__':
    main(num_top_elves=3)
