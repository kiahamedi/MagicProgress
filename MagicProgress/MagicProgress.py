"""
This library is used to implement various examples of progress bar.

Author: Kia Hamedi
Email: kia.arta9793@gmail.com
Website: kiahamedi.ir

Thank you dear Shahab Karimifar for the idea of developing this library.
"""

__author__ = "Kia Hamedi"
__email__ = "kia.arta9793@gmail.com"
__status__ = "planning"

from time import sleep
import sys


def Progress(x):
    progress_icon = "🟩"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['⬜️'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "⬜️"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"{progress} {x}%"
    print(end=f"\r {progress}")


def ProgressNoPercentage(x):
    progress_icon = "🟩"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['⬜️'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "⬜️"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"{progress}"
    print(end=f"\r {progress}")


def ProgressNoColor(x):
    progress_icon = "██"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['--'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "--"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"[{progress}] {x}%"
    print(end=f"\r {progress}")


def ProgressNoColorPercentage(x):
    progress_icon = "██"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['--'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "--"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"[{progress}]"
    print(end=f"\r {progress}")



def DrawProgress(x):
    progress_icon = "🟩"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['⬜️'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "⬜️"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"{progress} {x}%"
    return progress


def DrawProgressNoPercentage(x):
    progress_icon = "🟩"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['⬜️'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "⬜️"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"{progress}"
    return progress


def DrawProgressNoColor(x):
    progress_icon = "██"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['--'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "--"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"[{progress}] {x}%"
    return progress


def DrawProgressNoColorPercentage(x):
    progress_icon = "██"
    base=10
    p = base * round(x/base)
    if p == 0 : p = 1
    if p != 100:
        p = int(str(p).replace("0", ""))
        progress_list = ['--'] * 10
        pointer = 1
        for i in progress_list:
            if pointer <= p:
                progress_list[pointer - 1] = progress_icon
            else:
                progress_list[pointer - 1] = "--"
            pointer += 1
        progress = ''.join(progress_list)
    else:
        progress_list = [progress_icon] * 10
        progress = ''.join(progress_list)
    progress = f"[{progress}]"
    return progress
