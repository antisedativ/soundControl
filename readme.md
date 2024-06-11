# Sound Control on Key Press

This Python script allows you to control the sound (mute/unmute) of a specific program by pressing certain keys. It can be useful, for example, when you want to quickly mute a program without switching to it.

## How it Works

The script listens for specific key presses using the `pynput` library. When a predefined key combination is detected, it mutes or unmutes the sound of the specified program using the Windows Core Audio API.

### < Current Functionality >

- The script is currently configured to work with Google Chrome (`chrome.exe`).
- Pressing `AltGr` (right Alt) mutes the sound.
- Pressing `Ctrl_R` (right Ctrl) unmutes the sound.

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
    python main.py
    ```

3. Press the predefined key combination (default: AltGr + Ctrl) to mute/unmute the sound of the specified program.

## Requirements

- Python 3.x
- pynput
- PyCaw

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, feel free to open an issue or create a pull request.

### < Possible Improvements >

- **Enable Application Selection**: Add functionality to allow users to select the target application dynamically instead of hardcoding the application name in the script.
- **Key Reassignment**: Implement the ability to reassign the key combinations used for muting/unmuting the target application through configuration or user input.
- **User-Friendly Interface**: Develop a simple graphical user interface (GUI) to make the application more accessible and easier to use for non-technical users.
