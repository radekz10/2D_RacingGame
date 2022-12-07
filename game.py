import game_first_map
from resolution import draw_text
from load_image import *
from rects import *

import settings

pygame.init()


def collision_solo(car, map_border):
    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()


def collision_vs_pc(car, enemy_car, car_rect, enemy_rect, map_border, enemy_stopwatch, car_time_list, enemy_time_list):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    if FIRST_FINISH_LINE_X_RANGE < enemy_car.x < SECOND_FINISH_LINE_X_RANGE:
        if FIRST_FINISH_LINE_Y_RANGE < enemy_car.y < SECOND_FINISH_LINE_Y_RANGE:
            settings.enemy_lap += 1
            settings.enemy_start_time = pygame.time.get_ticks()
            settings.enemy_match_time = settings.enemy_match_time + enemy_stopwatch
            enemy_car.respawn_first_map()
            enemy_car.next_route_position = 0
            enemy_car.start_drive()

    if settings.enemy_lap == settings.max_laps:
        print(settings.enemy_lap)
        if settings.car_lap < settings.enemy_lap:
            draw_text(f"YOU LOST THE RACE!", normal_font, "red", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)
        if settings.car_lap > settings.enemy_lap:
            draw_text(f"YOU WON THE RACE!", normal_font, "gold", 800, 600, game_screen)

            pygame.display.update()
            pygame.time.wait(1000)
        stats_reset(car, enemy_car, car_time_list, enemy_time_list)

        check_new_game()
        game_first_map.game_first_map()


def collision_vs_player(car, enemy_car, car_rect, enemy_rect, map_border):
    if car_rect.colliderect(enemy_rect):
        car.car_collide()
    else:
        car.car_image = car.car_image
        car.max_speed = 3

    if enemy_rect.colliderect(car_rect):
        enemy_car.car_collide()
    else:
        enemy_car.car_image = enemy_car.car_image
        enemy_car.max_speed = 3

    if car.border_collide(pygame.mask.from_surface(map_border)):
        car.out_of_track()

    if enemy_car.border_collide(pygame.mask.from_surface(map_border)):
        enemy_car.out_of_track()


def check_new_game():
    settings.started = False

    while not settings.started:
        game_screen.blit(time_menu, (700, 200))
        draw_text("PLAY AGAIN - SPACE", normal_font, "white", 740, 250, game_screen)
        draw_text("EXIT TO MENU - X", normal_font, "cyan", 740, 350, game_screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = True
                settings.car_start_time = pygame.time.get_ticks()


def check_car_type(car):
    if settings.car_type == 1:
        car.first_map_car()
    if settings.car_type == 2:
        car.second_map_car()


def start_game():
    while not settings.started:
        draw_text(f"PRESS ANY KEY TO START", medium_font, "orange", 800, 600, game_screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                settings.started = True
                settings.car_start_time = pygame.time.get_ticks()


def start_countdown(car, enemy_car):
    if settings.countdown > 0:

        count_timer = pygame.time.get_ticks()
        car.max_speed = 0
        car.car_nitro = 0
        car.movement_speed = 0

        enemy_car.max_speed = 0
        enemy_car.car_nitro = 0
        enemy_car.movement_speed = 0

        if count_timer - settings.last_count > 1000:
            settings.countdown -= 1
            settings.last_count = count_timer

    if settings.countdown == 5 or settings.countdown == 4:
        game_screen.blit(semaphor_all_red, (880, 500))

    if settings.countdown == 3:
        draw_text(f"{str(settings.countdown)} - READY", normal_font, "red", 850, 570, game_screen)
        game_screen.blit(semaphor_red, (880, 500))

    if settings.countdown == 2:
        draw_text(f"{str(settings.countdown)} - STEADY", normal_font, "orange", 850, 570, game_screen)
        game_screen.blit(semaphor_orange, (880, 500))

    if settings.countdown == 1:
        draw_text(f"{str(settings.countdown)} - GO!", normal_font, "green", 880, 570, game_screen)
        game_screen.blit(semaphor_green, (880, 500))

    if settings.countdown == 0:
        # draw_text(f"", font, "white", 900, 500)

        car.max_speed = 3
        car.car_nitro = 5
        car.max_movement_speed = 2.5

        enemy_car.max_speed = 3
        enemy_car.car_nitro = 5
        enemy_car.max_movement_speed = 2.5


def stats_reset(car, enemy, car_time_list, enemy_time_list):
    car_time_list.clear()
    enemy_time_list.clear()

    settings.car_lap = 0
    settings.enemy_lap = 0
    settings.car_match_time = 0
    settings.enemy_match_time = 0

    car.respawn_first_map()
    enemy.respawn_first_map()
    enemy.next_route_position = 0
    settings.car_start_time = pygame.time.get_ticks()
    settings.enemy_start_time = pygame.time.get_ticks()
