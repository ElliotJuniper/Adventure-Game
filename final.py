import sys
import random
import time
import os

def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(0.04)
            else:
                time.sleep(1)
os.system("clear") #clear

def puzzle():  
    typewriter("""\n 
    Welcome to the tower...

    You look up and see a window on the side 
    of the tower that is to high, but with a 
    grappling hook and some rope you might be 
    able to reach the window and enter the tower. 
    you head over to the area below the tower to explore, 
    you notice a stone bench and walk over to examine it. 
    There is a key hole right in the middle 
    of the seat and a note on the bench.""") 

    answer = input("""\n
    Do you read the note?\n
>>>    \n""")
    if answer == "yes".lower():
        typewriter("""\n
    The note reads I know what you need, 
    answer this riddle to find what fits in the middle. 
    A box without hinges, key, or lid, 
    Yet golden treasure inside is hid.""") 
        answer = input("""
        What is the answer?\n
>>>   """)
    
        if answer == "egg".lower():
            typewriter("""\n
    Well done now where would you find an egg?
    In a distant tree you see a bird box 
    hanging from a branch, you make your and examine it.
    Inside you find a key. 
    you take the key over to the bench and into the keyhole. 
    you hear a click and a compartment opens and inside the 
    compartment you find a grappleing hook and rope.\n
            """)
            answer = input("""
    Would you like to use the hook?\n
>>>  """)
            if answer == "yes".lower():
                typewriter("""\n
    You swing the hook and with a mighty toss it catches on the window.
    You climb and climb, making sure no one can see. 
    One last pull off the ledge of the stoned window.
    Congratulations you made it into the citadel.""")        
            elif answer == "no".lower():
                typewriter("""\n
    You hear a large growl and turn round to see a 
    large bear running towards you, with one hit 
    the bear snaps your neck. 
    *************
    You are dead!
    *************\n""")
                sys.exit()
            else:
                typewriter("""\n
    Learn to spell this isn't a childrens game.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        else:
            typewriter("""
    You unfortunately slip on a banana.
    *************
    You are dead!
    *************""")
            sys.exit()

    elif answer == "no".lower():
        typewriter("""
    You dismiss the note and keep walking forward not 
    paying attention to your surroundings. 
    You fall in a spike pit and impale yourself. 
    *************
    You are dead!
    *************""")
        sys.exit()
        
    else:
        typewriter("""
    .................
    Invalid response!
    .................""")
        return puzzle()




health = 20
enemy_health = 20
def combat():
    global health, enemy_health
    while health > 0 and enemy_health > 0:
        attack = input("""
    Choose attack type. Heavy or Light\n
>>>   """)
        if attack.lower() == "heavy" or attack.lower() == "h":
            hit = random.randint(1,10)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            enemy_health -= hit 
        elif attack.lower() == "light" or attack.lower() == "l":
            hit = random.randint(3,5)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            enemy_health -= hit
        else:
            typewriter("""
    ....................
    Invalid Attack Type!\n
    ....................""")
            return combat()
        if enemy_health <= 0:
            typewriter("""
    $$$$$$$$$$$$$$$
    Enemy Defeated!
    $$$$$$$$$$$$$$$""")
            break # Just using that to exist the loop
        # Enemy's go
        enemy_hit = random.randint(2,5)
        typewriter(f"""
    The enemy hits you for {enemy_hit}""")
        health -= enemy_hit
        if health <=0:
            typewriter("""
    *************
    You are dead!
    *************""")
            sys.exit()
        #     break # Exiting the loop again        

vhealth = 400
vboss = 1000
def boss():
    global vhealth, vboss
    while vhealth > 0 and vboss > 0:
        attack = input("""
    Choose attack type. Heavy or Light\n
>>>   """)
        if attack.lower() == "heavy" or attack.lower() == "h":
            hit = random.randint(50,200)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            vboss -= hit 
        elif attack.lower() == "light" or attack.lower() == "l":
            hit = random.randint(80,110)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            vboss -= hit
        else:
            typewriter("""
    ....................
    Invalid Attack Type!
    ....................""")
            return boss()
        if vboss <= 0:
            typewriter("""
    $$$$$$$$$$$$$$$
    Enemy Defeated!
    $$$$$$$$$$$$$$$""")
            break # Just using that to exist the loop
        # Enemy's go
        enemy_hit = random.randint(20,70)
        typewriter(f"""
    The enemy hits you for {enemy_hit}""")
        vhealth -= enemy_hit
        if vhealth <=0:
            typewriter("""
    *************
    You are dead!
    *************""")
            sys.exit()
        #     break # Exiting the loop again          
        
mhealth = 25
vguard = 30
def guard():
    global mhealth, vguard
    while mhealth > 0 and vguard > 0:
        attack = input("""
    Choose attack type. Heavy or Light\n
>>>   """)
        if attack.lower() == "heavy" or attack.lower() == "h":
            hit = random.randint(1,10)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            vguard -= hit 
        elif attack.lower() == "light" or attack.lower() == "l":
            hit = random.randint(4,6)
            typewriter(f"""
    You hit the enemy for {hit}.""")
            vguard -= hit
        else:
            typewriter("""
    ....................
    Invalid Attack Type!
    ....................""")
            return guard()
        if vguard <= 0:
            typewriter("""
    $$$$$$$$$$$$$$$
    Enemy Defeated!
    $$$$$$$$$$$$$$$""")
            break # Just using that to exist the loop
        # Enemy's go
        enemy_hit = random.randint(3,5)
        typewriter(f"""
    The enemy hits you for {enemy_hit}""")
        mhealth -= enemy_hit
        if mhealth <=0:
            typewriter("""
    *************
    You are dead!
    *************""")
            sys.exit()
        #     break # Exiting the loop again          

def warrior():
    # if character.lower().strip() == "warrior" 
                
    global combat, vboss, guard
    answer = input("""
    Welcome Warrior, which route will you choose: 
            1 - Dark Forest

            2 - Lava Geyser's

            3 - Murky Swamp\n
>>>   """).lower().strip()

    if  answer == "1":
        print(r"""   
   ad88                                                  
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  
  
  \n""")
        typewriter("""
    Welcome to the Dark Forest Warrior.
    As you make your way through the darkness
    you glimpse at two piecing red dots staring
    right at you. 
    It charges for an attack out of the shadows. 
    it's a lesser demon!\n""")
        combat()            
        typewriter("""
    Well done, you have slain the enemy. 
    Take this brigadier claymore as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
      
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n

 """)
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
                
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()        
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
                                        
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
            
            
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()

        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
        
    

    elif answer == "2":
        print("""
                        (   (( . : (    .)   ) :  )
                          (   ( :  .  :    :  )  ))
                           ( ( ( (  .  :  . . ) )
                            ( ( : :  :  )   )  )
                             ( :(   .   .  ) .'
                              '. :(   :    )
                                (   :  . )  )
                                 ')   :   #@##
                                #',### " #@  #@
                               #/ @'#~@#~/\   #
                             ##  @@# @##@  `..@,
                           @#/  #@#   _##     `\\
                         @##;  `#~._.' ##@      \_
                       .-#/           @#@#@--,_,--\\
                      / `@#@..,     .~###'         `~.
                    _/         `-.-' #@####@          \\
                 __/     &^^       ^#^##~##&&&   %     \_
                /       && ^^      @#^##@#%%#@&&&&  ^    \\
              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._
           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     \\
          /akg ^^^ ___&&& X & && |n|   ^ ___ %____&& . ^^^^^   `~.
                   |M|       ---- .  ___.|n| /\___\  X
                             |mm| X  |n|X    ||___|   \n""")
        typewriter("""
    Welcome to the Lave Geyser's Warrior.
    You carefully walk along the scorching hot plains,
    Anticipating a sudden fiery geyser erupting from the ground.
    BOOOOOM!
    You turn your head in a whiplashed motion and your eyes pivot to the sky.
    40, no 50 meters high a geyser sprouts and
    the fire seems to lock on you.
    A Fire Elemental rushes!
    """)
        combat()    
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Solomons Rapier as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n

    """)
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open. """)
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
                
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
                ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
            
        elif  choice == "3":
            puzzle()
            typewriter("""
    You have made your way to the final boss.
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
            
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
    



    elif answer == "3":
        print(r""" 
,adPPYba, 8b      db      d8 ,adPPYYba, 88,dPYba,,adPYba,  8b,dPPYba,   
I8[    "" `8b    d88b    d8' ""     `Y8 88P'   "88"    "8a 88P'    "8a  
 `"Y8ba,   `8b  d8'`8b  d8'  ,adPPPPP88 88      88      88 88       d8  
aa    ]8I   `8bd8'  `8bd8'   88,    ,88 88      88      88 88b,   ,a8"  
`"YbbdP"'     YP      YP     `"8bbdP"Y8 88      88      88 88`YbbdP"'   
                                                           88           
                                                           88           
        \n""")
        typewriter("""
    Welcome to the Murky Swamp Warrior.
    With each step through the abysall looking waters
    your boots get heavier as they become more saturated
    from the tainted aqua pura.
    Suddenly! 
    A creature pulls you down to your knees where only 
    your head lay above the water.
    You riggle and squirm your way out of if it's grip and as
    you break free it rises soaked to it's core.
    It's a Swamp Treant!
    \n""") 
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Goliath Spear as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n
""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
                
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
            
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
    
    else:
        typewriter("""
    This is not a bug, you just can't
    count to 3\n
    *************
    You are dead!
    *************
    """)
        sys.exit()
# warrior()



def mage():
    # if character.lower().strip() == "mage":
    global combat, vboss, guard
    answer = input("""
    Welcome mage, which route will you choose: 
            1 - Dark Forest

            2 - Lava Geyser's
            
            3 - Murky Swamp\n
>>>   """).lower().strip()
    if answer == "1":
        print(r"""   
   ad88                                                  
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  
  
  \n""")
        typewriter("""
    Welcome to the Dark Forest Mage.
    As you make your way through the darkness
    you glimpse at two piecing red dots staring
    right at you. 
    It charges for an attack out of the shadows. 
    it's a lesser demon!\n""")
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Staff of Despair as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter("""
    You have made your way to the final boss.
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()    

    elif answer == "2":
        print("""
                        (   (( . : (    .)   ) :  )
                          (   ( :  .  :    :  )  ))
                           ( ( ( (  .  :  . . ) )
                            ( ( : :  :  )   )  )
                             ( :(   .   .  ) .'
                              '. :(   :    )
                                (   :  . )  )
                                 ')   :   #@##
                                #',### " #@  #@
                               #/ @'#~@#~/\   #
                             ##  @@# @##@  `..@,
                           @#/  #@#   _##     `\\
                         @##;  `#~._.' ##@      \_
                       .-#/           @#@#@--,_,--\\
                      / `@#@..,     .~###'         `~.
                    _/         `-.-' #@####@          \\
                 __/     &^^       ^#^##~##&&&   %     \_
                /       && ^^      @#^##@#%%#@&&&&  ^    \\
              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._
           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     \\
          /akg ^^^ ___&&& X & && |n|   ^ ___ %____&& . ^^^^^   `~.
                   |M|       ---- .  ___.|n| /\___\  X
                             |mm| X  |n|X    ||___|   \n""")
        typewriter("""
    Welcome to the Lave Geyser's Mage.
    You carefully walk along the scorching hot plains,
    Anticipating a sudden fiery geyser erupting from the ground.
    BOOOOOM!
    You turn your head in a whiplashed motion and your eyes pivot to the sky.
    40, no 50 meters high a geyser sprouts and
    the fire seems to lock on you.
    A Fire Elemental rushes!
    """)
        combat()    
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Starfire Tiara as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n  """)
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()

    elif answer == "3":
        print(r""" 
,adPPYba, 8b      db      d8 ,adPPYYba, 88,dPYba,,adPYba,  8b,dPPYba,   
I8[    "" `8b    d88b    d8' ""     `Y8 88P'   "88"    "8a 88P'    "8a  
 `"Y8ba,   `8b  d8'`8b  d8'  ,adPPPPP88 88      88      88 88       d8  
aa    ]8I   `8bd8'  `8bd8'   88,    ,88 88      88      88 88b,   ,a8"  
`"YbbdP"'     YP      YP     `"8bbdP"Y8 88      88      88 88`YbbdP"'   
                                                           88           
                                                           88           
        \n""")
        typewriter("""
    Welcome to the Murky Swamp Mage.
    With each step through the abysall looking waters
    your boots get heavier as they become more saturated
    from the tainted aqua pura.
    Suddenly! 
    A creature pulls you down to your knees where only 
    your head lay above the water.
    You riggle and squirm your way out of if it's grip and as
    you break free it rises soaked to it's core.
    It's a Swamp Treant!
    \n""") 
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Merlin's Sceptre as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
    else:
        typewriter("""
    This is not a bug, you just can't
    count to 3\n
    *************
    You are dead!
    *************
    """)
        sys.exit()


