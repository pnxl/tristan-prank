import pygame

pygame.init()

bgClr = (0,0,0)
scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sound = pygame.mixer.Sound("C:\Windows\Media\Windows Message Nudge.wav")

pygame.display.set_caption('You are an idiot!')
scr.fill(bgClr)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Sound.play(sound)