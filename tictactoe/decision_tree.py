from __future__ import print_function # Python 2/3 compatibility
import itertools
import tictactoe

def get_permutations(num):
    print('Generating permutations for num={}..'.format(num))
    return [x for x in itertools.permutations(range(1, num+1))]

def starts_with(starting_elements, array):
    """Filter out states that start with the n-th initial moves"""
    if starting_elements == array[:len(starting_elements)]:
        return array
    else:
        return None

def generate_decision_table(end_games, simulated_games):
    """
    Populate decision table with all possible states
    with outcomes from a simulated dataset.
    """

    print('Matching simulated games with possible end games...')
    table = []
    for game in simulated_games:
        gg = tuple(game[0])
        if gg in end_games:
            i = end_games.index(gg)
            new_game = {
                'state': list(end_games[i]),
                'choice': 0,
                'outcome': game[1]
            }
            table.append(new_game)

    print('Printing first 20 states...')
    for state in table[:20]:
        print(state)

    print('Returned {} states with outcomes.'.format(len(table)))
    wins = sum(1 for s in table if s.get('outcome') == 1)
    print('P1 won {} games.'.format(wins))
    return table


def main():
    p = get_permutations(9)
    simul = tictactoe.main()
    generate_decision_table(p, simul)


if __name__ == '__main__':
    main()
