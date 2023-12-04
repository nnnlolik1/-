from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
import numpy as np
import pyaudio
import matplotlib.pyplot as plt

class TunerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Создаем кнопки
        self.start_button = Button(text="Start Tuner", on_press=self.start_tuner)
        self.stop_button = Button(text="Stop Tuner", on_press=self.stop_tuner, state='normal')

        # Создаем метку для отображения частоты
        self.pitch_label = Label(text="Detected Pitch: ")

        # Создаем слайдер для настройки параметров обнаружения частоты (по желанию)
        self.slider = Slider(min=0, max=100, value=50)
        self.slider.bind(value=self.on_slider_change)

        # Добавляем элементы на макет
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.stop_button)
        self.layout.add_widget(self.pitch_label)
        self.layout.add_widget(self.slider)

        # Параметры для записи звука с микрофона
        self.chunk = 1024  # Размер блока для чтения с микрофона
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100  # Частота дискретизации

        self.audio = pyaudio.PyAudio()
        self.stream = None

        return self.layout

    def start_tuner(self, instance):
        if not self.stream:
            # Создаем поток для записи звука с микрофона
            self.stream = self.audio.open(format=self.sample_format,
                                          channels=self.channels,
                                          rate=self.fs,
                                          frames_per_buffer=self.chunk,
                                          input=True)

        # Запускаем процесс обработки звука
        self.process_audio()

    def stop_tuner(self, instance):
        # Останавливаем поток приложения
        self.stop()

    def process_audio(self):
        while self.stream.is_active():
            # Чтение данных из микрофона
            data = self.stream.read(self.chunk)
            samples = np.frombuffer(data, dtype=np.int16)

            # Выполняем обработку звука (ваш код по обнаружению частоты)
            detected_pitch = self.pitch_detection(samples)
            self.pitch_label.text = f"Detected Pitch: {detected_pitch:.2f} Hz"

    def pitch_detection(self, samples):
        # Ваш код по обнаружению частоты
        # Замените его соответствующим алгоритмом
        # Верните обнаруженную частоту

        return 0.0  # Замените на реальное значение

    def on_slider_change(self, instance, value):
        # Обработка изменения значения слайдера (по желанию)
        pass

if __name__ == '__main__':
    TunerApp().run()
