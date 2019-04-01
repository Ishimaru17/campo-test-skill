from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class CampoTest(MycroftSkill):

	def __init__(self):
		super(CampoTest, self).__init__(name="CampoTest")
	#that all the requirement for the function
	#the requirement are the .voc documents needed
	#if something is optional, there is the .optional() option
	@intent_handler(IntentBuilder("").require("campo"))
	def initialize(self, message):
		#get the message which was says by the user
		utterance = message.data.get['utterance']
		#Mycroft will say the content of the error.dialog file.
		self.speak_dialog('campo')
		#Mycroft will repeat exactly what was said.
		self.speak_dialog(utterance)

	def stop(self):
		pass

def create_skill():
	return CampoTest()

