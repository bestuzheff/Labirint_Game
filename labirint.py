import random
import pygame

# Размер ячейки
cell_size = 64

# Размер поля
size = (15 * cell_size, 15 * cell_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")

# Размеры лабиринта на будущее, если захочу сделать полностью динамический
size_x = 15
size_y = 15

# Шаблон лабиринта
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Функция которая щагрузает картинки и изменять их размер под размер ячейки
def load_image(image_file_name):
    full_image_file_name = 'images' + '/' + image_file_name
    try:
        image = pygame.image.load(full_image_file_name)
        image = pygame.transform.scale(image, (cell_size, cell_size)).convert_alpha()  # Изменение размера картинки
    except any:
        print("Ошибка загрузки изображения:", image_file_name)
        raise SystemExit()
    return image


# Функция определяет какой спрайт надо отрисовать
def define_sprite(x, y):
    if maze[x + 1][y] > 0 and maze[x - 1][y] > 0 and maze[x][y+1] == 0 and maze[x][y-1] == 0:
        return road_left_right
    if maze[x + 1][y] == 0 and maze[x - 1][y] == 0 and maze[x][y + 1] > 0 and maze[x][y - 1] > 0:
        return road_up_down
    return road_up_down


########################################################################################################################
# Функции для генерации лабиринта

# Функция выбирает соседние клетки для добавления их в лабиринт (выбор в лучайном порядке) + рекурсия
def cell_editing(x, y, depth):
    # Увеличим глубину
    depth += 1
    # Определим все возможные направления движения
    directions = []
    last_cell = True
    # Левая клетка 1
    if (x - 1) > 0:
        directions.append(1)
    # Верхняя клетка 2
    if (y + 1) < (size_y - 1):
        directions.append(2)
    # Правая клетка 3
    if (x + 1) < (size_x - 1):
        directions.append(3)
    # Нижняя клетка 4
    if (y - 1) > 0:
        directions.append(4)

    # Цикл по всем направлениям рандомно
    for _ in range(len(directions)):
        item = random.choice(directions)
        directions.remove(item)
        # Левая клетка 1
        if item == 1:
            if maze[x - 1][y] == 0 and maze[x - 2][y] == 1:
                last_cell = False
                maze[x - 1][y] = 1
                maze[x - 2][y] = 2
                cell_editing(x - 2, y, depth)
        # Верхняя клетка 2
        if item == 2:
            if maze[x][y + 1] == 0 and maze[x][y + 2] == 1:
                last_cell = False
                maze[x][y + 1] = 1
                maze[x][y + 2] = 2
                cell_editing(x, y + 2, depth)
        # Правая клетка 3
        if item == 3:
            if maze[x + 1][y] == 0 and maze[x + 2][y] == 1:
                last_cell = False
                maze[x + 1][y] = 1
                maze[x + 2][y] = 2
                cell_editing(x + 2, y, depth)
        # Нижняя клетка 4
        if item == 4:
            if maze[x][y - 1] == 0 and maze[x][y - 2] == 1:
                last_cell = False
                maze[x][y - 1] = 1
                maze[x][y - 2] = 2
                cell_editing(x, y - 2, depth)

    # Запишем грубину, ячейка с самой большйо глубиной будет концом лабиринта
    if last_cell:
        maze[x][y] = depth


# Процедура генерирует лабиринт
def create_maze():
    # Формируем список клеток которые надо поситить
    # Выбираем случайную клетку
    y = size_y - 2
    x = random.randint(1, size_y - 4)
    if x % 2 == 0:
        x += 1
    maze[x][y] = 3
    cell_editing(x, y, 0)


########################################################################################################################


# Подгружаем все спрайты
bg = load_image("bg_1.png")
road_up_down = load_image("road_up_down.png")
road_left_right = load_image("road_left_right.png")

create_maze()

for _x in range(size_x):
    for _y in range(size_y):
        # Все клетки заполняем BG
        # TODO Сделать несколько фонов и выбирать рандомно
        screen.blit(bg, (_x * cell_size, _y * cell_size))
        if maze[_x][_y] > 0:
            screen.blit(define_sprite(_x, _y), (_x * cell_size, _y * cell_size))

pygame.init()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
