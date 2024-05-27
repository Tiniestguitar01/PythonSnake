import Scripts.Dependency as Dependency
import Scripts.UI as UI

#Játék előtti menü
class MenuClass:
    def __init__(self,font,manager):
        self.font = font
        self.manager = manager
        self.ui = UI.UIClass(self.font)

    def run(self):
        Dependency.SCREEN.fill(Dependency.BLACK)

        #Szöveg
        self.ui.DisplayText('Snake',Dependency.WINDOW_WIDTH/2,20,Dependency.WHITE)
        self.ui.DisplayText('Press enter to start',Dependency.WINDOW_WIDTH/2,Dependency.WINDOW_HEIGHT/2,Dependency.WHITE,(30,30,30))
        self.ui.DisplayText('Press M to stop the music',Dependency.WINDOW_WIDTH/2,Dependency.WINDOW_HEIGHT - 20,Dependency.WHITE,(30,30,30))

        keys = Dependency.pygame.key.get_pressed()
        if keys[Dependency.pygame.K_RETURN]:
            self.manager.SetState("Game")
