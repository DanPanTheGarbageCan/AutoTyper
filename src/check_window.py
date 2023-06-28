from win32gui import GetWindowText, GetForegroundWindow


def check(driver):
    while len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    if GetWindowText(GetForegroundWindow()) != 'EdClub - Google Chrome':
        return True
