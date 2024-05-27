import Scripts.Dependency as Dependency

#Felíratok megjelenítéséhez
class UIClass:
    def __init__(self,font):
        self.font = font

    def DisplayText(self,text,x,y,color,backgroundColor = Dependency.BLACK):
        t = self.font.render(text, True, color,backgroundColor)
        textRect = t.get_rect()
        textRect.center = (x, y)
        Dependency.SCREEN.blit(t, textRect)