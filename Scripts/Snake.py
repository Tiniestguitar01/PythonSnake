import Scripts.Dependency as Dependency
import Scripts.UI as UI
import Scripts.Manager as Manager

import Scripts.States.Game as Game
import Scripts.States.Menu as Menu
import Scripts.States.GameOver as GameOver

#Fő osztály (Az adott állapottól függően jeleníti meg a képernyőt)
class SnakeClass:
    running  = True
    manager = Manager.ManagerClass("Menu")
    states = {}

    def __init__(self,running):
        Dependency.pygame.init()
        self.running = running
        self.font = Dependency.pygame.font.Font('Font/PressStart2P.ttf', 15)
        Dependency.pygame.display.set_caption('Snake')
        icon = Dependency.pygame.image.load('Images/icon.png')
        Dependency.pygame.display.set_icon(icon)
        Dependency.pygame.mixer.music.load('Sounds/Music/Will 2 pwr - half.cool.mp3')
        Dependency.pygame.mixer.music.play(-1)
        Dependency.pygame.mixer.music.set_volume(0.5)

        self.game = Game.GameClass(self.font,self.manager)
        self.menu = Menu.MenuClass(self.font,self.manager)
        self.gameover = GameOver.GameOverClass(self.font,self.manager)

        self.states['Game'] = self.game
        self.states['Menu'] = self.menu
        self.states['GameOver'] = self.gameover

    def run(self):
        #Játék ciklus
        while self.running:
        
            #Az aktuális állapot betöltése
            self.states[self.manager.GetState()].run()

            #Kilépés
            for event in Dependency.pygame.event.get():  
                if event.type == Dependency.pygame.QUIT:  
                    self.running = False
                
                if event.type == Dependency.pygame.KEYDOWN:
                    if event.key == Dependency.pygame.K_m:
                        global MUSIC
                        if MUSIC:
                            Dependency.pygame.mixer.music.stop()
                            MUSIC = False
                        else:
                            Dependency.pygame.mixer.music.play(-1)
                            MUSIC = True

            Dependency.pygame.display.update()