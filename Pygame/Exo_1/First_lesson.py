import pygame
import time



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


    def update(self, pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0, -1)

        if pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)

        if pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)

        if pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Garde le joueur à l’écran
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > surface_res[0]:
            self.rect.right = surface_res[0]

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= surface_res[1]:
            self.rect.bottom = surface_res[1]


        


pygame.init()
pygame.display.set_caption("Les évènements !")

white_color = (255, 255, 255)
black_color = (0, 0, 0)

surface_res = (500, 500)
surface = pygame.display.set_mode(surface_res, pygame.RESIZABLE)

myFont = pygame.font.Font("fonts/Nexa-Trial-Regular.ttf", 30)

myText = myFont.render("{} x {}".format(surface_res[0], surface_res[1]), True, white_color)

surface.blit(myText, [20, 20])
pygame.display.flip()

joueur = Player()
monSon = pygame.mixer.Sound("son/chord.wav")

running = True
while running: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE :
            monSon.play(2,3000,1000)
            surface.fill(black_color) # On efface tout
            myText = myFont.render("{} x {}".format(event.w, event.h), True, white_color)
            surface.blit(myText, [20, 20]) # On réaffiche le texte
            pygame.display.flip() # On actualise l'affichage
    # On efface la surface
    surface.fill((0, 0, 0))
    # On récupère les touches appuyées en début de frame
    pressed_keys = pygame.key.get_pressed()
    # On update le Sprite du joueur en fonction des touches
    joueur.update(pressed_keys)
    #On dessine le joueur à l'écran
    surface.blit(joueur.surf, joueur.rect)
    # On rafraîchit la surface
    pygame.display.flip()
    