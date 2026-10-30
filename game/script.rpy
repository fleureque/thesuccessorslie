# The script of the game goes in this file.

#glossary code partial credit to philat on lemmasoft renai us forum
init python:
    def glossary_handler(target):
        renpy.show_screen("glossary", target)
        renpy.restart_interaction()

    config.hyperlink_handlers["glossary"] = glossary_handler

    def alert(message):
        renpy.show_screen("alert", message)
        renpy.restart_interaction()
    
    def end_alert():
        renpy.hide_screen("alert")
        renpy.restart_interaction()


default glossary_dict = {

}

default messages = {
"Important choice": "Your next choice may greatly impact the storyline.",
}
    
image ctc:
    #ctc code credit to CheeryMoya and OokamiKasumi lemmasoft renai us forum
    "gui/ctc_icon.png" with Dissolve(0.4), #This is your image
    subpixel True #This line makes sure that ATL is smooth 

    yalign 0.76 xalign 0.85 #Adjust these numbers to fit your own textbox
    linear 0.5 yalign 0.77
    linear 0.5 yalign 0.76
    
    repeat

#variable initialisation
define r = Character("Runa", color="#4af5e4", what_color="#a0e8ed", ctc="ctc", ctc_position="fixed")
define l = Character("Lynn", color="#8f6464", what_color="#d7cdba", ctc="ctc", ctc_position="fixed")

define gui.text_font = "fonts/garamond.ttf"
define gui.text_instance = "light"
define gui.text_axis = {"width" : 125}
define gui.text_size = 35
 

label temp_end_message:
    hide osric 
    hide wynfled
    hide nightcumb
    "Hello! It's the author here."
    "The storyline after this section hasn't been written yet. I'll be sending you back to the main menu."
    "If you want to keep your progress, please navigate 'back' and save the story there."
    "Once more is written you should be able to access the rest from there."
    "Alright - bye!"
    $ MainMenu(confirm=False)()