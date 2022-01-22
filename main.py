import crane


def compute_input(crane, input_config, process_config):
    """ sample input: 3121401, 32222413140
        1: left
        2: right
        3: lift
        4: drop
        output: 2131401 """
    # initialize stacks array based on the given configuration
    crane.initialize_stacks(input_config)

    # execute process
    for instruction in process_config:
        if instruction == "0":
            break
        elif instruction == "1":
            crane.left()
        elif instruction == "2":
            crane.right()
        elif instruction == "3":
            crane.lift()
        elif instruction == "4":
            crane.drop()

    return crane.output()


def compute_process(crane, input_config, output_config):
    """ sample input and output: 3121401, 2131401
           1: left
           2: right
           3: lift
           4: drop
           output: 3224 """
    crane.initialize_stacks(input_config)
    steps = []
    box_change = []
    pickups = []
    drops = []

    # initialize box-change array based on input and output
    for i in range(len(input_config)):
        box_change.append(int(input_config[i]) - int(output_config[i]))  # might not need
        if box_change[i] > 0:
            pickups.append(i)  # create list of pickup box stacks
        elif box_change[i] < 0:
            drops.append(i)  # create list of drop box stacks

    while pickups and drops:
        distance = crane.stackIdx - pickups[0]
        move_crane(crane, distance, steps)

        # should now be at pickup stack (crane.stackIdx = pickups[0])
        steps.append('3')  # lift box
        box_change[crane.stackIdx] -= 1
        if box_change[crane.stackIdx] == 0:
            pickups.remove(crane.stackIdx)

        # now need to go to closest drop
        distance = drops[0] - crane.stackIdx
        move_crane(crane, distance, steps)

        # should now be at drop stack (crane.stackIdx = drop[0])
        steps.append('4')  # lift box
        box_change[crane.stackIdx] += 1
        if box_change[crane.stackIdx] == 0:
            drops.remove(crane.stackIdx)
    generated_process = ""

    return generated_process.join(steps)


def move_crane(crane, distance, generated_process):
    if distance > 0:
        while distance > 0:
            crane.right()
            generated_process.append('2')
            distance -= 1
    else:
        while distance < 0:
            crane.left()
            generated_process.append('1')
            distance += 1


if __name__ == "__main__":
    crane = crane.Crane()
    input_config = "3121401"
    process_config = "32222413140"
    output_config = "2131401"
    print(compute_input(crane, input_config, process_config))
    print(compute_process(crane, input_config, output_config))
