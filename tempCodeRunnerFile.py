
class Difficulty(Enum):
    BEGINNER = (9, 9, 10)      # rows, cols, mines
    INTERMEDIATE = (16, 16, 40)
    EXPERT = (16, 30, 99)
    
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows