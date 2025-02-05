


def chocolate(amount):
    chocolate=amount//3  # 15//3= 5
    wrapper=chocolate # 5

    while wrapper>=3:
        new_choco=wrapper//3  # 5//3= 1
        chocolate+=new_choco
        wrapper+=new_choco

    print(chocolate)
amount=15
chocolate(amount)