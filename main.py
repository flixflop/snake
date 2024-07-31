from view import TkinterSnakeGame
import tkinter as tk

def main():
    root = tk.Tk()
    game = TkinterSnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
