def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    image = pygame.image.load(file_path)
    return image

def load_font(font_path, size):
    """Load a font from the specified file path with the given size."""
    import pygame
    font = pygame.font.Font(font_path, size)
    return font

def draw_text(surface, text, font, color, position):
    """Render text on the given surface at the specified position."""
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def reset_game_settings():
    """Reset game settings to default values."""
    return {
        'score': 0,
        'high_score': 0,
        'gravity': 0.5,
        'jump_strength': -10
    }