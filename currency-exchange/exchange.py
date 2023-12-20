def exchange_money(budget, exchange_rate) -> float:
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    exchanged_value = budget / exchange_rate

    return exchanged_value


def get_change(budget, exchanging_value) -> float:
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    amount_left = budget - exchanging_value
    return amount_left


def get_value_of_bills(denomination, number_of_bills) -> int:
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    calculated_value_of_bills = denomination * number_of_bills
    return calculated_value_of_bills


def get_number_of_bills(amount, denomination) -> int:
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    number_of_bills = amount // denomination
    return number_of_bills


def get_leftover_of_bills(amount, denomination) -> float:
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    leftover = amount % denomination
    return leftover


def exchangeable_value(budget, exchange_rate, spread, denomination) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_percent = (spread / 100)
    exchanged_currency = (spread_percent * exchange_rate) + exchange_rate
    budget_after_exchange = exchange_money(budget, exchanged_currency)
    leftover = get_leftover_of_bills(budget_after_exchange, denomination)
    return int(budget_after_exchange - leftover)

