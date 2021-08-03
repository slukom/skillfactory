# Дописать функцию print_ladder так,
# чтобы она для числа n печатала лесенку следующего типа:
# n = 3
# *
# **
# ***

# n = 4
# *
# **
# ***
# ****


def print_ladder(n):
    def print_ladder(n):
        stairs = ""
        for i in range(n):
            stairs = stairs + "*"
            print(stairs)

