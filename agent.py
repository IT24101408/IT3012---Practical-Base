import random


class GreedyGridAgent:
    """Original Lab 1 random agent."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        return random.choice(self.actions_pool)



class SimpleReflexAgent:
    """
    Simple Reflex Agent.
    Uses only the current percept.
    Does not maintain memory/history.
    """

    def sense_and_act(self, percept: dict) -> str:

        # IF food_here THEN Suck and collect food
        if percept["food_here"]:
            return "Suck"

        # IF wall_ahead THEN turn left
        elif percept["wall_ahead"]:
            return "Left"

        # ELSE move forward
        else:
            return "Up"

class ModelBasedAgent:

    def __init__(self):
        self.visited_positions = set()
        self.last_action = None
        self.actions = ["Up", "Right", "Down", "Left"]


    def sense_and_act(self, percept):

        current_position = tuple(percept["agent_pos"])

        self.visited_positions.add(current_position)


        # If food exists
        if percept["food_here"]:
            self.last_action = "Suck"
            return "Suck"
        # If toxin detected, avoid staying
        if percept["smells_toxin"]:
            self.last_action = "Right"
            return "Right"

        # If wall ahead, choose another direction
        if percept["wall_ahead"]:

            for action in self.actions:

                if action != self.last_action:
                    self.last_action = action
                    return action


        # Normal exploration
        for action in self.actions:

            if action == self.last_action:
                continue


            if action == "Up":
                next_position = (
                    current_position[0],
                    current_position[1] + 1
                )

            elif action == "Down":
                next_position = (
                    current_position[0],
                    current_position[1] - 1
                )

            elif action == "Left":
                next_position = (
                    current_position[0] - 1,
                    current_position[1]
                )

            else:
                next_position = (
                    current_position[0] + 1,
                    current_position[1]
                )


            if next_position not in self.visited_positions:
                self.last_action = action
                return action


        # If all visited, move differently
        self.last_action = "Right"
        return "Right"