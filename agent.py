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

