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


def main():
    #  initialize rucksacks dict
    rucksacks = []
    # load the data
    with open("input.txt") as file:
        for line in file:
            # turn string of char into a list of items in the rucksack
            rucksack = [x for x in line.strip("\n")]
            # add the rucksack to a list of rucksacks
            rucksacks.append(rucksack)
    # get the errors in all the rucksacks
    errors = list(map(find_error, rucksacks))
    # get list of priorities
    priority_list = list(map(get_priority, errors))

    # get the sum of the priorities
    priority_sum = sum(priority_list)
    print("The sum of priorities: ", str(priority_sum))


if __name__ == '__main__':
    main()