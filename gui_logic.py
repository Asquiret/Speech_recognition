from gui import Ui_Dialog
from PyQt5 import QtWidgets
import speech_recognition as speech_r
import speech_recognition as sr
import pyaudio
import wave



CHUNK = 1024  # определяет форму ауди сигнала
FRT = pyaudio.paInt16  # шестнадцатибитный формат задает значение амплитуды
CHAN = 1  # канал записи звука
RT = 44100  # частота
REC_SEC = 5  # длина записи
OUTPUT = "output.wav"


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)
        # Установка пользовательского интерфейс
        self.setupUi(dialog)
        # Обработка нажатий клавиш
        self.strt_btn.clicked.connect(self.actions_from_strt)
        self.end_btn.clicked.connect(self.calculate)
        # self.btn_1.clicked.connect(self.actions_from_1)
        # self.btn_2.clicked.connect(self.actions_from_2)
        # self.btn_3.clicked.connect(self.actions_from_3)
        # self.btn_4.clicked.connect(self.actions_from_4)

    def sec_act(self):
        self.label.setText("Recording...")





    def actions_from_strt(self) -> None:
        self.label.setText("Recording...")
        # QTimer.singleShot(3000, self.sec_act)
    
        p = pyaudio.PyAudio()

        stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True,
                        frames_per_buffer=CHUNK)  # открываем поток для записи
        self.label.setText("Recording...")
        print("Record")
        frames = []  # формируем выборку данных фреймов
        for i in range(0, int(RT / CHUNK * REC_SEC)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("done")
        # и закрываем поток
        stream.stop_stream()  # останавливаем и закрываем поток
        stream.close()
        p.terminate()

        w = wave.open(OUTPUT, 'wb')
        w.setnchannels(CHAN)
        w.setsampwidth(p.get_sample_size(FRT))
        w.setframerate(RT)
        w.writeframes(b''.join(frames))
        self.label.setText("Done")

    # def actions_from_end(self) -> None:
    #     self.calculate


    def second_action(self) -> None:
        self.label.setText("Recording...")



    # def set_value(self, sign: str) -> None:
    #     self.label.setText("")
    #     text_now = self.label.text()
    #     self.label.setText(text_now + sign)
    #
    #     if "=" in text_now:
    #         text_now = ""
    #
    #     self.label.setText(text_now + sign)

    def calculate(self) -> None:

        sample = speech_r.WavFile('output.wav')

        r = speech_r.Recognizer()

        r = sr.Recognizer()

        hellow = sr.AudioFile('output.wav')
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("Text: " + s)
            self.label.setText("Text: " + s)
        except Exception as e:
            print("Exception: " + str(e))
        # self.w.close()
        # text_now = self.label_temp.text()
        #
        # if "=" in text_now:
        #     text_now = ""
        # else:
        #     self.lbl_temp.setText(text_now+"=")
        #     print(text_now)

