from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

puzzle_data = puzzle.input_data

data = list(
    map(
        lambda elves: list(map(lambda calories: int(calories), elves.split("\n"))),
        puzzle_data.split("\n\n"),
    )
)


def get_max_elf_calories():
    elf_calories = map(sum, data)
    max_elf_calories = max(elf_calories)

    return max_elf_calories


def get_top_three_elf_calories():
    elf_calories = map(sum, data)
    top_three_elf_calories = sorted(elf_calories, reverse=True)[:3]
    top_three_elf_calories_sum = sum(top_three_elf_calories)

    return top_three_elf_calories_sum


print(get_max_elf_calories())
print(get_top_three_elf_calories())
