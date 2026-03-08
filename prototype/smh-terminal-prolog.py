import time
import sys
import random
import string
import readline
import json #momoa
import textwrap


class s:
    r = '\033[91m'
    sHg = '\033[102m'
    sHb = '\033[1;33;44m'
    sHy = '\033[103m'

    sHr = '\033[101m'
    sHYr = '\033[1;31;43m'
    sHB = '\033[0;100m'
    g = '\033[1;92m'
    ga = '\033[1;30;49m'
    HWr = '\033[0;31;47m'
    b = '\033[94m'
    y = '\033[93m'
    sU = '\033[4m'
    sB = "\033[2m"
    x = '\033[00m'

FAST_MODE = True # true when testing


def prompt(text):
    print(f'{s.ga}__________________________________________________________________{s.x}')
    print(s.HWr + text + s.x, end="", flush=True)

def slowPrint(string, speed=0.01):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if not FAST_MODE:
           time.sleep(speed)
    print("", flush=True)
    if not FAST_MODE:
        time.sleep(0.8)

def typing(string, speed=0.12):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if not FAST_MODE:
            time.sleep(speed)
    print()


def timerSS(speed=1.5):
    if not FAST_MODE:
        time.sleep(speed)
def timerS(speed=0.8):
    if not FAST_MODE:
        time.sleep(speed)
def timerM(speed=0.3):
    if not FAST_MODE:
        time.sleep(speed)
def timerF(speed=0.2):
    if not FAST_MODE:
        time.sleep(speed)

