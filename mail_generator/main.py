PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in name_list:
        stripped_name = name.rstrip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w" ) as complete_letter:
            complete_letter.write(new_letter)

