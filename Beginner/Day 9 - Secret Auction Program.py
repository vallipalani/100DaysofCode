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

print("Welcome to the secret auction program")

bids_dict = {}
greatest_bid = 0

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    
    bids_dict[bid] = name
    if bid > greatest_bid:
        greatest_bid = bid
        
    user_input = input("Are there any other bidders? Type 'yes' or 'no' ")
    if user_input.lower() == "no":
        break
    else:
        print("\n" * 100)

greatest_bidder = bids_dict[greatest_bid]
print(f"The winner is {greatest_bidder} with a bid of ${greatest_bid}")
        
