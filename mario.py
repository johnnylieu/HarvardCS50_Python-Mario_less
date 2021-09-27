from cs50 import get_int

# loop
while True:
    height = get_int("Height: ")

    # height must be between 1 and 8
    if 1 <= height <= 8:
        # break out of loop
        break

for row in range(1, height + 1):
    print(' ' * (height - row) + '#' * row)