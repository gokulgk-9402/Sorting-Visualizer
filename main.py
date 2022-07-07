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
merge_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
quick_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
shell_sort_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

list_of_numbers = []
timings = {}

def generate_numbers(n, minimum, maximum):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(minimum, maximum))

    return numbers

def draw_static_items():
    window.fill(WHITE)
    title = TITLE_FONT.render("Sorting Visualizer", True, BLACK)
    rectangle = (WIDTH//2 - title.get_width()//2, 40)
    window.blit(title, rectangle)

    bubble_title = FONT.render("Bubble Sort", True, BLACK)
    window.blit(bubble_title, (15, 365))        

    insertion_title = FONT.render("Insertion Sort", True, BLACK)
    window.blit(insertion_title, (515, 365))

    merge_title = FONT.render("Merge Sort", True, BLACK)
    window.blit(merge_title, (15, 665))

    selection_title = FONT.render("Quick Sort", True, BLACK)
    window.blit(selection_title, (515, 665))

    selection_title = FONT.render("Selection Sort", True, BLACK)
    window.blit(selection_title, (15, 965))

    selection_title = FONT.render("Shell Sort", True, BLACK)
    window.blit(selection_title, (515, 965))

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

def draw_merge_surface(numbers, l, r, color_positions = {}):
    merge_sort_surface.fill(WHITE)

    for i in range(len(numbers)):
        if i < l or i > r:
            continue
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(merge_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(merge_sort_surface, (0,400))

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

def draw_quick_surface(numbers, color_positions = {}):
    quick_sort_surface.fill(WHITE)

    for i in range(len(numbers)):
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(quick_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(quick_sort_surface, (500,400))

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

def draw_shell_surface(numbers, color_positions = {}):
    shell_sort_surface.fill(WHITE)

    for i in range(len(numbers)):
        x = i * BAR_WIDTH + SURFACE_PADDING
        y = SURFACE_HEIGHT - (numbers[i]*BAR_HEIGHT) - SURFACE_PADDING

        color = COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * BAR_HEIGHT

        pygame.draw.rect(shell_sort_surface, color, (x, y, BAR_WIDTH, height))

    window.blit(shell_sort_surface, (500,700))

def bubble_sort(numbers):
    bubble_start = time.time()
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                draw_bubble_surface(numbers, {j:RED, j+1:GREEN})
                pygame.display.flip()
                time.sleep(0.01)

    bubble_end = time.time()
    timings["bubble"] = bubble_end - bubble_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['bubble'], 2)} seconds", True, BLACK)
    window.blit(time_text, (500-time_text.get_width()-20, 372))
    draw_bubble_surface(numbers)
    pygame.display.flip()

def insertion_sort(numbers):
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

    insertion_end = time.time()
    timings["insertion"] = insertion_end - insertion_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['insertion'], 2)} seconds", True, BLACK)
    window.blit(time_text, (1000-time_text.get_width()-20, 372))
    draw_insertion_surface(numbers)
    pygame.display.flip()

def merge_helper(numbers, left, right):
    # print(left, right)
    if len(numbers) > 1:
        draw_merge_surface(merge_sort_numbers[0:left] + numbers + merge_sort_numbers[right:], left, right, {left:RED, right:GREEN})
        pygame.display.flip()
    
        mid = len(numbers)//2

        left_numbers = numbers[:mid]
        right_numbers = numbers[mid:]
        
        merge_helper(left_numbers, left, left+mid-1)
        merge_helper(right_numbers, left+mid, right)

        i = j = k = 0
        while i < len(left_numbers) and j < len(right_numbers):
            if left_numbers[i] < right_numbers[j]:
                numbers[k] = left_numbers[i]
                draw_merge_surface(merge_sort_numbers[0:left] + numbers + merge_sort_numbers[right:], left, right, {k:RED, i:GREEN})
                pygame.display.flip()
                i += 1
            else:
                numbers[k] = right_numbers[j]
                draw_merge_surface(merge_sort_numbers[0:left] + numbers + merge_sort_numbers[right:], left, right, {k:RED, j:GREEN})
                pygame.display.flip()
                j += 1
            
            time.sleep(0.01)
            k += 1

        while i < len(left_numbers):
            numbers[k] = left_numbers[i]
            time.sleep(0.01)
            i += 1
            k += 1
        
        while j < len(right_numbers):
            numbers[k] = right_numbers[j]
            time.sleep(0.01)
            j += 1
            k += 1

        # print(merge_sort_numbers)

        draw_merge_surface(merge_sort_numbers[0:left] + numbers + merge_sort_numbers[right:], left, right)
        pygame.display.flip()

