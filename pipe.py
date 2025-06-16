import pygame

class Pipe:
    def __init__(self, x, height):
        self.x = x
        self.height = height
        self.width = 52  # Width of the pipe
        self.gap = 200   # Gap between the top and bottom pipes
        self.passed = False  # To check if the bird has passed the pipe

        # Placeholder images (replace with actual images if available)
        # Vert clair : (144, 238, 144)
        self.top_image = pygame.Surface((self.width, 320), pygame.SRCALPHA)
        self.top_image.fill((144, 238, 144))
        self.bottom_image = pygame.Surface((self.width, 320), pygame.SRCALPHA)
        self.bottom_image.fill((144, 238, 144))

    def move(self, speed):
        self.x -= speed

    def draw(self, surface):
        # Draw the top pipe
        surface.blit(self.top_image, (self.x, self.height - self.top_image.get_height()))
        # Draw the bottom pipe
        surface.blit(self.bottom_image, (self.x, self.height + self.gap))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_pipe_mask = self.get_top_mask()
        bottom_pipe_mask = self.get_bottom_mask()

        top_offset = (int(self.x - bird.x), int(self.height - self.top_image.get_height() - bird.y))
        bottom_offset = (int(self.x - bird.x), int(self.height + self.gap - bird.y))

        top_collision = bird_mask.overlap(top_pipe_mask, top_offset)
        bottom_collision = bird_mask.overlap(bottom_pipe_mask, bottom_offset)

        return top_collision or bottom_collision

    def get_top_mask(self):
        return pygame.mask.from_surface(self.top_image)

    def get_bottom_mask(self):
        return pygame.mask.from_surface(self.bottom_image)