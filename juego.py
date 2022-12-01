import pygame
from pygame.locals import QUIT
#Ventana del juego
Margen_V = 600
Margen_H = 800
FPS = 60
Fondo_Blanco = (225 , 225, 225)
def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((Margen_H, Margen_V))
    pygame.display.set_caption("Pong 1")

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(Fondo_Blanco)

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
