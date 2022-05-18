
class SceneBase:
    def __init__(self):
        self.next = self

    def processinput(self, events, pressed_keys):
        print("ERROR, you didn't override this in the child class")

    def update(self):
        print("Error, you didn't override this in the child class")

    def render(self, screen, surface,clock):
        print("Error, you didn't override this in the child class")

    def switchtoscene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switchtoscene(None)
