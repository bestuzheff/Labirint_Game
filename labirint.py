import random
import pygame

size = widht, height = (960, 960)
screen = pygame.display.set_mode(size)

# Размеры лабиринта на будущее
size_x = 15
size_y = 15

start_x = 0
start_y = 0
finish_x = 0
finish_y = 0

# Шаблон лабиринта
labirint = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Обработка соседних клеток
def cell_editing(x, y):
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
            if labirint[x - 1][y] == 1 and labirint[x - 2][y] == 0:
                last_cell = False
                labirint[x - 1][y] = 0
                labirint[x - 2][y] = 2
                cell_editing(x - 2, y)
        # Верхняя клетка 2
        if item == 2:
            if labirint[x][y + 1] == 1 and labirint[x][y + 2] == 0:
                last_cell = False
                labirint[x][y + 1] = 0
                labirint[x][y + 2] = 2
                cell_editing(x, y + 2)
        # Правая клетка 3
        if item == 3:
            if labirint[x + 1][y] == 1 and labirint[x + 2][y] == 0:
                last_cell = False
                labirint[x + 1][y] = 0
                labirint[x + 2][y] = 2
                cell_editing(x + 2, y)
        # Нижняя клетка 4
        if item == 4:
            if labirint[x][y - 1] == 1 and labirint[x][y - 2] == 0:
                last_cell = False
                labirint[x][y - 1] = 0
                labirint[x][y - 2] = 2
                cell_editing(x, y - 2)

    if last_cell:
        labirint[x][y] = 4
        print("Finish: ", x, y)



# Процедура генерирует лабиринт
def create_labirint():
    # Формируем список клеток которые надо поситить
    # Выбираем случайную клетку
    y = 13
    x = random.randint(1, 11)
    if x % 2 == 0:
        x += 1

    labirint[x][y] = 3
    print("Start: ", x, y)
    cell_editing(x, y)


# 0.Инициализировать лабиринт, выбрав в немслучайную клетку.
# 1.Выбрать любую соседнюю (для текущей клетки) клетку.
# Соседних клеток может быть 2, 3 или 4, в зависимости от расположения клетки.
# 2.Если соседняя клетка не является частью лабиринта –добавить ее в лабиринт,
# т.е.  убрать  стенку,  соединяющую  две  клетки.  Иначе переход к шагу 3.
# 3.Если не осталось непосещенных клеток –останов. Иначе переход к шагу 1.

def load_image(image_file_name):
    full_image_file_name = 'images' + '/' + image_file_name
    try:
        image = pygame.image.load(full_image_file_name).convert_alpha()
        # image = pygame.transform.scale(image, (64, 64)).convert() #Изменение размера картинки
    except any:
        print("Ошибка загрузка изображения:", image_file_name)
        raise SystemExit()
    return image


create_labirint()

white = load_image("white.png")
black = load_image("black.png")
green = load_image("green.png")

for x in range(size_x):
    for y in range(size_y):
        if labirint[x][y] == 0 or labirint[x][y] == 2:
            screen.blit(white, (x * 64, y * 64))
        if labirint[x][y] == 1:
            screen.blit(black, (x * 64, y * 64))
        if labirint[x][y] == 3 or labirint[x][y] == 4:
            screen.blit(green, (x * 64, y * 64))

pygame.init()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
