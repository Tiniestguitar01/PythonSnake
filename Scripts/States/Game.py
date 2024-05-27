import Scripts.Dependency as Dependency
import Scripts.UI as UI
import Scripts.Manager as Manager

#Játék osztály (Tartalmazza a játék logikáját)
class GameClass:

    #Kígyó adatai
    snake_size = 3
    snake_width = 20
    snake_height = 20
    x = 200
    y = 200
    direction = 1  #1->balra, 2->jobbra, 3->fel, 4->le
    moved = False
    snake_parts = []

    spawn_fruit = True
    collected = 0
    fruit_x = 0
    fruit_y = 0
    
    game_over = False

    def __init__(self,font,manager):
        self.font = font
        self.manager = manager
        self.ui = UI.UIClass(self.font)
        self.start_time = Dependency.pygame.time.get_ticks()
        self.Start()

    def SpawnFruit(self):
        fruit_x = Dependency.random.randrange( 0, Dependency.WINDOW_WIDTH - self.snake_width,self.snake_width)
        fruit_y = Dependency.random.randrange( self.snake_height*2, Dependency.WINDOW_HEIGHT - self.snake_height,self.snake_height)

        for i in range(1,self.snake_size):
            if fruit_x == self.snake_parts[i].x and fruit_y == self.snake_parts[i].y:
                fruit_x, fruit_y = self.SpawnFruit()

        return fruit_x,fruit_y
    
    def Start(self):
        #Kígyó adatai
        self.snake_size = 3
        self.x = 200
        self.y = 200
        self.direction = 1  #1->balra, 2->jobbra, 3->fel, 4->le
        self.moved = False
        self.game_over = False
        self.spawn_fruit = True
        self.collected = 0

        global GAMESPEED
        GAMESPEED = 120

        #Kígyó részei
        self.snake_parts.clear()
        for i in range(self.snake_size):
            self.snake_parts.append(Dependency.pygame.Rect(self.x + i*self.snake_width,self.y,self.snake_width,self.snake_height))

    def run(self):
        global GAMESPEED
        Dependency.pygame.time.delay(GAMESPEED)
        Dependency.SCREEN.fill(Dependency.BLACK)

        #Négyzetrács
        for i in range(0, Dependency.WINDOW_WIDTH, self.snake_width):
            for j in range(self.snake_height*2, Dependency.WINDOW_HEIGHT, self.snake_height):
                rect = Dependency.pygame.Rect(i, j, self.snake_width, self.snake_height)
                Dependency.pygame.draw.rect(Dependency.SCREEN, (20,20,20), rect, 1)
        
        if self.game_over == False:

            #Kígyó megjelenítése
            for i in range(1,self.snake_size):
                Dependency.pygame.draw.rect(Dependency.SCREEN,Dependency.WHITE,Dependency.pygame.Rect(self.snake_parts[i].x,self.snake_parts[i].y,self.snake_width,self.snake_height))
            Dependency.pygame.draw.rect(Dependency.SCREEN,(0, 150, 255),Dependency.pygame.Rect(self.x,self.y,self.snake_width,self.snake_height))

            #Szöveg
            self.ui.DisplayText('Point: ' + str(self.collected),Dependency.WINDOW_WIDTH - 70,20,Dependency.WHITE)

            #Gyümölcs lehelyezése
            if self.spawn_fruit == True:
                self.fruit_x, self.fruit_y = self.SpawnFruit()
                self.spawn_fruit = False
            Dependency.pygame.draw.rect(Dependency.SCREEN,(255,0,0),Dependency.pygame.Rect(self.fruit_x,self.fruit_y,self.snake_width,self.snake_height))

            #Gyümölcs felvétele
            if self.x == self.fruit_x and self.y == self.fruit_y:
                self.spawn_fruit = True
                self.collected += 1
                self.snake_size += 1
                self.snake_parts.append(Dependency.pygame.Rect(self.snake_parts[-1].x,self.snake_parts[-1].y,self.snake_width,self.snake_height))
                if GAMESPEED > 24:
                    GAMESPEED -= 2
                pickup = Dependency.pygame.mixer.Sound("Sounds/pickup.wav")
                Dependency.pygame.mixer.Sound.play(pickup)

            #Mozgás
            keys = Dependency.pygame.key.get_pressed()
            if (keys[Dependency.pygame.K_LEFT] or keys[Dependency.pygame.K_a]) and self.direction != 2:
                self.direction = 1
            elif (keys[Dependency.pygame.K_RIGHT] or keys[Dependency.pygame.K_d]) and self.direction != 1:
                self.direction = 2
            elif (keys[Dependency.pygame.K_UP] or keys[Dependency.pygame.K_w]) and self.direction != 4:
                self.direction = 3
            elif (keys[Dependency.pygame.K_DOWN] or keys[Dependency.pygame.K_s]) and self.direction != 3:
                self.direction = 4

            time = Dependency.pygame.time.get_ticks() - self.start_time
            if time >= GAMESPEED:
                if self.direction == 1:
                    if self.x <= 0:
                        self.x = Dependency.WINDOW_WIDTH - self.snake_width
                    else:
                        self.x -= self.snake_height
                    self.moved = True
                elif self.direction == 2:
                    if self.x >= Dependency.WINDOW_WIDTH - self.snake_width:
                        self.x = 0
                    else:
                        self.x += self.snake_height
                    self.moved = True
                elif self.direction == 3:
                    if self.y <= self.snake_height*2:
                        self.y = Dependency.WINDOW_HEIGHT - self.snake_height 
                    else:
                        self.y -= self.snake_height
                    self.moved = True
                elif self.direction == 4:
                    if self.y >= Dependency.WINDOW_HEIGHT - self.snake_height:
                        self.y = self.snake_height*2
                    else:
                        self.y += self.snake_height
                    self.moved = True
                self.start_time = Dependency.pygame.time.get_ticks()

            #A kígyó pozíciójának frissítése
            if self.moved:
                self.snake_parts[0].x = self.x
                self.snake_parts[0].y = self.y

                for i in range(self.snake_size - 1,0,-1):
                    self.snake_parts[i].x = self.snake_parts[i - 1].x
                    self.snake_parts[i].y = self.snake_parts[i - 1].y
                self.moved = False
                    
            #Tesztelés (Bele ütközött-e saját magába)
            for i in range(2,self.snake_size):
                if self.x == self.snake_parts[i].x and self.y == self.snake_parts[i].y:
                    self.game_over = True
                    Dependency.CURRENT_SCORE = self.collected
                    if Dependency.CURRENT_SCORE > Dependency.HIGH_SCORE:
                        Dependency.HIGH_SCORE = Dependency.CURRENT_SCORE
                    self.Start()
                    self.manager.SetState("GameOver")
                    break
 