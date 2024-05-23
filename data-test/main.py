def decode(message_file: str):

    with open(message_file, "r") as f:
        lines = f.readlines()

    table: dict = {}
    output: int = []

    for line in lines:
        number = int(line.split()[0])
        word = str(line.split()[1])
        table[number] = word

        for x in range(1000):
            if number == (int((x * x + x) / 2)):
                output.append(number)

    output.sort()

    for word in output:
        print(table[word])


decode("coding_qual_input.txt")
