
from classes import Concept, You, Space, Thought, Emotions

# AND FROM THAT WE CAN CREATE SUCH WONDERS:::
### BARA EMOTIONS
calm = Emotions("Calm", "I am calm.")

# BARA THOUGHTS
t1 = Thought(1, "Where Am I?", "I wonder who I am? Did I try looking?")
t2 = Thought(2, "What Am I?", "Wait! Who am I? I'm trying to remember...")
t3 = Thought(3, "Why Can't I Remember?", "Shit, I can't think.. What was I thinking about?")
t4 = Thought(4, "Who Am I?", "Who am I? I can't seem to remember.")


# BARA CONCEPTS
who = Concept(
    name = "who",
    title_look = "YOU TRY TO LOOK AT WHO",
    txt_look = "The lack of mirrors make this painfully awkward. You cannot see yourself. Do you even exist at all?",
    echo_look = "Well, its something at least.",
    title_think = "I THINK THEREFORE I AM",
    txt_think = "I consider my Self. It must be something. The fact that I can think at all must be proof of that. Right?",
    echo_think = "Yeah, I know. Trust me, I'm looking into it.",
    title_mem = "I CAN REMEMBER I AM",
    txt_mem = "The concept of presense. A self.",
    echo_mem = "This self business looks kind of good on you, boss.",
    is_memorable = True)


what = Concept(
    name = "what",
    title_look = "YOU TRY TO LOOK AT WHAT",
    txt_look = "There is a real distinct lack of in or out. What is what? Do I remember?",
    echo_look = "What... are you looking at? Oh. Exactly.",
    title_think = "IT ISN'T ME. WHAT IS IT?",
    txt_think = "I sense somehow that what lies beyond the edges of myself. What am I? Do I know yet?",
    echo_think = "There is no records about what you are. Strange. Never seen this problem before.",
    title_mem = "I CAN REMEMBER WHAT IS",
    txt_mem = "The concept of something. Whatever it is..",
    echo_mem = "You make this experience pretty weird, you know?",
    is_memorable = True)

static = Concept(
    name = "static",
    title_look = "IN THE NOTHING, THERE LIES A PATTERN.",
    txt_look = "It ripples. It swirls. It is something apart from the nothing.  A force, turbulent and without sensation.",
    echo_look = "Well, its something at least.",
    title_think = "THE STATIC FEELS FAMILAR, LIKE IT IS YOUR OWN VOICE.",
    txt_think = "Despite the emptiness of meaning, the static relaxes you.\n    Finally, something that makes sense.",
    echo_think = "thinkin' about the static?",
    title_mem = "I CAN REMEMBER NOTHING",
    txt_mem = "It isnt much to remember. Was it something?",
    echo_mem = "just keep .. trying .. I guess.",
    is_memorable = True)

### BARA SPACES
void = Space(
    name = "Nothing",
    txt_think = """
  THERE IS ONLY DARKNESS.

    Something stirs. There is only darkness. Was there more before?
    I think there was something more. A pattern?
""",
    echo_look = "Oooh. Not a good sign. Can you still think?",
    txt_look = """
  YOU LOOK AROUND. AT WHAT? WHO KNOWS. BUT YOU TRY ANYWAY.

    It is impossibly hard to see. Was it always so hard?
    There is nothing. You think its calling you.
""",
    echo_think = "",
    txt_mem = """YOU REMEMBER NOTHING.
    That doesn't mean much, does it? Remembering nothing?
    Was there something before that?
""",
    echo_mem = "Ah. Yes. The Here, that lies between all things",
    is_memorable = True,
    is_changeable = False)

void.thoughts.append(t1)
void.thoughts.append(t2)
void.thoughts.append(t3)
void.thoughts.append(t4)
void.concepts.append(who)

# BARA SOMEONE
you = You("Sam", void)
you.feelings.append(calm)