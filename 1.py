def count_morse_characters(user_input):
    string_input = user_input.split()

    count_element = 0

    for i in string_input:
        count_element += len(i)

    return count_element


test = ".--- .- ...- .-"
count_morse_characters(test)
print(count_morse_characters(test))
