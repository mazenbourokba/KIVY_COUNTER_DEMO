from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class MonApp(App):
    def build(self):
        self.compteur = 0
        layout = BoxLayout(orientation="vertical",
                          padding=20, spacing=10)
        self.label = Label(text="0", font_size=80)
        bouton = Button(text="Clique ici", font_size=30)
        bouton.bind(on_press=self.augmenter)
        layout.add_widget(self.label)
        layout.add_widget(bouton)
        return layout
    def augmenter(self, instance):
        self.compteur += 1
        self.label.text = str(self.compteur)
MonApp().run()