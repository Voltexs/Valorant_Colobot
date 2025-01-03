# Valorant Colorbot 🎯

Color-based trigger bot for Valorant with Arduino and Python implementations.

⚠️ **Educational purposes only. Use at your own risk.**

---

## Features

- **Dual Trigger Methods**: Arduino Leonardo or Python Keyboard
- **Customizable Settings**: Via config.json
- **Debug Window**: FPS and color detection monitoring
- **Toggle Controls**: Enable/disable during gameplay

---

## Requirements

- Python 3.x
- Required Python libraries
- Arduino Leonardo (for hardware method)

---

## Python Keyboard Setup

```bash
# Clone repository
git clone https://github.com/Voltexs/Valorant_Colobot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

### Configuration Example

```json
{
    "trigger_key": "0x01",
    "trigger_delay": 0.2,
    "color_tolerance": 20,
    "shoot_key": "k",
    "abort_key": "f12",
    "delay_between_shots": 0.2
}
```

---

## Arduino Leonardo Setup

```bash
# Clone repository
git clone [repository-url]

# Compile Python code
pyinstaller --onefile main.py

# Optional: Encode executable for security
# Use Themida or similar tools
```

---

## Configuration Options

- `trigger_key`: Bot enable/disable
- `trigger_delay`: Shot delay timing
- `color_tolerance`: Detection sensitivity
- `shoot_key`: Game firing key
- `abort_key`: Emergency stop

---

## Technical Details

- Color-based detection system
- Real-time screen monitoring
- Toggle controls: F10 (on/off), F12 (abort)
- FPS monitoring via debug window

---

## License

MIT License

---

## Disclaimer

This project is for educational purposes only. Developer not responsible for usage consequences or potential account actions.
