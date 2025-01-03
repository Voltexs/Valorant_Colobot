import json, time, threading, keyboard, sys
import win32api
from ctypes import WinDLL
import numpy as np
from mss import mss as mss_module
import logging
import cv2
import pyautogui

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('colorbot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def abortion():
    logging.info("Abortion function called - exiting program")
    try:
        exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b''))
    except:
        try:
            sys.exit()
        except:
            raise SystemExit
        
user32, kernel32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("kernel32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)

shcore.SetProcessDpiAwareness(2)
WIDTH, HEIGHT = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

ZONE = 4
GRAB_ZONE = (
    int(WIDTH / 2 - ZONE),
    int(HEIGHT / 2 - ZONE),
    int(WIDTH / 2 + ZONE),
    int(HEIGHT / 2 + ZONE),
)

class triggerbot:
    def __init__(self):
        self.sct = mss_module()
        self.triggerbot = False
        self.triggerbot_toggle = True
        self.exit_program = False 
        self.toggle_lock = threading.Lock()
        self.debug_window_active = True
        self.last_screenshot = None
        self.fps = 0
        self.fps_counter = 0
        self.last_time = time.time()
        
        with open('config.json') as json_file:
            data = json.load(json_file)

        try:
            self.trigger_key = int(data["trigger_key"],16)
            self.trigger_delay = data["trigger_delay"]
            self.color_tolerance = data["color_tolerance"]
            self.R = 255  # Red
            self.G = 255  # Green
            self.B = 0    # Blue
            self.abort_key = data["abort_key"]
            self.shoot_key = data["shoot_key"]
            self.delay_between_shots = data["delay_between_shots"]
            logging.info("Config loaded successfully")
        except Exception as e:
            logging.error(f"Error in config.json: {str(e)}")
            self.exit_program = True
            abortion()

    def update_fps(self):
        self.fps_counter += 1
        current_time = time.time()
        if current_time - self.last_time > 1:
            self.fps = self.fps_counter
            self.fps_counter = 0
            self.last_time = current_time

    def check_enem(self):
        # Get screenshot of center area - using mss instead of pyautogui for better performance
        img = np.array(self.sct.grab(GRAB_ZONE))
        self.last_screenshot = img
        
        # Color detection logic - optimized
        if self.triggerbot:
            # Simplified color check for better performance
            color_match = np.all(
                (img >= [self.B - self.color_tolerance, 
                        self.G - self.color_tolerance, 
                        self.R - self.color_tolerance, 0]) & 
                (img <= [self.B + self.color_tolerance, 
                        self.G + self.color_tolerance, 
                        self.R + self.color_tolerance, 255]), axis=2
            )
            
            if np.any(color_match):
                keyboard.press_and_release(self.shoot_key)
                logging.info("Shot fired")
                time.sleep(0.1)  # Minimal delay to prevent multiple shots

        self.update_fps()
        return np.sum(img)

    def debug_window(self):
        cv2.namedWindow('Triggerbot Debug', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Triggerbot Debug', 400, 400)

        while self.debug_window_active:
            if self.last_screenshot is not None:
                # Scale up the image
                display = cv2.resize(self.last_screenshot, (200, 200))
                
                # Add status information
                status = "ACTIVE" if self.triggerbot else "INACTIVE"
                cv2.putText(display, f"Status: {status}", (10, 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                cv2.putText(display, f"FPS: {self.fps}", (10, 40),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                cv2.putText(display, f"RGB: [{self.R},{self.G},{self.B}]", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                cv2.imshow('Triggerbot Debug', display)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.exit_program = True
                break

            time.sleep(0.016)  # ~60fps target

    def start_trig(self):
        # Start debug window in separate thread
        threading.Thread(target=self.debug_window, daemon=True).start()
        
        while not self.exit_program:
            self.check_enem()
            self.toggle()

    def toggle(self):
        if win32api.GetAsyncKeyState(self.trigger_key) < 0:
            self.triggerbot = True
        else:
            self.triggerbot = False

        # F10 toggle - simplified
        if keyboard.is_pressed('f10') and self.triggerbot_toggle:
            with self.toggle_lock:
                self.triggerbot_toggle = False
                self.triggerbot = not self.triggerbot
                kernel32.Beep(440, 50)  # Shorter beep
            threading.Thread(target=self.cooldown).start()

        # Abort key (F12)
        if keyboard.is_pressed(self.abort_key):
            self.exit_program = True
            self.debug_window_active = False
            cv2.destroyAllWindows()
            abortion()

    def cooldown(self):
        time.sleep(0.1)
        with self.toggle_lock:
            self.triggerbot_toggle = True

    def __del__(self):
        self.debug_window_active = False
        cv2.destroyAllWindows()

# Add logging to main loop
def on_trigger():
    logging.info("Color detected - Triggering action")
    # ... rest of your trigger code ...

# Add this to show when the program starts running
logging.info("Program started - waiting for trigger key")

# Add this near your main detection loop
try:
    with open('config.json') as f:
        config = json.load(f)
        logging.info("Config loaded successfully")
        logging.info(f"Trigger key: {config['trigger_key']}")
        logging.info(f"RGB values: {config['rgb']}")
except FileNotFoundError:
    logging.error("config.json not found!")
    sys.exit(1)

triggerbot().start_trig()