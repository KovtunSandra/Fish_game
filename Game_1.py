import sys
import pygame
import random
import math


pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Акваріум з рибками")


background_color = (0, 105, 148)
fish_colors = [(255, 99, 71), (255, 165, 0), (255, 215, 0), (0, 191, 255)]



class Fish:
    def __init__(self):
        self.color = random.choice(fish_colors)
        self.x = random.randint(0, screen_size[0])
        self.y = random.randint(0, screen_size[1])
        self.size = random.randint(20, 50)
        self.speed = random.uniform(1, 3)
        self.direction = random.choice([-1, 1])

    def swim(self):
        self.x += self.speed * self.direction
        if self.x < 0 or self.x > screen_size[0]:
            self.direction *= -1

    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.size, self.size // 2))

    def eat_food(self, food):
        distance = math.sqrt((self.x - food.x) ** 2 + (self.y - food.y) ** 2)
        return distance < self.size / 2 + food.size


class Plant:
    def __init__(self):
        self.x = random.randint(0, screen_size[0])
        self.y = screen_size[1]
        self.color = (34, 139, 34)
        self.height = random.randint(50, 150)

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y - self.height), 5)


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.color = (255, 255, 255)

    def fall(self):
        self.y += 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


class Aquarium:
    def __init__(self):
        self.fishes = [Fish() for _ in range(5)]
        self.plants = [Plant() for _ in range(10)]
        self.food = []

    def feed_fish(self, x, y):
        self.food.append(Food(x, y))

    def update(self):
        for fish in self.fishes:
            fish.swim()
        for food in self.food:
            food.fall()
        self.check_food()

    def check_food(self):
        for food in self.food[:]:
            for fish in self.fishes:
                if fish.eat_food(food):
                    self.food.remove(food)
                    break

    def draw(self):
        for plant in self.plants:
            plant.draw()
        for fish in self.fishes:
            fish.draw()
        for food in self.food:
            food.draw()



def main():
    aquarium = Aquarium()
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                aquarium.feed_fish(x, y)

        aquarium.update()
        aquarium.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()