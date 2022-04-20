class State:

    def __init__(self):
        self.is_stopped = True
        self.is_running = False
        self.is_paused = False

    def setStopped(self):
        self.is_stopped = True
        self.is_running = False
        self.is_paused = False

    def setRunning(self):
        self.is_stopped = False
        self.is_running = True
        self.is_paused = False

    def setPaused(self):
        self.is_stopped = False
        self.is_running = False
        self.is_paused = True
