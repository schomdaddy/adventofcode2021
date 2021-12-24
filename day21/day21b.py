from collections import Counter

def main():
    p1 = 7
    p2 = 3

    game_states = Counter()
    finished_game_states = Counter()

    game_states[(p1, p2, 0, 0, 1)] += 1

    while len(game_states) > 0:
        next_game_states = Counter()
        for state, qty in game_states.items():
            if state[4] == 1:
                for r1 in range(1, 4):
                    for r2 in range(1, 4):
                        for r3 in range(1, 4):
                            new_p1_pos = state[0] + r1 + r2 + r3
                            new_p1_pos = ((new_p1_pos - 1) % 10) + 1
                            new_p1_score = state[2] + new_p1_pos
                            new_state = (new_p1_pos, state[1], new_p1_score, state[3], 2)
                            if new_p1_score >= 21:
                                finished_game_states[new_state] += qty
                            else:
                                next_game_states[new_state] += qty
            else:
                for r1 in range(1, 4):
                    for r2 in range(1, 4):
                        for r3 in range(1, 4):
                            new_p2_pos = state[1] + r1 + r2 + r3
                            new_p2_pos = ((new_p2_pos - 1) % 10) + 1
                            new_p2_score = state[3] + new_p2_pos
                            new_state = (state[0], new_p2_pos, state[2], new_p2_score, 1)
                            if new_p2_score >= 21:
                                finished_game_states[new_state] += qty
                            else:
                                next_game_states[new_state] += qty
            game_states = next_game_states.copy()

    p1_wins = 0
    p2_wins = 0
    for state, cnt in finished_game_states.items():
        if state[2] >= 21:
            p1_wins += cnt
        else:
            p2_wins += cnt
    print(max(p1_wins, p2_wins))
main()