def shapeshifter():
    global combat, vboss, guard
    answer = input("""
    Welcome shapeshifter, which route will you choose: 
            1 - Dark Forest

            2 - Lava Geyser's
            
            3 - Murky Swamp\n
>>>   """).lower().strip()
    if answer == "1":
        print(r"""   
   ad88                                                  
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  
  
  \n""")
        typewriter("""
    Welcome to the Dark Forest Shapeshifter.
    As you make your way through the darkness
    you glimpse at two piecing red dots staring
    right at you. 
    It charges for an attack out of the shadows. 
    it's a lesser demon!\n""")
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Nightmare Talisman as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()


    elif answer == "2":
        print("""
                        (   (( . : (    .)   ) :  )
                          (   ( :  .  :    :  )  ))
                           ( ( ( (  .  :  . . ) )
                            ( ( : :  :  )   )  )
                             ( :(   .   .  ) .'
                              '. :(   :    )
                                (   :  . )  )
                                 ')   :   #@##
                                #',### " #@  #@
                               #/ @'#~@#~/\   #
                             ##  @@# @##@  `..@,
                           @#/  #@#   _##     `\\
                         @##;  `#~._.' ##@      \_
                       .-#/           @#@#@--,_,--\\
                      / `@#@..,     .~###'         `~.
                    _/         `-.-' #@####@          \\
                 __/     &^^       ^#^##~##&&&   %     \_
                /       && ^^      @#^##@#%%#@&&&&  ^    \\
              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._
           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     \\
          /akg ^^^ ___&&& X & && |n|   ^ ___ %____&& . ^^^^^   `~.
                   |M|       ---- .  ___.|n| /\___\  X
                             |mm| X  |n|X    ||___|   \n""")
        typewriter("""
    Welcome to the Lave Geyser's Shapeshifter.
    You carefully walk along the scorching hot plains,
    Anticipating a sudden fiery geyser erupting from the ground.
    BOOOOOM!
    You turn your head in a whiplashed motion and your eyes pivot to the sky.
    40, no 50 meters high a geyser sprouts and
    the fire seems to lock on you.
    A Fire Elemental rushes!
    """)
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Godfrey's Talisman as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()

    elif answer == "3":
        print(r""" 
,adPPYba, 8b      db      d8 ,adPPYYba, 88,dPYba,,adPYba,  8b,dPPYba,   
I8[    "" `8b    d88b    d8' ""     `Y8 88P'   "88"    "8a 88P'    "8a  
 `"Y8ba,   `8b  d8'`8b  d8'  ,adPPPPP88 88      88      88 88       d8  
aa    ]8I   `8bd8'  `8bd8'   88,    ,88 88      88      88 88b,   ,a8"  
`"YbbdP"'     YP      YP     `"8bbdP"Y8 88      88      88 88`YbbdP"'   
                                                           88           
                                                           88           
        \n""")
        typewriter("""
    Welcome to the Murky Swamp Shapeshifter.
    With each step through the abysall looking waters
    your boots get heavier as they become more saturated
    from the tainted aqua pura.
    Suddenly! 
    A creature pulls you down to your knees where only 
    your head lay above the water.
    You riggle and squirm your way out of if it's grip and as
    you break free it rises soaked to it's core.
    It's a Swamp Treant!
    \n""") 
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Dragonborn Talisman as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
    else:
        typewriter("""
    This is not a bug, you just can't
    count to 3\n
    *************
    You are dead!
    *************
    """)
        sys.exit()


