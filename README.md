Valorant Colorbot
This is a Valorant Colorbot (Triggerbot) that automatically triggers shooting actions based on color detection. It works by identifying specific color patterns in the game and simulating mouse/keyboard actions. The bot has two ways of triggering actions: one using an Arduino Leonardo with a mouse library (for better security), and the other using the Python Keyboard library (easier and no extra hardware needed).

While the bot is mostly undetected, use it at your own risk, and do not use it on main accounts.

Features
Two Trigger Methods: Choose between Arduino Leonardo or Python Keyboard library.
Customizable: Modify the settings easily via config.json.
Undetected: The bot is mostly undetected, but proceed with caution.
Debugging Options: A debug window to show FPS and other relevant information while the bot is active.
Requirements
Python 3.x installed (for Python Keyboard method).
Necessary Python libraries, which can be installed using the requirements.txt file.
Arduino Leonardo (for the Arduino method).
How to Use (Python Keyboard)
This method uses the Python Keyboard library, and it does not require any hardware except for your computer. Here's how you can set it up:

Steps:
Download the Source Code: Clone the repository.

Install Dependencies: Install required Python libraries by running:
pip install -r requirements.txt
Customize the Configuration: Modify config.json with your preferred settings. Key settings include:

The color to trigger the bot action.
Color tolerance.
The shoot_key in Valorant (e.g., 'k').
Other options such as abort_key to stop the bot.

Example of config.json:
{
    "trigger_key": "0x01",
    "trigger_delay": 0.2,
    "color_tolerance": 20,
    "shoot_key": "k",
    "abort_key": "f12",
    "delay_between_shots": 0.2
}
Run the Bot: Run the bot by executing main.py:
python main.py
Start Valorant: Launch Valorant.

Play the Game: The colorbot will now automatically detect specific color patterns and shoot when detected.

How to Use (Arduino Leonardo)
This method uses an Arduino Leonardo, making the bot act as an HID device to simulate mouse or keyboard actions. This method offers better security but requires more setup.

Steps:
Download the Source Code: Clone the repository.

Modify the Configuration: Modify config.json to set the values for your color trigger settings. You may also need to customize the Arduino sketch in the source code.

Flash the Arduino Sketch: Use the Arduino IDE to upload the sketch to the Arduino Leonardo.

Update config.json: Change the configuration in config.json to match the port and baudrate of the Arduino Leonardo.

Compile the Python Code: After making sure the Arduino is flashed and configured, compile the Python part using:
pyinstaller --onefile main.py
Encode the Executable (Optional): To enhance security, you may encode the compiled executable using Themida or another tool.

Run the Executable: After configuring everything, you can run the executable.

Start Valorant: Launch Valorant.

Play the Game: The bot will automatically trigger shooting actions based on detected target colors, using your Arduino as an HID device.

Configuration (Common to Both Methods)
Both methods use the config.json file for configuration. Here, you can define important values:

trigger_key: The key to press to enable/disable the bot.
trigger_delay: How long to wait before triggering a new shot.
color_tolerance: Set how much color variance is acceptable for detection.
shoot_key: The key used for the secondary shoot action in Valorant (e.g., 'k').
abort_key: The key used to abort the program and deactivate the bot.

How the Bot Works
Color Detection: The bot continuously monitors a part of the screen for a specific color. When that color is detected, it simulates pressing the shoot_key to trigger an action in Valorant.
FPS Display: There is an optional debug window showing FPS and color details.
Toggle Key: Press the trigger_key to turn on/off the bot at any time, or press F10 to toggle and F12 to abort it.

Disclaimer
Use this bot at your own risk. While it is mostly undetected, using cheats or bots can lead to consequences such as bans. The developer is not responsible for any consequences resulting from using this software. This bot is intended for educational purposes only.

License
This project is open-source and available under the MIT License.