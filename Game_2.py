import pygame
import sys

pygame.init()

screen_size = (700, 300)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Синтезатор')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)


key_width = 100
key_height = 300
white_key_width = key_width
black_key_width = 60


white_keys = [pygame.Rect(x * key_width, 0, white_key_width, key_height) for x in range(7)]
black_keys = [pygame.Rect(x * key_width + white_key_width - black_key_width / 2, 0, black_key_width, key_height / 2) for x in range(6) if x not in [2, 5]]

notes = {
    pygame.K_a: (pygame.mixer.Sound("Sounds/68437__pinkyfinger__piano-a.wav"), True),
    pygame.K_s: (pygame.mixer.Sound("Sounds/68438__pinkyfinger__piano-b.wav"), True),
    pygame.K_d: (pygame.mixer.Sound("Sounds/68441__pinkyfinger__piano-c.wav"), True),
    pygame.K_f: (pygame.mixer.Sound("Sounds/68442__pinkyfinger__piano-d.wav"), True),
    pygame.K_g: (pygame.mixer.Sound("Sounds/68443__pinkyfinger__piano-e.wav"), True),
    pygame.K_h: (pygame.mixer.Sound("Sounds/68446__pinkyfinger__piano-f.wav"), True),
    pygame.K_j: (pygame.mixer.Sound("Sounds/68448__pinkyfinger__piano-g.wav"), True),
    pygame.K_w: (pygame.mixer.Sound("Sounds/68439__pinkyfinger__piano-bb.wav"), False),
    pygame.K_e: (pygame.mixer.Sound("Sounds/68440__pinkyfinger__piano-c.wav"), False),
    pygame.K_t: (pygame.mixer.Sound("Sounds/68444__pinkyfinger__piano-eb.wav"), False),
    pygame.K_y: (pygame.mixer.Sound("Sounds/68445__pinkyfinger__piano-f.wav"), False),
    pygame.K_u: (pygame.mixer.Sound("Sounds/68447__pinkyfinger__piano-g.wav"), False),
}


keys_mapping = {
    pygame.K_a: 0,
    pygame.K_s: 1,
    pygame.K_d: 2,
    pygame.K_f: 3,
    pygame.K_g: 4,
    pygame.K_h: 5,
    pygame.K_j: 6,
    pygame.K_w: 0,
    pygame.K_e: 1,
    pygame.K_t: 2,
    pygame.K_y: 3,
    pygame.K_u: 4,
}

key_states = {key: False for key in notes.keys()}

def draw_piano():
    screen.fill(black)

    for index, key in enumerate(white_keys):
        color = blue if key_states.get(list(keys_mapping.keys())[index], False) else white
        pygame.draw.rect(screen, color, key)
        pygame.draw.rect(screen, black, key, 2)


    for index, key in enumerate(black_keys):
        color = blue if key_states.get(list(keys_mapping.keys())[index + 7], False) else black
        pygame.draw.rect(screen, color, key)
        pygame.draw.rect(screen, white, key, 2)

    pygame.display.flip()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in notes:
                    notes[event.key][0].play()
                    key_states[event.key] = True
                    draw_piano()
                    pygame.time.delay(100)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                if event.key in notes:
                    key_states[event.key] = False
                    draw_piano()

        pygame.display.flip()

if __name__ == "__main__":
    draw_piano()
    game_loop()