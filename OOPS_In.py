import tkinter as tk
from tkinter import messagebox
import random
from enum import Enum
from typing import List, Tuple, Optional, Callable
from abc import ABC, abstractmethod
import time

# Enums for game states and cell states
class CellState(Enum):
    HIDDEN = "hidden"
    REVEALED = "revealed"
    FLAGGED = "flagged"

class GameState(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
    PAUSED = "paused"

class Difficulty(Enum):
    BEGINNER = (9, 9, 10)      # rows, cols, mines
    INTERMEDIATE = (16, 16, 40)
    EXPERT = (16, 30, 99)
    
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines

# Observer Pattern for game events
class GameObserver(ABC):
    """Abstract observer for game events"""
    
    @abstractmethod
    def on_game_state_changed(self, new_state: GameState):
        pass
    
    @abstractmethod
    def on_cell_revealed(self, row: int, col: int):
        pass
    
    @abstractmethod
    def on_mine_count_changed(self, remaining_mines: int):
        pass

class Cell:
    """Represents a single cell in the minesweeper grid"""
    
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.is_mine = False
        self.state = CellState.HIDDEN
        self.adjacent_mines = 0
        self.button: Optional[tk.Button] = None
        
    def set_mine(self):
        """Set this cell as a mine"""
        self.is_mine = True
    
    def set_adjacent_mines(self, count: int):
        """Set the number of adjacent mines"""
        self.adjacent_mines = count
    
    def reveal(self) -> bool:
        """Reveal the cell. Returns True if it was a mine"""
        if self.state == CellState.FLAGGED:
            return False
            
        self.state = CellState.REVEALED
        return self.is_mine
    
    def toggle_flag(self) -> bool:
        """Toggle flag state. Returns True if flagged, False if unflagged"""
        if self.state == CellState.REVEALED:
            return self.state == CellState.FLAGGED
            
        if self.state == CellState.FLAGGED:
            self.state = CellState.HIDDEN
            return False
        else:
            self.state = CellState.FLAGGED
            return True
    
    def is_revealed(self) -> bool:
        return self.state == CellState.REVEALED
    
    def is_flagged(self) -> bool:
        return self.state == CellState.FLAGGED
    
    def is_hidden(self) -> bool:
        return self.state == CellState.HIDDEN

class MineGenerator:
    """Strategy pattern for mine generation algorithms"""
    
    @staticmethod
    def random_placement(grid: List[List[Cell]], mine_count: int, exclude_cell: Optional[Tuple[int, int]] = None):
        """Randomly place mines, optionally excluding a specific cell"""
        rows, cols = len(grid), len(grid[0])
        positions = [(r, c) for r in range(rows) for c in range(cols)]
        
        if exclude_cell:
            positions.remove(exclude_cell)
        
        mine_positions = random.sample(positions, mine_count)
        
        for row, col in mine_positions:
            grid[row][col].set_mine()

class GameBoard:
    """Core game logic and board management"""
    
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.remaining_mines = mines
        self.grid: List[List[Cell]] = []
        self.state = GameState.PLAYING
        self.observers: List[GameObserver] = []
        self.first_click = True
        self.revealed_cells = 0
        self.start_time = None
        
        self._create_grid()
    
    def _create_grid(self):
        """Initialize the grid with empty cells"""
        self.grid = []
        for row in range(self.rows):
            grid_row = []
            for col in range(self.cols):
                cell = Cell(row, col)
                grid_row.append(cell)
            self.grid.append(grid_row)
    
    def add_observer(self, observer: GameObserver):
        """Add observer for game events"""
        self.observers.append(observer)
    
    def notify_state_changed(self):
        """Notify observers of state change"""
        for observer in self.observers:
            observer.on_game_state_changed(self.state)
    
    def notify_cell_revealed(self, row: int, col: int):
        """Notify observers of cell revelation"""
        for observer in self.observers:
            observer.on_cell_revealed(row, col)
    
    def notify_mine_count_changed(self):
        """Notify observers of mine count change"""
        for observer in self.observers:
            observer.on_mine_count_changed(self.remaining_mines)
    
    def place_mines(self, exclude_cell: Tuple[int, int]):
        """Place mines on the board, excluding the first clicked cell"""
        MineGenerator.random_placement(self.grid, self.total_mines, exclude_cell)
        self._calculate_adjacent_mines()
    
    def _calculate_adjacent_mines(self):
        """Calculate adjacent mine counts for all cells"""
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.grid[row][col].is_mine:
                    count = self._count_adjacent_mines(row, col)
                    self.grid[row][col].set_adjacent_mines(count)
    
    def _count_adjacent_mines(self, row: int, col: int) -> int:
        """Count mines in adjacent cells"""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < self.rows and 
                    0 <= new_col < self.cols and
                    self.grid[new_row][new_col].is_mine):
                    count += 1
        return count
    
    def get_adjacent_cells(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Get coordinates of all adjacent cells"""
        adjacent = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    adjacent.append((new_row, new_col))
        return adjacent
    
    def reveal_cell(self, row: int, col: int) -> bool:
        """Reveal a cell and handle game logic. Returns True if game continues"""
        if self.state != GameState.PLAYING:
            return False
        
        cell = self.grid[row][col]
        
        if cell.is_revealed() or cell.is_flagged():
            return True
        
        # Handle first click
        if self.first_click:
            self.place_mines((row, col))
            self.first_click = False
            self.start_time = time.time()
        
        # Reveal the cell
        hit_mine = cell.reveal()
        
        if hit_mine:
            self.state = GameState.LOST
            self._reveal_all_mines()
            self.notify_state_changed()
            return False
        
        self.revealed_cells += 1
        self.notify_cell_revealed(row, col)
        
        # Auto-reveal adjacent cells if no adjacent mines
        if cell.adjacent_mines == 0:
            self._reveal_adjacent_empty_cells(row, col)
        
        # Check win condition
        if self.revealed_cells == (self.rows * self.cols - self.total_mines):
            self.state = GameState.WON
            self.notify_state_changed()
            return False
        
        return True
    
    def _reveal_adjacent_empty_cells(self, row: int, col: int):
        """Recursively reveal adjacent empty cells (flood fill algorithm)"""
        for adj_row, adj_col in self.get_adjacent_cells(row, col):
            adj_cell = self.grid[adj_row][adj_col]
            
            if not adj_cell.is_revealed() and not adj_cell.is_flagged():
                adj_cell.reveal()
                self.revealed_cells += 1
                self.notify_cell_revealed(adj_row, adj_col)
                
                if adj_cell.adjacent_mines == 0:
                    self._reveal_adjacent_empty_cells(adj_row, adj_col)
    
    def toggle_flag(self, row: int, col: int):
        """Toggle flag on a cell"""
        if self.state != GameState.PLAYING:
            return
        
        cell = self.grid[row][col]
        if cell.is_revealed():
            return
        
        was_flagged = cell.is_flagged()
        cell.toggle_flag()
        
        # Update mine counter
        if was_flagged:
            self.remaining_mines += 1
        else:
            self.remaining_mines -= 1
        
        self.notify_mine_count_changed()
    
    def _reveal_all_mines(self):
        """Reveal all mines when game is lost"""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].is_mine:
                    self.grid[row][col].state = CellState.REVEALED
                    self.notify_cell_revealed(row, col)
    
    def get_game_time(self) -> int:
        """Get elapsed game time in seconds"""
        if self.start_time is None:
            return 0
        return int(time.time() - self.start_time)
    
    def reset(self, rows: int = None, cols: int = None, mines: int = None):
        """Reset the game with optional new parameters"""
        if rows is not None:
            self.rows = rows
        if cols is not None:
            self.cols = cols
        if mines is not None:
            self.total_mines = mines
        
        self.remaining_mines = self.total_mines
        self.state = GameState.PLAYING
        self.first_click = True
        self.revealed_cells = 0
        self.start_time = None
        self._create_grid()

class GameUI(GameObserver):
    """GUI implementation using tkinter with Observer pattern"""
    
    def __init__(self, difficulty: Difficulty = Difficulty.BEGINNER):
        self.root = tk.Tk()
        self.root.title("Advanced Minesweeper")
        self.root.resizable(False, False)
        
        self.difficulty = difficulty
        self.game_board = GameBoard(difficulty.rows, difficulty.cols, difficulty.mines)
        self.game_board.add_observer(self)
        
        self.cell_buttons = []
        self.mine_label = None
        self.time_label = None
        self.face_button = None
        
        self._create_ui()
        self._update_timer()
        
        # Color schemes for different numbers
        self.number_colors = {
            1: "blue", 2: "green", 3: "red", 4: "purple",
            5: "maroon", 6: "turquoise", 7: "black", 8: "gray"
        }
    
    def _create_ui(self):
        """Create the complete user interface"""
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Beginner", command=lambda: self.set_difficulty(Difficulty.BEGINNER))
        game_menu.add_command(label="Intermediate", command=lambda: self.set_difficulty(Difficulty.INTERMEDIATE))
        game_menu.add_command(label="Expert", command=lambda: self.set_difficulty(Difficulty.EXPERT))
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)
        
        # Top panel with mine counter, face button, and timer
        top_frame = tk.Frame(self.root, bg="lightgray", relief=tk.RAISED, bd=2)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.mine_label = tk.Label(top_frame, text=f"{self.game_board.remaining_mines:03d}", 
                                  font=("Courier", 16, "bold"), bg="black", fg="red", width=3)
        self.mine_label.pack(side=tk.LEFT, padx=10)
        
        self.face_button = tk.Button(top_frame, text="🙂", font=("Arial", 16), 
                                    command=self.new_game, bg="lightgray")
        self.face_button.pack(side=tk.LEFT, expand=True)
        
        self.time_label = tk.Label(top_frame, text="000", 
                                  font=("Courier", 16, "bold"), bg="black", fg="red", width=3)
        self.time_label.pack(side=tk.RIGHT, padx=10)
        
        # Game board
        self._create_game_board()
    
    def _create_game_board(self):
        """Create the game board with buttons"""
        # Remove existing board if any
        if hasattr(self, 'board_frame'):
            self.board_frame.destroy()
        
        self.board_frame = tk.Frame(self.root, bg="lightgray", relief=tk.RAISED, bd=2)
        self.board_frame.pack(padx=5, pady=5)
        
        self.cell_buttons = []
        
        for row in range(self.game_board.rows):
            button_row = []
            for col in range(self.game_board.cols):
                btn = tk.Button(self.board_frame, width=2, height=1, font=("Arial", 10, "bold"))
                btn.grid(row=row, column=col, padx=1, pady=1)
                
                # Bind events
                btn.bind("<Button-1>", lambda e, r=row, c=col: self.left_click(r, c))
                btn.bind("<Button-3>", lambda e, r=row, c=col: self.right_click(r, c))
                
                button_row.append(btn)
                self.game_board.grid[row][col].button = btn
            
            self.cell_buttons.append(button_row)
        
        self._update_all_buttons()
    
    def left_click(self, row: int, col: int):
        """Handle left mouse click (reveal cell)"""
        if self.game_board.state == GameState.PLAYING:
            self.game_board.reveal_cell(row, col)
    
    def right_click(self, row: int, col: int):
        """Handle right mouse click (toggle flag)"""
        if self.game_board.state == GameState.PLAYING:
            self.game_board.toggle_flag(row, col)
            self._update_button(row, col)
    
    def new_game(self):
        """Start a new game"""
        self.game_board.reset()
        self.face_button.config(text="🙂")
        self._update_all_buttons()
    
    def set_difficulty(self, difficulty: Difficulty):
        """Change game difficulty"""
        self.difficulty = difficulty
        self.game_board.reset(difficulty.rows, difficulty.cols, difficulty.mines)
        self._create_game_board()
        self.root.geometry("")  # Auto-resize window
    
    def _update_button(self, row: int, col: int):
        """Update a specific button's appearance"""
        cell = self.game_board.grid[row][col]
        button = cell.button
        
        if cell.is_flagged():
            button.config(text="🚩", bg="yellow", relief=tk.RAISED)
        elif cell.is_revealed():
            if cell.is_mine:
                button.config(text="💣", bg="red", relief=tk.SUNKEN)
            else:
                text = str(cell.adjacent_mines) if cell.adjacent_mines > 0 else ""
                color = self.number_colors.get(cell.adjacent_mines, "black")
                button.config(text=text, fg=color, bg="lightgray", relief=tk.SUNKEN)
        else:
            button.config(text="", bg="lightgray", relief=tk.RAISED)
    
    def _update_all_buttons(self):
        """Update all button appearances"""
        for row in range(self.game_board.rows):
            for col in range(self.game_board.cols):
                self._update_button(row, col)
    
    def _update_timer(self):
        """Update the timer display"""
        if self.game_board.state == GameState.PLAYING and not self.game_board.first_click:
            elapsed = self.game_board.get_game_time()
            self.time_label.config(text=f"{min(elapsed, 999):03d}")
        
        # Schedule next update
        self.root.after(1000, self._update_timer)
    
    # Observer pattern implementations
    def on_game_state_changed(self, new_state: GameState):
        """Handle game state changes"""
        if new_state == GameState.WON:
            self.face_button.config(text="😎")
            messagebox.showinfo("Congratulations!", 
                              f"You won!\nTime: {self.game_board.get_game_time()} seconds")
        elif new_state == GameState.LOST:
            self.face_button.config(text="😵")
            messagebox.showinfo("Game Over", "You hit a mine!")
    
    def on_cell_revealed(self, row: int, col: int):
        """Handle cell revelation"""
        self._update_button(row, col)
    
    def on_mine_count_changed(self, remaining_mines: int):
        """Handle mine count changes"""
        self.mine_label.config(text=f"{remaining_mines:03d}")
    
    def run(self):
        """Start the game loop"""
        self.root.mainloop()

# Statistics and High Score System (Additional OOP Features)
class GameStatistics:
    """Track and manage game statistics"""
    
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.best_times = {
            Difficulty.BEGINNER: None,
            Difficulty.INTERMEDIATE: None,
            Difficulty.EXPERT: None
        }
        self.total_time_played = 0
    
    def record_game(self, won: bool, time_taken: int, difficulty: Difficulty):
        """Record the results of a completed game"""
        self.games_played += 1
        self.total_time_played += time_taken
        
        if won:
            self.games_won += 1
            current_best = self.best_times[difficulty]
            if current_best is None or time_taken < current_best:
                self.best_times[difficulty] = time_taken
    
    def get_win_percentage(self) -> float:
        """Calculate win percentage"""
        if self.games_played == 0:
            return 0.0
        return (self.games_won / self.games_played) * 100
    
    def get_average_game_time(self) -> float:
        """Calculate average game time"""
        if self.games_played == 0:
            return 0.0
        return self.total_time_played / self.games_played

# Factory Pattern for creating games with different configurations
class MinesweeperFactory:
    """Factory for creating minesweeper games with different configurations"""
    
    @staticmethod
    def create_beginner_game() -> 'GameUI':
        return GameUI(Difficulty.BEGINNER)
    
    @staticmethod
    def create_intermediate_game() -> 'GameUI':
        return GameUI(Difficulty.INTERMEDIATE)
    
    @staticmethod
    def create_expert_game() -> 'GameUI':
        return GameUI(Difficulty.EXPERT)
    
    @staticmethod
    def create_custom_game(rows: int, cols: int, mines: int) -> 'GameUI':
        # Create custom difficulty
        custom_difficulty = type('CustomDifficulty', (), {
            'rows': rows, 'cols': cols, 'mines': mines
        })()
        return GameUI(custom_difficulty)

# Main application class
class MinesweeperApp:
    """Main application controller"""
    
    def __init__(self):
        self.current_game = None
        self.statistics = GameStatistics()
    
    def start_new_game(self, difficulty: Difficulty = Difficulty.BEGINNER):
        """Start a new game with specified difficulty"""
        if self.current_game:
            self.current_game.root.destroy()
        
        self.current_game = GameUI(difficulty)
        return self.current_game
    
    def show_statistics(self):
        """Display game statistics"""
        stats_window = tk.Toplevel()
        stats_window.title("Game Statistics")
        stats_window.geometry("300x200")
        
        stats_text = f"""
Games Played: {self.statistics.games_played}
Games Won: {self.statistics.games_won}
Win Percentage: {self.statistics.get_win_percentage():.1f}%
Average Time: {self.statistics.get_average_game_time():.1f}s

Best Times:
Beginner: {self.statistics.best_times[Difficulty.BEGINNER] or 'N/A'}s
Intermediate: {self.statistics.best_times[Difficulty.INTERMEDIATE] or 'N/A'}s
Expert: {self.statistics.best_times[Difficulty.EXPERT] or 'N/A'}s
        """
        
        label = tk.Label(stats_window, text=stats_text, justify=tk.LEFT)
        label.pack(padx=20, pady=20)

# Demo function
def main():
    """Run the Minesweeper application"""
    print("Starting Advanced Minesweeper Game...")
    print("Features demonstrated:")
    print("- Complex OOP inheritance hierarchy")
    print("- Observer pattern for game events")
    print("- Strategy pattern for mine generation")
    print("- Factory pattern for game creation")
    print("- Encapsulation with private methods")
    print("- Polymorphism in UI updates")
    print("- Advanced algorithms (flood fill)")
    print("- GUI integration with tkinter")
    
    # Create and run the game
    app = MinesweeperApp()
    game = app.start_new_game(Difficulty.BEGINNER)
    
    print("\nGame Controls:")
    print("- Left click: Reveal cell")
    print("- Right click: Flag/unflag cell")
    print("- Face button: New game")
    print("- Menu: Change difficulty")
    
    game.run()

if __name__ == "__main__":
    main()