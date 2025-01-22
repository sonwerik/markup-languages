def ex5(gods):
    sorted_gods = []

    for god in gods:
        if god not in sorted_gods:
            sorted_gods.append(god)

    sorted_gods.sort()
    print(sorted_gods)


ex5(["Hermes", "Zeus", "Hestia", "Poseidon", "Hestia", "Hermes", "Poseidon", "Hera", "Hermes", "Artemis", "Demeter",
     "Hermes", "Aphrodite", "Athena", "Artemis", "Demeter", "Apollo", "Ares", "Hephaestus", "Artemis", "Hermes",
     "Hestia"])
