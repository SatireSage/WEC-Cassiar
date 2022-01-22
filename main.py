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


if __name__ == "__main__":
    crane = crane.Crane()
    input_config = "3121401"
    process_config = "32222413140"
    print(compute_input(crane, input_config, process_config))
