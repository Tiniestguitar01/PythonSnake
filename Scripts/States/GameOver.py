import Scripts.Dependency as Dependency
import Scripts.UI as UI

import Scripts.States.Game as Game

  
#Játék vége
class GameOverClass:

    def __init__(self,font,manager):
        self.font = font
        self.manager = manager
        self.ui = UI.UIClass(self.font)

    def run(self):
        Dependency.SCREEN.fill(Dependency.BLACK)

        #Szöveg
        self.ui.DisplayText('Game Over',Dependency.WINDOW_WIDTH/2,20,(255,0,0))
        self.ui.DisplayText('Press enter to restart',Dependency.WINDOW_WIDTH/2,Dependency.WINDOW_HEIGHT/2,Dependency.WHITE,(30,30,30))
        self.ui.DisplayText('High-Score: ' + str(Dependency.HIGH_SCORE),Dependency.WINDOW_WIDTH/2,Dependency.WINDOW_HEIGHT/2 + 20,Dependency.WHITE,(30,30,30))
        self.ui.DisplayText('Current Score: ' + str(Dependency.CURRENT_SCORE),Dependency.WINDOW_WIDTH/2,Dependency.WINDOW_HEIGHT/2 + 40,Dependency.WHITE,(30,30,30))

        keys = Dependency.pygame.key.get_pressed()
        if keys[Dependency.pygame.K_RETURN]:
            self.manager.SetState("Game")
