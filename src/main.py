import src.mute as mute

def main():
    PROGRAM = 'chrome.exe'
    print("Starting...")
    print(f"Current program: {PROGRAM}")
    mute.start(PROGRAM)

if __name__ == "__main__":
    main()