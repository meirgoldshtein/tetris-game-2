from abc import ABC, abstractmethod
import pygame
import random

# A cube shape object, a cornerstone for all shapes that have several cubes
class Shape(ABC):

    length_cube = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @abstractmethod
    def draw(self, surface):
        pass            


class Straight(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255,0,0)
        self.diraction = 0
    
# # Define the positions of all shape cubes relative to the base cube,
# considering the variable "diraction" that defines the shape rotation,
# Draw the shape if a screen parameter was received, if screen=none was set return the list of points
    
    def draw(self, surface):
        
        if self.diraction == 0 or self.diraction == 2:        
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x, self.x
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - 2*Shape.length_cube, self.y - 3*Shape.length_cube             
        elif self.diraction == 1 or self.diraction == 3:    
            self.x1, self.x2, self.x3, self.x4 = self.x - Shape.length_cube, self.x, self.x + Shape.length_cube, self.x + 2*Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y, self.y 

        points = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3],[self.x4, self.y4]] 
        if surface:

            for point in points:   
                rect = pygame.Rect(point[0], point[1], Shape.length_cube -1, Shape.length_cube -1)
                pygame.draw.rect(surface, self.color, rect, border_radius=2) 
        else:
            return points
        

class Cube(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (150,200,250)
    
    def draw(self, surface):
        self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x , self.x + Shape.length_cube
        self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y - Shape.length_cube, self.y - Shape.length_cube 
        
        points = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3],[self.x4, self.y4]] 
        if surface:
            for point in points:   
                rect = pygame.Rect(point[0], point[1], Shape.length_cube -1, Shape.length_cube-1)
                pygame.draw.rect(surface, self.color, rect, border_radius=2) 
        else:
            return points


class Plus(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255,255,255)
        self.diraction = 0

    def draw(self, surface):
            
        if self.diraction == 0 :   
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x + 2*Shape.length_cube, self.x + Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y, self.y - Shape.length_cube            
        elif self.diraction == 1:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x + Shape.length_cube, self.x
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - Shape.length_cube, self.y - 2*Shape.length_cube            
        elif self.diraction == 2:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x - Shape.length_cube, self.x, self.x + Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y -Shape.length_cube, self.y - Shape.length_cube 
        elif self.diraction == 3:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x, self.x - Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y , self.y - Shape.length_cube, self.y - 2*Shape.length_cube, self.y - Shape.length_cube

        points = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3],[self.x4, self.y4]] 
        if surface:
            for point in points:   
                rect = pygame.Rect(point[0], point[1], Shape.length_cube -1, Shape.length_cube-1)
                pygame.draw.rect(surface, self.color, rect, border_radius=2) 
        else:
            return points        
  

class Zigzag(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255,255,0)
        self.diraction = 0
    def draw(self, surface):
        
        if self.diraction == 0:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x + Shape.length_cube, self.x + 2*Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y - Shape.length_cube, self.y - Shape.length_cube 
        elif self.diraction == 1:
            self.x1, self.x2, self.x3, self.x4  = self.x, self.x, self.x - Shape.length_cube, self.x - Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - Shape.length_cube, self.y - 2*Shape.length_cube
        elif self.diraction == 2:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x, self.x - Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y,  self.y - Shape.length_cube, self.y - Shape.length_cube
        elif self.diraction == 3:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x + Shape.length_cube, self.x + Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - Shape.length_cube, self.y - 2*Shape.length_cube             

        points = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3],[self.x4, self.y4]] 
        if surface:

            for point in points:   
                rect = pygame.Rect(point[0], point[1], Shape.length_cube -1, Shape.length_cube-1)
                pygame.draw.rect(surface, self.color, rect, border_radius=2) 
        else:
            return points        
       

class Hook(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0,255,50)    
        self.diraction = 0    
    
    def draw(self, surface):
        
        if self.diraction == 0:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x, self.x + Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - 2*Shape.length_cube, self.y - 2*Shape.length_cube
        elif self.diraction == 1:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x, self.x - Shape.length_cube, self.x - 2*Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y - Shape.length_cube, self.y - Shape.length_cube, self.y - Shape.length_cube
        elif self.diraction == 2:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x + Shape.length_cube, self.x + Shape.length_cube
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y - Shape.length_cube, self.y - 2*Shape.length_cube
        elif self.diraction == 3:
            self.x1, self.x2, self.x3, self.x4 = self.x, self.x + Shape.length_cube, self.x + 2*Shape.length_cube, self.x
            self.y1, self.y2, self.y3, self.y4 = self.y, self.y, self.y, self.y - Shape.length_cube 

        points = [[self.x1, self.y1],[self.x2, self.y2],[self.x3, self.y3],[self.x4, self.y4]] 
        if surface:

            for point in points:   
                rect = pygame.Rect(point[0], point[1], Shape.length_cube -1, Shape.length_cube-1)
                pygame.draw.rect(surface, self.color, rect, border_radius=2) 
        else:
            return points        

