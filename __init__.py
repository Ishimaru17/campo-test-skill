from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class CampoSkill(MycroftSkill):

	def __init__(self):
		super(CampoSkill, self).__init__(name="CampoSkill")
	#that all the requirement for the function
	#the requirement are the .voc documents needed
	#if something is optional, there is the .optional() option
	@intent_handler(IntentBuilder("CampoIntent").require("campo").build())
	def handler_campo__intent(self, message):
		#get the message which was says by the user
		utterance = message.data.get('utterance')
		#Mycroft will say the content of the error.dialog file.
		#Mycroft will repeat exactly what was said.
		self.speak_dialog(utterance)

	def stop(self):
		pass

def create_skill():
	return CampoSkill()

