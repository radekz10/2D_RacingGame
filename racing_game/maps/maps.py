
from racing_game.cars.enemy import EnemyPlayer
from racing_game.cars.pc import PCPlayer
from racing_game.cars.player import Player
from racing_game.config import settings
from racing_game.maps.map_loop import MapLoop
from racing_game.ui import loading_images
from racing_game.ui.draw_ui import DrawUI


class AllMaps:

    # FIRST MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.first_map_route, loading_images.green_forest,
                     loading_images.first_map, loading_images.first_map_border,
                     AllMaps.first_map_vs_pc, Player.respawn_first_map, PCPlayer.respawn_first_map,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    @staticmethod
    def first_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, None, None, loading_images.green_forest,
                     loading_images.first_map, loading_images.first_map_border,
                     AllMaps.first_map_solo, Player.respawn_first_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    @staticmethod
    def first_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "I. MAP", loading_images.first_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, loading_images.green_forest,
                     loading_images.first_map, loading_images.first_map_border,
                     AllMaps.first_map_1v1, Player.respawn_first_map, EnemyPlayer.respawn_first_map,
                     loading_images.finish_line, settings.FINISH_LINES[1]["FINISH_LINE"],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[1]["FINISH_LINE_RANGES"][1][1],
                     settings.first_map_lap_times_file, settings.first_map_match_times_file)

    # SECOND MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def second_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.second_map_route, loading_images.dark_green_forest,
                     loading_images.second_map, loading_images.second_map_border,
                     AllMaps.second_map_vs_pc, Player.respawn_second_map, PCPlayer.respawn_second_map,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    @staticmethod
    def second_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, None, None, loading_images.dark_green_forest,
                     loading_images.second_map, loading_images.second_map_border,
                     AllMaps.second_map_solo, Player.respawn_second_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    @staticmethod
    def second_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "II. MAP", loading_images.second_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, loading_images.dark_green_forest,
                     loading_images.second_map, loading_images.second_map_border,
                     AllMaps.second_map_1v1, Player.respawn_second_map, EnemyPlayer.respawn_second_map,
                     loading_images.finish_line, settings.FINISH_LINES[2]["FINISH_LINE"],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[2]["FINISH_LINE_RANGES"][1][1],
                     settings.second_map_lap_times_file, settings.second_map_match_times_file)

    # THIRD MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def third_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.third_map_route, loading_images.green_forest,
                     loading_images.third_map, loading_images.third_map_border,
                     AllMaps.third_map_vs_pc, Player.respawn_third_map, PCPlayer.respawn_third_map,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    @staticmethod
    def third_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, None, None, loading_images.green_forest,
                     loading_images.third_map, loading_images.third_map_border,
                     AllMaps.third_map_solo, Player.respawn_third_map, None,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    @staticmethod
    def third_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "III. MAP", loading_images.third_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, loading_images.green_forest,
                     loading_images.third_map, loading_images.third_map_border,
                     AllMaps.third_map_1v1, Player.respawn_third_map, EnemyPlayer.respawn_third_map,
                     loading_images.finish_line, settings.FINISH_LINES[3]["FINISH_LINE"],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[3]["FINISH_LINE_RANGES"][1][1],
                     settings.third_map_lap_times_file, settings.third_map_match_times_file)

    # FOURTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fourth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, loading_images.dark_green_forest,
                     loading_images.fourth_map, loading_images.fourth_map_border,
                     AllMaps.fourth_map_vs_pc, Player.respawn_fourth_map, PCPlayer.respawn_fourth_map,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    @staticmethod
    def fourth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, None, None, loading_images.dark_green_forest,
                     loading_images.fourth_map, loading_images.fourth_map_border,
                     AllMaps.fourth_map_solo, Player.respawn_fourth_map, None,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    @staticmethod
    def fourth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "IV. MAP", loading_images.fourth_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, loading_images.dark_green_forest,
                     loading_images.fourth_map, loading_images.fourth_map_border,
                     AllMaps.fourth_map_1v1, Player.respawn_fourth_map, EnemyPlayer.respawn_fourth_map,
                     loading_images.finish_line_x3, settings.FINISH_LINES[4]["FINISH_LINE"],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[4]["FINISH_LINE_RANGES"][1][1],
                     settings.fourth_map_lap_times_file, settings.fourth_map_match_times_file)

    # FIFTH MAP --------------------------------------------------------------------------------------------------
    @staticmethod
    def fifth_map_vs_pc():

        DrawUI.loading_game("Loading", "VS PC", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, PCPlayer, PCPlayer.fourth_map_route, loading_images.green_forest,
                     loading_images.fifth_map, loading_images.fifth_map_border,
                     AllMaps.fifth_map_vs_pc, Player.respawn_fifth_map, PCPlayer.respawn_fifth_map,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_solo():

        DrawUI.loading_game("Loading", "SOLO", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, None, None, loading_images.green_forest,
                     loading_images.fifth_map, loading_images.fifth_map_border,
                     AllMaps.fifth_map_solo, Player.respawn_fifth_map, None,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)

    @staticmethod
    def fifth_map_1v1():

        DrawUI.loading_game("Loading", "1V1", "V. MAP", loading_images.fifth_map_loading)

        MapLoop.loop(Player, EnemyPlayer, None, loading_images.green_forest,
                     loading_images.fifth_map, loading_images.fifth_map_border,
                     AllMaps.fifth_map_1v1, Player.respawn_fifth_map, EnemyPlayer.respawn_fifth_map,
                     loading_images.finish_line_x2, settings.FINISH_LINES[5]["FINISH_LINE"],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][0],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][0][1],
                     settings.FINISH_LINES[5]["FINISH_LINE_RANGES"][1][1],
                     settings.fifth_map_lap_times_file, settings.fifth_map_match_times_file)
