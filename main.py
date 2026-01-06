import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Menu with Background")

# Load background image
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (600, 400))


def setDifficulty(value, difficulty):
  print(f"Difficulty set to {difficulty}")


def startGame():
  print("Game Started")


menu = pygame_menu.Menu("Welcome", 400, 300, theme=themes.THEME_BLUE)

menu.add.text_input("Name : ", default="Write Your Name")
menu.add.selector("Difficulty : ", [("Hard", 1), ("Easy", 2)],
                  onchange=setDifficulty)
menu.add.button("Play", startGame)
menu.add.button("Quit", pygame_menu.events.EXIT)

if __name__ == "__main__":
  menu.mainloop(screen)
