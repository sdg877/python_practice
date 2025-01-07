import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
import os

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
        load_dotenv() 
        self.api_key = os.getenv("WEATHER_API_KEY")
        
    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.setStyleSheet("""
                           QLabel, QPushButton {
                               font-family: "Calibri";
                           }
                           QLabel#city_label{
                               font-size: 40px;
                               font-style: italic;
                           }
                           QLineEdit#city_input{
                               font-size: 20px;
                           }
                           QPushButton#get_weather_button{
                               font-size: 30px;
                               font-weight: bold;
                           }
                           QLabel#temperature_label{
                               font-size: 75px;
                           }
                           QLabel#emoji_label{
                                font-size: 100px;
                                font-family: "Noto Color Emoji", "Segoe UI Emoji", "Apple Color Emoji", sans-serif;
                            }
                           QLabel#description_label:
                           font-size: 50px;
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)
        
        
    def get_weather(self):
 
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
                
            if data["cod"] == 200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError as http_error:  
            if response.status_code == 400:
                self.display_error("Bad Request:\n Please check your input")
            elif response.status_code == 401:
                self.display_error("Unauthorized:\n Please check your input")
            elif response.status_code == 403:
                self.display_error("Forbidden:\n Please check your input")
            elif response.status_code == 404:
                self.display_error("Not Found:\n Please check your input")
            elif response.status_code == 500:
                self.display_error("Internal Server Error:\n Please try again later")
            elif response.status_code == 502:
                self.display_error("Bad Gateway:\n Invalid response")
            elif response.status_code == 503:
                self.display_error("Service Unavailable:\n Server is Down")
            elif response.status_code == 504:
                self.display_error("Gateway Timeout:\n No response from the server")
            else:
                self.display_error(f"HTTP error occurred:\n{http_error}") 

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection!")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")
        except requests.exceptions.RequestException as e:
            self.display_error(f"Request Error:\n{e}")
        
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        
        self.temperature_label.setText(f"{temperature_c:.0f}ºC")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
        

    @staticmethod
    def get_weather_emoji(weather_id):
        
        if 200 >= weather_id <= 232:
            return "⛈️"
        elif 300 >= weather_id <= 321:
            return "🌥️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
        
        
            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    