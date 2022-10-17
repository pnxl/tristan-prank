import pygame
from sound import Sound
from ctypes import windll

pygame.init()

bgClr = (0, 0, 0)
scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sound = pygame.mixer.Sound("C:\Windows\Media\Windows Message Nudge.wav")
laugh = pygame.mixer.Sound("laugh.wav")
setWindowPos = windll.user32.SetWindowPos

NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2


def alwaysOnTop(boolean):
    zorder = (NOT_TOPMOST, TOPMOST)[boolean]
    hwnd = pygame.display.get_wm_info()['window']
    setWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE | NOSIZE)


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
        if event.type == pygame.KEYDOWN:
            pygame.mixer.Sound.play(laugh)
        if event.type == pygame.WINDOWSHOWN:
            if Sound.is_muted() == True:
                Sound.mute()
                Sound.volume_max()
                continue
            if Sound.is_muted() == False:
                Sound.volume_max()
                continue
