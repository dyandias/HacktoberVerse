from asyncio import TimerHandle
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class CountdownApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Enter target date (YYYY-MM-DD HH:MM:SS):")
        self.layout.addWidget(self.label)

        self.input_date = QLineEdit()
        self.layout.addWidget(self.input_date)

        self.start_button = QPushButton("Start Countdown")
        self.start_button.clicked.connect(self.start_countdown)
        self.layout.addWidget(self.start_button)

        self.time_remaining_label = QLabel("")
        self.layout.addWidget(self.time_remaining_label)

        self.setLayout(self.layout)

    def start_countdown(self):
        target_date = self.input_date.text()
        target_date = datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")

        self.timer = TimerHandle(self)
        self.timer.timeout.connect(lambda: self.update_countdown(target_date))
        self.timer.start(1000)

    def update_countdown(self, target_date):
        now = datetime.now()
        time_remaining = target_date - now

        if time_remaining.total_seconds() <= 0:
            self.timer.stop()
            self.time_remaining_label.setText("stop")
        else:
            mins, secs = divmod(time_remaining.seconds, 60)
            hours, mins = divmod(mins, 60)
            days = time_remaining.days
            timeformat = f"{days}d {hours:02d}:{mins:02d}:{secs:02d}"
            self.time_remaining_label.setText(timeformat)

def main():
    app = QApplication(sys.argv)
    ex = CountdownApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