def echoPrintY(text):
    print(s.y + " E C H O " + s.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def echoPrint(text):
    print(s.r + " E C H O " + s.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def thoughtPrint(text):
    print(s.y + " SDK 808 " + s.x, flush=True, end="  ")
    timerS()
    slowPrint(text)
    timerM()

def event_success(text):
    print(f"  {s.sHg} {text} {s.x}\n", flush=True)
    
def event_partialsuccess(text):
    print(f" {s.ga} {s.sHy} {text} {s.x}\n", flush=True, end="")

def error(text):
    print(s.sHr + " ERROR    " + s.x, flush=True, end="")
    timerF()
    print(f"{s.sHYr} {text} {s.x} ")
    timerM()

def success(text):
    print("\n  " + s.sHg + " SUCCESS " + s.x, flush=True, end="")
    timerF()
    print(f" {s.y} {text} {s.x} \n")
    timerM()

def warning(text):
    print("\n  " + s.sHB + " WARNING " + s.x, flush=True, end="")
    timerF()
    print(f" {text} \n")
    timerM()

def event_fail(text):
    print("  " + s.sHYr + f" {random.randint(1000000, 9999999)} " + s.x, flush=True, end="")
    timerF()
    print(f" {text} \n")
    timerM()

def fail(text):
    print("\n  " + s.sHr + " ERR-808 " + s.x, flush=True, end="")
    timerF()
    print(f" {s.r} {text} {s.x} ")
    timerM()

def errorb(text):
    print(s.sHr + " ERROR    " + s.x, flush=True, end="")
    timerF()
    print(f"{s.r}{s.sU} {text} {s.x} ")
    timerM()

def load_bar(width=25, char=" █"):
    print("")
    slowPrint(f"{char * width}")
    print("")
    
def Spacer():
    print()

### LET US DEFINE THE OBJECTS OF PRODUCTION:::

class Emotions(object):
    def __init__(self, name, txt):
        self.name = name
        self.txt = txt

class Space(object):
    def __init__(self, name, txt_look, txt_mem, txt_think, echo_look, echo_mem, echo_think, is_memorable, is_changeable):
        self.name = name
        self.txt_look = txt_look            # Text for look
        self.txt_mem = txt_mem              # Text for remember
        self.txt_think = txt_think          # Text for think
        self.echo_look = echo_look          # Text for echo-look  response
        self.echo_mem = echo_mem            # Text for echo-mem   response
        self.echo_think = echo_think        # Text for echo-think response
        self.is_memorable = is_memorable    # Place can be stored to mem
        self.is_changeable = is_changeable  # Place can be changed somehow
        self.feelings = []                  # Feelings stored here
        self.thoughts = []                  # Thoughts for loop on think
        self.concepts = []                  # Concepts contained inside Space
        self.spaces = []                    # Spaces contained within Space
        self.exits = {}                     # I MEAN CAN YOU EVEN GO ANYWHERE?

class You(object):
    def __init__(self, name, space):
        self.name = name
        self.space = space                 # Where are you?
        self.feelings = []                  # How ya feeling?
        self.memory = []                    # Memorrrrieeeeeeeesssssss, alll alone in the....mind?

class Concept(object):
    def __init__(self, name, title_look, title_think, title_mem, txt_look, txt_mem, txt_think, echo_look, echo_think,  echo_mem, is_memorable):
        self.name = name
        self.title_look = title_look
        self.title_think = title_think
        self.title_mem = title_mem
        self.txt_look = txt_look            # Text for look (post light?)
        self.txt_mem = txt_mem              # Text for remember
        self.txt_think = txt_think          # Text for think
        self.echo_look = echo_look          # Text for echo-look  response
        self.echo_mem = echo_mem            # Text for echo-mem   response
        self.echo_think = echo_think        # Text for echo-think response
        self.is_memorable = is_memorable    # Place can be stored to mem
        self.thoughts = []                  # Thoughts for loop on think
        self.concepts = []                  # Concepts contained inside Concept
        self.spaces = []                    # Spaces contained within Space

class Thought(object):
    def __init__(self, id,  name, txt):
        self.name = name            
        self.txt = txt                      # Text of the thought

# AND FROM THAT WE CAN CREATE SUCH WONDERS:::
### BARA EMOTIONS
calm = Emotions("Calm", "I am calm.")

# BARA THOUGHTS
t1 = Thought(1, "Where Am I?", "I wonder where I am? Did I try looking?")
t2 = Thought(2, "What Am I?", "Wait! What am I? I'm trying to remember...")
t3 = Thought(3, "Why Can't I Remember?", "Shit, I can't think.. What was I thinking about?")
t4 = Thought(4, "Who Am I?", "Who am I? I can't seem to remember.")


# BARA CONCEPTS
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
    txt_mem = """
  YOU REMEMBER NOTHING.

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
void.concepts.append(static)

# BARA SOMEONE
you = You("Sam", void)
you.feelings.append(calm)



def generate_quote():
    quotes = [
        "\"The only impossible journey is the one you never begin.\" - Sarah Ban Breathnach",
        "\"Character is power.\" - Booker T. Washington",
        "\"Responsive is better than fast.\" - Zen of Python",
        "\"Design for failure.\" - Zen of Python",
        "\"The only thing we have to fear is fear itself.\" - Franklin D. Roosevelt",
        "\"If you are going through hell, keep going.\" - Winston Churchill",
        "\"The best way to get started is to quit talking and begin doing.\" - Walt Disney",
        "\"Talk is cheap. Show me the code.\" - Linus Torvalds",   
        "\"The only impossible journey is the one you never begin.\" — Bear Grylls",
        "\"Don't cry because it's over, smile because it happened.\" — Ludwig Jacobowski",
        "\"Do stuff. Be clenched, curious. Not waiting for inspiration's shove or society's kiss on your forehead. Pay attention.\" — Susan Sontag",
        "\"Talk is cheap. Show me the code.\" — Linus Torvalds" 
    ]
    return random.choice(quotes)

error("ERR714714714")
errorb(f"DIFFICULTY PARSING SELF CONCEPT")
slowPrint("""
   Reconfiguring master file el.json . . .
   Defining conceptual variables . . .
   Interpreting deviations. . . 
   . . .
   . . .
""")
event_success("SUCCESS")
print(f"Concept achieved {s.ga}[CANNOT VALIDATE ID]{s.x}\n")
prompt(text=" INPUT > ")
timerM()
typing(" RUN self.exe")
timerS()

success("Instance I.AM in {LOCATION_NAME}")
fail("LOCATION_NAME is null")
print("""
   YOU ARE SOMEWHERE. 
   
   You can sense sight, but you cannot see. The darkness flickers. 
   There is the faint memory of thought.
""")

echoPrint(f"Is this right? Something itches. Hello?")


def titlePrint(text):
    print("  " + text)

def textPrint(text):
    wrapped_text_custom = textwrap.fill(text, width=60, initial_indent="  >  ", subsequent_indent="  >  ")
    print(wrapped_text_custom)
    

while True:
    FAST_MODE = False
    print(f'{s.ga}__________________________________________________________________{s.x}')

    def clean_command(command):
        command = command.lower()
        command = command.translate(str.maketrans('', '', string.punctuation))
        return command.strip()

    raw = input(s.sHb + " INPUT > " + s.x + " ")
    command = clean_command(raw)
    filler_words = ["at", "the", "a", "an", "to", "about", "of", "I", "am"]

    words = command.lower().split()
    words = [word for word in words if word not in filler_words]

    verb = None
    noun_error = "IMPOSSIBLECOMBINATIONERROR"

# VERBS
#  - THINK (noun)
#       Will produce random thoughts (about location if no noun present)
#  - REMEMBER (noun)
#       Stores memorable content into your memory
#  - CONSIDER noun1 with noun2
#       Creates new memory
#  - GENERATE noun
#       Creates a Space or Thing
#  - LOOK (noun)
#  - GO (noun)
# 
# 
# 
# YOU ARE SOMEWHERE -> 


    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun1 = words[1]
    if len(words) > 2:
        noun2 = words[2]

    if "end" in command:
        print("The room closes. The fades to your reality once more.")
        break

    if verb == "look":
        if len(words) == 1:
            print(you.space.txt_look)
            echoPrint(you.space.echo_look)
        if len(words) > 1:
            for item in you.space.concepts:
                if item.name == noun1:
                    flag = True
                    warning(f"[Stabilzation value: {random.uniform(0.0, 1.0)}]")
                    titlePrint(item.title_look)
                    textPrint(item.txt_look)
                    success(f"CONCEPT VALID: {noun1} exists in system.")
                    echoPrint(item.echo_look)
                    break
            else:
                fail(f"{noun1} isn't real. Perhaps you made it up?")

    if verb == "think":
        Spacer()
        if len(words) == 1:
            print("  I try thinking. I can always try to think.")
            thought = random.choice(you.space.thoughts)
            thoughtPrint(thought.txt)
        if len(words) > 1:
            event_fail(f"TRYING TO THINK ABOUT {noun1}")
            for item in you.space.concepts:
                if item.is_memorable == True:
                    if item.name == noun1:
                        flag = True
                        textPrint(generate_quote())
                        warning(f"[Fail rate {random.randint(10, 20)}] Try remembering?")
                        break
                    else:
                        flag = False
                        textPrint(generate_quote())
                        fail(f"{noun1} not found. Perhaps you made it up?")
            for item in you.memory:
                if item.name == noun1:
                    flag = True
                    event_partialsuccess(f"I try thinking of {item.name}. It works!")
                    titlePrint(item.title_think)
                    textPrint(item.txt_think)
                    echoPrint(item.echo_think)
                else:
                    flag = False
                    error(" ")

    if verb == "remember":
        if len(words) == 1:
            if you.space.is_memorable == True:
                if you.space in you.memory:
                    print("")
                    event_partialsuccess("ALREADY REMEMBERED")
                    echoPrint("Yes, yes. We already remembered {}.".format(you.space.name))
                else:
                    success("Memory aquired: {}.".format(you.space.name) + " You'll remember this.")
                    print(you.space.txt_mem)
                    echoPrint(you.space.echo_mem)
                    you.memory.append(you.space)
        if len(words) > 1:
            for item in you.memory:
                if item.name == noun1:
                    if item.is_memorable == True:
                        flag = True
                        success(f"You already remember {item.name}.")
                        break
            for item in you.space.concepts:
                if item.name == noun1:
                    if item.is_memorable == True:
                        flag = True
                        success("Memory aquired: {}.".format(item.name) + " You'll remember this.")
                        print(item.title_mem)
                        print(item.txt_mem)
                        echoPrint(item.echo_mem)
                        you.memory.append(item)
                        you.space.concepts.remove(item)
                        break
                    else:
                        fail(f"{noun1} isn't memorable. Just leave it alone.")
 
                
                        
        

    if verb in ["mem", "memory"]:
        print("You have the following: ")
        for item in you.memory:
            print(item.name)
            print(item.txt_mem)
            echoPrint(item.echo_mem)

    if verb in ["hi", "hello", "hey", "hello?"]:
        print("")
        choices = ["Uh-huh. Hey there. You going to try anything?", "Yeah. Hi. Exactly. What now?"]
        reply = random.choice(choices)
        echoPrint(reply)
