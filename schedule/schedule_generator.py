import uuid
import itertools
import random


class Game:
    def __init__(self, team1, team2):
        self.id = uuid.uuid4()
        self.team1 = team1
        self.team2 = team2

    def __str__(self):
        return f"{' / '.join(self.team1)} vs. {' / '.join(self.team2)}"


class Round:
    def __init__(self, round_number, games):
        self.id = uuid.uuid4()
        self.round_number = round_number
        self.games = games
        self.players_sitting_out = []

    def game_descriptions(self):
        return [f"Court {i + 1}: {str(game)}" for i, game in
                enumerate(self.games)]


def combinations(arr, size):
    return list(itertools.combinations(arr, size))


def generate_round(num_courts, player_names, games_counter, team_history):
    num_players = len(player_names)
    if num_players < 4:
        print("Error: Not enough players or player names provided.")
        return []

    player_indices = list(range(num_players))
    round_games = []
    used_players = set()
    all_players = set(player_indices)
    random.shuffle(player_indices)

    priority_players = sorted(
        player_indices, key=lambda x: games_counter[x])
    max_games_per_round = min(num_courts, num_players // 4)

    for combo in combinations(priority_players, 4):
        for team_indexes in combinations(combo, 2):
            remaining_indexes = set(combo) - set(team_indexes)

            if len(remaining_indexes) == 2:
                team1 = list(sorted(team_indexes))
                team2 = list(sorted(remaining_indexes))

                if team1 not in team_history and team2 not in team_history and used_players.isdisjoint(team1) and used_players.isdisjoint(team2):

                    new_game = Game([player_names[i] for i in team1], [
                                    player_names[i] for i in team2])
                    round_games.append(new_game)

                    team_history.append(team1)
                    team_history.append(team2)
                    used_players.update(team1)
                    used_players.update(team2)
                    for player in team1:
                        games_counter[player] += 1
                    for player in team2:
                        games_counter[player] += 1

                    if len(round_games) >= max_games_per_round:
                        sitting_out = [player_names[i]
                                       for i in (all_players - used_players)]
                        print('type', type(team_history))
                        return round_games, sitting_out, games_counter, team_history

    return None
