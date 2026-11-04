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

    def def_handle():
        for suspicion in observation_log:
            pass

    def show_image(image):
    #credit to XxrenxX on Lemmasoft forum
        renpy.window_hide()
        renpy.show(image)
        renpy.pause()
        renpy.hide(image)
        renpy.window_show()
    
    renpy.music.register_channel("ux")
    renpy.music.register_channel("ambiance")

    def add_observation(observation : dict):
        global observation_log
        global conclusions
        observation_log[observation["title"]] = observation["description"]
        observation_list = []
        for title in observation_log:
            observation_list.append(title)
        for conclusion in conclusions:
            if not conclusions[conclusion]["unlocked"]:
                conditions_met = True
                for condition in conclusions[conclusion]["meet_reqs"]:
                    if not condition in observation_list:
                        conditions_met = False
                if conditions_met:
                    alert(messages["Condition met"])
                    conclusions[conclusion]["unlocked"] = True


    def deduction_display():
        pass


default observation_log = {}

default conclusions = {
    "suspicious_maid" : {
        "display" : "The maid was checking inside your room. For what reason?",
        "meet_reqs" : ["says_wrong_room", "maid_has_keys"],
        "logic_display" : ["The maid had the keys to the room she intended to enter, yet still knocked.", "She must have lied."],
        "unlocked" : False
    }
}

default glossary_dict = {
"The Plague": "An ailment, glaring and recognisable no matter which canvas it appears  on. You'll all return to the same artist in the end, won't you?",
"Emperor Marchetti": "The Emperor who has long since forsaken people like you. To you, he'll always be 'the scumlord', ruler of nothing but inhumanity.",
"Myllith of Moon": "The religious figure of the empire, consecrated in legend and eternity.",
"Death": "The stench of bodies missing the warmth you've learned to love.",
"Revvers": "The pseudo-authority in your district. You have their protection. Still, you must be careful.",
"Trusty Stick": "The pummelling weapon you've used whenever it comes down to it. It's been with you through thick and thin.",
"Matriarch Marianne": "Known as the 'Angel of Velmonta'. Perhaps the only truly benevolent figure in Scab City. The reason everyone knows of Velmonta.",
"Sensations of Scab City": "Rotting wood, the pungent scent of filth, and the joint clamour of sickness and crime.",
"Velmonta": "A prestigious and incredibly well-known noble house, even in Scab City.",
"Velmonta's Reputation": "Known as a 'bastion of light' against darkness. The phrase is common knowledge.",
"Velmonta's Origin": "Granted nobility in reward for epic conquest.",
}


default messages = {
"Important choice": "Your next choice may greatly impact the storyline.",
"Condition met": "You've collected all the evidence needed for a new conclusion! Check it out in your log."
}
    
image ctc:
    #ctc code credit to CheeryMoya and OokamiKasumi lemmasoft renai us forum
    "gui/ctc_icon.png" with Dissolve(0.4), #This is your image
    subpixel True #This line makes sure that ATL is smooth 

    yalign 0.945 xalign 0.685 #Adjust these numbers to fit your own textbox
    linear 0.5 yalign 0.955
    linear 0.5 yalign 0.945
    repeat


