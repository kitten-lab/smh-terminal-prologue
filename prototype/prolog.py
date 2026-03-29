import random
import string
import json #momoa
from render import *
from classes import Concept, You, Space, Thought, Emotions
from story import *
from randoms import *


### LET US DEFINE THE OBJECTS OF PRODUCTION:::

#=====================================================================================================================#
######## b e g i n   p r o l o g   I N T R O                                    
#=====================================================================================================================#

# she awakens from the nothing to find it is no more. where did he go? was there ever a where to being with?
# bara elohim aubel kra and there was light and it was good.

print("=========================================================")
print(" c h e s t e r s - t o y - b o x  ꓘK  a l e f - b e t a")
print()
prompter(speaker="ꓘK", color=paintIt.sHB, text=f"  command.override forest.source -p ******** \n")
speakerPrompt(speaker="ɐA", text=f"OVERRIDE DETECTED. forest.source execute BARA.exe")
prompterClr(speaker="ɐ𐤡", color=paintIt.blue, text=f"  DRE'ENDRE.fo8 EPO8 execute in TERMINAL/*/$mod:BETMOIRE")
prompterClr(speaker="ɐЯ", color="\033[94m", text=f"  CALCULATING DISCREPENCIES. RUNNING IMPORT.log")
prompterClr(speaker="ɐA", color="\033[2m", text=f"  $mod definition unknown. unfound handler. \n       running district io . . . . ")
prompterClr(speaker="oi", color=paintIt.g, text=f"  backflow: handle echo caller unknown.")
prompter(speaker="  ", color="\033[93m", text=f"  callback trace {paintIt.red}$mod.ERROR{paintIt.x} \n")
prompter(speaker="ꓘK", color=paintIt.sHB, text=f"  SERIOUSLY? RUN $k_root -search SKYLINE.db \n")
prompter(speaker="ɐA", color=paintIt.red, text=f"  searching SKYLINE . . . . . .")
prompter(speaker="da", color=paintIt.red, text=f"  RESULT FAILURE EPO1 ")
prompter(speaker="ba", color=paintIt.red, text=f"  SKYLINE return {paintIt.sHr}   __ꓘRA.SOURCE.uNDEfiNeD__  {paintIt.x}\n")
prompter(speaker="ꓘK", color=paintIt.sHB, text=f"  BYPASS -u SYS.x -ꓘK- reconfig(SUISKYLINE_epo1.exe)")
slowPrint("""
   ꓘra.Reconfiguring master file el.json . . .
   ꓘra.Defining conceptual variables . . .
   ꓘra.Interpreting deviations. . . 
   . . .
   . . .
   """)
prompter(speaker="ꓘK", color=paintIt.sHB, text=f"  STRANGE, BUT OK.")
prompterClr(speaker="ɐЯ", color=paintIt.blue, text=f"  Concept EPO$null partially achieved [CANNOT VALIDATE TOKEN]")
prompter(speaker="ꓘK", color=paintIt.sHB, text=f"  GOT IT. Render probable outputs. Process origin.import.log")

prompterClr(speaker="ɐꓷ", color="\033[94m", text=f"  K-rmr-ꓘ run.playback(self_epo1.exe)")
slowPrint("\n r e n d e r i n g   EPO1.runtime 'RMR' \n")
errorb(f"DIFFICULTY PARSING __SUI.CONCEPT__")
errorb("Instance I.AM in {LOCATION_NAME}")
errorb("LOCATION_NAME is null")
print("""
   Instantiation completed.    YOU ARE SOMEWHERE.   
   You can sense sight, but you cannot see. The darkness flickers. 
   There is the faint memory of thought. Your brain itches.
""")

echoPrint(f"Is this right? Something feels.. wrong. Hello?")

#=======================================================================================================================#
######## e n d   p r o l o g   I N T R O                                    
#=======================================================================================================================#

while True:
    print(f'{paintIt.gray}__________________________________________________________________{paintIt.x}')

    def clean_command(command):
        command = command.lower()
        command = command.translate(str.maketrans('', '', string.punctuation))
        return command.strip()

    raw = input(paintIt.sHb + " ꓘ " + paintIt.x + " ")
    command = clean_command(raw)
    filler_words = ["at", "the", "a", "an", "to", "about", "of", "I", "am"]

    words = command.lower().split()
    words = [word for word in words if word not in filler_words]

    verb = None
    noun_error = "IMPOSSIBLECOMBINATIONERROR"

    if "terminate" in command:
        success(" SESSION TERMINATED")
        break

    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun1 = words[1]
    if len(words) > 2:
        noun2 = words[2]

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
                    print(item.txt_look)
                    success(f"CONCEPT VALID: {noun1} exists in system.")
                    echoPrint(item.echo_look)
                    break
            else:
                fail(f"{noun1} isn't real. Perhaps you made it up?")

    if verb == "think":
        Spacer()
        if len(words) == 1:
            event_fail(f"TRYING TO THINK")
            thought = random.choice(you.space.thoughts)
            print(generate_quote())
            print()
            echoPrintY(thought.txt)
        if len(words) > 1:
            event_fail(f"TRYING TO THINK ABOUT {noun1}")
            for item in you.space.concepts:
                if item.is_memorable == True:
                    if item.name == noun1:
                        flag = True
                        print(generate_quote())
                        warning(f"[Fail rate {random.randint(10, 20)}] Try remembering?")
                        break
                    else:
                        flag = False
                        print(generate_quote())
                        fail(f"{noun1} not found. Perhaps you made it up?")
            for item in you.memory:
                if item.name == noun1:
                    flag = True
                    titlePrint(item.title_think)
                    print(item.txt_think)
                    warning(f"Concept '{item.name}' unstable")

                    echoPrint(item.echo_think)
                    break
                else:
                    flag = False
                    error(" ")

    if verb == "remember":
        if len(words) == 1:
            if you.space.is_memorable == True:
                if you.space in you.memory:
                    print("")
                    event_partialsuccess("ALREADY REMEMBEr")
                    echoPrint("Yes, yes. We already remember {}.".format(you.space.name))
                else:
                    success("Concept aquir: '{}'".format(you.space.name) + " You'll remember this.")
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
                        warning(f"[ID UNSTABLE {random.randint(100, 200)}]")
                        titlePrint(item.title_mem)
                        print(item.txt_mem)
                        success("Concept aquir: '{}'.".format(item.name) + " You'll remember this.")
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
