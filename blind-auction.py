from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bid = {}
bid_finished = False


def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a highest bid of {highest_bid}")


while not bid_finished:

    name = input("What is your name?\n").lower()
    amount = int(input("What is your bidding amount ? $"))
    bid[name] = amount

    should_continue = input("Do you want to continue ? Say yes or no .\n").lower()
    if should_continue == "no":
        bid_finished = True
        find_highest_bidder(bid)
    elif should_continue == "yes":
        clear()
