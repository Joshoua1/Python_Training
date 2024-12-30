import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class JackpotGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jackpot Game")
        self.jackpot_number = random.randint(1, 100)
        self.attempts = 0

        self.init_ui()

    def init_ui(self):
        self.label = QLabel("I've picked a number between 1 and 100. Can you guess it?", self)
        self.label.move(50, 20)

        self.entry = QLineEdit(self)
        self.entry.move(50, 50)

        self.button = QPushButton("Submit", self)
        self.button.move(50, 80)
        self.button.clicked.connect(self.check_guess)

        self.setGeometry(300, 300, 300, 150)

    def check_guess(self):
        guess = int(self.entry.text())
        self.entry.clear()
        self.attempts += 1

        if guess < self.jackpot_number:
            QMessageBox.information(self, "Jackpot Game", "Too low! Try again.")
        elif guess > self.jackpot_number:
            QMessageBox.information(self, "Jackpot Game", "Too high! Try again.")
        else:
            QMessageBox.information(self, "Jackpot Game", f"Congratulations! You guessed the correct number in {self.attempts} attempts!")

if __name__ == '__main__':
    app = QApplication([])
    game = JackpotGame()
    game.show()
    app.exec_()
