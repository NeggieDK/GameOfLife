import json
from GameModels.Figure import Figure 
from GameModels.GameLayout import GameLayout

class JsonParser:

    @staticmethod    
    def LoadFile(path):
        with open(path, 'r') as f:
            data = json.load(f)
            return data
        

    @staticmethod 
    def CreateLayout(path):
        try:
            data = JsonParser.LoadFile(path)
            boxColor = (int(data["BoxColor"]["r"]),int(data["BoxColor"]["g"]),int(data["BoxColor"]["b"]))
            lineColor = (int(data["LineColor"]["r"]),int(data["LineColor"]["g"]),int(data["LineColor"]["b"]))
            layout = GameLayout(int(data["Width"]), int(data["Height"]), int(data["BoxSize"]),boxColor, lineColor, float(data["AutoRunTime"]))
            return layout
        except json.decoder.JSONDecodeError:
            print("Error in config file, loading default layout!")
            return GameLayout(20,20,20,(0,0,255),(0,0,200),0.5)

    @staticmethod
    def CreateFigure(path):
        try:
            data = JsonParser.LoadFile(path)
            figure = Figure()
            figure.MinSizeX = data["minSizeX"]
            figure.MinSizeY = data["minSizeY"]
            figure.ActiveCells = data["Active"]
            return figure
        except json.decoder.JSONDecodeError:
            print("Error in config file, loading default layout!")
            figure = Figure()
            return figure
        except FileNotFoundError:
            print("File not found!")
            figure = Figure()
            return figure

    @staticmethod
    def CreateJson(text):
        return json.dumps(text)
