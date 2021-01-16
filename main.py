from replit import clear
from art import logo

print(logo)
print("welcome to the secret auction program.")

total_bids = {}
winner = ""
max_bids = 0
isBids = True

while isBids:
  name = input("What's your name? ")
  bids = int(input("What's your bids? $"))
  total_bids[name] = bids
  is_any_bids = input("Is there any bids? Y/N ")

  clear()

  if is_any_bids == "n" or is_any_bids == "N":
    isBids = False


for key in total_bids:
  if total_bids[key] > max_bids:
    winner = key
    max_bids = total_bids[key]

print(f"The winner is {winner} with bids ${max_bids}")