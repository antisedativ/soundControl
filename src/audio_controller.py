from pycaw.pycaw import AudioUtilities
import warnings


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    devices = AudioUtilities.GetAllSessions()


class AudioController:
    def __init__(self, process_name=None):
        self.process_name = process_name
        self.sessions = AudioUtilities.GetAllSessions()
        self.interface = self.get_interface()


    def get_interface(self):
        for session in self.sessions:
            if session.Process and session.Process.name() == self.process_name:
                return session.SimpleAudioVolume
            

    def get_sessions(self):
        for session in self.sessions:
            if session.Process:
                yield session.Process.name()
            else:
                print("Found a session with no process")


    def mute(self):
        if self.interface:
            self.interface.SetMute(1, None)
            print(self.process_name, "has been muted.")


    def unmute(self):
        if self.interface:
            self.interface.SetMute(0, None)
            print(self.process_name, "has been unmuted.")


    def set_volume(self, decibels):
        if self.interface:
            self.interface.SetMasterVolume(decibels, None)
            print("Volume set to", decibels)


    def decrease_volume(self, decibels):
        if self.interface:
            self.interface.SetMasterVolume(max(0.0, self.interface.GetMasterVolume() - decibels), None)
            print("Volume reduced to", self.interface.GetMasterVolume())


    def increase_volume(self, decibels):
        if self.interface:
            self.interface.SetMasterVolume(min(1.0, self.interface.GetMasterVolume() + decibels), None)
            print("Volume raised to", self.interface.GetMasterVolume())
