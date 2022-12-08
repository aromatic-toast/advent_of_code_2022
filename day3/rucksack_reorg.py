# Author: Lesley Miller
from string import ascii_lowercase, ascii_uppercase
import pandas as pd

def get_priority(item_type):
    """
    Return the priority of the item type.

    Parameters
    ----------
    item_type (str) A single character of a-z or A-Z.

    Returns
    -------
    int
        The numeric priority of the item type.

    """
    # create the item type conversion map
    lower_case = [x for x in ascii_lowercase]
    upper_case = [x for x in ascii_uppercase]
    priority_map = pd.DataFrame({'item_type': lower_case + upper_case, 'priority': list(range(1, 53, 1))})
    # get the priority
    priority = priority_map.query('item_type ==@item_type').priority.values[0]
    return priority


def find_error(rucksack):
    """
    Return the error or the item in common between the two compartments in the rucksack

    Parameters
    ----------
    rucksack (list) A list of items representing the two compartments of the rucksack

    Returns
    -------
    str
        The item that intersects between the two compartments in the rucksack

    """
    # get total num items in a compartment
    num_items_in_compartment = int(len(rucksack) / 2)
    # get the compartments
    compartment1 = set(rucksack[0:num_items_in_compartment])
    compartment2 = set(rucksack[num_items_in_compartment:])
    error = list(compartment1.intersection(compartment2))[0]
    return error

def find_badge(rucksacks):
    """
    Return the item that is common between the 3 rucksacks
    Parameters
    ----------
    rucksacks (list) A list of rucksacks

    Returns
    -------
    str
        The item that intersects between the 3 rucksacks

    """
    sack1 = rucksacks[0]
    sack2 = rucksacks[1]
    sack3 = rucksacks[2]
    # get the intersection between the 3 sets
    badge = list(set(sack1) & set(sack2) & set(sack3))[0]
    return badge

def main():
    #  initialize rucksacks dict
    elf_groups = []
    rucksacks = []
    # load the data
    with open("input.txt") as file:
        i = 1
        group_num = 1
        for line in file:
            # turn string of char into a list of items in the rucksack
            rucksack = [x for x in line.strip("\n")]
            # add the rucksack to a list of rucksacks
            rucksacks.append(rucksack)
            if i % 3 == 0:
                # add list of rucksacks to master list of elf groups
                elf_groups.append(rucksacks)
                # reset the list of rucksacks back to empty
                rucksacks = []
                group_num += 1

            i += 1

    # get the badges for each elf group
    badges = list(map(find_badge, elf_groups))

    # get list of priorities
    priority_list = list(map(get_priority, badges))

    # get the sum of the priorities
    priority_sum = sum(priority_list)
    print("The sum of priorities: ", str(priority_sum))


if __name__ == '__main__':
    main()