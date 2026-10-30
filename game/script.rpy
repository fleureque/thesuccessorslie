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
"The Plague": "An ailment, glaring and recognisable no matter which canvas it appears  on. You'll all return to the same artist in the end, won't you?",
"Emperor Marchetti": "The Emperor who has long since forsaken people like you.",
"Myllith of Moon": "The religious figure of the empire, consecrated in legend and eternity.",
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
define l = Character("Lin", color="#8f6464", what_color="#d7cdba", ctc="ctc", ctc_position="fixed")
define narrator = Character(what_italic = True, ctc="ctc", ctc_position="fixed")

define gui.text_font = "fonts/garamond.ttf"
define gui.text_instance = "light"
define gui.text_axis = {"width" : 125}
define gui.text_size = 35
 

label temp_end_message:
    "Hello! It's the author here."
    "The storyline after this section hasn't been written yet. I'll be sending you back to the main menu."
    "If you want to keep your progress, please navigate 'back' and save the story there."
    "Once more is written you should be able to access the rest from there."
    "Alright - bye!"
    $ MainMenu(confirm=False)()


label start:

    define mc = Character("[name + ' (You)']", what_color="#bb799a", ctc="ctc", ctc_position="fixed")

    python:
        name = renpy.input("Enter your name: (max 20 chars)", length=20, default="Runa")
        name = name.strip().title()

        if not name:
            name = "Runa"
    
    jump shed_scene

label shed_scene:
    show lin normal
    menu:
        "L-Lin. It… it'll be over soon, okay?":
            pass
    "Your hand lies unmoving against your sister's."
    "Her hand's callused, the muscle beneath thin and firm."
    "She's lying on a blanket for a mattress, barely moving against the freezing floor."
    l "D-don't want it to be over."
    show lin sick
    "She frowns and lets out a hacking cough."
    menu:
        "Do you even hear yourself?":
            pass
    "You look away as you hear her response."
    show lin normal
    l "We promised to get out of here..."
    "From her lips come a laugh. It's a tinkling sound, jarring against her frailty."
    "Following her gaze to the vial in the corner, you dig your nails into your arm, carving marks in angry red."
    menu:
        "I can't leave you like this.":
            pass
    l "No, Runa. Don't be weak. Leave. And once you're done… get me out too."
    "A faint smile traces her lips."
    show lin sick
    "She opens her mouth to continue, but is interrupted by a succession of hard coughs. Coughs you've seen before."
    "This isn't the first time you've seen {a=glossary:The Plague}🔻 the plague{/a}."
    "A woman had been afflicted with the same ailment, claimed by the same painter. A woman, just like Lin, lying unmoving. Lips purple." 
    "Above her, a man screaming with all the soul he had left. The very world being torn from him. Eyes, flitting to yours before he crawled away; to die away from your witness. "
    "..."
    "You grit your teeth."
    menu:
        "*Make a motion to stand.*":
            show lin normal
            "Lin grabs your arm."
            l "Don't go..."
            menu:
                "What makes you think I'm going?":
                    pass
        "I know! That's why I'll survive!":
            "Lin laughs."
            l "You have to, 'kay?"
    menu:
        "I'm not going unless that damn scumlord drags me out of 'ere himself. With his fat, gleaming fingers.":
            "You shudder."
            "Lin tries to correct you - '{a=glossary:Emperor Marchetti}🔻 Emperor Marchetti{/a}, [name]!' - just like always."
            show lin sick
            "But her voice fails."
    show lin normal
    "You hum to her."
    "The same tune she taught you."
    "The same tune you'll remember her by."
    "Her lips curl upwards."
    "And then you freeze. The light hitting the corner of the room shifts slightly - not in intensity, but in shape."
    "The shadow's changed, and that means he's here. Time's up."
    "Lin's jaw tightens. Her eyes glaze over."
    "As you shake her, she stirs slightly, expression oddly serene."
    "You pray internally. '{a=glossary:Myllith of Moon}🔻 Myllith of Moon{/a}... please not again...'"
    menu:
        "Why's the plague flaring up again??":
            pass
        
    