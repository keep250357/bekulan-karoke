import time
import shutil
import sys
import random

# --- ТЕКСТ ПЕСНИ ---
LYRICS = """I wanna, I wanna rock right now
I wanna, I wanna rock right now
I wanna, I wanna rock right now
I wanna da-, I wanna dance in the lights
I wanna ro-, I wanna rock your body
I wanna go, I wanna go for a ride
Hop in the music and rock your body right
Rock that body, come on, come on, rock that body (rock that body)
Rock that body, come on, come on, rock that body
Rock that body, come on, come on, rock that body (rock your body)
Rock that body, come on, come on, rock that body""".splitlines()

# --- ANSI цвета ---
RESET = "\033[0m"
BOLD = "\033[1m"

# Неоновые цвета (можно добавлять свои)
COLORS = [
    "\033[91m",  # ярко-красный
    "\033[92m",  # ярко-зелёный
    "\033[93m",  # жёлтый
    "\033[94m",  # синий
    "\033[95m",  # фиолетовый
    "\033[96m",  # бирюзовый
    "\033[38;5;208m",  # оранжевый
    "\033[38;5;201m",  # розовый
]

def clear():
    """Очищает экран"""
    sys.stdout.write("\033[H\033[J")

def fit_line(line, width):
    """Обрезает строку по ширине терминала"""
    if len(line) <= width:
        return line
    if width > 3:
        return line[: width-3] + "..."
    return line[:width]

def karaoke_neon(lyrics, window=6, word_time=0.25):
    """Плавное появление слов + случайные цвета строк"""
    cols = shutil.get_terminal_size().columns
    total = len(lyrics)

    try:
        for i, line in enumerate(lyrics):
            color = random.choice(COLORS)  # выбираем случайный цвет для строки
            words = line.split()
            built_line = ""

            for w_i, w in enumerate(words):
                built_line += color + BOLD + w + RESET + " "

                # вычисляем диапазон видимых строк
                half = window // 2
                start = max(0, i - half)
                end = min(total, start + window)
                if end - start < window:
                    start = max(0, end - window)

                clear()
                # выводим строки в окне
                for j in range(start, end):
                    if j < i:
                        sys.stdout.write("  " + fit_line(lyrics[j], cols) + "\n")
                    elif j == i:
                        sys.stdout.write("  " + fit_line(built_line.strip(), cols) + "\n")
                    else:
                        sys.stdout.write("\n")
                sys.stdout.flush()
                time.sleep(word_time)

            # пауза между строками
            time.sleep(0.4)

        clear()
        print(random.choice(COLORS) + BOLD + "🎶 Все концерт окончен! 🎤" + RESET)
        time.sleep(1)

    except KeyboardInterrupt:
        clear()
        print("⏹ Karaoke stopped.")
        return


if __name__ == "__main__":
    karaoke_neon(LYRICS, window=6, word_time=0.25)