# the rows, columns, height, width, of the Tetris screen   
columns = 18
rows = 30
Screen_width = columns * Shape.length_cube
Screen_length = rows * Shape.length_cube


class Trafic_control():
    
    # A list into which the values of the positions of the cubes that are not in motion will be inserted, 
    # to the appropriate index according to the row and column number of the shape
    lines = [[None for _ in range(columns)] for _ in range(rows)]
    Deleted_lines = 0
    # Check if a shape doesn't go beyond the screen border on the right
    def right_border(shape):
        limit = Screen_width - Shape.length_cube
        shape.draw(surface=None)
        if shape.x1 >= limit or shape.x2 >= limit or shape.x3 >= limit or shape.x4 >= limit: 
            return False
        return True
    
    # Check if a shape doesn't go beyond the screen border on the left
    def left_border(shape):
        shape.draw(surface=None)
        if shape.x1 <= 0 or shape.x2 <= 0 or shape.x3 <= 0 or shape.x4 <= 0: 
            return False
        return True
    
    # If the screen borders were exceeded, move the shape into the screen, and return the value of the exception
    def fix_board(shape):        
        max_x = max(shape.x1, shape.x2, shape.x3, shape.x4)
        min_x = min (shape.x1, shape.x2, shape.x3, shape.x4)
        limit = Screen_width - Shape.length_cube
        if max_x > limit:
            rest = max_x - limit
            shape.x -= rest
            return rest
        if min_x < 0:
            rest = 0 + min_x
            shape.x -= rest
            return rest
        return 0
    
    # Draw all the shapes that have already finished falling, according to their points on the list
    def general_draw(Surface, point_list):
        for i in range(len(point_list)):
            for j in range(len(point_list[i])):
                if point_list[i][j] is not None:  
                    rect = pygame.Rect(point_list[i][j][0], point_list[i][j][1], Shape.length_cube -1, Shape.length_cube-1)
                    pygame.draw.rect(Surface, point_list[i][j][2], rect, border_radius=2)

    #  Check in the list if there is a row that has been filled with cubes, 
    # if so, delete the row and download all the rows above it
    def full_line(point_list):
        for y in range(len(point_list)):
            if all(point_list[y][x] for x in range(columns)):
                Trafic_control.Deleted_lines += 1
                for x_2 in range(columns):
                    point_list [y][x_2] = None
                for row in range(y - 1, 0, -1):
                    for x_3 in range(columns):
                        if point_list[row][x_3] is not None:
                            point_list[row][x_3][1] += Shape.length_cube
                            point_list[row + 1][x_3] = point_list[row][x_3]
                            point_list[row][x_3] = None
        return point_list

    # Add the dropped shape cubes to the list
    def add_to_list(lines, shape):
        point = shape.draw(surface=None)
        for i in range(len(shape.draw(surface=None))):
            lines[point[i][1]//Shape.length_cube][point[i][0]//Shape.length_cube] = point[i] + [shape.color]

    #  Check if a shape will collide with another shape already in the list
    def collision(shape, lines):
        points = shape.draw(surface=None)
        for i in range(len(points)):
            p = [points[i][0] // Shape.length_cube, (points[i][1]+Shape.length_cube) // Shape.length_cube]
            if 0 <= p[1]<= rows - 1 and p[0] < columns and lines[p[1]][p[0]] is not None :
                return True
        return False

     #  Check if the rotating shape will collide with another shape already in the list
    def collision_swich(shape, lines):
        points = shape.draw(surface=None)
        for i in range(len(points)):
            p = [points[i][0] // Shape.length_cube, (points[i][1]) // Shape.length_cube]
            if 0 <= p[1]<= rows - 1 and p[0] < columns  and lines[p[1]][p[0]] is not None :
                return True
        return False

    #  Check if the screen is free on the right from other shaps
    def check_right(shape, lines):
        points = shape.draw(surface=None)
        for i in range(len(points)):
            p = [(points[i][0]+Shape.length_cube) // Shape.length_cube, points[i][1] // Shape.length_cube]
            if 0 <= p[1] <= rows - 1 and p[0] < columns  and lines[p[1]][p[0]] is not None :
                return False
        return True

    #  Check if the screen is free on the left from other shaps
    def check_left(shape, lines):
        points = shape.draw(surface=None)
        for i in range(len(points)):
            p = [(points[i][0]-Shape.length_cube) // Shape.length_cube, points[i][1] // Shape.length_cube]
            if 0 <= p[1]<= rows - 1 and lines[p[1]][p[0]] is not None :
                return False
        return True


class Raning():


    def play():    
        vol = 0.0
        pygame.init()
        # music = pygame.mixer.music
        # music.load("Tetris_tune.mp3")
        # music.set_volume(vol)
        # music.play(loops=-1)
        surface = pygame.display.set_mode(((columns * 20) + 180, 600))
        # IMAGE = 'p.png'
        # img = pygame.transform.scale(pygame.image.load(IMAGE), (361, 600))
        clock = pygame.time.Clock()
        counter = 0
        text_2 = None
        font = pygame.font.Font(None, 40)
        new_shape = True
        next = True
        
        while True:
            # music.set_volume(vol)
            surface.fill((24, 64,  150))
            # surface.blit(img , (0, 0))
        
            rand_x = random.randrange(0, (Screen_width - (Shape.length_cube * 2)), Shape.length_cube)
            
            if new_shape:
                shape = random.choice([Straight, Cube, Plus, Zigzag, Hook])(rand_x, 0)
                new_shape = False  
            
            # If a shape can't start going down, it's game over
            if shape.y < Shape.length_cube and Trafic_control.collision(shape, Trafic_control.lines):
                text_2 = "game over"
                next = False
            
            # If there is already a shape from below or the shape has reached the bottom of the screen, add the shape to the list, 
            # check if a line is filled, and continue to the next shape
            if Trafic_control.collision(shape, Trafic_control.lines) or shape.y == (rows - 1) *20 and next:
                Trafic_control.add_to_list(Trafic_control.lines, shape)
                Trafic_control.full_line(Trafic_control.lines)
                counter = 0
                new_shape = True  
            
            #  If none of the above scenarios happened, move the shape down
            elif next:
                shape.y += Shape.length_cube
                shape.draw(surface)
            
            
            clock.tick(100)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
                #  Control the volume with the U and D keys
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    vol += 0.1 if vol <= 1 else 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    vol -= 0.1 if vol >= -0.1  else 0
                
                # Move the shape to the right or left by pressing the direction keys, 
                # as long as there is no collision with another shape or leaving the borders of the screen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and Trafic_control.right_border(shape) and Trafic_control.check_right(shape, Trafic_control.lines):
                    shape.x += Shape.length_cube                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and Trafic_control.left_border(shape) and Trafic_control.check_left(shape, Trafic_control.lines):                 
                    shape.x -= Shape.length_cube
                    
                #  By pressing the space key, give a value from 0 to 3 and rotate the shape
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    counter += 1
                    shape.diraction = counter  % 4
                    shape.draw(surface=None)                    
                    rest = (Trafic_control.fix_board(shape))
                    
                    #  If there is a collision following the rotation of the shape, cancel the rotation
                    if Trafic_control.collision_swich(shape, Trafic_control.lines):
                        counter -= 1
                        shape.diraction = counter  % 4
                        shape.draw(surface=None)
                        
                        #  If the screen borders are exceeded following the rotation, and the shape cannot be pushed in 
                        #  because it will collide with another shape, cancel pushing the shape
                        if rest and Trafic_control.collision_swich(shape, Trafic_control.lines):
                            shape.x += rest
                            shape.draw(surface=None)
                #  Speed the shape down by pressing the direction key 
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and not Trafic_control.collision(shape, Trafic_control.lines) and shape.y < 580:
                    shape.y += Shape.length_cube
            
            #  Draw all the shapes that are not
            Trafic_control.general_draw(surface, Trafic_control.lines)
            
            #  Draw height and width lines on the screen
            for i in range(rows):
                pygame.draw.line(surface, (100, 120, 250), (0, i * Shape.length_cube), (Screen_width, i * Shape.length_cube), 1)
            for i in range(columns + 1):
                pygame.draw.line(surface, (100, 120, 250), (i * Shape.length_cube, 0), (i * Shape.length_cube , Screen_length), 1)   
            
            text = f"{Trafic_control.Deleted_lines} points"    
            text_image = font.render(text, True, (255, 100, 255), (24, 64,  122))
            surface.blit(text_image, (410, 50))    
            text_image_2 = font.render(text_2, True, (255, 100, 100), (24, 64,  122))
            surface.blit(text_image_2, (120, 300))
            pygame.display.update()
        
Raning.play()