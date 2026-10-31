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

default suspicion_list = {}

default messages = {
"Important choice": "Your next choice may greatly impact the storyline.",
}
    
image ctc:
    #ctc code credit to CheeryMoya and OokamiKasumi lemmasoft renai us forum
    "gui/ctc_icon.png" with Dissolve(0.4), #This is your image
    subpixel True #This line makes sure that ATL is smooth 

    yalign 0.84 xalign 0.85 #Adjust these numbers to fit your own textbox
    linear 0.5 yalign 0.85
    linear 0.5 yalign 0.84
    
    repeat

#variable initialisation
define r = Character("Runa", color="#4af5e4", what_color="#a0e8ed", ctc="ctc", ctc_position="fixed")
define l = Character("Lin", color="#8f6464", what_color="#d7cdba", ctc="ctc", ctc_position="fixed")
define g = Character("[gideon]", color="#a9522a", what_color="#c7a691", ctc="ctc", ctc_position="fixed")
define narrator = Character(what_italic = True, ctc="ctc", ctc_position="fixed")
define e = Character("Estelle", color="#b93a00", what_color="#fdcdb0", ctc="ctc", ctc_position="fixed")
define npc = Character("[npc]", color="#747474", what_color="#c8c4c1", ctc="ctc", ctc_position="fixed")

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
    play music lin_theme loop
    show screen top_bar()
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
    "Lin's jaw tightens. Her eyes glaze over." with vpunch
    "As you shake her, she stirs slightly, expression oddly serene."
    "You pray internally. '{a=glossary:Myllith of Moon}🔻 Myllith of Moon{/a}... please not again...'"
    menu:
        "Why's the plague flaring up again??":
            pass
    "And then a sudden rush of stillness."
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
    show gideon hidden 
    "A clicking sound jolts you to your feet as a cloaked figure steps in." with vpunch
    
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
    
    "You pull your lips into a sneer as his approach drives you back."
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
        "N-nevermind.":
            "Gideon nods and looks back out the window."
        "Where do I find you in the future?":
            "His eyes widen."
            g "How direct."
            "He leans back."
            g "The barracks. They are a short distance from the outer wall."
    "In the warmth of the cloak Gideon draped around you, you grow drowsy despite the time."
    "As you drift off, you can't help but harbour the naive hope that Lin, somewhere out there, is doing well for herself."
    "You sleep for a while, mind floating out of your body."
    "The carriage suddenly jolts to a stop." with vpunch
    menu:
        "Are we here?":
            pass
    g "No. Don't move. Stay in the carriage."
    "Stirring, you see Gideon stepping out briskly with his brow furrowed. He slams the door with a clang, muttering darkly under his breath, “Should've chosen a better route.”" with vpunch
    "Your grogginess is now subsiding. You can't fall back asleep even if you want to."
    "...And besides, it's not the right time of day."
    menu:
        "*Look at the landscape outside*":
            $ witness_shove = False
            "Somewhere along the journey, the filth outside had become polished stone and shrubbery. You've never left Scab City before, but you can tell: you're beyond the forest already."
        "*Look at what Gideon's doing*":
            "You bring your face closer against the window. There isn't any physical altercation, despite the people below being armed. The opposition is clad in the same deep blue as Gideon - but their crests are slightly different."
            "No matter how much you strain your ears, the carriage muffles the sound, rendering it incomprehensible."
            "With nothing left to do, you drum your fingers on the window impatiently, reading their expressions. After all, you doubt that Gideon can hold them off alone."
            "A man shoves Gideon on the shoulder. You look away, distracting yourself."
            $ witness_shove = True
    "The carriage door swings open again."
    python:
        if witness_shove:
            dialogue_var = "where he'd been shoved"
        else:
            dialogue_var = "as if there was something dirty there"
    menu:
        "*Stay quiet*":
            pass
        "What happened?":
            g "Damn petty Rydells tried to refuse us passage." 
            "He brushes his hand against his shoulder [dialogue_var], grimacing."
            menu:
                "Rydells?":
                    g "A side family to Velmonta." 
                    "His hand falls onto his lap."
                    "Side… family?" 
                    "You blink a few times, then sigh." 
                "*Try to fall back asleep*":
                    "Despite your attempts, you really can't fall asleep again."
    menu:
        "How far're we from the estate?":
            g "We’ll get there after passing through the rest of the territory."
            menu:
                "Anything else I need to know?":
                    jump arrival
        "Anything else I need to know?":
            jump arrival


