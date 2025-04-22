from os import path

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
WEB_TIMEOUT = 8
API_MAX_WAIT_TIME = 3
UI_SCREENSHOT_ABS_DIR = path.abspath(path.dirname(__file__)) + "/screenshots/"

HEADLESS = True

BROWSER_NAME = "chrome"
DRIVER_TYPE = "selenium"

if __name__ == "__main__":
    print(UI_SCREENSHOT_ABS_DIR)
