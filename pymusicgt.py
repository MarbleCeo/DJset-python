import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt
import pygame

class DJPad(QWidget):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()  # Inicializa o mixer do pygame
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DJ Pad')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        self.buttons = []
        self.sounds = [
            'sound1.wav', 'sound2.wav', 'sound3.wav', 'sound4.wav', 'sound5.wav',
            'sound6.wav', 'sound7.wav', 'sound8.wav', 'sound9.wav', 'sound10.wav',
            'sound11.wav', 'sound12.wav', 'sound13.wav', 'sound14.wav', 'sound15.wav',
            'sound16.wav', 'sound17.wav', 'sound18.wav', 'sound19.wav', 'sound20.wav'
        ]

        for i in range(20):
            button = QPushButton(f'Sound {i+1}', self)
            button.clicked.connect(self.play_sound)
            button.setFixedSize(100, 100)
            grid_layout.addWidget(button, i // 5, i % 5)
            self.buttons.append(button)

        control_layout = QHBoxLayout()
        main_layout.addLayout(control_layout)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_sound)

        control_layout.addWidget(QLabel('Volume:'))
        control_layout.addWidget(self.volume_slider)
        control_layout.addWidget(self.stop_button)

        pygame.mixer.music.set_volume(0.5)  # Configura o volume inicial após a inicialização

    def play_sound(self):
        button = self.sender()
        index = self.buttons.index(button)
        sound_file = self.sounds[index]
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def set_volume(self, value):
        volume = value / 100
        pygame.mixer.music.set_volume(volume)

    def stop_sound(self):
        pygame.mixer.music.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dj_pad = DJPad()
    dj_pad.show()
    sys.exit(app.exec_())
