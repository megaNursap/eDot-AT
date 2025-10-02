import pytest
import subprocess
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 🔹 Nama emulator sesuai AVD Manager
EMULATOR_NAME = "Pixel_9_Pro_XL"

def is_emulator_running(device_name):
    """check if the emulator is already running"""
    output = subprocess.getoutput("adb devices")
    for line in output.splitlines()[1:]:
        if device_name in line and "device" in line:
            return True
    return False

def start_emulator(device_name):
    print(f"🔄 boot emulator {device_name}...")
    subprocess.Popen(['emulator', '-avd', device_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # wait until the emulator is fully booted
    while True:
        booted = subprocess.getoutput('adb shell getprop sys.boot_completed').strip()
        if booted == '1':
            break
        print("⏳ Emulator still booting...")
        time.sleep(20)
    print("✅ Emulator ready!")

@pytest.fixture(scope="session")
def appium_server():
    if not is_emulator_running(EMULATOR_NAME):
        start_emulator(EMULATOR_NAME)
    else:
        print(f"✅ Emulator {EMULATOR_NAME} sudah berjalan")

    appium_process = subprocess.Popen(
        ["appium", "--address", "127.0.0.1", "--port", "4723"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # wait a few seconds to ensure the server starts
    time.sleep(5)
    print("✅ Appium server started on http://127.0.0.1:4723")

    yield

    # Stop Appium server
    appium_process.terminate()
    appium_process.wait()
    print("🛑 Appium server stopped")


@pytest.fixture(scope="function")
def driver(appium_server):  # <-- Depend ke fixture appium_server
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platformVersion = "14"   # sesuaikan
    options.device_name = EMULATOR_NAME
    options.app_package = "id.edot.ework"
    options.app_activity = "id.edot.ework.ui.MainActivity"
    options.no_reset = True
    options.auto_grant_permissions = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()
