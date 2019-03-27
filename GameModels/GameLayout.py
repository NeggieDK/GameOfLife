class GameLayout:

    def __init__(self, horizontalLength, verticalLength, boxSize, boxColor, lineColor, autoRunTime):
        self._verticalLength = verticalLength
        self._horizontalLength = horizontalLength
        self.BoxSize = boxSize
        self.BoxColor = boxColor
        self.LineColor = lineColor
        self.DimensionsChanged = False
        self.AutoRunTime = autoRunTime

    def GetWindowDimensions(self):
        self.DimensionsChanged = False
        return (self.HorizontalLength*self.BoxSize,self.VerticalLength*self.BoxSize)

    @property
    def HorizontalLength(self):
        return self._horizontalLength

    @HorizontalLength.setter
    def HorizontalLength(self, value):
        self.DimensionsChanged = True
        self._horizontalLength = value

    @property
    def VerticalLength(self):
        return self._verticalLength

    @VerticalLength.setter
    def VerticalLength(self, value):
        self.DimensionsChanged = True
        self._verticalLength = value