def assassin():
    global combat, vboss, guard
    answer = input("""
    Welcome assassin, which route will you choose: 
            1 - Dark Forest

            2 - Lava Geyser's
            
            3 - Murky Swamp\n
>>>   """).lower().strip()
    if answer == "1":
        print(r"""   
   ad88                                                  
  d8"                                                ,d     
  88                                                 88     
MM88MMM ,adPPYba,  8b,dPPYba,  ,adPPYba, ,adPPYba, MM88MMM  
  88   a8"     "8a 88P'   "Y8 a8P_____88 I8[    ""   88     
  88   8b       d8 88         8PP"""""""  `"Y8ba,    88     
  88   "8a,   ,a8" 88         "8b,   ,aa aa    ]8I   88,    
  88    `"YbbdP"'  88          `"Ybbd8"' `"YbbdP"'   "Y888  
  
  \n""")
        typewriter("""
    Welcome to the Dark Forest Assassin.
    As you make your way through the darkness
    you glimpse at two piecing red dots staring
    right at you. 
    It charges for an attack out of the shadows. 
    it's a lesser demon!\n""")
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Elven Longbow as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n  """)
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-
"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()

    elif answer == "2":
        print("""
                        (   (( . : (    .)   ) :  )
                          (   ( :  .  :    :  )  ))
                           ( ( ( (  .  :  . . ) )
                            ( ( : :  :  )   )  )
                             ( :(   .   .  ) .'
                              '. :(   :    )
                                (   :  . )  )
                                 ')   :   #@##
                                #',### " #@  #@
                               #/ @'#~@#~/\   #
                             ##  @@# @##@  `..@,
                           @#/  #@#   _##     `\\
                         @##;  `#~._.' ##@      \_
                       .-#/           @#@#@--,_,--\\
                      / `@#@..,     .~###'         `~.
                    _/         `-.-' #@####@          \\
                 __/     &^^       ^#^##~##&&&   %     \_
                /       && ^^      @#^##@#%%#@&&&&  ^    \\
              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._
           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     \\
          /akg ^^^ ___&&& X & && |n|   ^ ___ %____&& . ^^^^^   `~.
                   |M|       ---- .  ___.|n| /\___\  X
                             |mm| X  |n|X    ||___|   \n""")
        typewriter("""
    Welcome to the Lave Geyser's Assassin.
    You carefully walk along the scorching hot plains,
    Anticipating a sudden fiery geyser erupting from the ground.
    BOOOOOM!
    You turn your head in a whiplashed motion and your eyes pivot to the sky.
    40, no 50 meters high a geyser sprouts and
    the fire seems to lock on you.
    A Fire Elemental rushes!
    """)
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Eaglewing Crossbow as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
    elif answer == "3":
        print(r""" 
,adPPYba, 8b      db      d8 ,adPPYYba, 88,dPYba,,adPYba,  8b,dPPYba,   
I8[    "" `8b    d88b    d8' ""     `Y8 88P'   "88"    "8a 88P'    "8a  
 `"Y8ba,   `8b  d8'`8b  d8'  ,adPPPPP88 88      88      88 88       d8  
aa    ]8I   `8bd8'  `8bd8'   88,    ,88 88      88      88 88b,   ,a8"  
`"YbbdP"'     YP      YP     `"8bbdP"Y8 88      88      88 88`YbbdP"'   
                                                           88           
                                                           88           
        \n""")
        typewriter("""
    Welcome to the Murky Swamp Assassin.
    With each step through the abysall looking waters
    your boots get heavier as they become more saturated
    from the tainted aqua pura.
    Suddenly! 
    A creature pulls you down to your knees where only 
    your head lay above the water.
    You riggle and squirm your way out of if it's grip and as
    you break free it rises soaked to it's core.
    It's a Swamp Treant!
    \n""") 
        combat()
        typewriter("""
    Well done, you have slain the enemy. 
    Take this Phoenix Bow as a reward.

    You walk with purpose for hours on end.
    Finally you reach the citadel.""")

        choice = input("""
    Which route will you choose:
            1 - Captured, to break out.

            2 - Charge the front gate.

            3 - Climb the tower.\n
>>>\n """)
        if  choice == "1":
            typewriter("""
    It cannot be seen, cannot be felt, Cannot be heard, 
    cannot be smelt It lies behind stars and under hills, 
    And empty holes it fills. It comes out first and follows 
    after,Ends life, kills laughter.\n""")
            answer = input("""
    What am I?\n
>>>   """)
            if answer == "dark":
                typewriter("""
    Congratulations you guessed correct. 
    The cell door swings open.""")
            else:
                typewriter("""
    You guessed wrong and die from starvation!
    *************
    You are dead!
    *************\n""")
                sys.exit()
            typewriter("""
    You sprint to the grand palace entrance 
    and swing the doors open.""") 
    
            choice = input("""
    Do you advance?\n
>>>   """)
            if choice == "yes":
                typewriter(r"""
    You have made your way to the final boss.""")
                print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
                boss()
                typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
                sys.exit()
            else:
                typewriter("""
    You become petrified at the
    thought of fighting a colossal demon.
    *************
    You are dead!
    *************\n""")
                sys.exit()
        elif  choice == "2":
            typewriter("""
    You charge at the demon guard
    watching the front gate.\n""")
            guard()
            typewriter(r"""
    You manage to defeat the guard with 
    blood dripping from your face,
    not knowing who's it is.
    You push the front gates open 
    and make your way.
    
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")
            sys.exit()
        elif  choice == "3":
            puzzle()
            typewriter(r"""
    You have made your way to the final boss.""")
            print(r"""
            ^\\
           )\_
           |':";=,-`;,._
            \\         "._
 ^\         //            ";=,-._      ^\\
  )\-._    ||         ;"._      "=.     )\\
  //  ";=,-.\      ^\    ".       "`~,_.;/._
 ||         "=.     )\    ";-._,`~;._      ".
 \\           "`~,_.;/_                     ";,
  ||                  ".      ;"-._          "=._
  ||                   ";,        "-,           ";-,_
  //    ;"-._            "=.        ";:=.-,_         ";-._           ^\\
 //         "-,            ";-,_           ":=;-,_.-";._ ";-._        )\\
 \\           ";:=.-,_          ";-._    ^\            ";=._  "`~,;,_.'/
  \\                 ":=;-,_.-";._  ";="._)\               ";,-`~";=-.\\
   \\    "=.,_.;=._              ";=._   ";/                          //
    ||            ";:=,-'"=._             \\      _..-======-.._     //
    ||                      "`~.-=;",_."-. \\   .-              -.  //
    \\                                  _,.-\\"/.=._          _.=.\ ||
     \\  ;"~`._                      _.;"     /     =-.    .-=     \//
      \\      ";=,-`~._           _."        |   ,"="'.\  /,"="'.   |".,
       \\              ";=-.__,.-="":.        |  '.--.'|!!|'.--.'  |   ",`
        ||                _."          _.,"-=, '.      )!!(      .'      ;`.
        ||           _."=:".         _.'-."-=". ".    /-!!-\    ."       ";.
        \\    _.--==:;".    ".      .-":_:'" ". |'.   \U::U/   .'|       "-_
        _\\=:"=".       ".         -"_.-= `~;", \ /\_.-====-._/\ /        :,
     .'".'=\,.   ".                .'.'       ", ||  \/\/\/\/  ||         ,"
   .'         ".                   ".'            \\/\/\/\/\/\//           `,
  .'                              ".'            ;.\.=-.__.-=./           ."
 .'                              ;."            ,_: '-......-'";           ;
