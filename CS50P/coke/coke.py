def coke_machine():
    cost = 50
    accepted_coins = [25, 10, 5]
    amount_paid = 0

    while amount_paid < cost:
        print(f"Amount Due: {cost - amount_paid}\n")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue

        if coin in accepted_coins:
            amount_paid += coin
        #else:
           # print(f"Amount Due: {cost - amount_paid} cents")

    change = amount_paid - cost
    print(f"Change Owed: {change}\n")

if __name__ == "__main__":
    coke_machine()
