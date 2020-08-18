# TODO: Write a function which will count the number of times any one character appears in a string of characters.
# Write a main function which takes the character to be counted from the user and calls the function, 
# outputting the result to the user.

def letter_counter(letter, given_string): 
    given_string = given_string.lower()

    letter = letter.lower()
    total = 0 

    for focus_letter in given_string: 
        if focus_letter == letter: 
            total += 1

    print (total)

if __name__ == "__main__":
    input_string =  input("Pick a string of characters.")
    input_letter = input("Pick a letter.")
    letter_counter(input_letter, input_string)

# def letter_counter(letter, given_string): 
#     given_string = given_string.lower()

#     letter = letter.lower()
#     total = 0 

#     for focus_letter in given_string: 
#         if focus_letter == letter: 
#             total += 1

    # return total

# example_letter = 'r'
# example_sentence = "The quick brown fox jumps over the lazy dog."

# example_variable = letter_counter(example_letter, example_sentence)
# print(example_variable)
# letter_counter(example_letter, example_sentence)