# Sound Control on Key Press

This Python script enables you to control the sound (mute/unmute) of a specific program by pressing certain keys. It can be handy, for example, when you need to quickly mute a program without switching to it.

## How it Works

The script listens for specific key presses using the `pynput` library. When a predefined key combination is detected, it mutes or unmutes the sound of the specified program using the Windows Core Audio API.

### < Current Functionality >

- The application allows users to select the target program from a dropdown menu.
- Users can then assign custom hotkeys for muting and unmuting the selected program.
- After configuring the hotkeys, users can control the sound (mute/unmute) of the selected program by pressing the assigned keys.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/sound-control-on-key-press.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `main.py` file and modify the `PROGRAM` variable to specify the name of the program whose sound you want to control.

2. Run the script:

    ```bash
    python src/main.py
    ```

3. Press the predefined key combination (default: AltGr + Ctrl) to mute/unmute the sound of the specified program.

**OR**

4. Run the script:
    ```pytohn
    pyinstaller --onefile --icon=assets/icon.ico --noconsole --name "Sound Control" src/main.py
    ```

## Requirements

- Python 3.x
- pynput
- tkinter
- PyCaw

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, feel free to open an issue or create a pull request.

### < Possible Improvements >

- **Volume Adjustment Functionality**: Implement features to adjust the volume of the target application, allowing users to increase or decrease the volume as needed.
- **Enhanced Visual Appearance**: Improve the aesthetics and user interface design to make the application more visually appealing and user-friendly.

<!-- ## Screenshots

 <p align="center">
   <img src="https://thumb.cloud.mail.ru/weblink/thumb/xw1/5vtx/Smu8dtD3A" width="600" height="400">
   <img src="https://thumb.cloud.mail.ru/weblink/thumb/xw1/6iAv/M5fHaYBLy" width="600" height="400">
   <img src="https://thumb.cloud.mail.ru/weblink/thumb/xw1/Ywdu/KXe8ctAD9" width="600" height="400">
</p> -->
