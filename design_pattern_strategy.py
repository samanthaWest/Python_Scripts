# Strategy Design Pattern : Provide users a way to change behaviour of a class w/o extending it.
# Method that lets the nested object do the work as well as a setter to replace obj during run time.
from abc import ABC, abstractmethod

# Behaviourl Interface
class Tool(ABC):
    @abstractmethod
    def draw(self, data: str):
        pass

class MarkerTool(Tool):
    def draw(self, data:str) -> str:
        return "Drawing " + data + " with marker."

class PencilTool(Tool):
    def draw(self, data:str) -> str:
        return "Drawing " + data + " with pencil."

class WhiteBoard():
    """ Defines whiteboard client will interact with. """

    def __init__(self, tool: Tool) -> None:
        self._tool = tool

    @property
    def tool(self) -> Tool:
        return self._tool

    @tool.setter
    def tool(self, tool: Tool) -> None:
        self._tool = tool

    def drawing(self) -> None:
        draw = self._tool.draw("kite")
        print(draw)


if __name__ == "__main__":
    board_1 = WhiteBoard(MarkerTool())
    board_1.drawing()

    board_2 = WhiteBoard(PencilTool())
    board_2.drawing()