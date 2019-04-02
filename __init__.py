import re

#Packages needed to use Microft
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

#The class must be the inheritance of the mycroftSkill class
class CampoSkill(MycroftSkill):

	#Initialization thank to the __init__ method of the superclass, with the name of our skill
	def __init__(self):
		super(CampoSkill, self).__init__(name="CampoSkill")

	


	#that all the requirement for the function
	#the requirement are the .voc documents needed
	#if something is optional, there is the .optional() option
	#the intent builder arg match the name of the func below 
	@intent_handler(IntentBuilder("CampoIntent").require("campo").build())
	def handler_campo__intent(self, message):
		#get the message which was says by the user
		utterance = message.data.get('utterance')
		#remove the occurance of the campo word in the message
		repeat = re.sub('^.*?' + message.data['campo'], '', utterance)
		self.speak_dialog(repeat.strip())

	#this intent only take place when the content of other AND campo are in input
	@intent_handler(IntentBuilder("CampoOtherIntent").require("campo").require("other").build())
	def handler_campo_other__intent(self, message):
		utterance = message.data.get('utterance')
		#We clear the text of the content of campo and 
		#change the content ofmycroft by Hi human, in the text 
		repeat = re.sub('^.*?' + message.data['campo'], '', utterance)
		modify_repeat = re.sub('^.*?' + message.data['other'], 'Hi human, ', utterance)
		self.speak_dialog(modify_repeat.strip())

	#stop function
	def stop(self):
		pass

#Creation of the skill.
def create_skill():
	return CampoSkill()

