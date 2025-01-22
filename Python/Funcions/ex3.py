def ex3(words):
    largest = words[0]
    shortest = words[0]

    for word in words:
        if len(largest) < len(word):
            largest = word
        if len(shortest) > len(word):
            shortest = word
    print(f"Largest: {largest}\nShortest: {shortest}")


ex3(["Zeus", "Poseidon", "Hera", "Demeter", "Aphrodite", "Athena", "Artemis", "Apollo", "Ares", "Hephaestus", "Hermes",
     "Hestia"])
