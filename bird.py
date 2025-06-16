import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gravity = 0.1
        self.lift = -5
        self.velocity = 0

        # Sprite sheet
        self.sprite_sheet = pygame.image.load("bird.png").convert_alpha()
        self.frames = []
        frame_width, frame_height = 64, 64
        for row in range(2):
            for col in range(4):
                rect = pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height)
                frame = self.sprite_sheet.subsurface(rect)
                frame = pygame.transform.scale2x(frame)  # Pixel perfect x2
                self.frames.append(frame)
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 6  # Plus petit = plus rapide

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        # Animation
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.animation_timer = 0

    def jump(self):
        self.velocity += self.lift

    def get_position(self):
        return self.x, self.y

    def draw(self, screen):
        frame = self.frames[self.current_frame]
        screen.blit(frame, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.frames[self.current_frame])