from login_function import login
from type_function import type
from check_window import check

import logging

import time

import keyboard

import kivy.clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")

Builder.load_file('frontend.kv')
logging.getLogger().setLevel(logging.WARNING)


class LauncherScreen(Screen):

    def launch(self):
        name = self.manager.current_screen.ids.school_name_input.text
        email = self.manager.current_screen.ids.email_input.text
        password = self.manager.current_screen.ids.password_input.text
        
        global driver
        driver = webdriver.Chrome(options=chrome_options)

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
        exit()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        self.title = 'AutoTyper'
        return RootWidget()


MainApp().run()
