class player:
    def __init__(self, MoveRight,MoveLeft,MoveUp,MoveDown):
        self.MoveRight = MoveRight
        self.Left = MoveLeft
        self.MoveUp = MoveUp
        self.MoveDown = MoveDown

    def MoveX_function(self,MoveRight):
        if (MoveRight == True):
            return 2.5
        else:
            return 0
    def MoveXMinus_function(self,MoveLeft):
        if (MoveLeft == True):
            return -2.5
        else:
            return 0
    def MoveY_function(self,MoveUp):
        if (MoveUp == True):
            return 2.5
        else:
            return 0
    def MoveYMinus_function(self,MoveDown):
        if (MoveDown == True):
            return -2.5
        else:
            return 0
