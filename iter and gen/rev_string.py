def reverse_text(text):
    curr_ind = len(text) - 1
    while curr_ind >= 0:
        yield text[curr_ind]
        curr_ind -= 1

for char in reverse_text("step"):
    print(char, end='')