import random
from tabulate import tabulate

# Generate the pot of 75 balls
pot = list(range(1, 76, 1))

B = []
I = []
N = []
G = []
O = []

while len(pot) > 0:
    # After every selection shuffle the whole pot again
    random.shuffle(pot)
    # Get some list element out of pot
    lucky_number = pot.pop()
    if lucky_number <= 15 and len(B) < 5:
        B.append(lucky_number)
    elif 15 < lucky_number <= 30 and len(I) < 5:
        I.append(lucky_number)
    elif 30 < lucky_number <= 45 and len(N) < 5:
        N.append(lucky_number)
    elif 45 < lucky_number <= 60 and len(G) < 5:
        G.append(lucky_number)
    elif 60 < lucky_number <= 75 and len(O) < 5:
        O.append(lucky_number)

# List of lists
table = [B, I, N, G, O]
# Transpose the list of list to get right structure for tabulating
transpose_table = list(map(list, zip(*table)))
final_bingo_table = tabulate(transpose_table, headers=["B", "I", "N", "G", "O"], tablefmt="grid")
print(final_bingo_table)

# Write it to file
try:
    # https://www.geeksforgeeks.org/reading-writing-text-files-python/
    with open('bingo_ticket.txt', 'a') as f:
        f.write(f"{final_bingo_table}\n\n")
        f.close()
except:
    print("An exception occurred")
