def bank_deposit(deposit_amount, deposit_time):
    if deposit_amount in range(1000,10000):
        terms_dict = {
            'begin_sum': 1000,
            'end_sum': 10000,
            '6': 5,
            '12': 6,
            '24': 5
        }
        deposit_return = deposit_amount / 100*terms_dict[deposit_time]/12*int(deposit_time)
        return deposit_return+deposit_amount
    elif deposit_amount in range(10000,100000):
        terms_dict = {
            'begin_sum': 10000,
            'end_sum': 100000,
            '6': 6,
            '12': 7,
            '24': 6.5
        }
        deposit_return = deposit_amount * 100 / terms_dict[deposit_time] / 12 * int(deposit_time)
        return deposit_return + deposit_amount
    elif deposit_amount in range(100000, 1000000):
        terms_dict = {
        'begin_sum': 100000,
        'end_sum': 1000000,
        '6': 7,
        '12': 8,
        '24': 7.5
        }
        deposit_return = deposit_amount * 100 / terms_dict[deposit_time] / 12 * int(deposit_time)
        return deposit_return + deposit_amount

