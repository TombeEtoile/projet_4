import json

from view.match_view import MatchView


class MatchController:

    def __init__(self):
        pass

    @staticmethod
    def get_player_data():

        with open("../player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    def tri_player_by_elo(self):
        """Tri par point elo"""

        data = self.get_player_data()

        return sorted(data, key=lambda x: x["Elo"])

    def elo_pair(self):

        pairs = []
        player_list = self.tri_player_by_elo()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs

    def elo_pair_to_json(self):
        with open("../paires_round_1.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)

    def tri_player_by_point(self):
        """Tri par point compétion"""

        data = self.point_distribution()

        return sorted(data, key=lambda x: x["Point"])

    def point_pair(self):

        pairs = []
        player_list = self.tri_player_by_point()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs

    def point_pair_to_json(self):
        with open("../paires_other_round.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)

    @staticmethod
    def list_for_point_distribution():
        """Création de listes contenant les victoires, défaites et égalités"""

        vote = MatchView.result_round_1()

        round_1_result = {"Victoire": vote[0], "Défaite": vote[1], "Égalité": vote[2] + vote[3]}

        return round_1_result

    def point_distribution(self):
        """Distribution des points"""

        result_match = self.list_for_point_distribution()
        all_players = self.get_player_data()

        for player in all_players:
            if player["Nom"] in result_match["Victoire"]:
                # print(f"{player["Nom"]} = V")
                player["Point"] = +1
            elif player["Nom"] in result_match["Défaite"]:
                # print(f"{player["Nom"]} = D")
                player["Point"] = +0
            elif player["Nom"] in result_match["Égalité"]:
                print(f"{player["Nom"]} = E")
                player["Point"] = +0.5

        return all_players


match_controller = MatchController()
# print(match_controller.get_player_data())

# print(match_controller.tri_player_by_elo())
# print(match_controller.elo_pair())
# print(match_controller.elo_pair_to_json())

# print(match_controller.tri_player_by_point())
# print(match_controller.point_pair())
# print(match_controller.point_pair_to_json())

# print(match_controller.list_for_point_distribution())
# print(match_controller.point_distribution())

