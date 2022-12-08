# Author: Lesley Miller
# Date: Dec 7, 2022

def pair1_in_pair2(pair1, pair2):
    """
    Return True if pair1 is fully contained in the range of pair2

    Parameters
    ----------
    pair1 (list) A list of the first two pairs of numbers
    pair2 (list) A list of the second pairs of numbers

    Returns
    -------
    bool
        True or False

    """
    # return true if pair1's range of numbers are fully contained in the range of pair2
    return pair1[0] >= pair2[0] and pair1[1] <= pair2[1]

def pair2_in_pair1(pair1, pair2):
    """
    Return True if pair2 is fully contained in the range of pair1
    Parameters
    ----------
    pair1 (list) A list of the first two pairs of numbers
    pair2 (list) A list of the second pairs of numbers

    Returns
    -------
    bool
        True or False
    """
    # return true if pair2's range of numbers are fully contained in the range of pair1
    return pair2[0] >= pair1[0] and pair2[1] <= pair1[1]

def main():
     with open('input.txt') as file:
         num_pairs = 0
         for line in file:
             list_of_pairs = [x.split("-") for x in line.strip("\n").split(",")]
             pair1 = [int(x) for x in list_of_pairs[0]]
             pair2 = [int(x) for x in list_of_pairs[1]]
             # turn the pairs into a set of numbers in the range
             pair1_set = set(range(pair1[0], pair1[1] + 1, 1))
             pair2_set = set(range(pair2[0], pair2[1] + 1, 1))
             len_of_intersection = len(pair1_set.intersection(pair2_set))

             # check for any overlaps between the pairs
             if len_of_intersection > 0:
                 # add to the count
                 num_pairs += 1
         print("Sum of pairs overlapping: ", num_pairs)

if __name__ == '__main__':
    main()