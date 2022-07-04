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
TIME_FONT = pygame.font.SysFont('comicsans', 15)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

bubble_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
insertion_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
selection_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

list_of_numbers = []
timings = {}

bubble_done = False
insertion_done = False
selection_done = False

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

    bubble_title = FONT.render("Bubble Sort", True, BLACK)
    window.blit(bubble_title, (15, 365))
    if bubble_done:
        time_text = TIME_FONT.render(f"  Time Taken: {round(timings['bubble'], 2)} seconds", True, BLACK)
        window.blit(time_text, (500-time_text.get_width()-20, 372))

    insertion_title = FONT.render("Insertion Sort", True, BLACK)
    window.blit(insertion_title, (515, 365))
    if insertion_done:
        time_text = TIME_FONT.render(f"  Time Taken: {round(timings['insertion'], 2)} seconds", True, BLACK)
        window.blit(time_text, (1000-time_text.get_width()-20, 372))

    selection_title = FONT.render("Selection Sort", True, BLACK)
    window.blit(selection_title, (15, 965))
    if selection_done:
        time_text = TIME_FONT.render(f"  Time Taken: {round(timings['selection'], 2)} seconds", True, BLACK)
        window.blit(time_text, (500-time_text.get_width()-20, 972))

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

def draw_selection_surface(numbers, color_positions = {}):
    selection_sort_surface.fill(WHITE)

    for i in range(len(numbers)):
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(selection_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(selection_sort_surface, (0,700))

def bubble_sort(numbers):
    global bubble_done
    bubble_start = time.time()
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                draw_bubble_surface(numbers, {j:RED, j+1:GREEN})
                pygame.display.flip()
                time.sleep(0.02)
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
            time.sleep(0.02)
            j -= 1
        
        if numbers[j+1] != key:
            numbers[j+1] = key
            draw_insertion_surface(numbers, {i:RED, j+1:GREEN})
            pygame.display.flip()
            time.sleep(0.02)
    insertion_done = True

    insertion_end = time.time()
    draw_insertion_surface(numbers)
    pygame.display.flip()
    timings["insertion"] = insertion_end - insertion_start


def selection_sort(numbers):
    global selection_done
    selection_start = time.time()
    for i in range(len(numbers)):
        minimum = i
        for j in range(i+1, len(numbers)):
            if numbers[minimum] > numbers[j]:
                # draw_selection_surface(numbers, {j:RED, minimum: GREEN})
                # pygame.display.flip()
                time.sleep(0.02)
                minimum = j

        if minimum != i:
            numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
            draw_selection_surface(numbers, {minimum:RED, i: GREEN})
            pygame.display.flip()
            time.sleep(0.02)

    selection_done = True

    selection_end = time.time()
    draw_selection_surface(numbers)
    pygame.display.flip()
    timings["selection"] = selection_end - selection_start

list_of_numbers = generate_numbers(50, 0, 100)

bubble_sort_numbers = list_of_numbers[:]
insertion_sort_numbers = list_of_numbers[:]
selection_sort_numbers = list_of_numbers[:]

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    draw_static_items()
    draw_bubble_surface(bubble_sort_numbers)
    draw_insertion_surface(insertion_sort_numbers)
    draw_selection_surface(selection_sort_numbers)

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
                    selection_thread = threading.Thread(target=selection_sort, args=(selection_sort_numbers, ))

                    bubble_thread.start()
                    insertion_thread.start()
                    selection_thread.start()

                    bubble_thread.join()
                    insertion_thread.join()
                    selection_thread.join()

                    print(timings)

    pygame.display.flip()