label arrival:
    "His hand flies to his chin, a finger hovering over his mouth."
    g "Don’t let yourself believe you’re safe simply given the way things will seem."
    menu:
        "What d'you mean?":
            "Your question is met with a simple shaking of the head."
        "*Ponder over his meaning*":
            "Your pondering doesn't work. You're even more confused now."
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
    "You shudder at the sudden blast of warmth, the source of the heat being the flames licking wildly at impervious stone."
    "Feudal brilliance is full of fiery brilliance, it seems. It suddenly occurs to you that {a=glossary:Velmonta's Reputation}🔻 Velmonta's reputation{/a} may have been more than symbolic."
    "Tearing my eyes away, you look back at Gideon. He hands an overly embellished document to the guard for inspection."
    "The guard clears his throat and hands the document back after briefly skimming over it."
    $ npc = "Guard"
    npc "Welcome to Velmonta. You may return to your carriage now."
    "Two people clad in deep blue liveries, with some effort, draw the doors open. The horses are spurred into movement again."
    "Gideon turns to you."
    g "Don't approach me until you're safe."
    "His hands trace around his sword scabbard. You're used to it by now."
    g "Truly safe. Not just fooled by the appearance of safety."
    menu:
        "Oh... okay.":
            "Gideon smiles briefly."
        "You have a habit of giving cryptic advice, Gideon.":
            "Gideon raises an eyebrow humorously."
    "You turn back to the window."
    "Extravagant black railing now lines the passage, with bountiful flower baskets hanging from each division. The fiery red begins to fade into a muted orange warmth as you approach the inner wall."
    #EXPRESSION smiling
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
    "The gate to the inner wall opens. A woman runs through, holding a pair of slippers."
    e "Hello, Miss [name]. I'm Estelle. It's great to meet you!"
    "Bending down, she slips the footwear onto your feet. It's strangely sleek against your skin, but not an unwelcome sensation."
    "She begins to guide you through the doorway."
    menu:
        "Bye, Gideon!":
            "Gideon looks disappointed that you've already forgotten his advice."
            "Below his expression, too, he looks slightly worried."
        "*Don't bid Gideon farewell*":
            "You decide it's better to follow his advice immediately."
    "You approach the softly lit inner chateau. It has spires that strech into the sky, and flags painting deep blue streaks in the air. The stairs stop before a pair of heavy-set double-oak doors."
    "Estelle knocks five times in a meaningful rhythm, and the doors creak open to reveal the unsmiling footmen who drew them open."
    "The floor's lined with marble, so polished that the light cascading from the chandelier reflects back in dazzling shades."
    "The foyer stretches out endlessly before you, spectacular and impossible."
    "Your heart beats faster. Velmonta's beautiful."
    "Beautiful, but devoid of life."

label first_blood:
    "You pull your cloak a bit tighter around yourself and look down at your slippers, snug against your feet."
    "Sensing my overwhelm, Estelle squeezed my shoulder lightly in encouragement."
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
            #EXPRESSION smiling
            e "Don't mention it, Miss!"
    "Carved wax candles line the wall murals. They depict complex battlefields. The candlelight dances in holsters to animate the scene."
    "Deep blue flags wave, dark against the blood-orange skies. Flags with the crest that you recognise as Velmonta’s."
    "So {a=glossary:Velmonta's Origin}🔻 Velmonta's origins{/a} are just like the other houses' then."
    "As the hallway continues, the murals are gradually replaced by framed portraits of ancestral family heads."
    #portrait of holy looking man
    "You can't help but notice that none look biologically related."
    "...Adoption wasn't a recent trend, then."
    #show portrait of cassian 
    "Estelle strokes your shoulder."
    e "That is your father, Miss [name]."
    menu:
        "An honour...":
            pass
    "You feel a strange repulsion, but know not at what."
    "The gallery ends. Estelle hurriedly wraps a shawl around you, guiding you across the lengthy courtyard."
    "You reach a mansion no less impressive than the main chateau. However, its outer edifice has polished wood in the place of carved stone."
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
            e "Dinner, Miss."
    "She swings the door open, handing you a pile of fresh clothes and a towel."
    "And finally, you're alone with the flowery fragrance of bathwater."

label bath_scene:
    "An unpleasant tingling instantly attacks you as you dip your feet into the swirling liquid. You hiss. It isn't unreasonably warm, but blood rushes into your limbs, bringing with it an intense itching."
    "Then comes the pain."
    menu:
        "*Pick at your skin to detract from the pain*.":
            "It gradually fades into the back of your mind, though you remain tense."
        "*Inspect your hand":
            "Raising your hand up against the gleaming chandelier, you see your clean wrist for the first time - something beyond your imagination. The colour of your skin - the true one - beneath all that grime. You let your hand fall again."
    "Today had passed by in a daze. Too much to think about, too much to take in, too much to see. Even the light was - no, is - dizzying."
    "Your mind suddenly flashes to Lin. What would her hand look like?"
    "Is it wrong that you feel glad, rather than guilty, for being taken here? Leaving her behind?"
    menu:
        "*Take deep breaths*":
            "You grab the rim of the bathtub to pull yourself up."
            "Nobody will care that you're overwhelmed. In fact, expressing it would only hurt you."
            "You have to suck it up."
    "You climb out of the bathtub."
    "A huge Myllith sigil hangs over the mirror, partly obscuring its surface. You frown, wondering why someone would choose such an impractical placement."
    "You shake the water off and step out. The nightdress is soft – too soft against your worn skin. Nevertheless, you shrug it on."
    