def merge_sort(numbers):
    merge_start = time.time()
    
    merge_helper(numbers, 0, len(numbers)-1)

    merge_end = time.time()
    timings["merge"] = merge_end - merge_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['merge'], 2)} seconds", True, BLACK)
    # merge_sort_surface.fill((255, 255, 255, 255))
    window.blit(time_text, (500-time_text.get_width()-20, 672))
    # draw_merge_surface(numbers, 0, len(numbers)-1)
    pygame.display.flip()

def quick_sort(numbers):
    quick_start = time.time()
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                draw_quick_surface(numbers, {j:RED, j+1:GREEN})
                pygame.display.flip()
                time.sleep(0.01)

    quick_end = time.time()
    timings["quick"] = quick_end - quick_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['quick'], 2)} seconds", True, BLACK)
    window.blit(time_text, (1000-time_text.get_width()-20, 672))
    draw_quick_surface(numbers)
    pygame.display.flip()

def shell_sort(numbers):
    shell_start = time.time()
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                draw_shell_surface(numbers, {j:RED, j+1:GREEN})
                pygame.display.flip()
                time.sleep(0.01)

    shell_end = time.time()
    timings["shell"] = shell_end - shell_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['shell'], 2)} seconds", True, BLACK)
    window.blit(time_text, (1000-time_text.get_width()-20, 972))
    draw_shell_surface(numbers)
    pygame.display.flip()

def selection_sort(numbers):
    selection_start = time.time()
    for i in range(len(numbers)):
        minimum = i
        for j in range(i+1, len(numbers)):
            if numbers[minimum] > numbers[j]:
                time.sleep(0.02)
                minimum = j

        if minimum != i:
            numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
            draw_selection_surface(numbers, {minimum:RED, i: GREEN})
            pygame.display.flip()
            time.sleep(0.02)

    selection_end = time.time()
    timings["selection"] = selection_end - selection_start
    time_text = TIME_FONT.render(f"  Time Taken: {round(timings['selection'], 2)} seconds", True, BLACK)
    window.blit(time_text, (500-time_text.get_width()-20, 972))
    draw_selection_surface(numbers)
    pygame.display.flip()

list_of_numbers = generate_numbers(50, 0, 100)

bubble_sort_numbers = list_of_numbers[:]
insertion_sort_numbers = list_of_numbers[:]
merge_sort_numbers = list_of_numbers[:]
selection_sort_numbers = list_of_numbers[:]
quick_sort_numbers = list_of_numbers[:]
shell_sort_numbers = list_of_numbers[:]

clock = pygame.time.Clock()
draw_static_items()

draw_bubble_surface(bubble_sort_numbers)
draw_insertion_surface(insertion_sort_numbers)
draw_merge_surface(merge_sort_numbers, 0, len(merge_sort_numbers)-1)
draw_selection_surface(selection_sort_numbers)
draw_quick_surface(selection_sort_numbers)
draw_shell_surface(selection_sort_numbers)

while True:
    clock.tick(60)

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    list_of_numbers = generate_numbers(50, 0, 100)
                    bubble_sort_numbers = list_of_numbers[:]
                    insertion_sort_numbers = list_of_numbers[:]
                    merge_sort_numbers = list_of_numbers[:]
                    selection_sort_numbers = list_of_numbers[:]
                    quick_sort_numbers = list_of_numbers[:]
                    shell_sort_numbers = list_of_numbers[:]
                    
                    draw_bubble_surface(bubble_sort_numbers)
                    draw_insertion_surface(insertion_sort_numbers)
                    draw_merge_surface(merge_sort_numbers, 0, len(merge_sort_numbers))
                    draw_selection_surface(selection_sort_numbers)
                    draw_quick_surface(selection_sort_numbers)
                    draw_shell_surface(selection_sort_numbers)
                
                elif event.key == pygame.K_SPACE:
                    bubble_thread = threading.Thread(target=bubble_sort, args=(bubble_sort_numbers,))
                    insertion_thread = threading.Thread(target=insertion_sort, args=(insertion_sort_numbers,))
                    merge_thread = threading.Thread(target=merge_sort, args=(merge_sort_numbers, ))
                    selection_thread = threading.Thread(target=selection_sort, args=(selection_sort_numbers, ))
                    shell_thread = threading.Thread(target=shell_sort, args=(shell_sort_numbers, ))
                    quick_thread = threading.Thread(target=quick_sort, args=(quick_sort_numbers, ))

                    bubble_thread.start()
                    insertion_thread.start()
                    merge_thread.start()
                    selection_thread.start()
                    shell_thread.start()
                    quick_thread.start()

                    bubble_thread.join()
                    insertion_thread.join()
                    merge_thread.join()
                    selection_thread.join()
                    shell_thread.join()
                    quick_thread.join()

                    # quick_sort(quick_sort_numbers)
                    # shell_sort(shell_sort_numbers)
                    # bubble_sort(bubble_sort_numbers)
                    # insertion_sort(insertion_sort_numbers)

                    print(timings)

    pygame.display.flip()