.'                               ;."           ,-"            :.          ;,
/.            ;.                 ;."          ,-=             ."_          )
.\             \                 ;."          ,"               ;.        _."
".              |                ;."          ,"             ,;         ,-;
";              |                ,;`          ,"       ,_;  ,"         ~,"
\,"             |                .,"          ,"      _.;'-=/          ;
 "_-            |                .,"          ,-:,.-=" ,-=:"         ."
 ,-:           /             _,.-=";          ;,      /_)\        _.=.
 ,;           |           _.-"     ;,         ".       _ /~";.:;="',;
 ,;           |=".-_,:;'-,"        ;.         ;,      ( / // // // /
  \           \|      ,;.          ",         '.       \_// // // /
  |           \         ".         /          ,;       ( / // /\_/
   |          ,;.         \       |;,`~ ;,'"-.L'        \_/\_/
  ,"             ". ,":.`~.\      .`.,' ;=.';. ".
  ;      -.=,":.`~.\\ \\ \\ \      "., ; = - `~\ \\
  `.==--._ \\ \\ \\ \".`./;./       ". \\ \\ \\ \ \\
          \,\\ \\ \\ \(_/(_/         ". \\ \\ \\ \/
          (_/"./`,/;./                `,.\\ \\ \\,\\
            (_/(_/(_/                  '., \ \\ \`.'    
                                           `." `.'
    ++++++++++++++++++
    Demon Lord Malkar!
    ++++++++++++++++++\n""")
            boss()
            typewriter("""
    You have vanquished the demon lord
    Truly, you are the
    |\/|\/|\/|\/|\/|\/|\/|\/|\/|
    *********** HERO ***********
    |/\|/\|/\|/\|/\|/\|/\|/\|/\|\n""")

            sys.exit()
        else:
                typewriter("""
    I said 1, 2 or 3. it's not that difficult... 
    *************
    You are dead!
    *************\n""")
                sys.exit()
    else:
        typewriter("""
    This is not a bug, you just can't
    count to 3\n
    *************
    You are dead!
    *************
    """)
        sys.exit()
       
print("""
Sorka's Vale was a land of beauty and mystery. 
Adventurers would come from the furthest lands 
to barter, settle and explore what this fruitful land had to offer. 
200 years of peace and prosperity until, the Malkroths came. 
A species of fierce demons that would seek to only destroy and conquer. 
3 years of endless battling took a toll on both sides, but thanks 
to the heroes summoning which can come about every 100 years in times of great need, 
the humans were able to push them back to the darkness forever. 
So they thought...

After the evil was defeated the hero was sent back to the spirit realm, to rest, 
waiting until the time comes when they need him the most. 
The people of Sorka's Vale had to rally up the few people they 
had left to help rebuild the city and forget about this tragic event. 

In the year 104PC (Post Calamity), the Malkroths have been 
slowly creeping out of the darkness into Sorka's Vale. 
The magic academy and warriors guild have been trying to 
stop there forces from entering the citadel but it's no use. 
The malkroths break down the towering steel door into the capital and swarm, 
forcing the people to leave and take refuge, 
hoping the Hero will come save them once again.

""")
def character_selection():
    
    response = input("""
    Who would you like to play as?\n
            a - Warrior\n
            b - Mage\n
            c - shapeshifter\n
            d - assassin\n
>>>\n   """)

    if response.upper() == "A":
        return warrior()
    elif response.upper() == "B":
        return mage()
    elif response.upper() == "C":
        return shapeshifter()
    elif response.upper() == "D":
        return assassin()
    else:
        return character_selection()
    # for character in response:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.02)
character_selection()