#variable initialisation
$ npc_color = {"label": "#747474", "speech": "#c8c4c1"}
define r = Character("Runa", color="#4af5e4", what_color="#a0e8ed", ctc="ctc", ctc_position="fixed")
define l = Character("Lin", color="#8f6464", what_color="#d7cdba", ctc="ctc", ctc_position="fixed", voice_tag = "lin")
define g = Character("[gideon]", color="#a9522a", what_color="#c7a691", ctc="ctc", ctc_position="fixed")
define narrator = Character(what_italic = True, ctc="ctc", ctc_position="fixed")
define e = Character("Estelle", color="#7dd94f", what_color="#fdcdb0", ctc="ctc", ctc_position="fixed")
define m = Character("Marianne", color="#c32131", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define d = Character("Dorian", color="#d07ecf", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define f = Character("Florence", color="#91ebff", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define c = Character("Cassian", color="#fafc91", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define m = Character("Silvian", color="#f5f1f1", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define t = Character("Tess", color="#c3a021", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define npc = Character("[npc]", ctc="ctc", ctc_position="fixed")
default chapter = "1: Fading Light"
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

'''label main_menu:
    show scene "gui/main_menu.png"
    return'''

label start:
    
    play audio transition

    define mc = Character("[name + ' (You)']", what_color="#bb799a", ctc="ctc", ctc_position="fixed")

    python:
        name = renpy.input("Enter your name: (max 20 chars)", length=20, default="Runa")
        name = name.strip().title()

        if not name:
            name = "Runa"
    
    jump shed_scene


label shed_scene:
    $ reputation = {
        "fool" : 0,
        "cunning" : 0,
        "sharp" : 0
    }
    $ mental_state = {
        "stress" : 10
    }
    show screen chapter_display()
    play music her_sickness loop fadein 1.0 fadeout 1.0 
    show old shed with dissolve
    show lin normal
    mc "L-Lin. It… it'll be over soon, okay?"
    "Your hand lies unmoving against your sister's."
    "Her hand's callused, the muscle beneath thin and firm."
    "She's lying on a blanket for a mattress, barely moving against the freezing floor."
    l "D-don't want it to be over."
    show lin sick
    "She frowns and lets out a hacking cough."
    mc "Do you even hear yourself?"
    "You look away as you hear her response."
    show lin normal
    l "We promised to get out of here..."
    "From her lips come a laugh. It's a tinkling sound, jarring against her frailty."
    "Following her gaze to the vial in the corner, you dig your nails into your arm, carving marks in angry red."
    mc "I can't leave you like this."
    l "No, [name]. Don't be weak. Leave. And once you're done… get me out too."
    "A faint smile traces her lips."
    show lin sick
    "She opens her mouth to continue, but is interrupted by a succession of hard coughs. Coughs you've seen before."
    "This isn't the first time you've seen {a=glossary:The Plague}🔻 the plague{/a}."
    "A woman had been afflicted with the same ailment, claimed by the same painter.{w} A woman, just like Lin, lying unmoving. Lips purple." 
    "Above her, a man screaming with all the soul he had left.{w} The very world being torn from him.{w} Eyes, flitting to yours before he crawled away; to die away from your witness. "
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
    "Lin's jaw tightens. Her eyes glaze over." with vpunch
    "As you shake her, she stirs slightly, expression oddly serene."
    "You pray internally. '{a=glossary:Myllith of Moon}🔻 Myllith of Moon{/a}... please not again...'"
    menu:
        "Why's the plague flaring up again??":
            pass
    "And then a sudden rush of stillness."
    play music last_moments loop fadein 1.0
    "Looking up aimlessly, you sense it."
    hide lin with dissolve
    "She's gone, isn't she?"
    "It's not your first time around {a=glossary:Death}🔻 death{/a}. But you bite your lip until it splits."
    "Ever since you'd come to know each other, you were always speaking in curses. Silent ones."
    "Curses towards the passing ladies that believed themselves to be charitable. Yes, charitable; even when imparting the opposite of aid."
    "Curses towards the emperor. Him, sleeping while you were beaten sore; eating while you starved; living in his lavish palace while you lived half-freezing in this shed."
    "Why'd you left it at curses? Lord!"
    "You could have done more. Should have done more. Why was your struggle so meaningless? You brush grime from Lin's still face."
    "Through your tears, you notice the light cast through the window slowly morphing."
    "The shadow's gone now."
    "A scream rings outside." with vpunch
    "The {a=glossary:Revvers}🔻 Revvers{/a} must be patrolling already. You press yourself against the wall, as time seems to stretch on and on..."
    "...They have been patrolling much more frequently lately. Political unrest and such."
    "...How much time do you have left to clean the shed?"
    jump first_meeting


label first_meeting:
    "The shed's now cleaner than it has ever been before, thanks to your handiwork. It had protected you and Lin to the very end - both from the cold and strange hagglers."
    "And all that remains now is the blanket. It'd done little to keep you warm, but you were lucky to have even that."
    "You hesitate but draw it close and fold it into a neat square, being careful not to give away the shape of the folder within."
    "The shadow had come at some point again this morning, and now you see it slipping away."
    "In the direction of the entrance, no less."
    menu:
        "*Conclude by giving Lin's memory Myllith's curved salute.*":
            pass
        "...May you be safe, Lin.":
            "Your words still don't feel final enough."
            "You rack your mind over what else to say, but you've already said all that needed to be said. All you can mutter is “please…” as you shut my eyes." 
    "You take in every {a=glossary:Sensations of Scab City}🔻 last sensation{/a} around you. "
    play sound footsteps loop
    show gideon hidden 
    "A clicking sound jolts you to your feet as a cloaked figure steps in." with vpunch
    stop sound fadeout 1.0
    
    $ gideon = "The Cloaked Figure"
    "You grab {a=glossary:Trusty Stick}🔻 Trusty Stick{/a}, wielding it defensively."
    menu:
        "Who're you?":
            g "You can call me Gideon. I'm not here to hurt you."
            $ gideon = "Gideon"
        "How'd you get 'ere?":
            g "I apologise, but this shed isn't incredibly special."
            "You grit your teeth."
            "He muses on."
            g "This place, no, isn't important. But you... you are."
    play sound footsteps loop
    "You pull your lips into a sneer as his approach drives you back."
    stop sound fadeout 1.0
    g "You're going to freeze."
    menu:
        "Look. I'll let you in on somethin'. Outsiders ain't welcome in these alleys.":
            pass
    g "You'll freeze tomorrow. Do you even have any other clothes? Those rags on your back aren't all you have, are they?"
    "You tense watching him swing his sword, then tut. He's doing it subconsciously."
    "A sour smile forms on your face. Your hand tightens around Trusty Stick."
    menu:
        "You dare run your mouth blabberin' like this, noble?":
            pass
    g "Your voice is shaking, child."
    "An emphasis on the last word. You flush."
    menu:
        "What's it to you?":
            pass
        "Even the church done forsaken this place. Whatever laws you're used to don't apply 'ere.":
            pass
    show gideon cloaked
    "He peels his hood down, eyes locking into yours."
    g "Come with me and you'll be safe."
    "You catch yourself softening and steel up again."
    menu:
        "This sorta kidnappin' happens all the time. Kids don't come back after they get taken.":
            pass
    g "Kidnapped? Not saved?"
    "You plant your feet in place, adamant."
    "[gideon] points at the emblem on his cloak."
    g "Do you really not recognise this crest?"
    "You find yourself at a loss for words."
    g "I'm a knight of {a=glossary:Velmonta}🔻 Velmonta{/a} - Gideon. Do you know what that means?"
    $ gideon = "Gideon"
    menu:
        "Think I'm stupid? Your blue cloak and crest ain't enough to prove noth'-!":
            pass
    "You get interrupted halfway through as he pulls out official-looking documents, as if having anticipated your reaction."
    "You grab them, hold them close, and examine them."
    "...At last, you hand them back and lower your stick."
    menu:
        "Well… what's someone from that lofty house doin' all the way out here?":
            pass
    g "You have been chosen for adoption by {a=glossary:Matriarch Marianne}🔻 Madame Marianne{/a} herself."
    menu:
        "Matriarch Marianne? I… oh, lord!":
            pass
    "Trusty Stick falls from your hands as your mouth hangs agape. You don't even hear it clatter on the ground." with vpunch
    "Gideon chuckles."
    g "Once again: come with me and you'll be safe."
    menu:
        "The orphanage? This is too sudden. I...":
            pass
    g "Not to the orphanage."
    jump carriage_ride


label carriage_ride:
    "Resting your head on your hand, you look through the carriage window. Emaciated children shiver as you pass them by. Is it awe? Or are they too lost to care at this point?"
    $ gideon_trust = 10
    show gideon normal
    "Gideon's gaze is directed towards them too, expression unreadable. Does it make him sick to his stomach, seeing their gaunt, haunting faces?"
    "Your nose starts to burn."
    "Turning away from the window, you tap your fingers on your lap."
    menu:
        "Your name was Gideon?":
            $ gideon_trust += 2
            g "Indeed. Why?"
        "*Stay silent and stare at him*":
            $ gideon_trust -= 2
            "..."
            g "Do you have something to say?"
    menu:
        "N-nevermind.":
            $ gideon_trust -= 2
            "Gideon nods and looks back out the window."
            $ gideon_alliance = False
        "Where do I find you in the future?":
            $ gideon_alliance = True
            $ gideon_trust += 5
            "His eyes widen."
            show gideon smiling
            g "How direct."
            "He leans back."
            g "The barracks. They are a short distance from the outer wall."
    scene black
    hide gideon
    "In the warmth of the cloak Gideon draped around you, you grow drowsy despite the time."
    "As you drift off, you can't help but harbour the naive hope that Lin, somewhere out there, is doing well for herself."
    "You sleep for a while, mind floating out of your body."
    "The carriage suddenly jolts to a stop." with vpunch
    show gideon normal
    menu:
        "Are we here?":
            pass
    g "No. Don't move. Stay in the carriage."
    "Stirring, you see Gideon stepping out briskly with his brow furrowed. He slams the door with a clang, muttering darkly under his breath, “Should've chosen a better route.”" with vpunch
    "Your grogginess is now subsiding. You can't fall back asleep even if you want to."
    "...And besides, it's not the right time of day."
    hide gideon
    menu:
        "*Look at the landscape outside*":
            show scene rydell_garden
            $ witness_shove = False
            "Somewhere along the journey, the filth outside had become polished stone and shrubbery. You've never left Scab City before, but you can tell: you're beyond the forest already."
        "*Look at what Gideon's doing*":
            show scene guard_altercation
            "You bring your face closer against the window. There isn't any physical altercation, despite the people below being armed. The opposition is clad in the same deep blue as Gideon - but their crests are slightly different."
            "No matter how much you strain your ears, the carriage muffles the sound, rendering it incomprehensible."
            "With nothing left to do, you drum your fingers on the window impatiently, reading their expressions. After all, you doubt that Gideon can hold them off alone."
            "A man shoves Gideon on the shoulder. You look away, distracting yourself."
            $ witness_shove = True
    show gideon normal
    "The carriage door swings open again." with vpunch
    python:
        if witness_shove:
            dialogue_var = "where he'd been shoved"
        else:
            dialogue_var = "as if there was something dirty there"
    menu:
        "*Stay quiet*":
            "You remain quiet for a while. Then you pipe up again."
        "What happened?":
            $ gideon_trust += 2
            g "Damn petty Rydells tried to refuse us passage." 
            "He brushes his hand against his shoulder [dialogue_var], grimacing."
            menu:
                "Rydells?":
                    $ gideon_trust += 2
                    show gideon normal
                    g "A side family to Velmonta." 
                    "His hand falls onto his lap."
                    "Side… family?" 
                    "You blink a few times, then sigh." 
                "*Try to fall back asleep*":
                    hide gideon
                    scene black
                    "Despite your attempts, you really can't fall asleep again."
    show gideon normal
    menu:
        "How far're we from the estate?":
            g "We’ll get there after passing through the rest of the territory."
            menu:
                "Anything else I need to know?":
                    jump arrival
        "Anything I need to know before we get there?":
            jump arrival


label arrival:
    show gideon normal
    if gideon_trust > 16:
        "His hand flies to his chin, a finger hovering over his mouth."
        g "Don’t let yourself believe you’re safe simply given the way things will seem."
        menu:
            "What d'you mean?":
                "Your question is met with a simple shaking of the head."
            "*Ponder over his meaning*":
                "Your pondering doesn't work. You're even more confused now."
    else:
        g "...Not especially."
    "The carriage passes by townspeople huddling around braziers. Firewood's being hauled from carts to maintain the flame. It looks like there are even people designated to do so."
    "...Not a hint of famine nor conflict in the people's expressions. They look to be at peace, at a loss for nothing."
    "In essence, the life you and Lin had always dreamed of..."
    "You dismiss her from your mind before it starts to hurt."
    menu:
        "Rydell seems to care for its people.":
            "Gideon sighs."
            g "Of course. All of us must love our citizens."
            menu:
                "Well… what about Scab City?":
                    "You keep your voice even, despite the bitterness inside."
                    g "The Lower District?"
                    "He tilts his head."
                    menu:
                        "Never mind. I'm just being unreasonable.":
                            "Scab City isn't any noble’s responsibility, after all. The damn law ensures that."
                "*Keep your bitterness to yourself.*":
                    pass
            "You silently curse the emperor again. Your ‘own fault’ for starving, huh?"
        "*Keep staring out the window*":
            pass
    "Your heart quickens as Gideon looks at the rags you'd insisted on bringing. However, he purses his lips and doesn't speak."
    "The carriage draws close to wrought iron gates embedded into a towering wall of grey stone. Upon the wall, flaming torches illuminate its perimeter."
    "It looks incredibly expensive to maintain. You hide a grimace."
    "Gideon nods at you and exits the carriage, leaving the door open this time."
    jump reach_mansion

label reach_mansion:
    "You shudder at the sudden blast of warmth, the source of the heat being the flames licking wildly at impervious stone."
    "Feudal brilliance is full of fiery brilliance, it seems. It suddenly occurs to you that {a=glossary:Velmonta's Reputation}🔻 Velmonta's reputation{/a} may have been more than symbolic."
    "Tearing your eyes away, you look back at Gideon. He hands an overly embellished document to the guard for inspection."
    "The guard clears his throat and hands the document back after briefly skimming over it."
    $ npc = "Guard"
    npc "Welcome to Velmonta. You may return to your carriage now."
    "Two people clad in deep blue liveries, with some effort, draw the doors open. The horses are spurred into movement again."
    "Gideon turns to you."
    if gideon_alliance:
        g "Don't approach me until you're safe."
        "His hands trace around his sword scabbard. You're used to it by now."
        g "Truly safe. Not just fooled by the appearance of safety."
        menu:
            "Oh... okay.":
                show gideon smiling
                "Gideon smiles briefly."
            "You have a habit of giving cryptic advice, Gideon.":
                show gideon smiling
                "Gideon raises an eyebrow humorously."
    "You turn back to the window."
    show gideon normal
    "Extravagant black railing now lines the passage, with bountiful flower baskets hanging from each division. The fiery red begins to fade into a muted orange warmth as you approach the inner wall."
    show gideon smiling
    g "How is it?"
    menu:
        "Beautiful.":
            "Internally, you think the opposite. But nobody needs to know."
        "Disgusting.":
            "Gideon stares at you evenly for a second."
            menu:
                "Um, I mean disgustingly beautiful.":
                    "Gideon doesn't pursue it further."
    g "The flames usually look even better over the backdrop of night."
    "A footman walks around, opening the door. He extends a hand."
    $ npc = "Footman"
    npc "Welcome, Young Lady [name]."
    show estelle normal at right
    "The gate to the inner wall opens. A woman runs through, holding a pair of slippers."
    show outer chateau with dissolve
    show estelle normal at right
    show gideon normal at left
    e "Hello, Miss [name]. I'm Estelle. It's great to meet you!"
    "Bending down, she slips the footwear onto your feet. It's strangely sleek against your skin, but not an unwelcome sensation."
    "She begins to guide you through the doorway."
    menu:
        "Bye, Gideon!":
            if gideon_alliance:
                "Gideon looks disappointed that you've already forgotten his advice."
                "Below his expression, too, he looks slightly worried."
            else:
                "Gideon nods and waves back."
        "*Don't bid Gideon farewell*":
            if gideon_alliance:
                "You decide it's better to follow his advice immediately."
            else:
                "You're not close with him anyways."
    hide gideon
    "You approach the softly lit inner chateau. It has spires that strech into the sky, and flags painting deep blue streaks in the air. The stairs stop before a pair of heavy-set double-oak doors."
    play sound knocking_urgent
    "Estelle knocks five times in a meaningful rhythm, and the doors creak open to reveal the unsmiling footmen who drew them open."
    play music [shimmering_wind, flaming_decadence] loop fadein 1.0 fadeout 1.0
    "The floor's lined with marble, so polished that the light cascading from the chandelier reflects back in dazzling shades."
    "The foyer stretches out endlessly before you, spectacular and impossible."
    "Your heart beats faster. Velmonta's beautiful."
    "Beautiful, but devoid of life."
    jump first_blood


label first_blood:
    $ chapter = "2: First Blood"
    "You pull your cloak a bit tighter around yourself and look down at your slippers, snug against your feet."
    "Sensing your overwhelm, Estelle squeezes your shoulder lightly in encouragement."
    "A shudder runs through you, looking at her painted expression. But you quickly bow your head, then gaze around."
    "Estelle joins you in your admiring, then coughs."
    e "Let’s move on for now. After I take you to your room, you can wash up and get fed, alright?"
    "She rushes you through countless salons and drawing rooms, then into a long gallery."
    e "It’s only empty because we were expecting you today!"
    menu:
        "*Evaluate her excuse*":
            "You blink up, smiling. Meanwhile, your head spins."
            "The adoption was premeditated then? Or did a message travel faster than the carriage?"
            "Or perhaps he sent a courrier right after Lin fell to rest..."
            "Why would the whole estate need to be empty just for you?"
            "Her answer is giving you more questions. You shake them out of your head."
        "Ah! That's so consid'rate of you!":
            e "Don't mention it, Miss!"
    "Carved wax candles line the wall murals. They depict complex battlefields. The candlelight dances in holsters to animate the scene."
    "Deep blue flags wave, dark against the blood-orange skies. Flags with the crest that you recognise as Velmonta’s."
    "So {a=glossary:Velmonta's Origin}🔻 Velmonta's origins{/a} are just like the other houses' then."
    "As the hallway continues, the murals are gradually replaced by framed portraits of ancestral family heads."
    "You can't help but notice that none look biologically related."
    "...Adoption wasn't a recent trend, then."
    "Estelle strokes your shoulder."
    e "That is your father, Miss [name]."
    menu:
        "An honour...":
            pass
    "You feel a strange repulsion, but know not at what."
    "The gallery ends. Estelle hurriedly wraps a shawl around you, guiding you across the lengthy courtyard."
    "You reach a mansion no less impressive than the main chateau.{w} However, its outer edifice has polished wood in the place of carved stone."
    e "This is the private residential."
    "You walk into the mansion, after being given the accede from the footmen flanking its heavy doors."
    "The residential building is tall and looming; however, you only march up one floor - “the successor’s floor” - before stopping outside a door next to a statue of a knight, cuirass and sword decorating his stone body."
    "Estelle speaks while drawing keys from her pocket."
    e "Your bath was drawn as soon as we saw the carriage. We do aim to be quick."
    menu:
        "Bath? What's that?":
            $ reputation["fool"] += 2
            "Estelle looks up and down your grimy figure. A hint of sympathy?"
            "Whatever it is in her expression, you bristle at it."
            "Estelle explains how to use a bath."
        "What happens after I bathe?":
            e "My, well you'll have dinner, Miss."
    "She swings the door open, handing you a pile of fresh clothes and a towel."
    "And finally, you're alone with the flowery fragrance of bathwater."
    jump bath_scene

label bath_scene:
    "An unpleasant tingling instantly attacks you as you dip your feet into the swirling liquid.{w} You hiss.{w} It isn't unreasonably warm, but blood rushes into your limbs, bringing with it an intense itching."
    "Then comes the pain."
    menu:
        "*Pick at your skin to detract from the pain*.":
            "It gradually fades into the back of your mind, though you remain tense."
        "*Inspect your hand*":
            "Raising your hand up against the gleaming chandelier, you see your clean wrist for the first time - something beyond your imagination.{w} The colour of your skin - the true one - beneath all that grime.{w} You let your hand fall again."
    "Today's passed by in a daze.{w} Too much to think about, too much to take in, too much to see.{w} Even the light was - no, is - dizzying."
    "Your mind suddenly flashes to Lin.{w} What would her hand look like?"
    "Is it wrong that you feel glad, rather than guilty, for being taken here?{w} Leaving her behind?"
    menu:
        "*Take deep breaths*":
            "You grab the rim of the bathtub to pull yourself up."
            "Nobody will care that you're overwhelmed. In fact, expressing it would only hurt you."
            "You have to suck it up."
    "You climb out of the bathtub."
    $ glossary_dict["Myllith Sigil"]: "A sign of the Goddess, used to entice Her Blessings. These can be anything, but are traditionally for loyalty to the Crown, improved social harmony and success in military conquest."
    "A huge {a=glossary:Myllith Sigil}🔻 Myllith sigil{/a} hangs over the mirror, partly obscuring its surface.{w} You frown, wondering why someone would choose such an impractical placement."
    "You shake the water off and step out.{w} The nightdress is soft – too soft against your worn skin. Nevertheless, you shrug it on."
    "You push the hanging metal aside."
    menu:
        "*Stare at your face*":
            "Expressionless eyes peer back at you, penetrating and deep."
            "You bring a hand up to your face and slowly morph it into a smile."
            "There."
            "Your face is a good tool."
        "*Stare at your body*":
            "An emaciated and gaunt body meets you."
            "It's as clean as a noble's now."
            "You don't know how to feel about it."
            "Being here will certainly change you.{w} You try to memorise the image before you.{w} After all, even your body will eventually transform."
    play sound open_door
    "After lingering before the mirror for slightly too long, you swallow and push the ornament back in place.{w} Then you don a shy expression and pull open the door."
    "Estelle greets you with a... professional... sunny expression."
    e "Don't you look a wonder, miss?"
    menu:
        "I-I… You’re pretty too, Estelle.":
            $ reputation["fool"] += 2
            "The words slip out smoothly, despite tasting strange on your tongue."
            $ dialogue_var = "I’m just a maid, dear."
        "After taking a bath? Well, that would be expected.":
            $ reputation["sharp"] += 5
            e "Something in the way Estelle looks at you changes."
            $ dialogue_var = "You're quite right, miss."
    e "[dialogue_var] Oh - here; your dinner’s already prepared."
    "She sets a ‘small’ meal before you – a dazzling spectacle of strange meats, salads, and fruits."
    "She closes the door for you to ‘enjoy the meal in private.’"
    "Awe. Disgust. This mixture of emotions grapples with you as you stare at the food."
    "It's more than you and Lin have even laid eyes on this whole winter, let alone come close to eating."
    jump alone

label alone:
    menu:
        "*Eat the food*":
            "Sighing, you lean back in your seat and have a few bites.{w} The butters and fats melt away on your tongue, leaving behind a sweet aftertaste.{w} Having never eaten for pure pleasure before, you now understood why so many people fall prey to gluttony."
            "It's delicious, but at the same time, terrible."
            "The intense flavour makes your head ring.{w} It's terribly different from the washed-out, flavourless potatoes and grain you've been forced to salvage."
            "Besides, you're sure your stomach would explode from having more."
            $ food_eaten = True
        "*Don't eat the food*":
            $ reputation["sharp"] += 3
            "You don't trust the food here yet."
            "Better not to eat it."
            $ food_eaten = False
    menu:
        "*Explore your room*":
            "Velmonta's crest is everywhere, golden against the greenish blue coating the walls."
            "A metal statue stands on a low-hanging shelf.{w} It depicts a woman, standing firm with a greatsword in her gloved hands: Myllith of Moon.{w} In all her beauty."
            "As you kneel down to examine the statue, your eyes fall on the plaque before it."
            "“A gift from Rosalind Marchetti.”"
            "An empress that you've never heard of."
            "How recent was her rule? Is Velmonta still close to the royal family?"
            "And if so, is that to be a good thing?"
            "Shaking your head, you tear yourself away from the statue, sitting on the bed. You feel as if you're sinking."
            "You frown, looking around the room once more. Where would be a good place for hiding documents?{w} Under the statue?{w} No, would they lift that?"
            "This room is filled with religious imagery.{w} Statues and rosaries.{w} Even that dagger in the drawer beneath the table.{w} Who had this room belonged to before? You run your fingers through the blanket. It's impossibly soft."
            "Even more than Lin’s embrace."
            $ add_observation({"title": "royalty_ties", "description": "Rosalind Marchetti had ties to Velmonta, close enough to send a gift."})
        "*Sit on the chair*":
            "Before the window is a heavy desk. A dip pen and ink lies next to a blank notebook and sparse parchments."
            "You relax into the chair's soft fabric. It has barely any resistance; you sink into it."
            "It's swallowing you whole."
            "Shaking your head, you stare out into the courtyard, leaning on the desk. The flames are everywhere.{w} The sky is slowly growing darker."
            "As Gideon had said, the fire really does stand out in the night.{w} But it can't possibly be practical to maintain.{w} Even your room is lit with candles and burning wax."
            "You look at the contraption on the side of your desk: a clock. From it comes an ever-present ticking."
            "You rest for a while."
    play sound knocking_urgent loop fadein 1.0 fadeout 1.0
    "A harsh knocking sound forces you to your feet." with vpunch
    stop sound fadeout 1.0
    "You need to hide your documents."
    menu:
        "*Hide them between the mattress and wooden planks.*":
            $ paper_loc = "mattress and wooden planks beneath"
        "*Fold them and hide them under the statue.*":
            $ paper_loc = "statue and the shelf"
    "You quickly bury the documents, taken from Lin's rags, between the [paper_loc]."
    play sound open_door
    "Then you open the door."
    "Nobody's there."
    play sound open_door
    "Your hairs raise. You shut the door and race to draw the curtains down."
    play sound knocking_urgent loop fadein 1.0 fadeout 1.0
    "The knocking starts again. But you're not sure who's outside anymore."
    "Looking at the door, you notice a glass hole offering vantage to the outside.{w} With aching arms, you drag the chair over.{w} You climb up to stand and peer through the hole."
    stop sound fadeout 1.0
    "A woman dressed in clothes identical to Estelle’s garb stands outside. A maid, then."
    menu:
        "*Open the door*":  
            jump maid_interaction
        "*Stay quiet and keep the door shut*":
            play sound knocking_urgent 
            "The knocking continues for a bit longer, then stops."
            play sound footsteps loop fadein 1.0 fadeout 1.0
            "You hear the rustling of fabric, and then footsteps."
            play sound open_door
            "And then the sound of a door swinging open. Judging by the time taken to travel that far, it's the door next to yours."
    jump scene_of_crime


label maid_interaction:
    $ npc = "Unknown Maid"
    $ npc_color["label"] = "#22792a"
    play sound open_door
    "You move the chair aside and open the door."
    mc "You scared me the first time ‘round! Outside was empty!{w} Did Estelle send you?"
    "You tilt your head. Why isn't she responding?"
    "She shakes her head vigorously."
    npc "I- I apologise, Miss. It seems I have identified the wrong room."
    $ add_observation({"title" : "says_wrong_room", "description" : "Maid claimed to have the wrong room."})
    "You watch her eyes wandering past you, into your room.{w} As much as you wait, she doesn't seem to plan on leaving.{w} You shift uncomfortably as she continues to linger at the doorway."
    mc "Need anythin'?"
    "She continues staring, her expression blank.{w} Lord, where's Trusty Stick when you need it?"
    "She finally shakes her head again."
    npc "I’ll… I’ll go now."
    mc "Okay?"
    menu:
        "*Quickly shut the door*":
            pass
        "*Watch where she goes*":
            play sound footsteps loop fadein 1.0 fadeout 1.0
            "You watch her retreat down the hallway, her hair whipping wildly as she looks around.{w} You watch her approach the room next to yours."
            play sound open_door
            "She takes out a set of keys, and you hear the sound of jingling as she steps inside."
            play sound open_door
            "You go back in your room and shut the door, confused."
            $ add_observation({"title": "maid_has_keys", "description": "The maid had keys to the room she was planning on entering."})
    jump scene_of_crime
    

label eavesdrop:
    "You hear the sound of a large crowd and a commotion outside."
    "Yet you can't make heads nor tails of what's happening. You're slightly disoriented."
    "The voices continue on for a while, then suddenly dissipate."
    "You hear the sound of a door slamming."
    "You're left incredibly confused."
    jump stigma


label scene_of_crime:
    play sound footsteps loop fadein 1.0 fadeout 1.0
    "You hear more footsteps and quickly scramble onto the stool again, just in time to see a shadow slip past."
    play sound scary_sound
    stop music
    "And then a scream." with vpunch
    play sound stampede loop fadein 0.2
    "More footsteps. Hurrying towards the scene. You jump off the chair. Multiple voices are now outside. So quickly?"
    stop sound
    play ambiance crowd loop fadein 1.0 fadeout 1.0
    menu:
        "*Open the door and check what happened*":
            $ saw_murder = True
        "*Stay inside and listen.*":
            $ saw_murder = False
            jump eavesdrop
    play sound open_door
    "Opening the door, you're careful not to make a large noise."
    "You freeze."
    "That maid is lying flat on the floor. Blood spills from a large gash in her neck."
    "Standing above her is a boy with dark hair, dirtied sword in hand.{w} He's frozen, seemingly shocked by what's just happened."
    "The crowd shifts, obscuring your vision. It's composed of servants."
    menu:
        "*Approach someone to ask what's happened*":
            jump walk_into_crowd
        "*Run back into your room*":
            play sound open_door
            "Vague, disconcerted voices continue to drift into your room as you shut the door."
            "It's good that you returned; you don't know if outside is safe or not."
            jump eavesdrop


label walk_into_crowd:
    "Such a large gaggle of visibly shocked, passive onlookers is likely safe to approach."
    "You step out tentatively and walk towards the clamour, fingers unconsciously tracing your neck."
    mc "What… happened here?"
    $ npc = "Brunette Valet"
    $ npc_color["label"] = "#a68250"
    "The valet's face is pale as he responds."
    npc "Someon-"
    "He stares behind you. You turn to see what he's so shocked by."
    show marianne serious
    "Marianne Velmonta, the matriarch.{w} She's the picture of perfection plastered on posters around Scab City."
    "But her mouth is thin and her gait hurried. Rushing over, she calls what appears to be the boy’s name."
    show marianne hesitant
    m "Dorian!" with vpunch
    "The boy slowly turns to her, eyes wide and unfocused.{w} With a stormy expression, she turns to the rest of us while grabbing his wrist protectively."
    stop ambiance fadeout 2.0
    show marianne serious
    m "Please, give us some time alone."
    "Her eyes fall on you."
    m "Ah - are you [name]?"
    "Nausea beginning to wash over you, you nod quietly."
    show marianne hesitant
    m "You too, please. I.. no. Yes, go back to your room. This will be explained to you. But not now."
    "She turns back to Dorian, giving you no further thought."
    "The sight of death is nothing new. But death in this fashion? In this mansion?" 
    "You glance one last time at Dorian, and hurry into your room. What had the valet been about to tell you?"
    jump stigma

label stigma:
    $ chapter = "3: Stigma"
    "Last night, you eventually drifted to sleep despite your worries. Estelle now awakens you."
    "Outside is not yet bright, but it seems that nobles have a different routine, waking up unnaturally early."
    if saw_murder:
        menu:
            "*Ask about the murder.*":
                $ reputation["fool"] += 2
                "You gaze up at her."
                mc "Miss Estelle?"
                e "Oh - there’s no need to call me ‘Miss’. But you have a question?"
                mc "Why’d a maid try to attack Dorian last night?"
                $ asked_estelle = True
                "Estelle blinks, then tucks her hair behind her ear."
                e "It doesn’t happen often."
                mc "But why?"
                "You swallow and sheepishly stare at the floor after receiving a sharp look from her."
                "She sighs."
                e "I’m sorry, Miss [name]. It’s just… I’m not entirely sure yet."
            "*Don't mention the murder*":
                "You decide it's better not to touch a sensitive spot so soon."
                $ asked_estelle = False
    "Rubbing your eyes, you watch as she turns to the closet to pick out clothes."
    e "These might not fit you yet, but they won’t be small; we got large ones just in case. You’ll be fitted sometime."
    "Estelle offers you a cheery grin."
    "As she explains the function of each clothing piece, its materials, and how to wear it, you nod along."
    "Her gaze is calm and measured as she speaks, despite her eager attitude."
    "Meanwhile, the fine lines and countless calluses on her hands betray her years of experience."
    e "I’ll be taking you to the Morning Parlour for breakfast." 
    "She corrects your posture gently with her hands."
    e "Last night was a bit different.{w} Usually meals are had with family."
    mc "Um. How many siblings do I have?"
    "She finishes adjusting the dress." 
    e "Three total.{w} Young Masters Silvian and Dorian, and Young Lady Florence.{w} Shall we go now?"
    "You commit their names to memory. And you're glad she's willing to answer your questions…"
    jump first_breakfast

label first_breakfast:
    "The Morning Room is bright and well lit, with the large white table laid with matching tableware and cloth.{w} At the end of the table sits the matriarch, Marianne, and patriarch, Cassian, whom you recognise from his portrait."
    "Opposite you is Dorian; next to him is Florence.{w} On your side, separating you from the family heads is Silvian."
    "The atmosphere in the room is heavy, in contrast to the light from the sprawling chandelier."
    "Cassian fidgets slightly, then clears his throat."
    c "Your name is [name]. Is that correct?"
    menu:
        "Y-yes, sir. I mean, Dad. No! Father. I apologise.":
            $ reputation["fool"] += 5
            "He nods tersely before turning to Marianne, whispering something in her ear while frowning.{w} She nods at him slowly after meeting his words with her own."
        "Yes. How do you know?":
            $ reputation["sharp"] += 5
            "Cassian has a distasteful look on his face."
            c "...It would be expected for me to know the name of my new daughter."
    "Gathering himself, he speaks again."
    c "Well, [name]. To celebrate your entry into this household, we shall bestow upon you a new name."
    python:
        noble_name = renpy.input("Enter your noble name: (max 20 chars)", length=20, default="Veruna")
        noble_name = name.strip().title()
        if not noble_name:
            noble_name = "Veruna"
    c "From now on, it shall be [noble_name]. Observe it well: [noble_name] Velmonta’."
    menu:
        "I'd prefer to keep my usual name, actually.":
            $ reputation["sharp"] += 2
            "Cassian and Marianne look at each other.{w} Sternly, Marianne lays her eyes on yours."
            m "It would do you well to listen in this household."
            "Your cheeks sting."
        "*Fidget with your collar, then bow your head.*":
            $ reputation["fool"] += 2
    "Of course, you need a new, fancier name, don't you? To mark your new life?"
    "What, was your old one too common?"
    "Tightening around my fork, your hand betrays a slight tremor.{w} You've barely touched the food before you, and you don't plan to do so anytime soon."
    "The patriarch sighs."
    c "Dear, allow me to introduce you to your new siblings." 
    "He rises, with everyone at the table following suit."
    "He begins walking –"
    c "This is Florence"
    "– naming each child in turn –"
    c "Dorian"
    "– and announcing the last –"
    c "And lovely Silvian"
    "– as he passes him by."
    "…You already know their names from Estelle's words."
    "Having completed a full circuit, Cassian sits, satisfied, with everyone mirroring him.{w} Dorian turns to lock gazes with you, an amused glint in his eyes."
    menu:
        "*Avert your gaze*":
            $ reputation["fool"] += 2
            "You quickly avert your gaze, taken aback."
        "*Stare him down*":
            $ reputation["sharp"] += 2
            "His eyes grow darker as he holds your gaze."    
    if saw_murder:
        "Is murdering people so common here that he can smile like this the day after?"
        "Had you not seen him take that maid’s life, you wouldn’t have guessed that anything was amiss."
    $ alert("First impressions are important. Choose wisely!")
    menu:
        "*Act stupid*":
            $ choice = "stupid"
            $ reputation["fool"] += 10
            "You bow your head." 
            mc "Nice to… meet you all. I’m – oh, never mind, you already… know."
            "You laugh, hands fidgeting under the table."
        "*Act calm*":
            $ choice = "calm"
            $ reputation["sharp"] += 10
            "You smile calmly."
            mc "Nice to meet you all. As you know, I'm [noble_name]. Wonderful to be part of this house."
    "Florence curves her lips up, ['unenthused' if choice == 'stupid' else 'eyes narrowing ever so slightly']."
    f "It is a pleasure, sister. Fate has ordained our meeting, it seems."
    "Such flowery language!"
    if choice =="stupid":
        "You beam at her."
        mc "Yes, our meetin’ is a miracle." 
    if choice == "calm":
        "You smile gently."
        mc "Of course."
    $ glossary_dict["Morllith"]: "An accessory used for guided prayer. It is considered outdated but remains a staple for the truly devout. Very rare in Scab City."
    "Your eyes wander down. Chained to her neck is a {a=glossary:Morllith}🔻 morllith{/a}, with Myllith’s sigil encased within the prayer strands."
    d "Name's Dorian. Welcome to Velmonta."
    if choice == "stupid":
        "You swallow, then nod."
        mc "A-ah, hi!"
    else:
        "You tilt your head slowly, then smile again."
        mc "Thank you. I hope we shall get along well."
    "The blonde boy calmly pushes his book aside." 
    s "Silvian. It’s nice to meet you too, sister [noble_name]."
    "You glance at the book’s cover. It's a vivid red."
    "You smile ['diffidently' if choice == 'stupid' else 'confidently'] back."
    "Cassian turns to the matriarch, picking at his decorated sleeves."
    c "Dear, Marianne - have you anything to add?"
    "She waits, thinking. {w} Then, evenly, she asks,"
    m "Are you aware of the successorship, [noble_name]?"
    "Florence, diagonal to you, grows pale.{w} Her fingers flit to her sleeved arm, flinching as she moves her fingers over the fabric."
    "The boy next to you - Silvian - tenses inconspicuously.{w} Dorian grins, eyes widening, but you can hear his leg jerking up and down opposite you."    
    "You clear my throat."
    if choice=="stupid":
        mc "N-no, Ma’am. I mean Miss. I! Mother."
        "You tilt your head down in defeat, cheeks flushing."
        "Marianne coughs quietly, atmosphere awkward."
    if choice=="calm":
        mc "No, Mother. But I'd like to know."
    m "No, no, it’s fine. Your father will talk to you later."
    if saw_murder:
        "You stare into her eyes that betray no hint of remembrance over last night’s occurrences.{w} Are these people crazy?{w} Or are you?"
    "Cassian’s eyes widen as he looks at his wife in… betrayal? He reaches for his wine, but spills some onto the tablecloth."
    c "Ah - forgive me." 
    "At their avoidance, you blink a few times, then turn back to the meal before you."
    "Dorian’s eyes are still digging deep into your soul. But so are the matriarch’s."
    "She's staring at your hand in what seems to be faint disapproval.{w} You follow her gaze down, tilting your head in mild confusion."
    "…You're holding the wrong fork, huh."
    "The breakfast continues."
    if saw_murder:
        "Nobody seems willing to address last night’s event."
        "We successors live on the same floor, do we not? Hazarding a guess - especially due to the proximity of Dorian’s room from yours - everyone was close enough to have heard the disturbance."
        "Yet nobody moves to talk about it. Still, the air remains heavy throughout."
    else:
        "The meal continues with a heavy atmosphere. You don't know why."
        "Did you kill the mood or something?"
    jump back_in_room


label back_in_room:
    "You sit, looking out towards the crackling fires in the courtyard.{w} Your hands push lightly against the window."
    "Glass is such a wonderful invention. No wonder it's everywhere."
    "Everywhere except Scab City."
    $ glossary_dict["About Thinking"] = "Thinking can help you orient yourself and inform your future decisions. But beware, as too much paranoia isn't healthy!"
    "You now have some free time.{w} You can choose either to rest or {a=glossary:About Thinking}🔻 analyse{/a} the situation a bit more."
    menu:
        "*Think about the situation*":
            if saw_murder:
                "Why did Marianne choose to bring you here before such an attack?{w} Did they truly have no knowledge beforehand?{w} Was it premeditated?{w} If so, by whom?{w} Or are you overthinking things?"
                if asked_estelle:
                    "Estelle told you that such attacks aren't common. Is that simply consolation? Otherwise, isn't it too on the nose for an attempt to happen immediately after coming here?"
                "Your plan to make yourself less of a ['target' if choice=='calm' else 'threat'] is succeeding so far."
                "Clearly the mealtime successfully established you as a ['strong character' if choice=='calm' else 'fool']."
        "*Rest for a while*":
            "You choose to rest. After all, being too stressed can't possibly be good."
    play sound knocking_urgent loop fadein 0.5 fadeout 0.5
    "A knock rings out. You bring your hand to your chest.{w} Who is it?"
    "Dragging the chair towards the door, you wonder how you managed to do so last night.{w} It feels much heavier today."
    mc "Scab, it's taking a while…"
    "The jingling of keys sounds outside."
    $ npc = "Tess"
    npc "I’m coming in, Miss."
    "Before you move the chair even halfway, the door slowly creaks open. A flash of brown hair precedes a round face."