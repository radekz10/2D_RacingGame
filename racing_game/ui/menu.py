import pygame

from racing_game.config.settings import Settings
from racing_game.maps.maps import AllMaps
from racing_game.storage.data_processing import DataProcessing
from racing_game.ui.draw_ui import DrawUI
from racing_game.ui.loading_images import LoadingImages
from racing_game.ui.button import Button


class Menu:
    TITLE_Y = 70
    TITLE_COLOR = "purple"
    QUIT_X = 977
    QUIT_Y = 980

    # MAP SELECTION --------------------------------------------------------------------------------------------------------
    @staticmethod
    def map_selection(first_button, second_button, third_button, fourth_button, fifth_button):
        while 1:

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("MAP SELECTION", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 680, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (1830, 250))
            DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.MEDIUM_FONT, "cyan", 1850, 210,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("I. MAP", LoadingImages.SMALL_FONT, "cyan", 410, 380, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("II. MAP", LoadingImages.SMALL_FONT, "cyan", 940, 340, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("III. MAP", LoadingImages.SMALL_FONT, "cyan", 1440, 315, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("IV. MAP", LoadingImages.SMALL_FONT, "cyan", 675, 615, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("V. MAP", LoadingImages.SMALL_FONT, "cyan", 1185, 615, LoadingImages.GAME_SCREEN)

            first_map_button = Button(button_image=LoadingImages.MAP_SELECTION[1]["MAP"], x_y=(500, 450),
                                      button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                      font_hover_color="cyan")

            second_map_button = Button(button_image=LoadingImages.MAP_SELECTION[2]["MAP"], x_y=(970, 450),
                                       button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                       font_hover_color="cyan")

            third_map_button = Button(button_image=LoadingImages.MAP_SELECTION[3]["MAP"], x_y=(1470, 450),
                                      button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                      font_hover_color="cyan")

            fourth_map_button = Button(button_image=LoadingImages.MAP_SELECTION[4]["MAP"], x_y=(700, 750),
                                       button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                       font_hover_color="cyan")

            fifth_map_button = Button(button_image=LoadingImages.MAP_SELECTION[5]["MAP"], x_y=(1220, 750),
                                      button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                      font_hover_color="cyan")

            settings_button = Button(button_image=LoadingImages.BUTTONS[5]["BUTTON"], x_y=(1860, 60), button_text="",
                                     font=LoadingImages.NORMAL_FONT,
                                     font_color="white", font_hover_color="cyan")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            first_map_button.button_render(LoadingImages.GAME_SCREEN)
            second_map_button.button_render(LoadingImages.GAME_SCREEN)
            third_map_button.button_render(LoadingImages.GAME_SCREEN)
            fourth_map_button.button_render(LoadingImages.GAME_SCREEN)
            fifth_map_button.button_render(LoadingImages.GAME_SCREEN)
            settings_button.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            if not Settings.win_coins >= 5:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (915, 400))

            if not Settings.win_coins >= 10:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (1420, 400))

            if not Settings.win_coins >= 20:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (655, 700))

            if not Settings.win_coins >= 30:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (1160, 700))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if first_map_button.on_click(mouse_coordinates):
                        first_button()

                    if second_map_button.on_click(mouse_coordinates):
                        if Settings.win_coins >= 5:
                            second_button()
                        else:
                            Menu.map_locked_alert()

                    if third_map_button.on_click(mouse_coordinates):
                        if Settings.win_coins >= 10:
                            third_button()
                        else:
                            Menu.map_locked_alert()

                    if fourth_map_button.on_click(mouse_coordinates):
                        if Settings.win_coins >= 20:
                            fourth_button()
                        else:
                            Menu.map_locked_alert()

                    if fifth_map_button.on_click(mouse_coordinates):
                        if Settings.win_coins >= 30:
                            fifth_button()
                        else:
                            Menu.map_locked_alert()

                    if settings_button.on_click(mouse_coordinates):
                        Menu.laps_settings()

                    if back_button.on_click(mouse_coordinates):
                        mode_selection()

            pygame.display.update()

    @staticmethod
    def map_locked_alert():
        DrawUI.draw_text("Map Locked!", LoadingImages.NORMAL_FONT, "red", 830, 230, LoadingImages.GAME_SCREEN)
        pygame.display.update()
        pygame.time.wait(1200)

    @staticmethod
    def laps_settings():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("LAPS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 880, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("DEFAULT - 3 LAPS", LoadingImages.MEDIUM_FONT, "grey", 1680, 1030,
                             LoadingImages.GAME_SCREEN)

            lap_button2 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(760, 400),
                                 button_text="2", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            lap_button3 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(970, 400),
                                 button_text="3", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            lap_button4 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(1180, 400),
                                 button_text="4", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            lap_button5 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(760, 600),
                                 button_text="6", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            lap_button6 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(970, 600),
                                 button_text="8", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            lap_button7 = Button(button_image=LoadingImages.ON_OFF_BUTTONS[2]["BUTTON"], x_y=(1180, 600),
                                 button_text="10", font=LoadingImages.NORMAL_FONT, font_color="white",
                                 font_hover_color="cyan")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            lap_button2.button_render(LoadingImages.GAME_SCREEN)
            lap_button3.button_render(LoadingImages.GAME_SCREEN)
            lap_button4.button_render(LoadingImages.GAME_SCREEN)
            lap_button5.button_render(LoadingImages.GAME_SCREEN)
            lap_button6.button_render(LoadingImages.GAME_SCREEN)
            lap_button7.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(lap_button2, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(lap_button3, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(lap_button4, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(lap_button5, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(lap_button6, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(lap_button7, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if lap_button2.on_click(mouse_coordinates):
                        Settings.max_laps = 2
                        Menu.set_text()

                    if lap_button3.on_click(mouse_coordinates):
                        Settings.max_laps = 3
                        Menu.set_text()

                    if lap_button4.on_click(mouse_coordinates):
                        Settings.max_laps = 4
                        Menu.set_text()

                    if lap_button5.on_click(mouse_coordinates):
                        Settings.max_laps = 6
                        Menu.set_text()

                    if lap_button6.on_click(mouse_coordinates):
                        Settings.max_laps = 8
                        Menu.set_text()

                    if lap_button7.on_click(mouse_coordinates):
                        Settings.max_laps = 10
                        Menu.set_text()

                    if back_button.on_click(mouse_coordinates):
                        mode_selection()

            pygame.display.update()

    @staticmethod
    def set_text():
        DrawUI.draw_text("LAPS SET!", LoadingImages.NORMAL_FONT, "green", 860, 230, LoadingImages.GAME_SCREEN)
        pygame.display.update()
        pygame.time.wait(700)

    # CAR SELECTION --------------------------------------------------------------------------------------------------------
    @staticmethod
    def car_formula_selection():
        Menu.car_color_selection("FORMULA", 790, "BLUE", "ORANGE", "YELLOW", "GREEN",
                                 "cyan", "orange", "yellow", "green",
                                 LoadingImages.FORMULA_SELECTION[1]["CAR"], LoadingImages.FORMULA_SELECTION[2]["CAR"],
                                 LoadingImages.FORMULA_SELECTION[3]["CAR"], LoadingImages.FORMULA_SELECTION[4]["CAR"],
                                 1, 2, 3, 4)

    @staticmethod
    def car_lambo_selection():
        Menu.car_color_selection("SPORTS CAR I.", 710, "BLUE", "CRIMSON", "L - BLUE", "PINK",
                                 "blue", "red", "cyan", "pink",
                                 LoadingImages.SPORTS_CAR_I_SELECTION[1]["CAR"],
                                 LoadingImages.SPORTS_CAR_I_SELECTION[3]["CAR"],
                                 LoadingImages.SPORTS_CAR_I_SELECTION[2]["CAR"],
                                 LoadingImages.SPORTS_CAR_I_SELECTION[4]["CAR"],
                                 5, 7, 6, 8)

    @staticmethod
    def car_spoiler_car_selection():
        Menu.car_color_selection("SPORTS CAR II.", 710, "CYAN", "PURPLE", "ORANGE", "PINK",
                                 "cyan", "violet", "orange", "pink",
                                 LoadingImages.SPORTS_CAR_II_SELECTION[2]["CAR"],
                                 LoadingImages.SPORTS_CAR_II_SELECTION[1]["CAR"],
                                 LoadingImages.SPORTS_CAR_II_SELECTION[3]["CAR"],
                                 LoadingImages.SPORTS_CAR_II_SELECTION[4]["CAR"],
                                 10, 9, 11, 12)

    @staticmethod
    def car_cabrio_selection():
        Menu.car_color_selection("CABRIO", 820, "BLUE", "L - BLUE", "YELLOW", "RED",
                                 "blue", "cyan", "yellow", "red",
                                 LoadingImages.CABRIO_SELECTION[1]["CAR"], LoadingImages.CABRIO_SELECTION[2]["CAR"],
                                 LoadingImages.CABRIO_SELECTION[4]["CAR"], LoadingImages.CABRIO_SELECTION[3]["CAR"],
                                 13, 14, 16, 15)

    @staticmethod
    def car_color_selection(car_title, title_x, title1, title2, title3, title4,
                            color1, color2, color3, color4,
                            image1, image2, image3, image4,
                            car_option1, car_option2, car_option3, car_option4):
        while 1:

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text(car_title, LoadingImages.BIG_FONT, Menu.TITLE_COLOR, title_x, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (1830, 250))
            DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.MEDIUM_FONT, "cyan", 1850, 210,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text(title1, LoadingImages.SMALL_FONT, color1, 330, 340, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(title2, LoadingImages.SMALL_FONT, color2, 717, 340, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(title3, LoadingImages.SMALL_FONT, color3, 1120, 340, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(title4, LoadingImages.SMALL_FONT, color4, 1530, 340, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("DEFAULT - BLUE FORMULA", LoadingImages.MEDIUM_FONT, "grey", 1580, 1030,
                             LoadingImages.GAME_SCREEN)

            first_button = Button(x_y=(350, 550), button_image=image1, button_text="",
                                  font=LoadingImages.SMALL_FONT,
                                  font_color="white", font_hover_color="cyan")

            DrawUI.draw_text("FREE", LoadingImages.SMALL_FONT, "grey", 335, 750, LoadingImages.GAME_SCREEN)

            second_button = Button(x_y=(750, 550), button_image=image2, button_text="",
                                   font=LoadingImages.SMALL_FONT,
                                   font_color="white", font_hover_color="cyan")

            DrawUI.draw_text("5 WINS NEEDED", LoadingImages.SMALL_FONT, "grey", 695, 750, LoadingImages.GAME_SCREEN)

            third_button = Button(x_y=(1150, 550), button_image=image3, button_text="",
                                  font=LoadingImages.SMALL_FONT,
                                  font_color="white", font_hover_color="cyan")

            DrawUI.draw_text("15 WINS NEEDED", LoadingImages.SMALL_FONT, "grey", 1090, 750, LoadingImages.GAME_SCREEN)

            fourth_button = Button(x_y=(1550, 550), button_image=image4, button_text="",
                                   font=LoadingImages.SMALL_FONT,
                                   font_color="white", font_hover_color="cyan")

            DrawUI.draw_text("25 WINS NEEDED", LoadingImages.SMALL_FONT, "grey", 1490, 750, LoadingImages.GAME_SCREEN)

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            first_button.button_render(LoadingImages.GAME_SCREEN)
            second_button.button_render(LoadingImages.GAME_SCREEN)
            third_button.button_render(LoadingImages.GAME_SCREEN)
            fourth_button.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            if not Settings.win_coins >= 5:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (700, 380))

            if not Settings.win_coins >= 15:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (1100, 380))

            if not Settings.win_coins >= 25:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.lock_icon, (1500, 380))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if first_button.on_click(mouse_coordinates):
                        Settings.car_type = car_option1
                        DrawUI.draw_text("Car Selected!", LoadingImages.NORMAL_FONT, color1, 810, 230,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)
                        Menu.main_menu()

                    if second_button.on_click(mouse_coordinates):

                        if Settings.win_coins >= 5:
                            Settings.car_type = car_option2
                            DrawUI.draw_text("Car Selected!", LoadingImages.NORMAL_FONT, color2, 810, 230,
                                             LoadingImages.GAME_SCREEN)
                            pygame.display.update()
                            pygame.time.wait(1200)
                            Menu.main_menu()
                        else:
                            Menu.car_locked_alert()

                    if third_button.on_click(mouse_coordinates):

                        if Settings.win_coins >= 15:
                            Settings.car_type = car_option3
                            DrawUI.draw_text("Car Selected!", LoadingImages.NORMAL_FONT, color3, 810, 230,
                                             LoadingImages.GAME_SCREEN)
                            pygame.display.update()
                            pygame.time.wait(1200)
                            Menu.main_menu()

                        else:
                            Menu.car_locked_alert()

                    if fourth_button.on_click(mouse_coordinates):

                        if Settings.win_coins >= 25:
                            Settings.car_type = car_option4
                            DrawUI.draw_text("Car Selected!", LoadingImages.NORMAL_FONT, color4, 810, 230,
                                             LoadingImages.GAME_SCREEN)
                            pygame.display.update()
                            pygame.time.wait(1200)
                            Menu.main_menu()

                        else:
                            Menu.car_locked_alert()

                    if back_button.on_click(mouse_coordinates):
                        Menu.car_selection()

            pygame.display.update()

    @staticmethod
    def car_locked_alert():
        DrawUI.draw_text("Car Locked!", LoadingImages.NORMAL_FONT, "red", 810, 230, LoadingImages.GAME_SCREEN)
        pygame.display.update()
        pygame.time.wait(1200)

    @staticmethod
    def car_selection():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("CAR SELECTION", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 680, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (1830, 250))
            DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.MEDIUM_FONT, "cyan", 1850, 210,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("FORMULA", LoadingImages.SMALL_FONT, "white", 320, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("SPORTS CAR I.", LoadingImages.SMALL_FONT, "white", 700, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("SPORTS CAR II.", LoadingImages.SMALL_FONT, "white", 1095, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("CABRIO", LoadingImages.SMALL_FONT, "white", 1520, 330, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("DEFAULT - BLUE FORMULA", LoadingImages.MEDIUM_FONT, "grey", 1580, 1030,
                             LoadingImages.GAME_SCREEN)

            formula_button = Button(x_y=(350, 550), button_image=LoadingImages.CAR_SELECTION[1]["CAR"], button_text="",
                                    font=LoadingImages.SMALL_FONT,
                                    font_color="white", font_hover_color="cyan")

            lambo_button = Button(x_y=(750, 550), button_image=LoadingImages.CAR_SELECTION[2]["CAR"], button_text="",
                                  font=LoadingImages.SMALL_FONT,
                                  font_color="white", font_hover_color="cyan")

            spoiler_car_button = Button(x_y=(1150, 550), button_image=LoadingImages.CAR_SELECTION[3]["CAR"],
                                        button_text="",
                                        font=LoadingImages.SMALL_FONT, font_color="white", font_hover_color="cyan")

            cabrio_button = Button(x_y=(1550, 550), button_image=LoadingImages.CAR_SELECTION[4]["CAR"], button_text="",
                                   font=LoadingImages.SMALL_FONT, font_color="white", font_hover_color="cyan")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            formula_button.button_render(LoadingImages.GAME_SCREEN)
            lambo_button.button_render(LoadingImages.GAME_SCREEN)
            spoiler_car_button.button_render(LoadingImages.GAME_SCREEN)
            cabrio_button.button_render(LoadingImages.GAME_SCREEN)
            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if formula_button.on_click(mouse_coordinates):
                        Menu.car_formula_selection()

                    if lambo_button.on_click(mouse_coordinates):
                        Menu.car_lambo_selection()

                    if spoiler_car_button.on_click(mouse_coordinates):
                        Menu.car_spoiler_car_selection()

                    if cabrio_button.on_click(mouse_coordinates):
                        Menu.car_cabrio_selection()

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()

    # GAME BINDS -----------------------------------------------------------------------------------------------------------
    @staticmethod
    def binds():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("BINDS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 850, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("CAR CONTROL", LoadingImages.NORMAL_FONT, "purple", 495, 200, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("W", LoadingImages.MEDIUM_FONT, "white", 625, 280, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Forward", LoadingImages.MEDIUM_FONT, "cyan", 1220, 280, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("S", LoadingImages.MEDIUM_FONT, "white", 630, 330, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Backward", LoadingImages.MEDIUM_FONT, "cyan", 1220, 330, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("A", LoadingImages.MEDIUM_FONT, "white", 630, 380, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Left", LoadingImages.MEDIUM_FONT, "cyan", 1220, 380, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("D", LoadingImages.MEDIUM_FONT, "white", 630, 430, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Right", LoadingImages.MEDIUM_FONT, "cyan", 1220, 430, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("CAR ABILITIES", LoadingImages.NORMAL_FONT, "purple", 495, 480, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("E", LoadingImages.MEDIUM_FONT, "white", 632, 560, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Nitro", LoadingImages.MEDIUM_FONT, "cyan", 1220, 560, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("Q", LoadingImages.MEDIUM_FONT, "white", 630, 610, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Faster Movement", LoadingImages.MEDIUM_FONT, "cyan", 1220, 610, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("IN-GAME", LoadingImages.NORMAL_FONT, "purple", 550, 660, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("R", LoadingImages.MEDIUM_FONT, "white", 630, 740, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Restart Game", LoadingImages.MEDIUM_FONT, "cyan", 1220, 740, LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("X", LoadingImages.MEDIUM_FONT, "white", 630, 790, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("Exit", LoadingImages.MEDIUM_FONT, "cyan", 1220, 790, LoadingImages.GAME_SCREEN)

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()

    # GAME SETTINGS --------------------------------------------------------------------------------------------------------
    @staticmethod
    def game_settings():
        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("SETTINGS", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 790, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("AUDIO", LoadingImages.NORMAL_FONT, "cyan", 620, 300, LoadingImages.GAME_SCREEN)
            # draw_text("CAMERA FOCUS", normal_font, "cyan", 620, 400, GAME_SCREEN)
            DrawUI.draw_text("VSYNC", LoadingImages.NORMAL_FONT, "cyan", 620, 400, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("UI", LoadingImages.NORMAL_FONT, "cyan", 620, 500, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("FPS", LoadingImages.NORMAL_FONT, "cyan", 620, 600, LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("CAR XY", LoadingImages.NORMAL_FONT, "cyan", 620, 700, LoadingImages.GAME_SCREEN)

            audio_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 340),
                                     button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                     font_hover_color="cyan")

            audio_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 340),
                                      button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                      font_hover_color="purple")

            # camera_on_button = Button(button_image=on_off_button, x_y=(1220, 440),
            # button_text="ON", font=small_font, font_color="white", font_hover_color="white")

            # camera_off_button = Button(button_image=on_off_button, x_y=(1300, 440),
            # button_text="OFF", font=small_font, font_color="white", font_hover_color="white")

            vsync_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 440),
                                     button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                     font_hover_color="cyan")
            vsync_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 440),
                                      button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                      font_hover_color="purple")

            show_ui_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 540),
                                       button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                       font_hover_color="cyan")
            show_ui_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 540),
                                        button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="purple")

            show_fps_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 640),
                                        button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="cyan")
            show_fps_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 640),
                                         button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                         font_hover_color="purple")

            show_xy_on_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1220, 740),
                                       button_text="ON", font=LoadingImages.SMALL_FONT, font_color="white",
                                       font_hover_color="cyan")
            show_xy_off_button = Button(button_image=LoadingImages.ON_OFF_BUTTONS[1]["BUTTON"], x_y=(1300, 740),
                                        button_text="OFF", font=LoadingImages.SMALL_FONT, font_color="white",
                                        font_hover_color="purple")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            audio_on_button.button_render(LoadingImages.GAME_SCREEN)
            audio_off_button.button_render(LoadingImages.GAME_SCREEN)

            # camera_on_button.button_render(GAME_SCREEN)
            # camera_off_button.button_render(GAME_SCREEN)

            vsync_on_button.button_render(LoadingImages.GAME_SCREEN)
            vsync_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_ui_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_ui_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_fps_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_fps_off_button.button_render(LoadingImages.GAME_SCREEN)

            show_xy_on_button.button_render(LoadingImages.GAME_SCREEN)
            show_xy_off_button.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(audio_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(audio_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(vsync_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(vsync_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_ui_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_ui_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_fps_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_fps_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(show_xy_on_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(show_xy_off_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if audio_on_button.on_click(mouse_coordinates):
                        Settings.audio = 1
                        DrawUI.draw_text("AUDIO ON!", LoadingImages.NORMAL_FONT, "green", 850, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if audio_off_button.on_click(mouse_coordinates):
                        Settings.audio = 2
                        DrawUI.draw_text("AUDIO OFF!", LoadingImages.NORMAL_FONT, "green", 850, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    # if camera_on_button.on_click(mouse_coordinates):
                    #  settings.camera_focus = 1
                    #  draw_text("CAMERA FOCUS ON!", normal_font, "green", 730, 210, GAME_SCREEN)
                    #  pygame.display.update()
                    # pygame.time.wait(2000)

                    # if camera_off_button.on_click(mouse_coordinates):
                    # settings.camera_focus = 2
                    # draw_text("CAMERA FOCUS OFF!", normal_font, "green", 730, 210, GAME_SCREEN)
                    # pygame.display.update()
                    # pygame.time.wait(2000)

                    if vsync_on_button.on_click(mouse_coordinates):
                        Settings.vsync = 1
                        DrawUI.draw_text("VSYNC ON!", LoadingImages.NORMAL_FONT, "green", 850, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if vsync_off_button.on_click(mouse_coordinates):
                        Settings.vsync = 0
                        DrawUI.draw_text("VSYNC OFF!", LoadingImages.NORMAL_FONT, "green", 850, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if show_ui_on_button.on_click(mouse_coordinates):
                        Settings.show_ui = 1
                        DrawUI.draw_text("UI ON!", LoadingImages.NORMAL_FONT, "green", 900, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if show_ui_off_button.on_click(mouse_coordinates):
                        Settings.show_ui = 2
                        DrawUI.draw_text("UI OFF!", LoadingImages.NORMAL_FONT, "green", 900, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if show_fps_on_button.on_click(mouse_coordinates):
                        Settings.show_fps = 1
                        DrawUI.draw_text("FPS ON!", LoadingImages.NORMAL_FONT, "green", 890, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if show_fps_off_button.on_click(mouse_coordinates):
                        Settings.show_fps = 2
                        DrawUI.draw_text("FPS OFF!", LoadingImages.NORMAL_FONT, "green", 890, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    if show_xy_on_button.on_click(mouse_coordinates):
                        Settings.show_xy = 1
                        DrawUI.draw_text("X-Y ON!", LoadingImages.NORMAL_FONT, "green", 890, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    # Menu.change_settings(show_xy_on_button, mouse_coordinates, Settings.show_xy == 1, "X-Y ON!", 890)

                    if show_xy_off_button.on_click(mouse_coordinates):
                        Settings.show_xy = 2
                        DrawUI.draw_text("X-Y OFF!", LoadingImages.NORMAL_FONT, "green", 890, 210,
                                         LoadingImages.GAME_SCREEN)
                        pygame.display.update()
                        pygame.time.wait(1200)

                    # Menu.change_settings(show_xy_off_button, mouse_coordinates, Settings.show_xy == 2, "X-Y OFF!", 890)

                    # change_settings(show_xy_off_button, mouse_coordinates, settings.show_xy, 2, "X-Y OFF!")

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()

    @staticmethod
    def change_settings(button, mouse_coordinates, command, title, title_x):

        if button.on_click(mouse_coordinates):
            settings = command
            DrawUI.draw_text(title, LoadingImages.NORMAL_FONT, "green", title_x, 210, LoadingImages.GAME_SCREEN)

            pygame.display.update()
            pygame.time.wait(1200)

            return settings

    # MAIN MENU ------------------------------------------------------------------------------------------------------------
    @staticmethod
    def main_menu():
        pygame.display.set_caption("2D Racing Game - Menu")

        while 1:

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text("MAIN MENU", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 750, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (1830, 250))
            DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.MEDIUM_FONT, "cyan", 1850, 210,
                             LoadingImages.GAME_SCREEN)

            play_button = Button(button_image=LoadingImages.BUTTONS[2]["BUTTON"], x_y=(976, 430),
                                 button_text="PLAY",
                                 font=LoadingImages.BIG_FONT,
                                 font_color="white", font_hover_color="cyan")

            car_selection_button = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(756, 630),
                                          button_text="SELECT CAR",
                                          font=LoadingImages.NORMAL_FONT,
                                          font_color="white", font_hover_color="cyan")

            stats_button = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(1196, 630),
                                  button_text="STATS",
                                  font=LoadingImages.NORMAL_FONT,
                                  font_color="white", font_hover_color="cyan")

            # binds_button = Button(button_image=button_transparent_image, x_y=(976, 630), button_text="BINDS",
            # font=normal_font,
            # font_color="white", font_hover_color="cyan")

            binds_button = Button(button_image=LoadingImages.BUTTONS[6]["BUTTON"], x_y=(60, 60), button_text="",
                                  font=LoadingImages.NORMAL_FONT,
                                  font_color="white", font_hover_color="cyan")

            # settings_button = Button(button_image=settings_button_icon, x_y=(960, 550), button_text="SETTINGS",
            # font=normal_font,
            # font_color="white", font_hover_color="cyan")

            settings_button = Button(button_image=LoadingImages.BUTTONS[5]["BUTTON"], x_y=(1860, 60), button_text="",
                                     font=LoadingImages.NORMAL_FONT,
                                     font_color="white", font_hover_color="cyan")

            quit_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="QUIT",
                                 font=LoadingImages.NORMAL_FONT,
                                 font_color="orange", font_hover_color="red")

            play_button.button_render(LoadingImages.GAME_SCREEN)
            car_selection_button.button_render(LoadingImages.GAME_SCREEN)
            stats_button.button_render(LoadingImages.GAME_SCREEN)
            binds_button.button_render(LoadingImages.GAME_SCREEN)
            settings_button.button_render(LoadingImages.GAME_SCREEN)
            quit_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(play_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(car_selection_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(stats_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(binds_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(settings_button, mouse_coordinates, LoadingImages.GAME_SCREEN)
            Button.button_hover_render(quit_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.on_click(mouse_coordinates):
                        mode_selection()
                    if car_selection_button.on_click(mouse_coordinates):
                        Menu.car_selection()
                    if stats_button.on_click(mouse_coordinates):
                        # stats_first_map()
                        Menu.first_map_stats()
                    if binds_button.on_click(mouse_coordinates):
                        Menu.binds()
                    if settings_button.on_click(mouse_coordinates):
                        Menu.game_settings()
                    if quit_button.on_click(mouse_coordinates):
                        pygame.quit()

            pygame.display.update()

    # MAP STATS ------------------------------------------------------------------------------------------------------------
    @staticmethod
    def first_map_stats():
        Menu.map_stats("FIRST MAP STATS", Settings.FILE_PATHS[1]["LAP_TIMES"], Settings.FILE_PATHS[1]["MATCH_TIMES"],
                       2, 1, 2, Menu.second_map_stats)

    @staticmethod
    def second_map_stats():
        Menu.map_stats("SECOND MAP STATS", Settings.FILE_PATHS[2]["LAP_TIMES"], Settings.FILE_PATHS[2]["MATCH_TIMES"],
                       1, 1, Menu.first_map_stats, Menu.third_map_stats)

    @staticmethod
    def third_map_stats():
        Menu.map_stats("THIRD MAP STATS", Settings.FILE_PATHS[3]["LAP_TIMES"], Settings.FILE_PATHS[3]["MATCH_TIMES"],
                       1, 1, Menu.second_map_stats, Menu.fourth_map_stats)

    @staticmethod
    def fourth_map_stats():
        Menu.map_stats("FOURTH MAP STATS", Settings.FILE_PATHS[4]["LAP_TIMES"], Settings.FILE_PATHS[4]["MATCH_TIMES"],
                       1, 1, Menu.third_map_stats, Menu.fifth_map_stats)

    @staticmethod
    def fifth_map_stats():
        Menu.map_stats("FIFTH MAP STATS", Settings.FILE_PATHS[5]["LAP_TIMES"], Settings.FILE_PATHS[5]["MATCH_TIMES"],
                       1, 2, Menu.fourth_map_stats, 2)

    @staticmethod
    def map_stats(title, lap_times_file, match_times_file,
                  show_pointer_left, show_pointer_right,
                  pointer_left_map, pointer_right_map):

        global pointer_left_button, pointer_right_button

        loading = 1

        while 1:
            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))

            while loading:
                LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[2]["BACKGROUND"], (0, 0))
                DrawUI.draw_text("Loading Stats.", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)

                DrawUI.draw_text("Loading Stats..", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)

                DrawUI.draw_text("Loading Stats...", LoadingImages.NORMAL_FONT, "white", 780, 230,
                                 LoadingImages.GAME_SCREEN)
                pygame.display.update()
                pygame.time.wait(300)
                loading = False

            LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
            mouse_coordinates = pygame.mouse.get_pos()

            DrawUI.draw_text(title, LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 630, Menu.TITLE_Y,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text("FASTEST LAP TIMES", LoadingImages.MEDIUM_FONT, "purple", 580, 330,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text("FASTEST RACE TIMES", LoadingImages.MEDIUM_FONT, "purple", 1080, 330,
                             LoadingImages.GAME_SCREEN)

            lap_times = DataProcessing.load_lap_times(lap_times_file)
            match_times = DataProcessing.load_match_times(match_times_file)

            DrawUI.draw_text(f"1. - {lap_times[0]}" + "s", LoadingImages.SMALL_FONT, "green", 670, 400,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"2. - {lap_times[1]}" + "s", LoadingImages.SMALL_FONT, "green", 670, 450,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"3. - {lap_times[2]}" + "s", LoadingImages.SMALL_FONT, "yellow", 670, 500,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"4. - {lap_times[3]}" + "s", LoadingImages.SMALL_FONT, "orange", 670, 550,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"5. - {lap_times[4]}" + "s", LoadingImages.SMALL_FONT, "red", 670, 600,
                             LoadingImages.GAME_SCREEN)

            DrawUI.draw_text(f"1. - {match_times[0]}" + "s", LoadingImages.SMALL_FONT, "green", 1170, 400,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"2. - {match_times[1]}" + "s", LoadingImages.SMALL_FONT, "green", 1170, 450,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"3. - {match_times[2]}" + "s", LoadingImages.SMALL_FONT, "yellow", 1170, 500,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"4. - {match_times[3]}" + "s", LoadingImages.SMALL_FONT, "orange", 1170, 550,
                             LoadingImages.GAME_SCREEN)
            DrawUI.draw_text(f"5. - {match_times[4]}" + "s", LoadingImages.SMALL_FONT, "red", 1170, 600,
                             LoadingImages.GAME_SCREEN)

            pointer_right_button = Button(button_image=LoadingImages.POINTERS[2]["POINTER"], x_y=(1600, 500),
                                          button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                          font_hover_color="white")

            pointer_left_button = Button(button_image=LoadingImages.POINTERS[1]["POINTER"], x_y=(320, 500),
                                         button_text="", font=LoadingImages.NORMAL_FONT, font_color="white",
                                         font_hover_color="white")

            back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                                 button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                                 font_hover_color="red")

            if show_pointer_left == 1:
                pointer_left_button.button_render(LoadingImages.GAME_SCREEN)

            if show_pointer_right == 1:
                pointer_right_button.button_render(LoadingImages.GAME_SCREEN)

            back_button.button_render(LoadingImages.GAME_SCREEN)

            Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if show_pointer_left == 1:
                        if pointer_left_button.on_click(mouse_coordinates):
                            pointer_left_map()

                    if show_pointer_right == 1:
                        if pointer_right_button.on_click(mouse_coordinates):
                            pointer_right_map()

                    if back_button.on_click(mouse_coordinates):
                        Menu.main_menu()

            pygame.display.update()


# GAME MODE SELECTION --------------------------------------------------------------------------------------------------
def mode_selection():
    while 1:

        LoadingImages.GAME_SCREEN.blit(LoadingImages.MENU_BACKGROUND[1]["BACKGROUND"], (0, 0))
        mouse_coordinates = pygame.mouse.get_pos()

        DrawUI.draw_text("MODE SELECTION", LoadingImages.BIG_FONT, Menu.TITLE_COLOR, 650, Menu.TITLE_Y,
                         LoadingImages.GAME_SCREEN)

        LoadingImages.GAME_SCREEN.blit(LoadingImages.trophy_icon, (1830, 250))
        DrawUI.draw_text(f"{Settings.win_coins}", LoadingImages.MEDIUM_FONT, "cyan", 1850, 210,
                         LoadingImages.GAME_SCREEN)

        against_pc = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(760, 420),
                            button_text="VERSUS PC", font=LoadingImages.NORMAL_FONT, font_color="white",
                            font_hover_color="cyan")

        one_vs_one = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(1160, 420),
                            button_text="1 VS 1", font=LoadingImages.NORMAL_FONT, font_color="white",
                            font_hover_color="cyan")

        solo = Button(button_image=LoadingImages.BUTTONS[1]["BUTTON"], x_y=(960, 580),
                      button_text="SOLO", font=LoadingImages.NORMAL_FONT, font_color="white",
                      font_hover_color="cyan")

        back_button = Button(button_image=LoadingImages.BUTTONS[3]["BUTTON"], x_y=(Menu.QUIT_X, Menu.QUIT_Y),
                             button_text="BACK", font=LoadingImages.NORMAL_FONT, font_color="orange",
                             font_hover_color="red")

        solo.button_render(LoadingImages.GAME_SCREEN)

        against_pc.button_render(LoadingImages.GAME_SCREEN)
        one_vs_one.button_render(LoadingImages.GAME_SCREEN)
        back_button.button_render(LoadingImages.GAME_SCREEN)

        Button.button_hover_render(solo, mouse_coordinates, LoadingImages.GAME_SCREEN)

        Button.button_hover_render(against_pc, mouse_coordinates, LoadingImages.GAME_SCREEN)
        Button.button_hover_render(one_vs_one, mouse_coordinates, LoadingImages.GAME_SCREEN)
        Button.button_hover_render(back_button, mouse_coordinates, LoadingImages.GAME_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo.on_click(mouse_coordinates):
                    Menu.map_selection(AllMaps.first_map_solo, AllMaps.second_map_solo,
                                       AllMaps.third_map_solo, AllMaps.fourth_map_solo, AllMaps.fifth_map_solo)

                if against_pc.on_click(mouse_coordinates):
                    Menu.map_selection(AllMaps.first_map_vs_pc, AllMaps.second_map_vs_pc,
                                       AllMaps.third_map_vs_pc, AllMaps.fourth_map_vs_pc, AllMaps.fifth_map_vs_pc)

                if one_vs_one.on_click(mouse_coordinates):
                    Menu.map_selection(AllMaps.first_map_1v1, AllMaps.second_map_1v1,
                                       AllMaps.third_map_1v1, AllMaps.fourth_map_1v1, AllMaps.fifth_map_1v1)

                if back_button.on_click(mouse_coordinates):
                    Menu.main_menu()

        pygame.display.update()
