from EnumTypes.RunMode import RunMode

class GameState:
    def __init__(self):
        self.RunMode = RunMode.MANUAL
        self.Done = False
        self.AllowNextStep = False
        self.StepNumber = 0
        self.Reset = False

    
