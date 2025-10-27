from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
import requests

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(
            text='МОЁ ПЕРВОЕ ПРИЛОЖЕНИЕ 2025!',
            font_size='20sp',
            size_hint_y=0.3
        )
        
        self.input = TextInput(
            hint_text='Введите текст здесь...',
            size_hint_y=0.2
        )
        
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.3)
        
        btn1 = Button(text='ПОКАЗАТЬ ТЕКСТ')
        btn1.bind(on_press=self.show_text)
        
        btn2 = Button(text='КОПИРОВАТЬ')
        btn2.bind(on_press=self.copy_text)
        
        btn3 = Button(text='ОЧИСТИТЬ')
        btn3.bind(on_press=self.clear_text)
        
        btn_layout.add_widget(btn1)
        btn_layout.add_widget(btn2)
        btn_layout.add_widget(btn3)
        
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn_layout)
        
        return layout
    
    def show_text(self, instance):
        if self.input.text:
            self.label.text = f'ВЫ ВВЕЛИ: {self.input.text}'
        else:
            self.label.text = 'ВВЕДИТЕ ТЕКСТ, МУДАК!'
    
    def copy_text(self, instance):
        if self.input.text:
            Clipboard.copy(self.input.text)
            self.label.text = 'ТЕКСТ СКОПИРОВАН!'
    
    def clear_text(self, instance):
        self.input.text = ''
        self.label.text = 'ТЕКСТ ОЧИЩЕН!'

if __name__ == '__main__':
    MyApp().run()
