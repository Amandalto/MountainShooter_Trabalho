import pygame
from pygame import Surface

from code.Const import C_RED


class GameOverScreen:
    def __init__(self, window: Surface):
        self.window = window
        self.bg_image = pygame.image.load('./asset/GameOverBg.png').convert()

    def show(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Reinicia ao pressionar Enter
                        return

            self.window.blit(self.bg_image, (0, 0))
            self.display_text("GAME OVER", 60, C_RED, (self.window.get_width() // 2, 100))
            self.display_text("Pressione ENTER para voltar ao menu", 24, (255, 255, 255),
                              (self.window.get_width() // 2, self.window.get_height() - 100))

            pygame.display.flip()
            clock.tick(30)

    def display_text(self, text: str, size: int, color: tuple, position: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.window.blit(text_surface, text_rect)
