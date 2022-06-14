import random
import subprocess
from colorthief import ColorThief
import numpy as np


def closest(color_list, color):
    color_list = np.array(color_list)
    color = np.array(color)
    distances = np.sqrt(np.sum((color_list - color) ** 2, axis=1))
    index_of_smallest = np.where(distances == np.amin(distances))
    smallest_distance = color_list[index_of_smallest]
    return smallest_distance


def __get_tuple(r: str, g: str, b: str, name: str):
    return int(r, 16), int(g, 16), int(b, 16), name


colors = [
    __get_tuple("8B", "B1", "58", ""),
    __get_tuple("66", "A8", "CB", "Aqua"),
    __get_tuple("59", "72", "C3", "Blue"),
    __get_tuple("99", "70", "52", "Brown"),
    __get_tuple("99", "99", "99", "Grey"),
    __get_tuple("CC", "82", "3F", "Orange"),
    __get_tuple("CE", "6C", "A2", "Ping"),
    __get_tuple("84", "63", "C5", "Purple"),
    __get_tuple("B7", "4C", "4A", "Red"),
    __get_tuple("C4", "A6", "66", "Sand"),
    __get_tuple("59", "C3", "AD", "Teal")
]

rawFile = subprocess.check_output("gsettings get org.cinnamon.desktop.background picture-uri", shell=True)
file = str(rawFile)[10:-4]
print(file)

thief = ColorThief(file)
thief_color = thief.get_color(quality=10)
print(f"Color: {thief_color}")

color_vars = list(map(lambda value: [value[0], value[1], value[2]], colors))
print(color_vars)
closest_color = closest(color_vars, [thief_color[0], thief_color[1], thief_color[2]])[0]
print(f"Closest color: {closest_color}")

selected = list(filter(
    lambda value: value[0] == closest_color[0] and
                  value[1] == closest_color[1] and
                  value[2] == closest_color[2],
    colors
))[0][3]
print(selected)

theme_name = "Mint-Y-Dark"
if len(selected) > 0:
    theme_name += f"-{selected}"

subprocess.call(f"gsettings set org.cinnamon.desktop.interface icon-theme '{theme_name}'", shell=True)
subprocess.call(f"gsettings set org.cinnamon.desktop.interface gtk-theme '{theme_name}'", shell=True)
subprocess.call(f"gsettings set org.cinnamon.theme name '{theme_name}'", shell=True)

