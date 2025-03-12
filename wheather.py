
# wheather app project 3
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        # Layout
        layout = QVBoxLayout()

        # City input field
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name...")
        layout.addWidget(self.city_input)

        # Weather info label
        self.weather_label = QLabel("Weather Info will be displayed here.", self)
        layout.addWidget(self.weather_label)

        # Check weather button
        self.check_btn = QPushButton("Check Weather", self)
        self.check_btn.clicked.connect(self.check_weather)
        layout.addWidget(self.check_btn)

        # Set layout
        self.setLayout(layout)

    def check_weather(self):
        city = self.city_input.text().strip()
        if city:
            self.get_weather_data(city)
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")

    def get_weather_data(self, city):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                main = data["main"]
                weather = data["weather"][0]
                temperature = main["temp"]
                description = weather["description"]

                # Display the weather information
                self.weather_label.setText(f"Temperature: {temperature}°C\nDescription: {description.capitalize()}")
            else:
                QMessageBox.warning(self, "Error", "City not found. Please try again.")
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "API Error", f"Error fetching weather data: {e}")

# Run the application
app = QApplication(sys.argv)
window = WeatherApp()
window.show()
sys.exit(app.exec_())


