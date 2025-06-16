import random
import pygame
import time
from bird import Bird
from pipe import Pipe
from utils import draw_text

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.clock = pygame.time.Clock()
        self.bird = Bird(100, 300)
        self.pipes = []
        self.score = 0
        self.last_score_update = pygame.time.get_ticks()
        self.game_over = False
        self.scroll_speed = 2
        self.pipe_distance = 300
        self.font = pygame.font.SysFont("consolas", 64, bold=True)

    def reset(self):
        self.bird = Bird(100, 300)
        self.pipes = []
        self.score = 0
        self.last_score_update = pygame.time.get_ticks()
        self.game_over = False

    def create_pipe(self):
        # Crée le pipe juste après le bord droit de la fenêtre
        pipe = Pipe(self.screen_width, random.randint(100, 400))
        self.pipes.append(pipe)

    def handle_collisions(self):
        for pipe in self.pipes:
            # You need to implement collision logic based on your Pipe and Bird classes
            if pipe.collide(self.bird):
                self.game_over = True

    def update_score(self):
        for pipe in self.pipes:
            if not pipe.passed and pipe.x < self.bird.x:
                self.score += 1
                pipe.passed = True

    def update(self):
        if self.game_over:
            return
        self.bird.update()
        # Crée un nouveau pilier si le dernier est assez éloigné
        if (
            len(self.pipes) == 0 or
            self.pipes[-1].x < self.screen_width - self.pipe_distance
        ):
            self.create_pipe()
        for pipe in self.pipes:
            pipe.move(self.scroll_speed)
        self.handle_collisions()
        self.update_score()
        # Remove pipes that have gone off screen
        self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.width > 0]

        now = pygame.time.get_ticks()
        if now - self.last_score_update >= 100:  # 0.1s
            self.score += 1
            self.last_score_update = now

    def draw_score(self):
        # Format du score : 0'000'000
        score_str = f"{self.score:07d}"
        score_str = f"{score_str[0]}'{score_str[1:4]}'{score_str[4:]}"
        digit_w, digit_h = self.font.size("0")
        total_w = digit_w * len(score_str)
        x = (self.screen_width - total_w) // 2
        y = 20

        # Cadre
        frame_rect = pygame.Rect(x - 10, y - 10, total_w + 20, digit_h + 20)
        pygame.draw.rect(self.screen, (0, 0, 0), frame_rect, border_radius=12)
        pygame.draw.rect(self.screen, (255, 255, 255), frame_rect, 3, border_radius=12)

        # Texte
        text_surface = self.font.render(score_str, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def draw(self):
        # Bleu roi : (65, 105, 225)
        self.screen.fill((65, 105, 225))
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.bird.draw(self.screen)
        self.draw_score()