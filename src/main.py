import logging
import time
from subprocess import CREATE_NO_WINDOW

import keyboard
import kivy.clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from check_window import check
from login_function import login
from type_function import type

logging.disable()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
Builder.load_file('frontend.kv')


class LauncherScreen(Screen):

    def launch(self):
        name = self.manager.current_screen.ids.school_name_input.text
        email = self.manager.current_screen.ids.email_input.text
        password = self.manager.current_screen.ids.password_input.text

        serv = ChromeService(ChromeDriverManager().install())
        serv.creationflags = CREATE_NO_WINDOW
        global driver
        driver = webdriver.Chrome(service=serv, options=chrome_options)
        driver.maximize_window()
        driver.get("https://clever.com")
        login(name, email, password, driver)

        keyboard.press('Alt')
        keyboard.press_and_release('Tab')
        keyboard.release('Alt')
        self.manager.current = 'typer_screen'


class TyperScreen(Screen):

    def start(self):
        time.sleep(0.1)
        self.start_keybind = self.manager.current_screen.ids.start_keybind_input.text
        self.stop_keybind = self.manager.current_screen.ids.stop_keybind_input.text
        self.typing = False
        self.loop(1)

    def loop(self, dt):

        if keyboard.is_pressed(self.start_keybind):
            self.typing = True

        if self.typing:
            if keyboard.is_pressed(self.stop_keybind) or check(driver):
                self.typing = False
            try:
                type(driver)
            except:
                typing = False

        if self.manager.current_screen.ids.stop_button.state == 'normal':
            kivy.clock.Clock.schedule_once(self.loop)

    def quit(self):
        driver.close()
        App.get_running_app().stop()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        self.title = 'AutoTyper'
        return RootWidget()


MainApp().run()
