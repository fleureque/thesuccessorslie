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
    
    def alter_npc(name, namecard_color="#747474", speech_color="#c8c4c1"):
        global npc
        npc = Character(name, color=namecard_color, what_color=speech_color, ctc="ctc", ctc_position="fixed")

    def change_expanded(id):
        conclusions[id]["expanded"] = not conclusions[id]["expanded"]

    def choose_conclusion(id, choice):
        conclusions[id]["chosen_choice"] = choice


default observation_log = {}

default conclusions = {
    "suspicious_maid" : {
        "display" : "The maid was checking inside your room. For what reason?",
        "meet_reqs" : ["says_wrong_room", "maid_has_keys"],
        "logic_display" : ["The maid had the keys to the room she intended to enter, yet still knocked.", 
        "She must have lied."],
        "unlocked" : False,
        "choices": ["She was looking for something in your room.", "She was scouting the room for someone else."],
        "chosen_choice": "",
        "expanded": False
    },
    "the_truth" : {
        "display" : "Someone must be lying.",
        "meet_reqs" : ["rydell_seen", "inconsistency"],
        "logic_display" : ["Between Tess, Cassian, and Gideon, something doesn't match up.", 
        "Everyone says that you're safe 'for now'.", 
        "Sure, Tess could be genuinely unaware.", 
        "But what are Cassian and Gideon trying to trick you into believing?"
        ],
        "unlocked" : False,
        "choices": ["He wants to keep you passive and dependent.", 
        "Gideon's helping the house by keeping you calm.",
        "He's testing you with the 'appearance of safety'."],
        "chosen_choice": "",
        "expanded": True
    },
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
"Myllithism": "The Empire's only official religion. Its history stretches on from the Empire's founding."
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
define l = Character("Lin", color="#8f6464", what_color="#d7cdba", ctc="ctc", ctc_position="fixed", voice_tag = "lin")
define g = Character("[gideon]", color="#a9522a", what_color="#e18569", ctc="ctc", ctc_position="fixed")
define narrator = Character(what_italic = True, ctc="ctc", ctc_position="fixed")
define e = Character("Estelle", color="#7dd94f", what_color="#d7ffcc", ctc="ctc", ctc_position="fixed")
define m = Character("Marianne", color="#c32131", what_color="#ea969e", ctc="ctc", ctc_position="fixed")
define d = Character("Dorian", color="#d07ecf", what_color="#d7afdc", ctc="ctc", ctc_position="fixed")
define f = Character("Florence", color="#91ebff", what_color="#b4f1f9", ctc="ctc", ctc_position="fixed")
define c = Character("Cassian", color="#5e77a4", what_color="#d0eafe", ctc="ctc", ctc_position="fixed")
define s = Character("Silvian", color="#f5f1f1", what_color="#d4d6d1", ctc="ctc", ctc_position="fixed")
define t = Character("Tess", color="#ad7f23", what_color="#dbd195", ctc="ctc", ctc_position="fixed")
define r = Character("Rosette", color="#ce4070", what_color="#e193c0", ctc="ctc", ctc_position="fixed")
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


label start:
    
    play audio transition
    define mc = Character("[name + ' (You)']", color="#cecd95", what_color="#f0edbc", ctc="ctc", ctc_position="fixed")

    python:
        name = renpy.input("Enter your name: (max 20 chars)", length=20, default="Runa")
        name = name.strip().title()

        if not name:
            name = "Runa"
    
    jump ch1_1_shed


label ch1_1_shed:
    $ renpy.notify("hey")
    $ time = "Day 1, Afternoon."
    $ bearings = "Scab City. Your shed."
    $ part = "1"
    show screen info_display()
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
    play music lone_house loop fadein 1.0
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
    jump ch1_2_gideon


label ch1_2_gideon:
    $ time = "Day 2. Afternoon."
    $ part = "2"
    "The shed's now cleaner than it has ever been before, thanks to your handiwork.{w} It protected you and Lin to the very end - both from the cold and strange hagglers."
    "And all that remains now is the blanket. It's done little to keep you warm, but you were lucky to have even that."
    "You hesitate but draw it close and fold it into a neat square, being careful not to give away the shape of the folder within."
    "The shadow came at some point again this morning, and now you see it slipping away."
    "In the direction of the entrance, no less."
    menu:
        "*Conclude by giving Lin's memory Myllith's curved salute.*":
            pass
        "...May you be safe, Lin.":
            "Your words still don't feel final enough."
            "You rack your mind over what else to say, but you've already said all that needed to be said. All you can mutter is “please…” as you shut my eyes." 
    "You take in every {a=glossary:Sensations of Scab City}🔻 last sensation{/a} around you.{w} After all, your time is nearly up."
    play sound footsteps loop
    show sprite cloaked
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
    mc "Look. I'll let you in on somethin'. Outsiders ain't welcome in these alleys."
    g "You'll freeze tomorrow. Do you even have any other clothes? Those rags on your back aren't all you have, are they?"
    "You tense watching him swing his sword, then tut. He's doing it subconsciously."
    "A sour smile forms on your face. Your hand tightens around Trusty Stick."
    mc "You dare run your mouth blabberin' like this, noble?"
    g "Your voice is shaking, child."
    "An emphasis on the last word. You flush."
    mc "What's it to you?"
    mc "Even the church done forsaken this place. Whatever laws you're used to don't apply 'ere."
    hide sprite
    show gideon cloaked 
    "He peels his hood down, eyes locking into yours."
    g "Come with me and you'll be safe."
    "You catch yourself softening and steel up again."
    mc "This sorta kidnappin' happens all the time. Kids don't come back after they get taken."
    g "Kidnapped? Not saved?"
    "You plant your feet in place, adamant."
    "[gideon.capitalize()] points at the emblem on his cloak."
    g "Do you really not recognise this crest?"
    "You find yourself at a loss for words."
    g "I'm a knight of {a=glossary:Velmonta}🔻 Velmonta{/a} - Gideon. Do you know what that means?"
    $ gideon = "Gideon"
    mc "Think I'm stupid? Your blue cloak and crest ain't enough to prove noth'-!"
    "You get interrupted halfway through as he pulls out official-looking documents, as if having anticipated your reaction."
    "You grab them, hold them close, and examine them."
    "...At last, you hand them back and lower your stick."
    mc "Well… what's someone from that lofty house doin' all the way out here?"
    g "You have been chosen for adoption by {a=glossary:Matriarch Marianne}🔻 Madame Marianne{/a} herself."
    mc "Matriarch Marianne? I… oh, lord!"
    "Trusty Stick falls from your hands as your mouth hangs agape. You don't even hear it clatter on the ground." with vpunch
    "Gideon chuckles."
    g "Once again: come with me and you'll be safe."
    mc "The orphanage? This is too sudden. I..."
    g "Not to the orphanage."
    jump ch1_3_carriage_ride


label ch1_3_carriage_ride:
    $ time = "Day 2. Early evening."
    $ bearings = "The Carriage."
    $ part = "3"
    show inside_carriage with dissolve
    "Resting your head on your hand, you look through the carriage window. Emaciated children shiver as you pass them by.{w} Is it awe?{w} Or are they too lost to care at this point?"
    show gideon normal
    "Gideon's gaze is directed towards them too, expression unreadable. Does it make him sick to his stomach, seeing their gaunt, haunting faces?"
    "Your nose starts to burn."
    "Turning away from the window, you tap your fingers on your lap."
    menu:
        "Your name was Gideon?":
            g "Indeed. Why?"
        "*Stay silent and stare at him*":
            "..."
            g "Do you have something to say?"
    menu:
        "Where do I find you in the future?":
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
    mc "Are we here?"
    g "No. Don't move. Stay in the carriage."
    "Stirring, you see Gideon stepping out briskly with his brow furrowed. He slams the door with a clang, muttering darkly under his breath, “Should've chosen a better route.”" with vpunch
    "Gideon throws a hand up in the air while exclaiming something loudly."
    "All the guards turn to look at you, sitting there in the carriage."
    "Your grogginess is now subsiding. You can't fall back asleep even if you want to."
    "...And besides, it's not the right time of day."
    hide gideon
    "Somewhere along the journey, the filth outside became polished stone and shrubbery. You've never left Scab City before, but you can tell: you're beyond the forest already."
    menu:
        "*Look at what Gideon's doing*":
            "You bring your face closer against the window. There isn't any physical altercation, despite the people below being armed. The opposition is clad in the same deep blue as Gideon - but their crests are slightly different."
            "No matter how much you strain your ears, the carriage muffles the sound, rendering it incomprehensible."
            "With nothing left to do, you drum your fingers on the window impatiently, reading their expressions. After all, you doubt that Gideon can hold them off alone."
            "A man shoves Gideon on the shoulder. You look away, distracting yourself."
    show gideon normal
    "The carriage door swings open again." with vpunch
    mc "What happened?"
    g "Damn petty Rydells tried to refuse us passage.{w} Dammit! I told them it was important.{w} After all, we need to get you there quickly." 
    $ add_observation({"title": "rydell_seen", "description": "The Rydells saw you. Gideon even pointed out your existence to them."})
    "He brushes his hand against his shoulder where he'd been shoved, grimacing."
    mc "Rydells?"
    g "A side family to Velmonta." 
    "His hand falls onto his lap."
    "Side… family?" 
    "You blink a few times, then sigh." 
    menu:
        "How far're we from the estate?":
            g "We’ll get there after passing through the rest of the territory."
            menu:
                "Anything else I need to know?":
                    jump ch1_4_arrival
        "Anything I need to know before we get there?":
            jump ch1_4_arrival


label ch1_4_arrival:
    $ time = "Day 2. Late evening."
    $ bearings = "Near Velmonta."
    $ part = "4"
    "His hand flies to his chin, a finger hovering over his mouth."
    g "Don’t let yourself believe you’re safe simply given the way things will seem."
    mc "What d’you mean?"
    "You're met by the shaking of a head."
    "You pass by townspeople huddling around braziers.{w} Firewood is hauled from carts to maintain the flames.{w} It looks like there are even people designated to do so."
    "There's no hint of famine nor conflict in the peoples’ expressions.{w} They look to be at peace, at a loss for nothing."
    "The life that Lin and you always dreamed of…"
    "You dismiss her from your mind." 
    mc "Rydell seems to care for its people."
    "Gideon sighs."
    g "Of course. All of us must love our citizens."
    $ glossary_dict["Scab City"] = "The place you hail from. The only place plagued by decentralisation and poverty in the Empire."
    mc "Well… what about {a=glossary:Scab City}🔻 Scab City{/a}?"
    "You keep your voice even, despite the bitterness inside."
    g "The Lower District?" 
    "He tilts his head."
    mc "Never mind. I’m just… being unreasonable."
    "Scab City isn't any noble’s responsibility, after all. The damn law's ensured that."
    "You silently curse the emperor again.{w} The inhabitants' ‘own fault’ for starving, huh?{w} You weren't even around for the Original Sin."
    "Your heart quickens as Gideon looks at the rags that you insisted on bringing. However, he purses his lips and doesn't speak."
    "The carriage draws close to wrought iron gates embedded into a towering wall of grey stone. Upon the wall, flaming torches illuminate its perimeter."
    "It looks incredibly expensive to maintain. You hide a grimace."
    "Gideon nods at you. He exits the carriage, leaving the door open this time.{w} You shudder at the sudden blast of warmth.{w} It originates from the flames that lick wildly at the impervious stone."
    "Feudal brilliance is full of fiery brilliance, it seems. It suddenly occurs to you that {a=glossary:Velmonta's Reputation}🔻 Velmonta's reputation{/a} may be more than symbolic."
    show gideon normal at left
    show sprite cloaked at right
    "Tearing your eyes away, you look back at Gideon.{w} He hands an official-looking document to the guard for inspection."
    "Clearing his throat, the guard hands the document back after skimming over it."
    $ alter_npc("Guard", "#4a64d7", "#98aaf0")
    $ bearings = "Velmonta's Main Estate."
    npc "Welcome to Velmonta. You may return to your carriage now."
    "Two people clad in deep blue liveries, with some effort, draw the doors open. The horses are spurred into movement again."
    hide sprite with dissolve
    show gideon normal at center
    "Gideon turns to you."
    g "Don’t approach me until you’re safe."
    "His hand traces around his sword scabbard."
    g "Truly safe. Not just fooled by the appearance of safety."
    mc "Oh… okay."
    "You linger on his advice, then look out the window again."
    "Extravagant black railing now lines the passage, with bountiful flower baskets hanging from each division.{w} The fiery red begins to fade into a muted orange warmth as you approach the inner wall."
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
    show gideon normal
    g "The flames look even better over the backdrop of night."
    "His expression is... conflicted, but you don't press further."
    "The road wraps around a fountain spewing crystal-like water.{w} The carriage rattles through, grinding to a halt."
    "A footman walks around, opening the door. He extends a hand."
    $ alter_npc("Footman", "#f671e4", "#f8d8f9")
    npc "Welcome, Young Lady [name]."
    mc "Thank y-you, sir."
    play sound footsteps
    show gideon normal at left
    show estelle normal at right
    "The gate to the inner wall opens. A woman runs through, holding a pair of slippers."
    e "Hello, Miss [name]. I’m Estelle. It’s great to meet you."
    "Bending down, she slips the footwear onto your feet. It's strangely sleek against your filthy skin, but not an unwelcome sensation."
    menu:
        "Bye, Gideon!":
            "Gideon looks disappointed that you've already forgotten his advice."
            "Below his expression, too, he looks slightly worried."
        "*Don't bid Gideon farewell*":
            "You decide it's better to follow his advice immediately."
    hide gideon
    "You and Estelle approach the softly lit chateau.{w} It has spires that stretch into the sky, and flags painting deep blue streaks in the air.{w} The stairs stop before a pair of heavy-set double-oak doors."
    play sound knocking_urgent
    "She knocks five times in a meaningful rhythm, and the doors creak open to reveal the unsmiling footmen who drew them open."
    play music [shimmering_wind, flaming_decadence, twelfth_yearning] loop fadein 1.0 fadeout 1.0
    "The floor is lined with marble, so polished that the light cascading from the chandelier reflects back in dazzling shades.{w} The foyer stretches out endlessly before you, spectacular and impossible. Your heart beats faster.{w} Velmonta is beautiful." 
    "Beautiful, but devoid of life."


label ch2_1_first_blood:
    $ part = "1"
    $ chapter = "2: First Blood"
    "You pull your cloak a bit tighter around yourself and look down at your slippers, snug against your feet."
    "Sensing your overwhelm, Estelle squeezes your shoulder lightly in encouragement."
    "A shudder runs through you, looking at her painted expression. But you quickly bow your head, then gaze around."
    "Estelle joins you in your admiring, then coughs."
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
    e "Let’s move on for now. After I take you to your room, you can wash up and get fed, alright?"
    "She rushes you through countless salons and drawing rooms, then into a long gallery."
    "Carved wax candles line the wall murals.{w} They depict complex battlefields.{w} The candlelight dances in holsters to animate the scenes."
    "Deep blue flags wave, dark against the blood-orange skies.{w} Flags with the crest that you recognise as Velmonta’s." 
    "So {a=glossary:Velmonta's Origin}🔻 Velmonta's origins{/a} are just like the other houses' then."
    "As the hallway continues, the murals are gradually replaced by framed portraits of ancestral family heads."
    "They don't appear biologically related.{w} Rudeus Velmonta has a high-set nose and washed-out eyes, while his predecessor, Harrick, has a large beard and heavy features instead."
    "Adoption isn't a recent trend, then."
    "Estelle strokes your shoulder."
    "You meet the tired eyes of a holy-looking man.{w} His portrait is placed close to the end of the hall.{w} For a reason you can't identify, some part of you resonates with his weary piety - even though you are not well-versed in {a=glossary:Myllithism}🔻 Myllithism{/a}."
    "The last portrait in the hallway is that of Cassian Velmonta, the reigning patriarch. He has a stern expression."
    "Something about his painting is starkly different from the preceding ones, but you can't quite clock what it is yet."
    e "That is your father, Miss [name]."
    menu:
        "An honour...":
            pass
        "Disgusting.":
            "Estelle looks at you."
            "...You messed up. She's definitely reporting this back."
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
            "Estelle looks up and down your grimy figure. A hint of sympathy?"
            "Whatever it is in her expression, you bristle at it."
            "Estelle explains how to use a bath."
        "What happens after I bathe?":
            e "My, well you'll have dinner, Miss."
    "She swings the door open, handing you a pile of fresh clothes and a towel."
    hide estelle with dissolve
    $ bearings = "Velmonta's Main Estate. Your quarters."
    "And finally, you're alone with the flowery fragrance of bathwater."
    jump ch2_2_wash


label ch2_2_wash:
    $ part = "2"
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
        "*Call for hotter water to drown your pain*":
            "You wrap yourself in a towel and open the door. Estelle looks at you in surprise."
            mc "More... hot, please."
            e "Are you sure? It could be dangerous..."
            mc "Y-yes. Please! No, I demand it. Do it. Do it. Do... do it."
            "Estelle looks at the tears streaming from your face."
            e "Alright, we'll fill it hotter."
            "You crawl back in after the water's refilled and scream in pain."
            $ alert("Ending unlocked: Early Death!")
            "You feel like you're exploding."
            "Your consciousness begins fading."
            "Your entire body itches and itches and itches."
            "A swelling sensation hits you."
            "Maybe you should've listened to Estelle..."
            $ MainMenu(confirm=False)()
    "You climb out of the bathtub."
    $ glossary_dict["Myllith Sigil"] = "A sign of the Goddess, used to entice Her Blessings. Blessings traditionally grant loyalty to the Crown, improved social harmony and success in military conquest."
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
    show estelle normal
    "Estelle greets you with a... professional... sunny expression."
    e "Don't you look a wonder, miss?"
    mc "I-I… You’re pretty too, Estelle."
    "The words slip out smoothly, despite tasting strange on your tongue."
    e "I'm just a maid, dear. Oh - here; your dinner’s already prepared."
    "She sets a ‘small’ meal before you – a dazzling spectacle of strange meats, salads, and fruits."
    hide estelle 
    play sound open_door
    "She closes the door for you to ‘enjoy the meal in private.’"
    "Awe. Disgust. This mixture of emotions grapples with you as you stare at the food."
    "It's more than you and Lin have even laid eyes on this whole winter, let alone come close to eating."
    jump ch2_3_alone


label ch2_3_alone:
    $ part = "3"
    "Sighing, you lean back in your seat and have a few bites.{w} The butters and fats melt away on your tongue, leaving behind a sweet aftertaste.{w} Having never eaten for pure pleasure before, you now understood why so many people fall prey to gluttony."
    "It's delicious, but at the same time, terrible."
    "The intense flavour makes your head ring.{w} It's terribly different from the washed-out, flavourless potatoes and grain you've been forced to salvage."
    "Besides, you're sure your stomach would explode from having more."
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
    "{size=50}Even more than Lin’s embrace.{/size}"
    $ add_observation({"title": "royalty_ties", "description": "Rosalind Marchetti had ties to Velmonta, close enough to send a gift."})
    "Before the window is a heavy desk. A dip pen and ink lies next to a blank notebook and sparse parchments."
    "You relax into the chair's soft fabric. It has barely any resistance; you sink into it."
    "It's swallowing you whole."
    "Shaking your head, you stare out into the courtyard, leaning on the desk. The flames are everywhere.{w} The sky is slowly growing darker."
    "As Gideon had said, the fire really does stand out in the night.{w} But it can't possibly be practical to maintain.{w} Even your room is lit with candles and burning wax."
    $ glossary_dict["About Clocks"] = "The only clock you've ever seen is the giant one attached to the Myllith Church's abandoned building."
    "You look at the contraption on the side of your desk: a {a=glossary:About Clocks}🔻 clock{/a}. From it comes an ever-present ticking."
    "You rest for a while."
    play sound knocking_urgent loop fadein 1.0 fadeout 1.0
    "A harsh knocking sound forces you to your feet." with vpunch
    stop sound fadeout 1.0
    "{size=40}You need to hide your documents.{/size}"
    "You quickly bury the documents, taken from Lin's rags, between the mattress and wooden planks."
    play sound open_door
    "Then you open the door."
    "{size=70}Nobody's there.{/size}"
    play sound open_door
    "Your hairs raise. You shut the door and race to draw the curtains down."
    play sound knocking_urgent loop fadein 1.0 fadeout 1.0
    "The knocking starts again. But you're not sure who's outside anymore."
    "Looking at the door, you notice a glass hole offering vantage to the outside.{w} With aching arms, you drag the chair over.{w} You climb up to stand and peer through the hole."
    stop sound fadeout 1.0
    show killermaid
    "A woman dressed in clothes identical to Estelle’s garb stands outside. A maid, then."
    jump ch2_4_maid


label ch2_4_maid:
    $ part = "4"
    "You move the chair aside and open the door." 
    mc "You scared me the first time ‘round! Outside was empty!" 
    "You tilt your head.{w} Why isn't she responding?"
    "She shakes her head vigorously."
    $ alter_npc("Unknown Maid", "#ff3103", "#f8574c")
    npc "I- I apologise, Miss. It seems I have identified the wrong room."
    $ add_observation({"title" : "says_wrong_room", "description" : "Maid claimed to have the wrong room."})
    "You watch her eyes wandering past you, into your room.{w} As much as you wait, she doesn't seem to plan on leaving.{w} You shift uncomfortably as she continues to linger at the doorway."
    "{size=50}Something feels wrong.{/size}"
    menu:
        "*Shut the door quickly*":
            "As you try to shut the door, her eyes lock onto your hand."
            "A strange look comes over her face as she slams herself against the door, stopping it from shutting."
            "You cuss as she sweeps inside. She locks the door for you."
            mc "Wh-what are you-?"
            play sound scary_sound
            stop music
            "She reaches into her long, bulky sock as you back away.{w} Her hand comes out again, dagger in grasp."
            "You have barely any time to react, but inch away."
            "Running doesn't save you. Well, how could it? You're entirely unarmed."
            $ alert("Ending unlocked: Early Death!")
            "Next thing you know, you're in a world of pain."
            "Your story ends here, without you even knowing why."
            "What a sad way to go out.{w} Lin will join you soon, won't she?"
            $ MainMenu(confirm=False)()
        "*Stare at her cluelessly":
            mc "Need anythin'?"
    "She continues staring, her expression blank." 
    "Where's Trusty Stick when you need it?"
    "She finally shakes her head."
    npc "I’ll… I’ll go now."
    mc "Okay?" 
    "You watch her retreat down the hallway, her hair whipping wildly as she looks around."
    hide killermaid
    "You shut the door but keep listening. Her footsteps pause close to your door - the room next to yours?{w} The jingling of keys resounds."
    $ add_observation({"title": "maid_has_keys", "description": "The maid had keys to the room she was planning on entering."})
    "Why’d she knocked instead of just unlocking your door then? After all, she has the keys to the room that she wanted to access."
    jump ch2_5_murder


label ch2_5_murder:
    $ bearings = "Velmonta's Main Estate. The Successors' corridor."
    $ part = "5"
    play sound footsteps loop fadein 1.0 fadeout 1.0
    "You hear more footsteps and quickly scramble onto the stool again, just in time to see a shadow slip past."
    play sound scary_sound
    stop music
    "And then a scream." with vpunch
    play sound stampede loop fadein 0.2
    "More footsteps. Hurrying towards the scene. You jump off the chair. Multiple voices are now outside. So quickly?"
    stop sound
    play ambiance crowd loop fadein 1.0 fadeout 1.0
    "Opening the door, you're careful not to make a large noise."
    "You freeze."
    "That maid is lying flat on the floor. Blood spills from a large gash in her neck. In her hand is... a dagger."
    show dorian dazed at left
    "Standing above her is a boy with dark hair, dirtied sword in hand.{w} He's frozen, seemingly shocked by what's just happened."
    "The crowd shifts, obscuring your vision. It's composed of servants."
    "Such a large gaggle of visibly shocked, passive onlookers is likely safe to approach."
    "You step out tentatively and walk towards the clamour, fingers unconsciously tracing your neck."
    mc "What… happened here?"
    $ alter_npc("Brunette Valet", "#c5a056", "#b9b28c")
    show tess worried
    "The valet's face is pale as he responds."
    npc "Someon-"
    "He stares behind you.{w} You turn to see what he's so shocked by."
    hide tess
    show marianne serious at right
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
    m "You too, please. I..{w} no.{w} Yes,{w} go back to your room.{w} This will be explained to you.{w} But not now."
    $ glossary_dict["Dorian"] = "Marianne called the boy with the sword by that name. Didn't she?"
    "She turns back to {a=glossary:Dorian}🔻 Dorian{/a}, giving you no further thought."
    "The sight of death is nothing new. But death in this fashion? In this mansion?" 
    hide marianne
    hide dorian
    "You glance one last time at Dorian, and hurry into your room. What had the valet been about to tell you?"
    jump ch3_1_stigma


label ch3_1_stigma:
    $ time = "Day 3. Early morning."
    $ bearings = "Velmonta's Main Estate. Your quarters."
    play music [shimmering_wind, flaming_decadence, twelfth_yearning] loop fadein 1.0 fadeout 1.0
    $ part = "1"
    $ chapter = "3: Stigma"
    "You'd eventually drifted to sleep despite your worries.{w} Estelle now awakens you.{w} Outside is not yet bright, but it seems that nobles had a different routine, waking up unnaturally early."
    show estelle normal at right
    "Tentatively,you gaze up at her."
    mc "Miss Estelle?"
    e "Oh - there’s no need to call me ‘Miss’. But you have a question?"
    mc "Why’d a maid try to attack Dorian last night?"
    "She blinks, then tucks her hair behind her ear." 
    e "It doesn’t happen often."
    mc "But why?"
    "You swallow and sheepishly stare at the floor after receiving a sharp look from her." 
    "She sighs."
    e "I’m sorry, Miss [name]. It’s just… I’m not entirely sure yet."
    "Rubbing your eyes, you watch as she turns to the closet to pick out clothes."
    e "These might not fit you yet, but they won’t be small; we got large ones just in case.{w} You’ll be fitted sometime."
    "She shoots you a cheery grin."
    "As she explains the function of each clothing piece, its materials, and how to wear it, you nod along."
    "Her gaze is calm and measured as she speaks, despite her eager attitude.{w} Meanwhile, the fine lines and countless calluses on her hands betray her years of experience."
    e "I’ll be taking you to the Morning Parlour for breakfast." 
    "She corrects your posture gently with her hands."
    e "Last night was a bit different. Usually meals are had with family."
    mc "There are other successors, right?"
    e "Successors? Technically, mayhaps. It's better to call them your brethren though."
    mc "Um. How many siblings do I have?"
    "She finishes adjusting the dress."
    e "Three total. Young Masters Silvian and Dorian,{w} and Young Lady Florence.{w} Shall we go now?"
    "You commit their names to memory. And you're glad she's willing to answer your questions..."
    hide estelle


label ch3_2_breakfast:
    $ time = "Day 3. Morning."
    $ bearings = "Velmonta's Main Estate. The Morning Room."
    $ part = "2"
    show marianne serious at right
    show cassian normal at left
    "The Morning Room is bright and well lit, the large white table laid with matching tableware and cloth.{w} At the end of the table sits the matriarch, Marianne, and patriarch, Cassian, whom you recognise from his portrait."
    hide cassian
    hide marianne
    show dorian normal
    show florence normal at right
    show silvian normal at left
    "Opposite you is Dorian; next to him is Florence.{w} On your side, separating you from the heads is Silvian.{w} The atmosphere in the room is heavy, in contrast to the lithe light from the sprawling chandelier."
    hide dorian
    hide florence
    hide silvian
    show cassian normal
    "Cassian fidgets slightly, then clears his throat."
    c "Your name was [name]. Is that correct?"
    mc "Y-yes, sir. I mean, Dad. No! Father. I apologise."
    "He nods tersely before turning to Marianne, whispering something in her ear while frowning.{w} She nods at him slowly after meeting his words with her own." 
    "Gathering himself, he speaks again." 
    python:
        valid_name = False
        while not valid_name:
            noble_name = renpy.input("Enter your noble name: (max 20 chars)", length=20, default="Veruna")
            noble_name = noble_name.strip().title()
            if not noble_name:
                noble_name = "Veruna"
            if not noble_name == name:
                valid_name = True
            else:
                alert("Your new name cannot be the same as your old one. Try again.")
    c "From now on, it shall be [noble_name].{w} Observe it well: '[noble_name] Velmonta'."
    menu:
        "I'd prefer to keep my usual name, actually.":
            "Cassian and Marianne look at each other.{w} Sternly, Marianne lays her eyes on yours."
            m "It would do you well to listen in this household."
            "Your cheeks sting."
        "*Fidget with your collar, then bow your head.*":
            "Marianne looks satisfied at your obedience."
    "Of course, you need a new, fancier name, don't you?{w} What, to mark your new life?"  
    "What, is your old one too common?"
    "Tightening around your fork, your hand betrays a slight tremor. You've barely touched the food before you, and you don't plan to do so anytime soon." 
    "The patriarch sighs."
    c "Dear, allow me to introduce you to your new siblings."
    "He rises, with everyone at the table following suit."
    "He begins walking –"
    hide cassian
    hide marianne hesitant
    hide dorian
    show florence normal at left
    c "This is Florence,"
    "– naming each child in turn –"
    show dorian normal
    c "Dorian,"
    "– and announcing the last –"
    show silvian normal at right
    c "And lovely Silvian."
    "– as he passes him by."
    "…You already know their names from Estelle's words."
    "Having completed a full circuit, Cassian sits, satisfied, with everyone mirroring him.{w} Dorian turns to lock gazes with you, an amused glint in his eyes."
    "You quickly avert your gaze, taken aback.{w} Is murdering people so common here that he can smile like this the day after?"
    "Had you not seen him take that maid’s life, you wouldn’t have guessed anything amiss."
    "You bow your head."
    mc "Nice to… meet you all.{w} I’m –{w} oh, never mind,{w} you already… know."
    "You laugh, hands fidgeting under the table."
    hide dorian
    hide silvian
    "Florence curves her lips up, unenthused."
    f "It is a pleasure, sister.{w} Fate has ordained our meeting, it seems."
    "Such flowery language!" 
    "You beam at her."
    mc "Yes, our meetin’ is a miracle."
    $ glossary_dict["Morllith"] = "An accessory used for guided prayer. It is considered outdated but remains a staple for the truly devout. Very rare in Scab City."
    "Your eyes wander down. Chained to her neck is a {a=glossary:Morllith}🔻 morllith{/a}, with Myllith’s sigil encased within the prayer strands."
    show dorian normal
    hide florence
    d "Name’s Dorian. Welcome to Velmonta."
    "You swallow, then nod."
    mc "A-ah, hi!"
    show silvian normal at right
    hide dorian
    "The silver-blonde boy calmly pushes his book aside."
    s "Silvian. It’s nice to meet you too, sister [noble_name]."
    "You glance at his book cover. It's a vivid red.{w} You smile diffidently back."
    hide silvian
    show cassian normal at right
    c "Dear, Marianne - have you anything to add?"
    "Cassian turns to the matriarch, picking at his decorated sleeves."
    show marianne hesitant at left
    "She waits, thinking. Then she begins to speak evenly."
    hide cassian
    m "Are you aware of the successorship, [noble_name]?"
    hide marianne
    show florence normal at right
    "Florence, diagonal to you, grows pale.{w} Her fingers flit to her sleeved arm, flinching as she moves her fingers over the fabric." with vpunch
    show silvian normal
    "The boy next to you - Silvian - tenses inconspicuously."
    show dorian normal at left
    "Dorian grins, eyes widening. You can hear his leg jerking up and down opposite you."
    "You clear your throat." 
    mc "N-no, Ma’am. I mean Miss. I! Mother."
    "You tilt your head down in defeat, cheeks flushing."
    hide silvian
    show marianne hesitant
    "Marianne coughs quietly." 
    m "No, no, it’s fine. Your father will talk to you later."
    show marianne serious
    "You stare into her eyes that betray no hint of remembrance over last night’s occurrences.{w} Are these people crazy?{w} Or - are you?"
    hide dorian
    show cassian normal at left
    "Cassian’s eyes widen as he looks at his wife in… betrayal?{w} He reaches for his wine, but spills some onto the tablecloth."
    c "Ah - forgive me."
    "At their avoidance, you blink a few times, then turn back to the meal before you."
    "Dorian’s eyes are still digging deep into your soul.{w} But so are the matriarch’s.{w} She's staring at your hand in what seems to be faint disapproval.{w} You follow her gaze down, tilting your head in confusion."
    "…You're holding the wrong fork, huh."
    "The breakfast continues, but nobody seems willing to address last night’s event."
    "You successors live on the same floor, do you not? Hazarding a guess - especially due to the proximity of Dorian’s room from yours - everyone was close enough to have heard the disturbance."
    "Yet nobody moves to address it."
    hide marianne hesitant
    hide cassian
    hide florence
    jump ch3_3_room


label ch3_3_room:
    $ bearings = "Velmonta's Main Estate. Your quarters."
    $ time = "Day 3. Morning."
    hide marianne 
    hide dorian
    $ part = "3"
    "You sit, looking out towards the crackling fires in the courtyard.{w} Your hands push lightly against the window."
    "Glass is such a wonderful invention. No wonder it's everywhere."
    "Everywhere except Scab City."
    $ glossary_dict["About Thinking"] = "Thinking can help you orient yourself and inform your future decisions. But beware, as too much paranoia isn't healthy!"
    "You now have some free time.{w} You can choose either to rest or {a=glossary:About Thinking}🔻 analyse{/a} the situation a bit more."
    menu:
        "*Think about the situation*":
            "Why did Marianne choose to bring you here before such an attack?{w} Did they truly have no knowledge beforehand?{w} Was it premeditated?{w} If so, by whom?{w} Or are you overthinking things?"
            "Estelle told you that such attacks aren't common.{w} Is that simply consolation? Otherwise, isn't it too on the nose for an attempt to happen immediately after coming here?"
            "Your plan to make yourself less of a target is succeeding so far."
            "Clearly the mealtime successfully established you as a fool."
        "*Rest for a while*":
            "You choose to rest. After all, being too stressed can't possibly be good."
    play sound knocking_urgent loop fadein 0.5 fadeout 0.5
    "A knock rings out. You bring your hand to your chest.{w} Who is it?"
    "Dragging the chair towards the door, you wonder how you managed to do so last night.{w} It feels much heavier today."
    stop sound
    mc "Scab, it's taking a while…"
    "The jingling of keys sounds outside."
    $ alter_npc("Unknown Male Voice")
    npc "I’m coming in, Miss."
    play sound open_door
    "Before you move the chair even halfway, the door slowly creaks open. A flash of brown hair precedes a round face."
    show tess normal
    "You blink."
    mc "Ah - you?"
    "It's the brunette you asked yesterday about the murder."
    "His eyes flicker in recognition."
    t "Oh! Yes. I’m Tess, your valet. It seems we meet again."
    mc "Ah! I’m - no, you already know. Sorry."
    "You notice ink stains on his fingertips as you tilt your head down."
    mc "Is it just you ‘nd Estelle?"
    "He blinks."
    t "Yes. You can appeal to your parents if you need more help…"
    mc "No, no. More’s too many."
    "You chuckle."
    mc "Oh - where’s Estelle?"
    t "She's sorting your clothes."
    "Smacking his hand against his head, he looks at you apologetically."
    t "I forgot, I came here to deliver a message.{w} The patriarch would like to meet you in his private study."
    "He rubs his neck."
    t "Do you want to go now?"
    "You look at him, taken aback for a moment."
    mc "Alright."
    hide tess
    jump ch3_4_mandate
    

label ch3_4_mandate:
    $ bearings = "Cassian's Study."
    $ time = "Day 3. Late morning."
    $ part = "4"
    show cassian normal
    c "Sit, [noble_name]."
    "Cassian pulls a chair out, watching you closely as you acquiesce."
    c "I’m required by mandate, you see, to inform you about the successorship."
    mc "A-ah, yes, Father."
    "You stammer, watching as he sits himself down in front of you."
    "The study smells of ash – there are no windows, and the only source of light comes from holstered candles pinned to the walls.{w} It's an oddly threatening room."
    c "You are eligible to be selected as Velmonta’s successor." 
    "He stares into your eyes."
    "Is this it? Is this why everyone had such averse reactions to its mention then?"
    "You jerk your head up, bringing your hand to your chest."
    mc "I couldn’t dream o-"
    c "Perhaps there will come a time when you wish to vie for the position. And you will have the opportunity, [noble_name]."
    "You gape, then check yourself and nod quietly."
    c "Good."
    "He smiles."
    menu:
        "*Confront him about the murder*":
            jump ch3_5a_confront

label ch3_5a_confront:
    $ part = "5"
    mc "One more thing, Father. If… if you would."
    "He pauses." 
    c "Yes, [noble_name]?"
    mc "Dorian yesterday. What happened? With the…"
    c "Ah." 
    "His smile falls."
    c "We are trying to find the house that sent the attacker."
    "He looks to his right."
    c "Though it is hard, since the assassin is now deceased."
    mc "Anything happ’ning next?"
    c "Next? We shall file paperwork and identify, if possible, where the woman’s allegiances lay."
    mc "You can take lives?? Just like that? All you gotta do is paperwork?"
    "You swallow.{w} Blinking, he tilts his head."
    c "Sorry?"
    mc "Why’d they try to kill Dorian yesterday?"
    c "[noble_name]."
    mc "Am I in danger too? Tell me! I can’t…"
    "A sob slips from your lips."
    "He pats your shoulder, staring you in the eyes calmly."
    c "It doesn’t happen often.{w} You’ll learn how to deal with these situations as you spend more time here."
    $ add_observation({"title" : "murder_rare", "description" : "Cassian claimed that murders are rare and that you'll adapt."})
    "Learn to deal with these situations?{w} How?{w} You stare at the ground unmoving.{w} He closes his eyes."
    c "[noble_name]."
    mc "DON'T CALL ME THAT!" with vpunch
    "His eyes widen."
    "You freeze, then grit your teeth."
    mc "Sorry. I’m bein’ unreasonable."
    jump ch3_6_lunch


label ch3_6_lunch:
    $ time = "Day 3. Noon."
    $ part = "6"
    c "Let us head to luncheon."
    "Cassian slowly rises."
    "He looks away from you; is he mad?{w} Disappointed?{w} Understanding?"
    show tess worried at right
    "You follow him out quietly, glancing to Tess who joins you at your side." 
    "He's glancing back at you, worried, measuring how you're handling the revelation."
    "You train your eyes on Cassian’s figure.{w} Eventually they wander back to the valet’s darkened fingertips."
    hide tess
    hide cassian


label ch4_1_mutual_benefit:
    $ time = "Day 4. Afternoon."
    $ bearings = "Your quarters."
    $ part = "1"
    $ chapter = "4: For Mutual Benefit"
    show tess normal
    "You haven't been able to get the thought of the dead maid out of your mind."
    "And certainly haven't been able to forget how close of a shave you had with death."
    "On your first day, at that."
    "You'd opened the door like a fool. What if that dagger had been aimed at, well, you?"
    "Luckily, Tess is right in front of you, waiting on you."
    menu:
        "*Ask Tess about the murder*":
            jump ch4_1a_confront
        "*Avoid mentioning the murder*":
            jump ch4_1b_silence

label ch4_1a_confront:
    mc "You were there. You saw it."
    "Tess’s hand pauses."
    t "I was, Miss."
    "He puts the teapot down."
    t "Well, I assume you’re speaking about… that?"
    mc "Last night? Yes." 
    "You run your hand over the notebook cover."
    mc "I won’t push you ‘bout what she was tryin’ to do nor why she had to die.{w} But you need to tell me if I’m in danger too."
    "Of course, whatever response he gives you will serve his own interests.{w} All the more information.{w} But also, all the more questions."
    t "In danger…" 
    "He rubs his neck with an innocent expression.{w} You reach for the teacup, but it's searing hot.{w} Your hand jerks away. He doesn't seem to notice.{w} You thank Myllith for saving you from embarrassment."
    "Finally, he notices your stare." 
    show tess worried
    t "I’m not really in a place to say, Miss."
    mc "I’m serious, Tess." 
    "You wave your hand over the cup, judging its temperature.{w} Still too hot."
    mc "Nobody’d have peace of mind after seeing someone dead like that."
    "You swallow."
    t "As far as I'm aware, movements both into and out of Velmonta are monitored."
    mc "But that maid still got here."
    t "Not only movements." 
    "He picks the teapot up again." 
    show tess normal
    t "Information is monitored as well.{w} Nobody outside of here should know about you yet.{w} And certainly not enough to pinpoint you as a target."
    t "Do you know just how rare such an attack is?{w} It takes a miracle for someone to even get that close to a successor.{w} Suffice to say, you're safe."
    "So the attacks come from outside; that makes sense."
    "But why are the successors targeted?{w} You can't rest easy just yet without knowing."
    mc "So what’m I meant to do ‘till then?{w} Do I just stay here?{w} Wait here with death loomin’ over me?"
    "He blinks."
    t "Miss Florence spends her time in the Summertide Chapel.{w} Master Silvian either reads or studies.{w} Master Dorian does… things."
    mc "That’s too lax of them." with vpunch
    show tess worried
    t "I don’t quite understand, Miss."
    "You stare at him.{w} His expression remains dumb."
    mc "Alright then, Tess. You can go now." 
    hide tess
    "You wave your hand. He bows and leaves. You turn to the ticking clock. How long will it be until the next attack?"
    $ glossary_dict["Myllith Dagger"] = "A ceremonial dagger. It is not frowned upon to use it outside of prayer. After all, Myllith thrives on bloodshed."
    "The {a=glossary:Myllith Dagger}🔻 Myllith dagger{/a} in the drawer. From when you were exploring your room."
    "You've never gripped one like this before, only seen them paraded around by the Church.{w} This one’s velvet scabbard is engraved with Velmonta’s sigil."  
    "Who is your enemy? Whose observation do you have to avoid?{w} Paranoia has saved you too many times to count; it won't hurt now.{w} You slip the dagger into your dress pocket."
    "Before the bathroom mirror, you're assured that the fabric falls smoothly over the pocket, as if there's nothing there."
    "You walk out of the bathroom and cast your gaze towards Lin’s rags."
    "Had you really been considering slicing them into strips?{w} Your face twitches into a half-smile. A wistful one."
    "You should go catch up with Gideon.{w} All this suspicion is driving you crazy."
    "You can trust him to give you a straight answer, too."
    play sound open_door
    $ bearings = "Outside your room."
    "You leave your room."
    "Despite being aware that this is a corridor, the absence of sunlight makes you uneasy.{w} You wrinkle your nose as you walk by Dorian’s room.{w} There isn't a single remnant of blood. It looks and smells of artificial cleanliness."
    "Your neck tingles. Hand on pocket, you make it through the passage, down the stairs, rushing until the courtyard.{w} You stop to breathe, nose burning in the strange mixture of fresh air and crackling fire."
    jump ch4_2_gideon


label ch4_1b_silence:
    "You avoid looking at Tess."
    "After all, doing so simply brings back memories of... well, that."
    "The courtyard fires are still crackling on and on at this time of day."
    "Fire. Fire and warmth. They feel stifling here."
    "It's slightly awkward with you and Tess not speaking."
    mc "Um. Is Estelle... going to come back?"
    t "Yes, Miss. Why? Is my service unsatisfactory?"
    mc "Oh! No, I didn't mean that at all. I was just curious."
    "Another awkward silence."
    "Tess quickly excuses himself and leaves. You're all alone."
    "You stare up at the ceiling, tired."
    "May as well have a little nap."
    "Before long, you wake up again."
    "What time is it? You turn to the clock."
    "Ten minutes until dinner. May as well set out."
    jump ch4_3_dinner


label ch4_2a_gideon:
    $ bearings = "The Barracks."
    $ time = "Day 4. Late afternoon."
    $ part = "2"
    show gideon normal
    "Gideon looks at you languidly. His hair is like rust and the sweat on his face its catalyst."
    show gideon smiling
    g "[name]. Or is it Miss [noble_name] now?{w} You’re cleaner than ME now. How delightful."
    "You feel up your smooth wrist." 
    mc "Suppose so. Not sure how happy I’m meant to be ‘bout it though."
    "Your gaze falls onto his sword, lying on the same hay-pile as him." 
    mc "Interrupting your trainin’?"
    show gideon normal
    g "No.{w} But it seems you’ve already forgotten the message I repeated for you before."
    "His eyes are unsmiling as he stares at you."
    mc "Message? Oh!"
    "You tap your finger against your forehead." 
    mc "That round-‘bout advice? You coulda been more straightforward."
    g "Was it really that hard to understand?{w} You weren’t meant to come and find me until you were safe." 
    "He taps his foot up and down."
    g "Well, what’s done has been done."
    "Again. He's trying to warn you of danger, protect you from Velmonta’s ‘hidden enemies’.{w} But is he really acting in your best interests?"
    "You spit at the ground." 
    mc "Me?{w} Safe?{w} I watched a maid die right after getting ‘ere.{w} Pierced by the boy she was try’na kill. What sorta safety’s anyone givin’ me?{w} Protection? A tad bit o’ consolation? Explanations, at least?{w} No, nothing.{w} So when d’you think I’ll ever be safe?"
    "You let your hands shake as you clutch them to your chest."
    show gideon smiling
    "He pinches his brow." 
    g "It seems I’ve been rather harsh on you. I apologise."
    mc "Sorry."
    "You run your hands through your groomed hair."
    show gideon normal
    mc "I’m just… I need to understand.{w} Something, anything. What d’you mean by danger?{w} I know I’m dyin’ soon. But you speak like there’s something else I’ve gotta be scared of."
    "Information, even manipulative or coercive, is something you need right now.{w} You can't just stay meek waiting for the end."
    "He drums his fingers on the steel of his sword." 
    g "You’re lucky you chose to find me so early." 
    "His eyes pierce yours." 
    g "Have you seen the documentation yet?"
    "You shake your head." 
    mc "Father told me a bit ‘bout the succession though."
    g "Did he inform you that maximum four children roam Velmonta’s halls at a time?{w} As imposed by the Emperor?"
    "He stares towards the outer wall."
    mc "No?"
    g "The matriarch, Madame Marianne, accepted Miss Florence into the main line.{w} And then the side families discovered they could plant their own inside these castle walls."
    mc "So it’s the side families targetin’ us?"
    g "Now that the seats are full, yes."
    mc "Okay…{w} what d’you mean by lucky? By comin’ so early, I mean."
    show gideon smiling
    "The side families likely haven’t discovered your adoption into Velmonta yet.{w} Hence, you are, I suppose, safe for now."
    $ add_observation({"title": "inconsistency", "description": "Gideon said the side families don't know you're here, knowing that Rydell's aware of your existence."})
    "Well, that matches up with what Tess told you earlier. To some extent."
    "But Gideon's lying through his teeth, isn't he?"
    "You hold in a frown." 
    mc "Alright. But what’s that got to do with comin’ to find you?"
    g "That’s exactly it. Don’t come again.{w} Or at least, not until the side families no longer track your every movement."
    "He stands. You follow suit, sensing that the conversation's wrapping up now." 
    mc "Was nice talkin’, Gideon." 
    "You keep your tone light and airy."
    g "It would be best to stay unnoticed on the way back."
    "He sits back on his hay, picking his sword up."
    mc "Alright."
    hide gideon with dissolve
    "Your spine crawls as you leave the barracks."
    $ time = "Day 4. Early evening."
    $ bearings = "Gallery."
    $ part = "3"
    "Velmonta is no longer as empty as it was when you first arrived.{w} You now see maids and servants walking around with pails of water and mops in hand. A woman with a different livery hauling firewood.{w} But still, no nobility from other houses. Everyone here is from the main line."
    "So had Estelle been right? Was it empty yesterday only due to your arrival? But if so, why?{w} To avoid commotion? If anything, it would only stir up more suspicion from the other houses."
    "You sheepishly approach a friendly-looking maid."
    mc "Excuse me, d’you know where we have dinner?"
    $ alter_npc("Friendly-Looking Maid")
    npc "Miss [noble_name]? The dining hall’s down that end."
    mc "‘Kay, thank you!"
    "Some of the staff throw you some glances; aside from that, you don't attract attention as you walk through the salons to the gallery."
    $ glossary_dict["Myllith's Salute"] = "A curved salute resembling the moon. It is thought to both demonstrate loyalty to the Crown (scumlord) and bring Her Blessings upon the recipient."
    "You can't help but pause as you pass the tired man’s portrait again in the gallery. Weary dedication and effortless piety still radiate from his kind face.{w} You perform {a=glossary:Myllith's Salute}🔻 the curved salute{/a} in acknowledgement of his faith."
    jump ch4_3_dinner


label ch4_3_dinner:
    $ bearings = "Dining Hall."
    "Entering the dining hall, you glance around. A valet and a maid for each successor;{w} two lady’s maids for Marianne; two valets for Cassian at the head of the table;{w} a butler and kitchen staff scattered through the room, setting the table."
    show estelle normal
    "Tess and Estelle are already there. The other valets and maids are conversing in a subdued manner, while yours were silent and taciturn.{w} Estelle guides you to your seat. You smile at her."
    hide estelle 
    show marianne serious
    "Marianne nods. You return the gesture gratefully."
    hide marianne
    show dorian normal at left
    "You never noticed before, but the servants look at Dorian differently from the rest of you. It makes sense. He killed a girl."
    show florence normal at right
    "Dorian meets your eyes as you look up from the tablecloth. You flinch away.{w} He’s been looking at you like that ever since you arrived here.{w} But what's stranger is Florence’s calm gaze. She tucks her hair behind her ear, then looks away."
    show marianne serious
    "Marianne clears her throat." 
    m "You may eat now."
    hide marianne
    "You make sure to use the right cutlery this time." 
    if conclusions["the_truth"]["unlocked"]:
        "But as you look at your food, another image appears in your mind.{w} Gideon’s face. You dig your fork hard into the veal."
        $ glossary_dict["The Gathering"] = "The esteemed event where side families have the chance to send their children to the main line."
        "Estelle had told you earlier that only side families can visit the main estate before {a=glossary:The Gathering}🔻 the Gathering{/a}.{w} Meanwhile, Gideon claims that nobody outside of Velmonta knows your existence yet."
        "There's no way Rydell wouldn’t receive word of an offshoot’s visit, bordering Velmonta - and no such family had visited, the estate being empty upon your arrival.{w} So they knew where the carriage was from." 
        "But they saw you, a dirty orphan with no business in a noble house, through the carriage windows.{w} Even went the extra mile to halt you as you tried to pass through. Rydell certainly knows of your existence."
        "And Rydell's the most hostile side family of all, no? Yet not a stir."
        "Your cheeks burn. Had Gideon really believed that you wouldn’t see past his nonsense?{w} No, it's too soon to let your pride get the better of you. You have to clear your mind."
    else:
        "You feel awkward and mechanical."
        "You're still not used to all this..."
    "As you chew the tough meat, you meet Dorian’s stare head-on.{w} Are you amusing to him? Is he trying to provoke you?{w} You can't see past the wide grin on his face. It's like an ironically expressive mask."
    "You smile back at him, tilting your head to the side, eyes blank and stupid.{w} There; the perfect fool."
    "Cassian’s voice rings out." 
    show cassian normal
    c "[noble_name]. How are you adjusting to life here?"
    hide dorian
    "Your eyes widen and you break the deadlock with the boy opposite you."
    mc "I- I’m doing well. It’s comfortable. Thank you."
    "The patriarch's voice is warm as he responds."
    c "That is fortunate to hear. Feel free to express any future troubles you may encounter, be it over family meals or in private."
    "You blush." 
    mc "Thank you."
    show marianne serious at left
    "Marianne nods." 
    m "It is good that you are adjusting quickly, child."
    mc "T-thank you, again."
    "Florence’s eyes are upon you once more.{w} You watch her too, from the periphery of your vision. She twists back in her chair to whisper something to the ash-haired maid behind her.{w} After the maid’s response, Florence’s gaze moves up, landing on Tess behind you."
    "You maintain the subtle shake in your hands until the rest of the family - aside from Dorian - loses interest in your fragility."
    hide florence
    hide marianne
    hide cassian
    jump ch4_4_night


label ch4_4_night:
    $ bearings = "Private quarters."
    $ time = "Day 4. Night."
    $ part = "4"
    "Night. It's your second night without Lin by your side. Your second night without biting cold numbing your fingers.{w} The blankets warm you. Your room itself is a bastion of warmth. "
    "What are you to do now? There are clear answers: prepare before they learn of your existence, learn to fend assailants off, gather information on this house. But something still doesn't sit right with you."
    "Who do people report to in this household? Estelle, Gideon, Tess; even the patriarch and matriarch. They each have their own motives for acting. You can sense it." 
    if conclusions["the_truth"]["unlocked"]:
        jump ch4_4a_think
    else:
        "You easily drift off to sleep. Something about doesn't feel right, but you can't place what it is."
        "Maybe you should have asked Tess earlier about it."
        "No, it was better that you didn't. You don't know who he reports back to."
    jump ch5_1_fools_parade

label ch4_4a_think:
    "The most immediate reasoning that you need to challenge is Gideon’s."
    "Why had he lied to you?"
    "Either he had lied about Rydell being unaware of your existence, or he had lied about the changes in legislation."
    "And now, his motive for creating this juxtaposition."
    "Them being unaware - is it to console you on your way back? No, that's too optimistic.{w} Still, he had created a false sense of security around you."
    "Tess had said the same thing. Is he lying to you too?{w} But Tess had implicitly confirmed that you would be murdered if they knew about you. Similar to Gideon’s narrative."
    "You stare up at the ceiling, clutching your duvet to your chest."
    "Were Tess and Gideon aligned under the same motive to lie to you? Whatever it is, it doesn't seem like they're telling you the truth."
    "It's certainly possible; you need to watch out for that.{w} If so, though, why? To create a sense of incoming danger? Convince you, using your witness to the maid’s death, that you're under threat too?"
    "What a clever plan, to use such reasoning: ‘you’re under danger. Don’t look in the right direction, stay paranoid. The only reason you’re not being attacked right now, the one thing we cannot influence, is because they don’t know you exist.’"
    "That would make sense, but then what would the greater danger be? Or do they have another motive?{w} No, that's overreaching. The worst possible scenario you can think of. But it'll kill you if you ignore it too much."
    "There are other possibilities too."
    "Come to think of it, why did he believe that you wouldn't not catch him out in his lie? Because you know no-one here to ask? Your insides boil hot in anger; you fan yourself down."
    "If he had lied about their reason to murder you, that would be more interesting than anything." 
    "Or was his lie even more primal? What if he spun a lie about why the maid had died, based on what he knows you know?{w} If he and Tess were collaborating, then the valet would’ve overheard Cassian painting the maid’s death as an intended assassination."
    "But what if it wasn’t, and Cassian was only presenting it in a different light to hide something? You can't trust noble houses to be truthful, after all."
    "A sharp jolt of pain in your head. You bite the inside of your mouth."
    "There are endless more possibilities you can consider right now. So many that it's almost useless to ponder over each one.{w} You need more information to guide you in the right direction."
    "But there's nobody to ask, and nobody you're confident would give the truth or even related gossip that you could ‘conveniently’ overhear."
    "Your stomach drops as the next thought comes.{w} What if you're not safe after all?{w} That maid had access to at least one room. Who's stopping anyone from coming in tonight? You have the dagger by your bedside, but it doesn't guarantee safety. Not in any way."
    "You've watched too many people die from knife fights. Too many to believe you'll get out of one easily alive, let alone unscathed."
    "But you have to survive somehow."
    "For Lin, your dear sister."
    jump ch5_1_fools_parade


label ch5_1_fools_parade:
    $ time = "Day 5. Late morning."
    $ chapter = "5: A Fool's Parade"
    $ part = "1"
    "You're commited to breaking out of your paralysis."
    menu:
        "*Go to the library*":
            jump ch5_1a_library
        "*Go to the chapel*":
            jump ch5_1b_chapel

label ch5_1a_library:
    $ bearings = "Library."
    "After waking, you committed to breaking out of your paralysis. You're going to get information, and you'll start with the one place that can't avoid you for certain.{w} Even if it lies to you, it lies to everyone equally."
    $ glossary_dict["About Wealth"] = "No wonder the rich only get richer. They have so, so many more resources than you from the very beginning."
    "The {a=glossary:About Wealth}🔻 library{/a} is huge and daunting. Closing the door behind you quietly, you walk around, simply taking in the sight of such boundless knowledge."
    "You begin looking around for books. But not long into the expedition, a woman approaches from behind." 
    "You great her, stammering, as your heartbeat slowly settles down once more."
    $ alter_npc("Librarian", "#ce4070", "#e193c0")
    npc "Are you searching for something?{w} Oh – Miss [noble_name]! How can I help you? What topic would you like to learn about?"
    "You swallow, taking a step back as she barrages you with questions." 
    npc "Empire’s history."
    "She thinks for a few seconds, then begins walking." 
    r "Is there any particular author you’re trying to find, miss?"
    npc "Well, I don’t know an-{w} I mean, I’d just like somethin’ related to noble houses."
    "She purses her lips. Why?"
    npc "Is there a date you’d like it from?"
    "You reply, voice hoarse."
    mc "Recent years?"
    "She whispers numbers under her breath, then registers something.{w} Her eyes widen, and she hesitates before regaining her smile."
    npc "Oh, uh – Young Miss, I’ll… find some specific books, just to get you started."
    mc "Amazin’. Thank you."
    npc "Pleasure." 
    "She rubs her nose, then sets the completed pile before you."
    npc "Study’s over there, Miss [noble_name]. And you’re welcome to take the books back to your room."
    "Thanks again.{w} And how’m I meant to address you?"
    r "Rosette, Miss."
    "You glance down at the pile. You want to ask her why she hadn’t reached for any books on the previous century.{w} But you have another goal. Well, there's nothing to do other than swallow your pride."
    "A short bow in acknowledgement. The bell struck. I was late for lunch."
    jump ch5_2_challenge


label ch5_1b_chapel:
    $ bearings = "Summertide Chapel."
    "The Summertide Chapel has the scent of moon petals. To be expected, of course."
    $ glossary_dict["Harith Formation"] = "A specific formation of Myllith sigils that represents self-reflection and integrity. With myriad reflections, it's thought to be impossible to escape judgement."
    "Myllith sigils hang all around you, chained to each other in the {a=glossary:Harith Formation}🔻 Harith formation{/a}."
    "It's disconcerting, to say the least."
    "There's a strange twinkling, too."
    "Somehow it's empty. Isn't this place meant to be popular?"
    "You wander up to the basin at the front."
    "It's filled with petals and a red liquid."
    "Many self-sacrifices have been made, then."
    "You purse your lips."
    "The twinkling sound is getting to you."
    "Statues of Myllith are everywhere. So are pictures of Velmonta."
    $ glossary_dict["Sword Ritual"] = "Community sacrifice. Representatives gather in a circle, joined by their swords, before offerings are made into a shared basin."
    "It's strange. Velmonta doesn't position itself as holy. It hasn't, but the chapel has murals upon murals of Velmontans {a=glossary:Sword Ritual}🔻 in a circle{/a}, armed with silver."
    "Your mind flits back to the statue of Myllith in your room."
    "The likely conclusion is that Velmonta was once a deeply religious place."
    "Strange, then, that Florence is the only person that even bothers to wear a morllith anymore."
    "You walk back over to the basin."
    "...Myllith still seems to obtain many sacrifices. There are definitely believers after all."
    "You leave."
    "Dinner should be soon. Maybe all the staff are preparing for it."
    jump ch5_2_challenge

label ch5_2_challenge:
    $ part = "2"
    $ time = "Day 5. Noon."
    $ bearings = "Lunch Hall."
    "The light slants through the tall windows, casting brightness all around the hall. You stab at your poached egg, watching the yolk bleed across the plate.{w} Your head is ringing again, like it's been for the past few days.{w} You try to hide it."
    $ glossary_dict["Her Stare"] = "People do that when they're about to attack, no?"
    show florence normal
    "Florence is still staring at you. Her gaze is hungry. You stare her dead in the eye.{w} For a moment, her {a=glossary:Her Stare}🔻 eyes widen{/a}. You pause your fork in the air."
    "Setting her cutlery down with a deliberate clink, she dabs at her mouth with a handkerchief, then sets her hands down in reluctant virtue." 
    f "Father. Mother."
    "She tilts her head in concerned grace."
    f "I feel that I have a duty to report something that has… lately been… troubling my conscience."
    show marianne serious at right
    "Marianne looks up from her newspaper.{w} Cassian's hand tightens around his cufflinks."
    m "And what matter would that be?"
    "Florence’s eyes dart to you, then look away."
    f "It concerns my dear sister’s… conduct… with the servants."
    hide marianne
    "The table goes silent.{w} You set your fork down and look towards Tess and Estelle, confused. Dorian’s knife stops mid-air."
    "Her voice dripping with sympathy, she clasps her hands."
    f "It has come to my attention that she has… had some charged exchanges with her servant, Tess."
    "Silvian’s brow furrows."
    "With a quick sob, she puts her hand to her mouth." 
    f "I was walking in the courtyard and looked up – and I… I…"
    "What? How are you meant to respond to this?{w} A claim of impropriety. Its purpose… right, to plant a seed of doubt.{w} Even if nobody believes it, your reputation'll be stained.{w} And why wouldn’t they believe holy Florence, admired by all?"
    "If you respond angrily, defensively, guiltily, or with acceptance, Florence wins either way." 
    "Oh – Lin would’ve loved this place, wouldn’t she? Being in the centre of attention?{w} After all, everyone’s eyes are on you. What to do, what to do, what to-!"
    menu:
        "*Diffuse the situation at your own expense*":
            jump ch5_3_fool
            

label ch5_3_fool:
    $ part = "3"
    "You laugh, the sound ringing through the room.{w} Florence blinks."
    f "Sister [noble_name]?"
    mc "Brother Dorian!" 
    "You turn to him, beaming." 
    mc "You heard that?" 
    "You wipe a tear from your eye, dissolving into further laughter."
    "He stares at you, lost. The usual glint in his eye is marred with confusion."
    "Turning back to Florence, you stop laughing."
    f "Sister. I am aware of why you are saying this."
    "Her hand flies to her morllith."
    f "And…{w} why might that be?"
    "You grin. You internally cackle at your own shamelessness.{w} However, you continue. You puff your chest out and meet her with a question of your own."
    mc "Is it ‘cause you’ve seen how nice he is? How he escorts me ‘round? How he talks with such a kind voice?"
    "Her nose wrinkles. You watch Tess pale visibly in the corner of your eye.{w} Conspiratorially, you lean in."
    mc "I’m disappointed, sister. If you wanted Tess all to yourself, you coulda just asked, ‘kay?"
    "And with that, you resume eating, donning a prideful expression."
    "Cassian coughs."
    c "Dear [noble_name], what evidence do you have to support your sister’s…"
    "He doesn't finish."
    "Bringing your finger to your chin, you twist your mouth into a pout."
    mc "I…{w} I feel it. But my feelings ain't never wrong.{w} Right, Estelle?"
    "In brief distaste, Estelle clears her throat."
    e "Yes, Miss [noble_name]. You’re the very picture of intelligent thought."
    "You turn to Tess next."
    mc "Tess? C’mon, help me out here, eh?"
    "His lips are drawn as he stares ahead, ignoring you. You pause.{w} What? Is he on Florence’s side?{w} Damn, your pride. You feel it flying away already."
    show dorian normal at right
    "Dorian snorts. It's a small, strangled sound. But it's deafening in the dead silence.{w} Raising a hand to his mouth, shoulders shaking, he tries to calm down."
    d "I… forgive me, I just…"
    "Florence can't help but smile despite herself too. Cassian stares at the two, as if about to apprehend them.{w} But Marianne puts her palm down on the table."
    m "That’s enough. This conversation ends here."
    hide dorian
    "The breakfast continues as if nothing had happened."
    "Florence stares at you. She brings her hand to her mouth, shaking."
    f "Sorry – if I may, I’d like to excuse myself.{w} You see, I have a slight headache."
    hide florence
    "You don't quite understand.{w} Aren't there larger enemies to fight? Why play for reputation? Or is that her scheme?{w} Oh, you'll be sure to hold this grudge."
    "You would’ve burned in shame had you not been trying to paint yourself as shameless.{w} The rest of the meal is silent."
    "As you trudge back to your room, the servants avoid you; great.{w} This is fine. There wasn’t a better solution, right? And you'd done well."
    "Yes, you'd planned on being a fool from the start."
    "But wow."
    jump ch5_4_aftermath

label ch5_4_aftermath:
    $ part = "4"
    $ time = "Day 5. Late afternoon."
    $ bearings = "Your quarters."
    "Nobody responds when you ring the bell. Neither Tess nor Estelle.{w} You sigh. At least surveillance is looser now, after all that stir. You have time to gather your thoughts.{w} But being too much of a non-threat puts a target on your back too, as someone easy to kill." 
    "You bite your lip and turn back to the book." 
    "Shivers run down your spine, recalling the time Lin had been beaten – nearly to death – just to relieve a blacksmith’s fury. The main empire was thriving and the Emperor had played a little game of information control."
    "And what did it cause? A period of massive protests and anger in Scab City. Nobody liked the nobility in the first place, but the Marchetti Campaign was the last straw.{w} Too bad reaching the district was a one-way thing."
    "The only blood spilled was of the same origins as the protesters. The blood of Scab City. The blood of people like you and Lin, powerless before the swarm."
    "Those nobles had simply waited it out while you were threatened with death."
    "You don't doubt that half Scab City's outrage was from bruised pride. You didn't have time to care about historical preservation, or whatnot. But he’d looked down on your intelligence.{w} And now he even dares to look down on the nobility? You check for the author. Blank."
    "You run your hands over the cover.{w} You want to know why Rosette chose this book for you."
    "You have half a mind to throw it across the room."
    "Since when have you been this violent and rash-headed? Without Lin here to ground you, perhaps this was inevitable. But it's a sore self-realisation."
    "If only Lin was here with you.{w} If only she was able to read.{w} If only she was ruthless enough, paranoid enough, rational enough to hold her own here."
    "But you're grateful at the same time. She didn’t think enough. She would’ve brashly done whatever she’d have thought right without a second thought. We’d always agreed that you were the calmer one."
    "You reach for the bell again, then decide against it. No point in proving your isolation again. If anything, this has proved that the servants don't answer to you. Any loyalty you've felt from them was loyalty to Velmonta."
    "You're cautious around Rosette when returning the book. She seems shifty when you glance at the bookshelf. You tell her you can't read, that you struggled with my letters, and that's your reason for giving the book back so soon.{w} That sudden lie seems to calm her, but why? You assumed it's because of my newfound reputation, somehow."
    "So many mysteries."
    "Well, if the answers won't come to you, it looks like you'll have to go to them yourself."
    menu:
        "*Talk to Cassian*":
            $ choice = "Cassian"
        "*Talk to Marianne*":
            $ choice = "Marianne"
    $ bearings = "The gallery"
    "Just earlier this morning, you'd been feeling at home among the masses in the halls. Being able to do your own thing.{w} That's just the way you like it.{w} In the direct aftermath of the confrontation, they’d been silent. But now their gazes change. Eyes and quiet chatter follows each step you take."
    "Before, you'd been a new novelty in the household, not special enough to latch onto. Now they see you as an absolute fool."
    "At least the fool persona isn't too meek to retaliate, and they knew that.{w} You're stupid, but not stupid enough to back down.{w} The dissatisfaction follows you around regardless, but at least it's not confrontational.{w} You mentally curse Florence as you shoot a sunny smile at a valet. He blinks, then smiles back, before turning to the boy next to him. That'll keep them happy, won't it? A new piece of gossip?"
    "In some ways, nobles and slum kids are the same.{w} Always looking for something to gloat over; even better if it's a person."
    $ part = "5"
    $ time = "Day 5. Early evening."
    if choice == "Marianne":
        jump ch5_5a_marianne
    else:
        jump ch5_5b_cassian


label ch5_5a_marianne:
    play sound knocking_urgent
    "You stop before Marianne’s study. You've never been inside.{w} Well, there are always firsts, aren't there? You knock thrice, hearing no voices through the door. Estelle taught you the different knocks and when to use them." 
    m "Yes?" 
    mc "Mother, it’s [noble_name]. May I speak to you?"
    m "A moment."
    "You look around the gallery in the meantime. Her public study is closer to the salons than Cassian’s.{w} Does that mean she takes the onus for receiving guests? Or is that a stretch?{w} You shake your head. Yes, it's probably a stretch. This room's probably been here for decades. How long has Velmonta been around?"
    m "Come in."
    "You oblige."
    play sound open_door
    $ bearings = "Marianne's Study."
    "Her study is warmer than Cassian’s. Strange, because Marianne herself is colder. It maintains a delicate balance. The bright blue of the windows gives the room an airy quality."
    $ glossary_dict["Chair"] = "It's not a wooden one; it's one of those sinking chairs, the type that swallows you into the earth."
    show marianne serious
    "She pulls out a {a=glossary:The Plague}🔻 chair{/a} for you.  You sit into its embrace only reluctantly."
    m "Why have you sought me for a meeting, [noble_name]?" 
    "You don't know whether to meet her hazelnut eyes or avoid them.{w} Lord, she's beautiful. You aren't usually a connoisseur for faces, but there's nobody else more suitable to represent Velmonta.{w} Her skin glows from underneath, radiant from within. Her eyes are piercing and shadowed, but hesitant, caring.{w} You clear your throat."
    mc "I’m mighty sorry for today."
    show marianne hesitant
    m "You need not be."
    mc "Really, since the death, I’ve been scared out my wits ‘round here." 
    "You let a sob slip from your lips, before quickly covering your mouth, turning your head down, and letting your hair fall over your face."
    show marianne serious
    m "Be not afraid. Lift your head."
    "She moves the candle closer, illuminating both your faces.{w} You gaze up at her, smoothing the crease between your brows while maintaining the tension in your face."
    m "It is because you are not yet prepared, [noble_name]."
    mc "Sorry?" 
    m "If I remember correctly, that night I told you that, at some point, you would learn about the reason for the murder.{w} And why someone attempted to assassinate Dorian."
    mc "And I'm ‘bout to find out now?"
    "She turns to look at the portraits on the wall."
    m "A good question. Do I tell you? Or do I keep you in the dark?{w} Would you be able to bear the truth?"
    "I’ll try. I will."
    "You bite your lip, daring to look her in the eye.{w} Mouth slightly open, she stares at you."
    m "It does not benefit anyone for you grasp at shadows. I would have informed you either way.{w} But it is good to hear your conviction spoken of."
    "She traces her hands over her necklace and smiles. Benefit no-one for you to be kept in the shadows?"
    "Are you to trust her or not? She seems so confident and assured."
    $ glossary_dict["The Lower District"] = "The sanitised name for 'Scab City.' The name itself is counterfactual; it's topologically high-altitude and embedded in the middle of the Marchetti Empire. It's only 'lower' in status. But of course, that's all that matters, huh?"
    "You hail from the {a=glossary:The Lower District}🔻 Lower District{/a}.{w} So you would have seen the ‘gangs’ fighting. Over food, water, shelter - anything scarce."
    "You nod, mouth dry." 
    mc "Revvers protected me."
    "She pays no heed, seemingly lost in thought."
    mc "That’s why they’re tryin’ to kill us?"
    "She adjusts her hair, though beautiful either way. Her eyes curve upwards."
    m "How direct.{w} But yes.{w} In this case, the side families are fighting for power."
    m "There can only be four successors at a time. The quota has been fulfilled now, you see."
    m "You might not understand how much weight your position carries, but they certainly do.{w} It's a prime opportunity."
    mc "So why’m I not being protected?{w} Why’re none of us gettin’ help?"
    show marianne hesitant
    "Marianne freezes, then looks away."
    mc "Mother?"    
    m "It is time for dinner, child."
    mc "When’re we continuing this?"
    "She walks towards the door."
    show marianne serious
    "Stand, [noble_name]."
    mc "Mother, I need a sword at lea-"
    m "-let there be no more qualms. You are sufficiently learned now."
    "She stops waiting and walks out."
    hide marianne
    jump temp_end_message

label ch5_5b_cassian:
    jump temp_end_message