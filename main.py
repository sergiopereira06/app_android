from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        # Layout vertical para organizar a tela
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Texto principal
        self.label = Label(text="Olá! App criado no Celular!", font_size='20sp')
        
        # Botão com ação
        btn = Button(text="Clique Aqui", size_hint=(1, 0.3), background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.ao_clicar)
        
        # Adicionando elementos na tela
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def ao_clicar(self, instance):
        self.label.text = "Você clicou no botão! 🎉"

if __name__ == '__main__':
    MeuApp().run()
