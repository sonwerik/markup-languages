def ex4(gods, new_god):
    gods_lower = [god.lower() for god in gods]

    if new_god.lower() in gods_lower:
        print("This God is already an Olympian God")
    else:
        gods.append(new_god)
        print("God added")
    print(gods)


ex4(["Zeus", "Poseidon", "Hera", "Demeter", "Aphrodite", "Athena", "Artemis", "Apollo", "Ares", "Hephaestus", "Hermes",
     "Hestia"], "Dionysus")
