"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number) -> list:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = list(range(number, number + 3))
    return rounds


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    total_rounds_list = rounds_1 + rounds_2
    return total_rounds_list


def list_contains_round(rounds: list, number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: list) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    black_joe = sum(hand) / len(hand)
    return black_joe


def approx_average_is_average(hand: list) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    hand_average = card_average(hand)
    first_last_average = (int(hand[0] + hand[-1])) / 2
    middle_index = len(hand) // 2
    middle_card = hand[middle_index]

    return hand_average in (first_last_average, middle_card)


def average_even_is_average_odd(hand: list) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_index_numbers = []
    odd_index_numbers = []

    for index, number in enumerate(hand):
        if index % 2 == 0:
            even_index_numbers.append(number)
        else:
            odd_index_numbers.append(number)

    return card_average(even_index_numbers) == card_average(odd_index_numbers)


def maybe_double_last(hand: list) -> list:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22

    return hand
