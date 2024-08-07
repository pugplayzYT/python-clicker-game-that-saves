import tkinter as tk
import json
import os

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        self.click_count = 0
        self.load_clicks()

        self.label = tk.Label(root, text=f"Clicks: {self.click_count}", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.click_button = tk.Button(root, text="Click me!", command=self.click, font=("Helvetica", 16))
        self.click_button.pack(pady=20)

        self.save_button = tk.Button(root, text="Save Clicks", command=self.save_clicks, font=("Helvetica", 16))
        self.save_button.pack(pady=20)

    def click(self):
        self.click_count += 1
        self.label.config(text=f"Clicks: {self.click_count}")

    def load_clicks(self):
        if os.path.exists("clicks.json"):
            with open("clicks.json", "r") as file:
                data = json.load(file)
                self.click_count = data.get("click_count", 0)

    def save_clicks(self):
        with open("clicks.json", "w") as file:
            json.dump({"click_count": self.click_count}, file)

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
