import os
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.abspath(__file__))
    train_mp3_path = os.path.join(dir_path, 'train.mp3')
    texte_txt_path = os.path.join(dir_path, 'texte/texte.txt')

    pygame.mixer.init()
    pygame.mixer.music.load(train_mp3_path)
    pygame.mixer.music.play(loops=-1)

    with open(texte_txt_path) as f:
        line = f.readline()
        while line:
            print(line.strip())
            time.sleep(3.75)
            line = f.readline()

    input()
