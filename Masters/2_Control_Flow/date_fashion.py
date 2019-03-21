def date_fashion(you, date):
    if you >= 8 or date >= 8:
        return 2
    elif you < 8 or date < 8:
        return 0
    else:
        return 1