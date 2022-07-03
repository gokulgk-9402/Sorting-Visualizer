import time
import pygame
import random
import sys

pygame.init()

class ScreenInfo:
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    GREEN = 100, 255, 100
    RED = 255, 100, 100
    GREY = 150, 150, 150
    BLUE = 100, 100, 255
    BG = WHITE

    # COLORS = [(200, 200, 200), (150, 150, 150), (100, 100, 100)]
    COLORS = [(150, 150, 255), (175, 175, 255), (200, 200, 255)]


    PADDING = 50

    def __init__(self, w, h, numbers):
        self.WIDTH = w
        self.HEIGHT = h

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sorting Visualizer")
        self.set_numbers(numbers)

    def set_numbers(self, nums):
        self.nums = nums
        self.maximum = max(self.nums)
        self.minimum = min(self.nums)

        self.bar_width = (self.WIDTH - (2*self.PADDING)) // len(self.nums)
        self.bar_height = (self.WIDTH - 2 * self.PADDING) // self.maximum
        self.start_graph_x = self.PADDING
        self.start_graph_y = self.HEIGHT - self.PADDING

def generate_numbers(n, minimum, maximum):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(minimum, maximum))

    return numbers

def draw(screen_info):
    screen_info.window.fill(screen_info.BG)
    draw_bars(screen_info)
    pygame.display.flip()

def draw_bars(screen_info, color_positions = {}, clear = False):
    numbers = screen_info.nums

    if clear:
        rectangle = (screen_info.PADDING, screen_info.PADDING, 
        screen_info.WIDTH - 2*screen_info.PADDING, 
        screen_info.HEIGHT - 2 * screen_info.PADDING)

        pygame.draw.rect(screen_info.window, screen_info.BG, rectangle)

    for i in range(len(numbers)):
        x = i * screen_info.bar_width + screen_info.PADDING
        y = screen_info.HEIGHT - (numbers[i] * screen_info.bar_height) - screen_info.PADDING
        
        color = screen_info.COLORS[i%3]

        if i in color_positions:
            color = color_positions[i]

        height = numbers[i] * screen_info.bar_height

        pygame.draw.rect(screen_info.window, color, (x, y, screen_info.bar_width, height))
    
    if clear:
        pygame.display.flip()

def bubble_sort(screen_info):
    nums = screen_info.nums

    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                draw_bars(screen_info, {j:screen_info.RED, j+1:screen_info.GREEN}, True)
                time.sleep(0.05)
                # return False
                # yield True

    return True

def main():
    clock = pygame.time.Clock()

    numbers = generate_numbers(50, 0, 100)
    screen_info = ScreenInfo(800, 800, numbers)
    sorting = False

    while True:
        clock.tick(60)
        draw(screen_info)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    numbers = generate_numbers(50, 0, 100)
                    screen_info.set_numbers(numbers)
                    sorting = False

                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True

        if sorting:
            sorted = bubble_sort(screen_info)
            if sorted:
                sorting = False
            

        pygame.display.flip()

if __name__ == "__main__":
    main()