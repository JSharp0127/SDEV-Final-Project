"""
Author: John Sharp
File: Character_Sheet.py

This module holds many of the backend functions for the main program, such as saveing, loading, making stat changes, and choosing the correct character features.

"""


import json #used to save character sheets
import random #used for dice rolls



#Charcter stats are brought in and converted into a dictionary then sent to Save_Character

def Player_Sheet(name, race, player_Class, player_hp, level, str_Stat, dex_Stat, con_Stat, int_Stat, win_Stat, cha_Stat):

    global character_sheet
    character_sheet = {"Name": name, "Race": race, "Class": player_Class, "Str": str_Stat, "Dex": dex_Stat, "Con": con_Stat, "Int": int_Stat, "Wis": win_Stat, "Cha": cha_Stat,
                      "HP": player_hp, "Level": level}
    #print(character_sheet)
    Save_Character(name)
    
#Brings in the rolled stat value and returns the modifier

def MODIFIER(roll):
    mod = -5
    for count in range(1,30,2):
        if roll == count or roll == count - 1:
            #print(type(mod))
            return mod
        mod +=1

#Brings in class for hit die, con_mod, and level then returns hit point value
        
def HIT_POINTS(player_class, con_mod = None, level = None, race = None):
    class_dict = {"Barbarian": 12, "Bard": 8, "Cleric": 8, "Druid": 8, "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 10, "Rogue": 8, "Sorcerer": 6, "Warlock": 8, "Wizard": 6}
    
    #Separate class_dict into 2 lists (class_select and hit_dice)

    class_select = []
    hit_dice  = []
    x = -1
    for i in class_dict:
        class_select.append(i)
        hit_dice.append(class_dict[i])
    
    #Cylce through class_selection until it equals the players chosen class.         

    for selection in class_select:
        x += 1 #records current position in class_selection
        if player_class == selection:
            roll_total = 0
            
            #count up to the players level and roll a number  between 1 and the hit_dice that matches class_selection    
    
            for count in range(level):
                roll = random.randint(1,hit_dice[x])
                roll_total = roll + roll_total
                count+=1
    hp = roll_total + (con_mod * level) 
    if player_class == "Sorcerer":
        hp = hp + (level * 1)
    if race == "Dwarf":
        hp = hp + (level * 1)
    
    return hp

#Brings in dex_mod and returns armor class (Barbarian and Monk also bring in con_mod or wis_mod)
        
def  ARMOR_CLASS(dex= None,player_class = None, con = None, wis = None, level = None):
    player_ac = 10 + dex
    if player_class == "Barbarian":
        player_ac += con
    if player_class == "Monk":
        player_ac += wis
    if player_class == "Sorcerer":
        player_ac += 3
    if player_class == "Paladin" and (level == '2' or level == '3'):
        player_ac += 1
    return player_ac

#Character save and LOAD_CHARACTER

def Save_Character(file_name):
    with open(file_name + ".json", 'w') as f:
        json.dump(character_sheet, f)
        
def LOAD_CHARACTER(file_name):
    with open(file_name + ".json", 'r') as f:
        loaded_sheet = json.load(f)
        f.close()
        return loaded_sheet
    

#Character Features (Race/Class)
#Specail Race and Class abilities and features given based on  player choices

def CHARACTER_FEAT(player_race = None, player_class = None, player_background = None, level = None, spell_mod = None ):
    
    r_feat = "" #race features
    c_feat = "" #class features
    
    #Player chosen race features
    
    #Dwarf

    if player_race == "Dwarf":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Dwarven Resilence: Advantage on saving throws against\n poison, and resistance against poison in combat.\n" + 
                  "Dwaven Combat Training: Proficiency with\nbattleaxe, handaxe, light hammer and warhammer\n" + 
                  "Tool Proficiency: Proficency with smith's tools, brewer's supplues, or mason's tools.\n" + 
                  "Stonecunning: Proficiency x2 for history checks related to \nstone work\n" + "Languages: Common, Dwarvish\n" + 
                  "Sub Race: Hill Dwarf\n")
        
    #Elf
     
    if player_race == "Elf":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Keen Senses: Profiency in Perception skill.\n" + 
                  "Fey Ancestry: Advantage on saving throws against\n being charmed, and magic cant put you to sleep\n"+ 
                  "Trance: You don't sleep but instead go into a trance for 4 hours\n gaining the benifits of 8 hours  rest\n" + 
                  "Languages: Common, Elvish\n"+ "Subrace: High Elf\n" + 
                  "Elf Weapon Training: Proficiency with longswords, shortbows,\n shortswords, and longbows.\n" + 
                  "Cantrip: You know the firebolt (1d10) cantrip\n INT is your spellcasting ability.\n"+ 
                  "Extra Language: You can speak and read Celestrial\n")
     
    #Halfling
        
    if player_race == "Halfling":
        r_feat = ("Lucky: When you roll a 1 on an attack, ability, or saving roll\n you can reroll the die and must keep the new roll\n" + 
                  "Brave: Advantage on saveing throws against being frieghtened.\n" + 
                  "Halfling Nimbleness: You can move through the \nspace of any creature that is a size larger than you\n" + 
                  "Languages: Common and Halfling.\n"+ 
                  "Subrace: Lightfoot\n" + 
                  "Naturally Stealthy: You can hide \neven when being obscured by a creature larger then you.\n")
        
    #Human
        
    if player_race == "Human":
        r_feat = "Languages: Common and Dwarvish or Elvish.\n"
        
    #Gnome
        
    if player_race == "Gnome":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Gnome Cunning: Advantage on INT, WIS, and CHA \nsaving throws against magic\n" + 
                  "Languages: Common and Gnomish\n" + 
                  "Subrace: Rock Gnome\n" + "Artificer's Lore: Profiency x2 for history checks\non magic items,  alchemical objects, or technological devices.\n" + 
                  "Tinker: Using Tinker's Tools spending 1 hour and 10g:\nTiny Clockwork Device\nAC:5\nHp:1\nCan have up to 3 at a time.\nChoose one of the following:\n" + 
                  "Clockwork Toy: A small clockwork animal, dragon or soldier.\nWhen placed on the ground, the toy moves 5 feet\nin a random direction per turn.\nIt makes noise.\n" + 
                  "Fire Starter: Device produces a miniture flame which can light\ncandles, campfires, or torches.\n" + 
                  "Music Box: Plays a song while open and stops when closed or done playing.\n")
        
    #Half-Elf
        
    if player_race == "Half-Elf":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Fey Ancestry: Advantage on saving throws against\n being charmed, and magic cant put you to sleep\n" + 
                  "Languages: Common, Elvish\n")
        
    #Half-Orc
        
    if player_race == "Half-Orc":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Menacing: Proficiency with Intimidation skill.\n" + 
                  "Relentless Endurance: When you would be dropped to 0 hit points\nbut not outright killed, you instead drop to 1 hitpoint.\nYou can only use this\nfeature once a long rest.\n" +
                  "Savage Attacks: When you score a critical hit with a melee\nweapon  attack, you can roll once of the weapon's damage\ndice one additiional time and add it to the\nextra damage of the critical hit.\n" + 
                  "Languages: Common and Orc.\n")
        
    #Tiefling
        
    if player_race == "Tiefling":
        r_feat = ("Darkvision: 60ft\n" + 
                  "Hellish Resistance: Resistance to fire damage.\n" + 
                  "Infernal Legacy:\nLevel 1: Thaumaturgy\nLevel 3: Hellish Rebuke\nLevel 5: Darkness, once a long rest\nCHA is your spellcasting ability.\n"+ 
                  "Languages: Common and Infernal\n")
        
    #Dragonborn

    if player_race == "Dragonborn":
        r_feat = (
            "Dragon Ancestry: You are a descendent of a Red dragon." +
            "\nBreath Attack: You gain a breath ATK dealing fire DMG in a 15ft cone" +
            f"\nBreath Attack Save DC: {8+2+2}.A creature takes 2d6 on a fail and halk DMG on a success. Your breath ATK recharges after a short or long rest." +
            "\nDamage Resistance: You have DMG resistance to fire." +
            "\nLanguages: You know common and draconic.\n"
            )
        
    #Player choses class features

    #Barbarian

    if player_class == "Barbarian":
        rage = "Rages: 2"
        rage_dmg = "Rage DMG: + 2"
        bonus = 2
        if level >= '3':
            rage = "Rages: 3"
        prof = [
            ("Armor: Light and medium armor. Sheilds"),
            ("Weapons: Simple, martial weapons"),
            ("Tools: none"),
            ("Saving Throws: STR and CON")
            ]
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        c_feat = ""
        #List of class features used to fill c_feat
        c_table = [
                    ("Rage: While raging and not wearing armor gain the follwing effects:\n" +
                    "Advantage on STR checks and STR saving throws.\nWhen you make a melee weapon attack using STR,\nyou gain a bonus for the DMG roll that\n" +
                    "increase as you gain levels as a barbarian.\nYou have resistance to bludgeoning, piercing, and slashing DMG.\nIf you can cast spells, you can't cast or\n" +
                    "concentrate on them while raging.\nRage last 1 minute.\nYou can end your rage early.\nIt ends early if you don't DMG a hostile creature in a turn or\n" +
                    "if you don't take DMG in a turn.\nRage counts reset after a long rest."),
                   ("Unarmored Defense: While you are not wearing any armor\n" +
                    "your AC equals 10 + Dex mod + Con mod.\nYou can use a shield and still gain this benefit"),
                   ("Reckless Attack:  Starting at 2nd Level, you can\n"+
                   "gain advantage on STR melee attacks during this teurn but attacks against you\nalso gain advantage until your next turn."),
                   ("Danger Sense: You gain advantage no DEX saving throws against effects you can see, such as traps and spells.\nTo gain this effect you can't beblinded, deafened, or incapacitated."),
                   ("Sub-Class: Path of the Berserker"),
                   ("Frenzy: You can go into a frenzy whiel you rage.\nIf so for the duraction of your rage you can make\na bonus attrack on each of your turns after this one.\n" +
                   "When you rage ends, you suffer one level of exhaustion.")
                   ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{c_table[0]}\n{rage}\n{rage_dmg}\n{c_table[1]}"
        if level >= '2':
            c_feat += f"\n{c_table[2]}\n{c_table[3]}"
        if level >= '3':
            c_feat  += f"\n{c_table[4]}\n{c_table[5]}"
    
    #Bard

    if player_class == "Bard":
        bonus = 2
        prof = [
            ("Armor: Light armor"),
            ("Weapons: Simple weapons, hand crossbows,\nlongbows, rapiers, shortswords"),
            ("Tools: Three muscial istruments of your choice"),
            ("Saving Throws: DEX and CHA")
            ]
        cantrips = "Cantrips: 2"
        spells_known = "Spells Known: 4"
        slots = "Spell Slots: 1st: (2)"
        spells = "Cantrips:\nVicious Mockery\nTrue Strike\n1st:\nHideous Laughter\nThunderwave\nSilent Image\nCure Wounds"
        bard_inspir_charge = spell_mod
        song_dice = "1d6"
        if bard_inspir_charge < 1:
            bard_inspir_charge = 1
        if level == '2':
            spells_known = "Spells Known: 5"
            slots = "Spell Slots: 1st: (3)"
            spells = "Cantrips:\nVicious Mockery\nTrue Strike\n1st:\nHideous Laughter\nThunderwave\nSilent Image\nCure Wounds\nComprehend Languages"
        if level == '3':
            spells_known = "Spells Known: 6"
            slots = "Spell Slots: 1st: (4) 2nd:  (2)"
            spells = "Cantrips:\nVicious Mockery\nTrue Strike\n1st:\nHideous Laughter\nThunderwave\nSilent Image\nCure Wounds\nComprehend Languages\n2nd:\nEnthrall"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        spell_attack = bonus + spell_mod
        spell_attack_str = f"Spell Attack Modiifier: {spell_attack}"
        bard_inspir_str = f"Bardic Inspiration Charges: {bard_inspir_charge}"
        c_feat = ""
        c_table = [
                    ("Bardic Inspiration: You use a bonus actrion to give a creature\nthat can hear you in 60ft to give them a inspiration die. 1d6\n"+
                    "In the next 10 minutes the creature can roll the die and add it to a\nability check, attack roll, or saving throw. This can be done after\nthe d20 has been rolled" +
                    "but before the DM says if it\nsuceeds or fails. The die is then lost.\nYou gain charges of Bardic Inspiration back after a long rest."),
                   (f"Jack of All Trades: You can add half you proficiency bonus\n(rounded down)to any abilty check you are\nnot already proficent with.Add {int(bonus/2)} to result"),
                   (f"Song of Rest: At the end of a short rest any friendly creautre or\nyourself that used hit dice to heal can add a {song_dice}"),
                   ("Expertise: Double proficiency bonus on 2 skills: Preformance and Persuasion"),
                   ("Sub-Class: College of Lore"),
                   ("Cutting Words: As a reaction you can spend a Bardic Inspiration\n"+
                     "charge when a hostile creature makes a attack roll, damage roll, or ability check within 60ft.\nSubtract the result from the hostile creatures result.\nThe creature is immune if iut can't hear you or can't be charmed.")
                   ]
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{spell_dc_str}\n{spell_attack_str}\n{cantrips}\n{spells_known}\n{slots}\n{spells}\n{bard_inspir_str}\n{c_table[0]}"   
        if level >= '2':
            c_feat += f"\n{c_table[1]}\n{c_table[2]}"
        if level >= '3':
            c_feat  += f"\n{c_table[3]}\n{c_table[4]}\n{c_table[5]}"
    
    #Cleric

    if player_class == "Cleric":
        bonus = 2
        prof = [
            ("Armor: Light and medium armor, and shields"),
            ("Weapons: Simple weapons"),
            ("Tools: none"),
            ("Saving Throws: WIS and CHA")
            ]
        cantrips = "Cantrips: 3"
        spells_known = f"Spells Prepared: {int(level) + spell_mod}"
        slots = "Spell Slots: 1st: (2)"
        spells = "Cantrips:\nSacred Flame\nGuidance\nSpare the Dying"
        if level == '2':
            cantrips = "Cantrips: 3"
            spells_known = f"Spells Prepared: {int(level) + spell_mod}"
            slots = "Spell Slots: 1st: (3)"
            spells = "Cantrips:\nSacred Flame\nGuidance\nSpare the Dying"
        if level == '3':
            cantrips = "Cantrips: 3"
            spells_known = f"Spells Prepared: {int(level) + spell_mod}"
            slots = "Spell Slots: 1st: (4) 2nd: (2)"
            spells = "Cantrips:\nSacred Flame\nGuidance\nSpare the Dying"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        spell_attack = bonus + spell_mod
        spell_attack_str = f"Spell Attack Modiifier: {spell_attack}"
        domain = "Life"
        domain_spells = ""
        if domain == "Life":
            domain_spell_list = [
                ("1st: Bless, Cure Wounds"),
                ("3rd: Lesser Restoration, Spiritual Weapon"),
                ("5th: Beacon of Hope, Revivify"),
                ("7th: Death Ward, Guardioan of Faith"),
                ("9th: Mass Cure Wounds, Raise Dead")
                ]
            if level >= '1':
                domain_spells += domain_spell_list[0]
            if level >= '3':
                domain_spells += f"\n{domain_spell_list[1]}"
            if level >= '5':
                domain_spells += f"\n{domain_spell_list[2]}"
            if level >= '7':
                domain_spells += f"\n{domain_spell_list[3]}"
            if level >= '9':
                domain_spells += f"\n{domain_spell_list[4]}"
        c_feat = ""
        c_table = [
            ("Preparing Spells: You can choose spell from the Cleric spell list as long as they are\nthe same or below your avalibale slots.\nYou can change your spell list after a long rest."),
                   ("Divine Domain: Life Domain"),
                   ("Domain Spells: These spell are always prepared and \ndon't go against your total prepared spells"),
                   (domain_spells),
                   ("Bonus Proficiency: Heavy Armor"),
                   ("Disciple of Life: When useing healing spell level 1 or higher\nthe creature gains addition HP equal to 2 + the spells level."),
                   ("Channel Divinity: Regain Channel Divinity after a long or short rest"),
                   ("Channel Divinity Turn Undead: As an action you can make \neach undead within 30ft that can see or hear you make a \nWIS saving throw. If failed the undead must use their \nturn to move as far from you as possible. \nThe undead can not use reations and can only use its actions \nto dash or escape from something that makes it unable to move\n" +
                    "If the undead has nowhere to move,\nit can use the Dodge action."),
                   ("Channel Divinity Preserve Life: Spend an action to heal for 5 times your cleric level.\nThe healing can be divided amongs any creature in 30ft.\n" +
                    "You can not heal for more then half the max HP of the creature.\nThis feature can't be used on undead or constructs.")
                    ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{spell_dc_str}\n{spell_attack_str}\n{cantrips}\n{spells_known}\n{slots}\n{spells}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}\n{c_table[3]}\n{c_table[4]}\n{c_table[5]}"    
        if level >= '2':
            c_feat += f"\n{c_table[6]}\n{c_table[7]}\n{c_table[8]}"
        if level >= '3':
            c_feat  += f"\n"
    
    #Druid  
          
    if player_class == "Druid":
        bonus = 2
        prof = [
            ("Armor: Light and medium armor, and shields.\n(Druid do not wear or use shields made of metal)"),
            ("Weapons: Clubs, daggers, javelins, maces,\nquarterstaffs, scimatars, sickles, slings,\nspears."),
            ("Tools: Herbalism kit"),
            ("Saving Throws: INT and WIS")
            ]
        cantrips = "Cantrips: 2"
        spells_known = f"Spells Prepared: {int(level) + spell_mod}"
        slots = "Spell Slots: 1st: (2)"
        spells = "Cantrips:\nPoison Spray\nGuidance"
        if level == '2':
            cantrips = "Cantrips: 3"
            spells_known = f"Spells Prepared: {int(level) + spell_mod}"
            slots = "Spell Slots: 1st: (3)"
            spells = "Cantrips:\nPoison Spray\nGuidance\nProduce Flame"
        if level == '3':
            cantrips = "Cantrips: 3"
            spells_known = f"Spells Prepared: {int(level) + spell_mod}"
            slots = "Spell Slots: 1st: (4) 2nd: (2)"
            spells = "Cantrips:\nPoison Spray\nGuidance\nProduce Flame"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        spell_attack = bonus + spell_mod
        spell_attack_str = f"Spell Attack Modiifier: {spell_attack}"
        circle_terrain = "Forest"
        circle_spells = ""
        if circle_terrain == "Forest":
           circle_spell_list = [
               ("3rd: Barkskin, Spider Climb"),
               ("5th: Call Lightning, Plant Growth"),
               ("7th: Divination, Freedom of Movement"),
               ("9th: Commune with Nature, Tree Stride")
               ]
           if level >= '3':
                circle_spells += circle_spell_list[0]
           if level >= '5':
                circle_spells += f"\n{circle_spell_list[1]}"
           if level >= '7':
                circle_spells += f"\n{circle_spell_list[2]}"
           if level >= '9':
                circle_spells += f"\n{circle_spell_list[3]}"
        c_feat = ""
        c_table = [
                   ("Druidic: You know the bonus language of the duids."),
                   ("Preparing Spells: You can choose spell from the Druid spell list as long as they are the same or below your avalibale slots. You can change your spell list after a long rest."),
                   ("Sub-Class: Circle of the Land"),
                   ("Bonus Cantrip: You earn 1 additional cantrip"),
                   ("Natural Recovery: You can regain spell slots during a short rest equal to half \nyou druid level rounded up and the spell is not 6th level or higher"),
                   ("Circle Spells: These spell are always prepared and \ndon't go against your total prepared spells"),
                   (circle_spells)
                   ] 
        wild_shape = [
                      ("Wild Shape: You can spend an action to turn into a beast.\nYou have 2 charges of this ability that return after a long or short rest."),
                      ("You can stay in this beast shape for a\nnumber of hours equal to half your druid level rounded down."),
                      ("You automatically revert back to normal if:\nyou are knocked unconscious \ndrop to 0 HP \ndie"),
                      ("The following rules apply while transformed:"),
                      ("You gain the stats of the beast except you reatin your INT WIS and CHA.\nYou also retain your skills and saving throws proficiencies in addition to gaining those of the beast.\nIf you and the beast share proficiencies then take the higher of the two.\nYou do not gain any legendary or lair actions."),
                      ("While transformed you assume the beast HP and hit dice.\nWhen you revert back you return to the HP you had before transforming.\nIf you a forced to revert due to dropping to 0 HP any damage over your remaining beast HP is deducted  from your normal forms HP."),
                      ("You are unable to cast spells in your beast form.\nHowever you don't lose any concentration or effects from spells cast before you transformed."),
                      ("You retain any race or class features as long as your beast form is physically capable of them.\nHowever you can not use any specail senses such as darkvison unless your beast for is capable of them")
                      ]
        wild_shape_str = ""
        for count in wild_shape:
            wild_shape_str += f"{count}\n"           
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{spell_dc_str}\n{spell_attack_str}\n{cantrips}\n{spells_known}\n{slots}\n{spells}\n{c_table[0]}\n{c_table[1]}"    
        if level >= '2':
            c_feat += f"\n{wild_shape_str}\n{c_table[2]}\n{c_table[3]}\n{c_table[4]}\n{c_table[5]}\n{c_table[6]}\n"
        if level >= '3':
            c_feat  += f"\n"
            
    #Fighter

    if player_class == "Fighter":
        bonus = 2
        prof = [("Armor: All armor and shields"), 
                ("Weapons: Simple and martial weapons"), 
                ("Tools: None"), 
                ("Saving Throws: STR and CON")]
        
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        
        c_feat = ""
        c_table = [
            ("Fightering Style:: Great Weapon Fighting"), 
            ("When you roll a 1 or 2 on a DMG die for an attack with a two handed weapon, you may reroll the die and must take the new roll."),
            ("Second Wind: During your turn you cna spend a bonus action to heal for 1d10 + your fighter level. This ability recharges after a short or long rest."),
            ("Action Surge: During you turn you can use this action to take one addition action. This ability recharges after a short or long rest."),
            ("Sub-Class: Champion"),
            ("Improved Critical: Your weapon attacks score a critial hit on a roll of 19 or 20.")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}"    
        if level >= '2':
            c_feat += f"\n{c_table[3]}"
        if level >= '3':
            c_feat  += f"\n{c_table[4]}\n{c_table[5]}"

    #Monk

    if player_class == "Monk":
        bonus = 2
        prof = [("Armor: None"), 
                ("Weapons: Simple weapons and shortswords"), 
                ("Tools: 1 artisan tool or 1 musical instrument"), 
                ("Saving Throws: STR and DEX")]
        martial_atk = ["1d4"]
        martial_str = f"Your Martial Arts DMG is {martial_atk}"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        ki_point = [0 , 2, 3]
        if level == '1':
            ki = ki_point[0]
        if level == '2':
            ki = ki_point[1]
        if level == '3':
            ki = ki_point[2]
        ki_str = f"You have {ki} Ki Points"
        unarmored_move = [0, 10]
        if level == '1':
            move = unarmored_move[0]
        if level == '2' or level == '3':
            move = unarmored_move[1]
        unarmored_move_str = f"You have {move}ft of Unarmored Movement"
        ki_save = 8 + bonus + spell_mod
        ki_save_str = f"Ki Save DC: {ki_save}"
        c_feat = ""
        c_table = [
            ("Unarmored Defense: While wearing no armor your AC is equal to 10 + DEX mod + WIS mod."),
            ("Martial Arts: While unarmed or wielding a \"Monk Weapon\" (shortsword or simple weapon) you gain the following benifits:"),
            ("You can use DEX instead of STR for attack and DMG rolls"),
            ("You can roll a d4 instead of the normal unarmed or monk weapon DMG. This die is based on you Martial Arts."),
            ("If you attack with with a monk weapon or unarmed, you can make a unarmed attack as a bonus action."),
            ("Ki: You can spend a ki point to preform a certain feature. You regain ki points after a short or long rest."),
            ("Ki features:"),
            ("Flurry of Blows: Spend 1 ki point after making an attack to make two unarmed attacks as a bonus action"),
            ("Patient Defense: Spend 1 ki point to take Dodge as a bonus action"),
            ("Step of the Wind: Spend 1 ki point to either Disengage or Dash as a bonus action. Your jump distance is doubled this turn"),
            ("Unarmored Movement: While not wearing armor or wielding a shield you gain extra movement."),
            ("Deflect Missles: If hit by a ranged weapon attack you can reduce the DMG by 1d10 + your DEX mod + monk level. If you reduce the DMG to 0 you can catch the missle and throw it back. This attack uses proficiency and counts as a monk weapon with normal range of 20ft and long range of 60ft."),
            ("Sub-Class: Way of the Open Hand"),
            ("Open Hand Technique: after using Flurry of Blows you can use one of these features:"),
            ("Target must succeed on a DEX saveing throw of be knocked prone"),
            ("Target must succeed a STR saving throw or be pushed back 15ft"),
            ("It can't make a reaction until the end of your next turn")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{martial_str}\n{ki_str}\n{unarmored_move_str}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}\n{c_table[3]}\n{c_table[4]}"    
        if level >= '2':
            c_feat += f"\n{c_table[5]}\n{c_table[6]}\n{c_table[7]}\n{c_table[8]}\n{c_table[9]}\n{c_table[10]}"
        if level >= '3':
            c_feat  += f"\n{c_table[11]}\n{c_table[12]}\n{c_table[13]}\n{c_table[14]}\n{c_table[15]}\n{c_table[16]}"
    
    #Paladin

    if player_class == "Paladin":
       bonus = 2
       prof = [
           ("Armor: All armor and shields "), 
               ("Weapons: Simple and martial weapons"), 
               ("Tools: None"), 
               ("Saving Throws: WIS and CHA")
               ]
       spells_known = f"Spells Prepared: {int(level)/2 + spell_mod}"
       slots = "Spell Slots: 1st: (2)"
       spells = "1st:\nxxxxx"
       oath_epells = [
           ("3rd: Protection from Evil and Good, Sanctuary"),
           ("5th: Lesser Restoration, Zone of Truth"),
           ("9th: Beacon of Hope, Dispel Magic"),
           ("13th: Freedom of Movement, Guardian of Faith"),
           ("17th: Commune, Flame Strike")
           ]
       prof_bonus = f"Proficiency Bonus: +{bonus}"
       spell_dc = 8 + bonus + spell_mod
       spell_dc_str = f"Spell Save DC: {spell_dc}"
       spell_attack = bonus + spell_mod
       spell_attack_str = f"Spell Attack Modiifier: {spell_attack}"
       c_feat = ""
       c_table = [
           ("Divin Sense: Within 60ft you can sense any celestial, fiend, or undead unless it is behind total cover. You can identify which type of creature it is but not it's identity (A specific vampire or angel for example.) You also can aslo detect the presence of any place or object that has been consecrated or desecrated, as if with the \'hallow\' spell. You can use this feature a number of times equal to 1+ your CHA mod. this feature recharges after a long rest."),
           (f"Divin Senese Charges: {1 + spell_mod}"),
           ("Lay on Hands: You have a pool of healing that recharges after a long rest. As an action you can touch a creature and heal it for up to its max HP. You can also expend 5 HP from the pool to cure the target of one disease or neutralize one poison afftecting it. this feature has no effect on undead or constructs."),
           (f"Lay on Hands Pool: {int(level) * '5'}"),
           ("Fighting Style: Defense: While wearing armor you gain + 1 to AC"),
           ("Preparing Spells: You can choose spell from the Paladin spell list as long as they are\nthe same or below your avalibale slots. \nYou can change your spell list after a long rest."),
           ("Divine Smite: When you hit a creatre with a melee weapon ATk, you can expend one spell slot to deal readiant DMG to the target. This DMG is in addition to the normal weapon DMG. The extra DMG is 2d8 for a 1st LVL slot plus 1d8 for each slot higher to a max of 5d8. The DMG increases by 1d8 if the target is an udead or fiend."),
           ("Divine Health: You are immune to disease."),
           ("Sub-Class: Oath of Devotion"),
           ("Tenets of Devotion:"),
           ("Honesty: Don't lie or cheat. Let your word be your promise."),
           ("Courage: Never fear to act, though caution is wise."),
           ("Compassion: Aid others, protect the weak, and punish those who threaten them. show mercy to your foes, but temper it with wisdon."),
           ("Honor: Threat others with fainess, and let your honorable deeds be an example to them. Do as much good as possible while causeing the lease amount of harm."),
           ("Duty: Be responsible for your actions and their consequences, protect those entrusted to your care, and obey those who have authority over you."),
           ("(While these tenets are mostly for RP flavoring, breaking them can cause your character to lose favor with their diety and lose their paladin abilities.)"),
           ("Oath Spells:"),
           ("Channel Divinity: Sacred Weapon and Turn the Unholy"),
           ("Sacred Weapon: You can imbue one weapon you are holding with holy energy. For 1 minute you add your CHA mod to attack rolls made by the weapon. The weapon also emits bright light in a 20ft radius and dim light 20ft beyond that. If the weapon is not magical then it becomes magical for the duration"),
           ("Turn the Unholy: As an action each fiend or undead within 30ft of you that can see or hear you must make a WIS saving throw. If the creature failes it is turned for 1 minute or untul it takes DMG. A turned creature must takes its turn trying to move as far from the you as possible. The creature can not use reations and can only use its actions \nto dash or escape from something that makes it unable to move")
           ] 
       if level >= '1':
           c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{spell_dc_str}\n{spell_attack_str}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}\n{c_table[3]}"    
       if level >= '2':
           c_feat += f"\n{c_table[4]}\n{c_table[5]}\n{c_table[6]}"
       if level >= '3':
           c_feat  += f"\n{c_table[7]}\n{c_table[8]}{c_table[9]}\n{c_table[10]}\n{c_table[11]}\n{c_table[12]}\n{c_table[13]}\n{c_table[14]}\n{c_table[15]}\n{c_table[16]}\n{oath_epells[0]}\n{c_table[17]}\n{c_table[18]}\n{c_table[19]}"

    #Ranger

    if player_class == "Ranger":
        bonus = 2
        prof = [("Armor: Light and medium armor. Shields"), 
                ("Weapons: Simple and martial weapons"), 
                ("Tools: None"), 
                ("Saving Throws: STR and DEX")] 
        spells_known = "Spells Known: 2"
        slots = "Spell Slots: 1st: (2)"
        spells = "1st:\nHunter's Mark\nLongstrider"
        if level == '3':
            spells_known = "Spells Known: 3"
            slots = "Spell Slots: 1st: (3)"
            spells = "1st:\nHunter's Mark\nLongstrider\nFog Cloud"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        favored_terrain_info = (
            ("Difficult terrain doesn't slow your group's travel\n") +
        ("Even when you are engaged in another activity while traveling you remain alert to danger.\n") +
        ("If you are traveling alone, you can move stealthily at a normal pace.\n") +
        ("When you forage, you find twice as much food as you normally would.\n") +
        ("While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.")
        )
        c_feat = ""
        c_table = [
            ("Favored Enemy: Choose a type of creature or two races of humanoids, such as either beasts or dragons or two humanoids like gnolls and orcs. You have advatage on WIS (Survival) checks to track your favored enemy as well as INt checks to recall information about them. You also know a language spoken by your favored enemy or one of the two humanoids."),
            ("Natural Explorer: Choose	one	type of	favored	terrain: arctic, coast,	desert, forest, grassland, mountain, or swamp."),
            ("When you make INT or WIS checks realted to your favored terrain your proficency bonus is doubled if your were already profiecent in that skills."),
            (favored_terrain_info),
            ("Fighting Style: Archery, you gain +2 bonus to attack rolls you make with a ranged weapon."),
            ("Primeval Awarness: As an action you can expend a spell slot and for one minute, per spell level, you can sense whether the following types of creatures are presnt within one mile or six miles if you are in your favored terrain."),
            ("Aberration, celestials, dragons, elementals, fey, fiends, and undead."),
            ("This feature doesn't reveal the creatures location or number."),
            ("Sub-Class: Hunter"),
            ("Hunter's Prey: gain one of the following features:"),
            ("Colossus Slayer: When you hit a creature that is below its HP max you can deal 1d8 extra DMG once per turn"),
            ("Giant Killer: When a large or lager creautre within 5ft of you hits or misses you with an attack you can use a reaction to immediatly attack that creature."),
            ("Horde Breaker: Once during each of your turns when you make a weapon ATK you can make another attck with the same weapon against another creature that is within 5ft of the original target and within range.")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}\n{c_table[3]}"    
        if level >= '2':
            c_feat += f"\n{c_table[4]}\n{spells_known}\n{slots}\n{spells}\n{c_table[5]}\n{c_table[6]}\n{c_table[7]}"
        if level >= '3':
            c_feat  += f"\n{c_table[8]}\n{c_table[9]}\n{c_table[10]}\n{c_table[11]}\n{c_table[12]}"

    #Rogue

    if player_class == "Rogue":
        bonus = 2
        prof = [("Armor: Light armor"), 
                ("Weapons: simple weapons, hand crossbows, longswords, rapiers, and shortswords"), 
                ("Tools: Thieves' tools"), 
                ("Saving Throws: DEX and INT")]
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        sneak_dmg = [("1d6"), ("2d6")]
        sneak_atk = sneak_dmg[0]
        if level == '3':
            sneak_atk = sneak_dmg[1]
        sneak_atk_str = f"Sneak Attack Damage: {sneak_atk}"
        c_feat = ""
        c_table = [
            ("Expertise: Choose two of your skills or one skill and your profiency with thieves' tools. You double the your profiecency bonus for ability checks with those skills."),
            ("Sneak Attack: Once per turn you can deal an extra 1d6 damage to one creature you hit with an attack you have advantage on. The attack must use a finesse or ranged weapon. You don't need advatage if another enmey to the target is within 5ft of it, that enemy isn't incapaciated, and you don't have disadvatage."),
            ("Thieves' Cant: You know the additional langauge theives' cant."),
            ("Cunning Action: You can Hide, Dash, or Disenage as a bonus action."),
            ("Sub-Class: Theif"),
            ("Fast Hands: You can preform a Sleight of Hands check or use you theives' tools as a bonus action."),
            ("Second-Story Work: Climbing no longer cost extra movement. In addition when you take a running jump, you jump increases by a number of feet equal to your DEX mod. ")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{c_table[0]}\n{c_table[1]}\n{sneak_atk_str}\n{c_table[2]}"    
        if level >= '2':
            c_feat += f"\n{c_table[3]}"
        if level >= '3':
            c_feat  += f"\n{c_table[4]}\n{c_table[5]}\n{c_table[6]}"

    #Sorcerer

    if player_class == "Sorcerer":
       bonus = 2
       prof = [("Armor: None"), 
               ("Weapons: Daggers, darts, slings, quarterstaffs, light crossbows"), 
               ("Tools: None"), 
               ("Saving Throws: CON and CHA")]
       cantrips = "Cantrips: 4"
       spells_known = f"Spells known: 2"
       slots = "Spell Slots: 1st: (2)"
       spells = "Cantrips:\nFire Bolt\nRay of Frost\nDancing Lights\nChill Touch\n1st:\nBurning Hands\nSleep"
       if level == '2':
        spells_known = f"Spells known: 3"
        slots = "Spell Slots: 1st: (3)"
        spells = "Cantrips:\nFire Bolt\nRay of Frost\nDancing Lights\nChill Touch\n1st:\nBurning Hands\nSleep\nMagic Missle"
        sorc_points = "Sorcery Points: 2"
       if level == '3':
        spells_known = f"Spells known: 4"
        slots = "Spell Slots: 1st: (4) 2nd (2)"
        spells = "Cantrips:\nFire Bolt\nRay of Frost\nDancing Lights\nChill Touch\n1st:\nBurning Hands\nSleep\nMagic Missle\n2nd:\nScorching Ray"
        sorc_points = "Sorcery Points: 3"
       prof_bonus = f"Proficiency Bonus: +{bonus}"
       spell_dc = 8 + bonus + spell_mod
       spell_dc_str = f"Spell Save DC: {spell_dc}"
       points_to_spells = """Spell Slot Level  Sorcery Points
       1st                      2
       2nd                     3
       3rd                     5
       4th                      6
       5th                      7"""
                       
       c_feat = ""
       c_table = [
           ("Sub-Class: Draconic Bloodline"),
           ("Dragon Ancestor: You are a  descended of a green dragon. You gain the bonus language draconic and have double your profiecency bonus on CHA checks against dragons."),
           ("Font of Magic: You gain sorcery points that can be used for the following features:"),
           ("Creating Spell Slots: You can transform unspent sorcery points into one spell slot as a bonus action."),
           ("Converting a Spell Slot to a Sorcery Points: You can turn a spell slot into a certain number of sorcery points as a bonus action."),
           ("Metamagic: You gain two effects that empower you spell for the  cost of sorcery points."),
           ("Empower Spell: When you roll DMG for a spell you can spend one sorcery point to reroll the DMG diceup to your CHA mod. You can use this metamagic along with other metamagic effects."),
           ("Quickened Spell: When you cast a spell that has a casting time of one action you can spend two sorcery points to change the casting time to one bonus action.")
           ] 
       if level >= '1':
           c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{cantrips}\n{spells_known}\n{slots}\n{spells}\n{c_table[0]}\n{c_table[1]}"    
       if level >= '2':
           c_feat += f"\n{c_table[2]}\n{c_table[3]}\n{c_table[4]}\n{sorc_points}\n{points_to_spells}"
       if level >= '3':
           c_feat  += f"\n{c_table[5]}\n{c_table[6]}\n{c_table[7]}"

    #Warlock

    if player_class == "Warlock":
        bonus = 2
        prof = [("Armor: Light armor"), 
                ("Weapons: Simple weapons"), 
                ("Tools: None"), 
                ("Saving Throws: WIS and CHA")]
        cantrips = "Cantrips: 2"
        spells_known = f"Spells Known: 2"
        slots = "Spell Slots: 1 at 1st level"
        spells = "Cantrips:\nEldritch Blast\nChill Touch\nSpells:\nHellish Rebuke\nCharm Person"
        if level == '2':
            cantrips = "Cantrips: 2"
            spells_known = f"Spells Known: 3"
            slots = "Spell Slots: 2 at 1st level"
            spells = "Cantrips:\nEldritch Blast\nChill Touch\nSpells:\nHellish Rebuke\nBurning Hands\nCommand"
        if level == '3':
            cantrips = "Cantrips: 5"
            spells_known = f"Spells Known: 4"
            slots = "Spell Slots: 2 at 2nd level"
            spells = "Cantrips:\nEldritch Blast\nChill Touch\nVicious Mockery\nThaumaturgy\nMage Hand\nSpells:\nHellish Rebuke\nBurning Hands\nCommand\nScorching Ray"
        fiend_spells =[
            ("1st: Buring Hands and Command"),
            ("2nd: Blindness/Deafness and Scorching Ray"),
            ("3rd: Fireball and Stinking Cloud"),
            ("4th: Fire Shield and Wall of Fire"),
            ("5th: Flame Strike and Hallow")
            ]
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        c_feat = ""
        c_table = [
            ("Pact Magic: When you cast a spell you cast it at the highest level possible for your level. You regain spell slots after a short or long rest."),
            ("Sub-Class: Otherworldly Patron: The Fiend"),
            ("Fiend spells: These spells are added to your Warlock spell list:"),
            ("Dark One's Blessing: When you reduce a hostile creature to zero HP you gain temporary HP equal to your CHA mod + warlock level."),
            ("Eldritch Invocations: You gain the following features:"),
            ("Agonizing Blast: Add your CHA mod to the DMG done with eldritch blast"),
            ("Repelling Blast: When you hit with a creature with eldritch blast you can push the creature up to 10ft away from you in a straight line"),
            ("Pact Boon: You gain a feature from you patron."),
            ("Pact of the Tome: You gain three cantrips from any spell list and they  are treated as warlock spells.")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{cantrips}\n{spells_known}\n{slots}\n{spells}\n{c_table[0]}\n{c_table[1]}\n{c_table[2]}\n{fiend_spells[0]}\n{fiend_spells[1]}\n{fiend_spells[2]}\n{fiend_spells[3]}\n{fiend_spells[4]}\n{c_table[3]}"    
        if level >= '2':
            c_feat += f"\n{c_table[4]}\n{c_table[5]}\n{c_table[6]}"
        if level >= '3':
            c_feat  += f"\n{c_table[7]}\n{c_table[8]}"

    #Wizard

    if player_class == "Wizard":
        bonus = 2
        prof = [
            ("Armor: None"), 
            ("Weapons: Daggers, dart, slings, quaterstaffs, and light crossbows"), 
            ("Tools: None"), 
            ("Saving Throws: INT and WIS")
            ]
        cantrips = "Cantrips: 3"
        spells_known = f"Spellbook:\nCantrips:\nFire Bolt\nMessage\nMage Hand\n1st:\nBurning Hands\nColor Spray\nDetect Magic\nFeather Fall\nMage Armor\nSheild"
        slots = "Spell Slots: 1st: (2)"
        if level == '2':
            cantrips = "Cantrips: 3"
            spells_known = f"Spellbook:\nCantrips:\nFire Bolt\nMessage\nMage Hand\n1st:\nBurning Hands\nColor Spray\nDetect Magic\nFeather Fall\nMage Armor\nSheild\nMagic Missle\nThunderwave"
            slots = "Spell Slots: 1st: (3)"
        if level == '3':
            cantrips = "Cantrips: 3"
            spells_known = f"Spellbook:\nCantrips:\nFire Bolt\nMessage\nMage Hand\n1st:\nBurning Hands\nColor Spray\nDetect Magic\nFeather Fall\nMage Armor\nSheild\nMagic Missle\nThunderwave\n2nd:\nAcid Arrow\nScorching Ray"
            slots = "Spell Slots: 1st: (4)  2nd: (2)"
        prof_bonus = f"Proficiency Bonus: +{bonus}"
        spell_dc = 8 + bonus + spell_mod
        spell_dc_str = f"Spell Save DC: {spell_dc}"
        c_feat = ""
        c_table = [
            ("Arcane Recovery: Once per day when you finish a short rest you can recover spell slots levels up to half you wizard level rounded up, as long as the spell level isn't over 6th."),
            ("Sub-Class: School of Evocation"),
            ("Sculpt Spell: When you cast an evocation spell that effects other creatures you can choose a number of then equal to 1 + the spells level. The chosen creatures automatically succeed on their save against the spell and they take no DMG if they would have taken half DMG.")
            ] 
        if level >= '1':
            c_feat = f"{prof[0]}\n{prof[1]}\n{prof[2]}\n{prof[3]}\n{prof_bonus}\n{cantrips}\n{slots}\n{spells_known}\n{c_table[0]}"    
        if level >= '2':
            c_feat += f"\n{c_table[1]}\n{c_table[2]}"
        if level >= '3':
            c_feat  += f""
           
    return f"Race Features:\n{r_feat}\nClass Features:\n{c_feat}"
        
#Charcter Picture Chooser

def CHARACTER_IMAGE(character):
    if character == "Human":
        return "human.jpg"
    if character == "Elf":
        return "elf.jpg"
    if character == "Half-Elf":
        return "halfelf.jpg"
    if character == "Gnome":
        return "gnome.jpg"
    if character == "Dwarf":
        return "dwarf.jpg"
    if character == "Half-Orc":
        return "halforc.jpg"
    if character == "Tiefling":
        return "tiefling.jpg"
    if character == "Dragonborn":
        return "dragonborn.jpg"
    if character == "Halfling":
        return "halfling.jpg"

#Skill Builder

def SKILLS(stre=0, dex=0, con=0, intel=0, wis=0, cha=0, player_class= None, level = None):    #Brings in stat modifiers to determine skills
    skill_list = {"Athletics":stre,"Acrobatics":dex,"Sleight of Hand":dex,"Stealth":dex,"Arcana":intel,"History":intel
                  ,"Investigation":intel,"Nature":intel,"Religion":intel,"Animal Handling":wis,"Insight":wis,
                  "Medicine":wis,"Perception":wis,"Survival":wis,"Deception":cha,"Intimidation":cha,"Performance":cha,"Persuasion":cha}
    skill_block = "" #final returned skill list
    skills =[] #Lists to be filled with  appended information from skill_list
    stats = []
    index = -1 #indexes through skills and  stats
    prof_bonus = 2
    
    #Separates kill_list into 2 lists (skills and stats)

    for i  in skill_list: 
        skills.append(i)
        stats.append(skill_list[i])
        
    #based on the class choice stats are altered and chosen
    
    if player_class == "Barbarian":
        stats[15] += prof_bonus
        stats[0] += prof_bonus
    if player_class == "Bard":
        stats[17] += prof_bonus
        stats[16] += prof_bonus
        stats[10] += prof_bonus
        if level  >= '2':
            stats[17] += prof_bonus
            stats[16] += prof_bonus
        if level >= '3':
            stats[5] += prof_bonus
            stats[8] += prof_bonus
            stats[4] += prof_bonus
    if player_class == "Cleric":
        stats[8] += prof_bonus
        stats[10] += prof_bonus
    if player_class == "Druid":
        stats[7] += prof_bonus
        stats[13] += prof_bonus
    if player_class == "Fighter":
        stats[12] += prof_bonus
        stats[15] += prof_bonus
    if player_class == "Monk":
        stats[0] += prof_bonus
        stats[1] += prof_bonus
    if player_class == "Paladin":
        stats[9] += prof_bonus
        stats[17] += prof_bonus
    if player_class == "Ranger":
        stats[6] += prof_bonus
        stats[12] += prof_bonus
        stats[13] += prof_bonus
    if player_class == "Rogue":
        stats[2] += prof_bonus
        stats[3] += prof_bonus
        stats[14] += prof_bonus
        stats[6] += prof_bonus
    if player_class == "Sorcerer":
        stats[4] += prof_bonus
        stats[15] += prof_bonus
    if player_class == "Warlock":
        stats[4] += prof_bonus
        stats[5] += prof_bonus
    if player_class == "Wizard":
        stats[4] += prof_bonus
        stats[6] += prof_bonus
        
    #Skills and stats are indexed through and combined into  a string (skill_bloack) to be returned

    for x in skills:
        index+=1
        skill_block = skill_block + f"{skills[index]}: {stats[index]} "   
        
    
    return skill_block
    




#Used for testing

if __name__=="__main__":
   while True:
    choice = input("mod test (mod/hp)")
    while choice == "mod":
        roll = int(input("roll"))
        #print(MODIFIER(roll))
    while choice == "hp":
        player_class = input("player class")
        con_mod = int(input("con mod"))
        level = int(input("level"))
        #print(HIT_POINTS(player_class, con_mod, level))
    while choice == "skill":
       stre = input("str:")
       dex = input("dex:")
       con = input("con:")
       intel = input("int:")
       wis = input("wis:")
       cha = input("char:")
       SKILLS(stre,dex,con,intel,wis,cha)
    while choice == "save":
        Save_Character()
        

    
        
        
    
