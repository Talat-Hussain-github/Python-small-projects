from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys
import math

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Machine Esab")
        
        # Create a central widget and set it
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create a vertical layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Create a result entry field
        self.result_entry = QLineEdit()
        self.result_entry.setAlignment(Qt.AlignRight)
        self.result_entry.setReadOnly(True)
        self.result_entry.setStyleSheet("font-size: 24px; padding: 10px;")
        self.layout.addWidget(self.result_entry)
        
        # Create a grid layout for buttons
        self.button_grid = QGridLayout()
        self.layout.addLayout(self.button_grid)
        
        # Define buttons and their layout positions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('sqrt', 4, 0), ('^', 4, 1), ('C', 4, 2), ('(', 4, 3),
            (')', 5, 0), ('pi', 5, 1), ('e', 5, 2), ('exp', 5, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            self.button_grid.addWidget(button, row, col)
        
        # Adjust grid layout
        for i in range(6):
            self.button_grid.setRowStretch(i, 1)
        for i in range(4):
            self.button_grid.setColumnStretch(i, 1)
        
        # Set the window size to approximate the Windows calculator size
        self.setGeometry(100, 100, 320, 480)  # Approximate size of the Windows calculator

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.current_input = ''
        elif button_text == '=':
            try:
                expression = self.current_input.replace('^', '**').replace('sqrt', 'math.sqrt')
                expression = expression.replace('pi', str(math.pi)).replace('e', str(math.e)).replace('exp', 'math.exp')
                result = eval(expression)
                self.current_input = str(result)
            except Exception:
                self.current_input = 'Error'
        else:
            self.current_input += button_text
        self.result_entry.setText(self.current_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
