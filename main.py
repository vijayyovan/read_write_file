with open("my_file.txt") as f:
    contents = f.read()
    print(contents)


with open("new_file.txt", mode="w") as f:
    f.write("\nNew text.")
