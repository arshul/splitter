import math


def split(amount, kind):
    print(amount, kind)

    if kind == 1:
        daily_donation = math.floor(amount / 10 * 100) / 100.0
        balance_amount = round(amount - (daily_donation * 9), 2)
        data = {
            "daily_donation": daily_donation,
            "balance_amount": balance_amount
        }
        print(data)
        return data

    if kind == 2:
        odd_day_donation = math.floor(2 / 3 * amount / 5 * 100) / 100.0
        even_day_donation = math.floor(1 / 3 * amount / 5 * 100) / 100.0

        balance_amount = round(amount - (odd_day_donation * 5 + even_day_donation * 4), 2)
        data = {
            "odd_day_donation": odd_day_donation,
            "even_day_donation": even_day_donation,
            "balance_amount": balance_amount
        }
        print(data)
        return data
