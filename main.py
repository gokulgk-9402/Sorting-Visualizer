import time
import pygame
import random
import sys
import threading

pygame.init()

HEIGHT = 1000
WIDTH = 1000

BLACK = 0,0,0
WHITE = 255, 255, 255
GREEN = 100, 255, 100
RED = 255, 100, 100
GREY = 150, 150, 150
BLUE = 100, 100, 255

COLORS = [(150, 150, 255), (175, 175, 255), (200, 200, 255)]

SURFACE_HEIGHT = 270
SURFACE_WIDTH = 500

SURFACE_PADDING = 20

BAR_WIDTH = (SURFACE_WIDTH - 2*SURFACE_PADDING)//50
BAR_HEIGHT = (SURFACE_HEIGHT - 2*SURFACE_PADDING)//100

TITLE_FONT = pygame.font.Font('freesansbold.ttf', 40)
FONT = pygame.font.SysFont('comicsans', 20)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

bubble_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
insertion_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

list_of_numbers = []
timings = {}

bubble_done = False
insertion_done = False

def generate_numbers(n, minimum, maximum):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(minimum, maximum))

    return numbers

def draw_static_items():
    global bubble_done, insertion_done
    window.fill(WHITE)
    title = TITLE_FONT.render("Sorting Visualizer", True, BLACK)
    rectangle = (WIDTH//2 - title.get_width()//2, 40)
    window.blit(title, rectangle)
    b_text = "Bubble Sort"
    if bubble_done:
        b_text += f"  Time Taken: {round(timings['bubble'], 2)} seconds"
    bubble_title = FONT.render(b_text, True, BLACK)
    window.blit(bubble_title, (15, 362))
    i_text = "Insertion Sort"
    if insertion_done:
        i_text += f"  Time Taken: {round(timings['insertion'], 2)} seconds"
    insertion_title = FONT.render(i_text, True, BLACK)
    window.blit(insertion_title, (515, 362))

def draw_bubble_surface(numbers, color_positions = {}):
    bubble_sort_surface.fill(WHITE)

    for i in range(len(numbers)):
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(bubble_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(bubble_sort_surface, (0,100))

def draw_insertion_surface(numbers, color_positions = {}):
    insertion_sort_surface.fill(WHITE)
    
    for i in range(len(numbers)):
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(insertion_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(insertion_sort_surface, (500, 100))

def bubble_sort(numbers):
    global bubble_done
    bubble_start = time.time()
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                draw_bubble_surface(numbers, {j:RED, j+1:GREEN})
                pygame.display.flip()
                time.sleep(0.01)
    bubble_done = True

    bubble_end = time.time()
    draw_bubble_surface(numbers)
    pygame.display.flip()
    timings["bubble"] = bubble_end - bubble_start

def insertion_sort(numbers):
    global insertion_done
    insertion_start = time.time()
    for i in range(1, len(numbers)):
        key = numbers[i]

        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            draw_insertion_surface(numbers, {j:RED, j+1:GREEN})
            pygame.display.flip()
            time.sleep(0.01)
            j -= 1
        
        if numbers[j+1] != key:
            numbers[j+1] = key
            draw_insertion_surface(numbers, {i:RED, j+1:GREEN})
            pygame.display.flip()
            time.sleep(0.01)
    insertion_done = True

    insertion_end = time.time()
    draw_insertion_surface(numbers)
    pygame.display.flip()
    timings["insertion"] = insertion_end - insertion_start

list_of_numbers = generate_numbers(50, 0, 100)

bubble_sort_numbers = list_of_numbers[:]
insertion_sort_numbers = list_of_numbers[:]

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    draw_static_items()
    draw_bubble_surface(bubble_sort_numbers)
    draw_insertion_surface(insertion_sort_numbers)

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    list_of_numbers = generate_numbers(50, 0, 100)
                    bubble_sort_numbers = list_of_numbers[:]
                    insertion_sort_numbers = list_of_numbers[:]
                    bubble_done = False
                    insertion_done = False

                
                elif event.key == pygame.K_SPACE:
                    bubble_thread = threading.Thread(target=bubble_sort, args=(bubble_sort_numbers,))
                    insertion_thread = threading.Thread(target=insertion_sort, args=(insertion_sort_numbers,))

                    bubble_thread.start()
                    insertion_thread.start()

                    bubble_thread.join()
                    insertion_thread.join()

                    print(timings)

    pygame.display.flip()