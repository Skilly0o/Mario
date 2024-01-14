# НАСТРОЙКИ ИГРЫ МЕНЯТЬ НА СВОЙ СТРАХ И РИСК
from screeninfo import get_monitors


def get_monitor_size() -> tuple:
    global SIZE, WIDTH, HEIGHT
    monitor = get_monitors()[0]
    SIZE = WIDTH, HEIGHT = monitor.width, monitor.height
    return SIZE



title_size = 64

WIDTH, HEIGHT = get_monitor_size()

def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


level_map = load_level('script/data/maps/level_1.txt')

