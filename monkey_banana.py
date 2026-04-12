def monkey_banana():
    monkey = "A"
    box = "B"
    banana = "C"
    on_box = False

    print("Initial State:")
    print(monkey, box, on_box)

    # Step 1: Move monkey to box
    monkey = box
    print("Monkey moves to box:", monkey)

    # Step 2: Push box to banana
    box = banana
    monkey = banana
    print("Monkey pushes box to banana:", box)

    # Step 3: Climb box
    on_box = True
    print("Monkey climbs box")

    # Step 4: Grab banana
    if on_box and monkey == banana:
        print("Monkey grabs banana 🍌")

monkey_banana()
