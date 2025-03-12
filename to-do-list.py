import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 500)
        
        # Main layout
        layout = QVBoxLayout()

        # Task input field
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        layout.addWidget(self.task_input)

        # Task list
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        # Buttons
        self.add_btn = QPushButton("Add Task", self)
        self.add_btn.clicked.connect(self.add_task)
        layout.addWidget(self.add_btn)

        self.add_btn.setStyleSheet("""
            background-color: blue;
        """)

        self.remove_btn = QPushButton("Remove Task", self)
        self.remove_btn.clicked.connect(self.remove_task)
        layout.addWidget(self.remove_btn)

        self.remove_btn.setStyleSheet("""
            background-color: red;
        """)
        self.clear_btn = QPushButton("Clear All", self)
        self.clear_btn.clicked.connect(self.clear_tasks)
        layout.addWidget(self.clear_btn)

        self.clear_btn.setStyleSheet("""
            background-color: white;
        """)
        # Set layout
        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:
            self.task_list.takeItem(selected_task)
        else:
            QMessageBox.warning(self, "Warning", "No task selected!")

    def clear_tasks(self):
        self.task_list.clear()

# Run the application
app = QApplication(sys.argv)
window = ToDoApp()
window.show()
sys.exit(app.exec_())
