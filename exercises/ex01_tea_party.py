"""EX01 Tea Party"""

__author__ = "730466997"


def main_planner(guests: int) -> None:
    """Main function of the program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    tea_count: int = tea_bags(people=guests)
    treat_count: int = treats(people=guests)
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(cost(tea_count=tea_count, treat_count=treat_count)))
    return None


def tea_bags(people: int) -> int:
    """Finds number of tea bags."""
    return people * 2


def treats(people: int) -> int:
    """Find number of treats."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the party."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
