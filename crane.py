class Crane:
    def __init__(self):
        self.carryingBox = False
        self.stackIdx = 0
        self.stacks = [0 for i in range(7)]

    def left(self):
        if self.stackIdx == 0:
            print("Cannot decrement index of value 0")
            return
        self.stackIdx -= 1

    def right(self):
        if self.stackIdx == len(self.stacks) - 1:
            print("Cannot increment index beyond max size")
            return
        self.stackIdx += 1

    def lift(self):
        """ lifts a box from the stack associated with the objects stack index """
        if self.stacks[self.stackIdx] == 0 or self.carryingBox:
            print("Error lifting up box")
            return
        self.stacks[self.stackIdx] -= 1
        self.carryingBox = True

    def drop(self):
        """ drops a box onto the stack associated with the objects stack index """
        if self.stacks[self.stackIdx] == 4 or (not self.carryingBox):
            print("Error dropping box onto the current stack " + str(self.carryingBox) + str(self.stacks[self.stackIdx]))
            return
        self.stacks[self.stackIdx] += 1
        self.carryingBox = False

    def initialize_stacks(self, config):
        for i in range(len(config)):
            num_boxes = int(config[i])
            while num_boxes > 4 or num_boxes < 0:
                num_boxes = input("Please enter a new number of boxes for the current stack (min 0, max 4): ")
            self.stacks[i] = num_boxes

    def output(self):
        output_string = ""
        for val in self.stacks:
            output_string += str(val)
        return output_string
