import pygame
import os
import tkinter as tk
from tkinter import filedialog

pygame.init()
pygame.mixer.init()

root = tk.Tk()
root.title("Reprodutor de Música")
root.geometry("300x150")

music_folder = ""
music_files = []
current_music = 0

def load_music():
    global music_folder, music_files
    music_folder = filedialog.askdirectory()
    music_files = [file for file in os.listdir(music_folder) if file.endswith(".mp3")]

def play_music():
    global current_music
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_music]))
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music
    current_music = (current_music + 1) % len(music_files)
    stop_music()
    play_music()

def previous_music():
    global current_music
    current_music = (current_music - 1) % len(music_files)
    stop_music()
    play_music()

load_button = tk.Button(root, text="Selecionar Pasta", command=load_music)
load_button.pack()

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

pause_button = tk.Button(root, text="Pausar", command=pause_music)
pause_button.pack()

unpause_button = tk.Button(root, text="Despausar", command=unpause_music)
unpause_button.pack()

stop_button = tk.Button(root, text="Parar", command=stop_music)
stop_button.pack()

previous_button = tk.Button(root, text="Anterior", command=previous_music)
previous_button.pack()

next_button = tk.Button(root, text="Próxima", command=next_music)
next_button.pack()

root.mainloop()
