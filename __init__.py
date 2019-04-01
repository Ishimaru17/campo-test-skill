from mycroft import MycroftSkill, intent_file_handler


class CampoTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.campo.intent')
    def handle_test_campo(self, message):
        self.speak_dialog('test.campo')


def create_skill():
    return CampoTest()

