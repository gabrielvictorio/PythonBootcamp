#!/usr/bin/env python3

with open("./Input/Names/invited_names.txt") as file:
    list_names = file.readlines()

final_list = []

for name in list_names:
    final_list.append(name.strip("\n"))


with open("./Input/Letters/starting_letter.txt") as file:
    starting_content = file.read()

for name in final_list:
    new_letter = starting_content.replace("[name]", f"{name}")
    with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as file:
        file.write(new_letter)
