# import pygame
#
#
# class Board:
#     # создание поля
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#         # значения по умолчанию
#         self.left = 10
#         self.top = 10
#         self.cell_size = 30
#
#     # настройка внешнего вида
#     def set_view(self, left, top, cell_size):
#         self.left = left
#         self.top = top
#         self.cell_size = cell_size
#
#     def render(self, screen):
#         # i = y
#         for i in range(self.height):
#             # j = x
#             for j in range(self.width):
#                 pygame.draw.rect(screen, 'white', (j * self.cell_size + self.left, i * self.cell_size + self.top,
#                                                    self.cell_size, self.cell_size), 1)
#
#     def get_cell(self, mouse_pos):
#         board_width = self.width * self.cell_size
#         board_height = self.height * self.cell_size
#         if self.left < mouse_pos[0] < self.left + board_width:
#             if self.top < mouse_pos[1] < self.top + board_height:
#                 cell_coords = (mouse_pos[1] - self.left) // self.cell_size, \
#                             (mouse_pos[0] - self.top) // self.cell_size
#                 return cell_coords
#         return None
#
#
#
# board = Board(5, 7)
# size = width, height = 400, 400
# pygame.display.set_caption('Инициализация игры')
# screen = pygame.display.set_mode(size)
# screen.fill((0, 0, 0))
# board.render(screen)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(board.get_cell(event.pos))
#     # screen — холст, на котором нужно рисовать:
#     board.render(screen)
#     pygame.display.flip()
#


# from yandex_testing_lesson import is_palindrome(data)
def is_palindrome(string):
    if string == "":
        return False
    if string == string[::-1]:
        return True
    else:
        return False


# if is_palindrome("1011"):
#     print("NO")
# elif is_palindrome(""):
#     print("NO")
# else:
#     print("YES")

def test():
    er = ['roror', 'Roror', ' Or  drod r ', 'q', 'Roy']
    tr_f = [True, False, False, True, False]
    for i in range(len(er)):
        if is_palindrome(er[i]) != tr_f[i]:
            return "NO"
    return "YES"


print(test())
print(11123)
