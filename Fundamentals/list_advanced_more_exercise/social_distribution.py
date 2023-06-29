population = [int(number) for number in input().split(', ')]
min_wealth = int(input())
for digit in population:
    if digit < min_wealth:
        max_wealth = max(population)
        for number in population:
            if number == max_wealth:
                if (max_wealth - (min_wealth - digit)) >= min_wealth:
                    population[population.index(number)] -= (min_wealth - digit)
                else:
                    print('No equal distribution possible')
                    exit()
        population[population.index(digit)] = min_wealth
print(population)
