import json
import random

#--UNUSED-- Player stats, for saving/converting

def Player_Sheet(name, race, player_Class, str_Stat, dex_Stat, con_Stat, int_Stat, win_Stat, cha_Stat, aC, speed):

    """
    Player Stats
    """
    name = ""
    race = ""
    player_Class = ""
    str_Stat = 0
    dex_Stat = 0
    con_Stat = 0
    int_Stat = 0
    win_Stat = 0
    cha_Stat = 0
    aC = 0
    speed = 0
    
    global character_Sheet
    character_Sheet = {"Name": name, "Race": race, "Class": player_Class, "Str": str_Stat, "Dex": dex_Stat, "Con": con_Stat, "Int": int_Stat, "Wis": win_Stat, "Cha": cha_Stat,
                      "AC": aC, "Speed": speed }
    
#Brings in the rolled stat value and returns the modifier

def MODIFIER(roll):
    mod = -5
    for count in range(1,30,2):
        if roll == count or roll == count - 1:
            print(type(mod))
            return mod
        mod +=1

#Brings in class for hit die, con_mod, and level then returns hit point value
        
def HIT_POINTS(player_class, con_mod = None, level = None):
    class_dict = {"Barbarian": 12, "Bard": 8, "Cleric": 8, "Druid": 8, "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 10, "Rogue": 8, "Sorcerer": 6, "Warlock": 8, "Wizard": 6}
    class_select = []
    hit_dice  = []
    x = -1
    for i in class_dict:
        class_select.append(i)
        hit_dice.append(class_dict[i])
        print(class_select)
        print(hit_dice)
    for selection in class_select:
        x += 1
        if player_class == selection:
            roll_total = 0
            for count in range(level):
                roll = random.randint(1,hit_dice[x])
                roll_total = roll + roll_total
                print(roll)
                print(roll_total)
                count+=1
    hp = roll_total + (con_mod * level) 
    if player_class == "Dwarf":
        hp = hp + (level * 1)
    print(hp)
    return hp

#Brings in dex_mod and returns armor class
        
def  ARMOR_CLASS(dex= None):
    player_ac = 10 + dex
    return player_ac

#--UNUSED-- Character save

def Save_Character():
    file_Name = input("Enter Save Name\n")
    with open(file_Name + ".json", 'w') as f:
        json.dump(character_Sheet, f)
        

#Character Features (Race/Class)

def CHARACTER_FEAT(player_race = None, player_class = None, player_background = None, level = None ):
    p_feat = ""
    c_feat = ""
    if player_race == "Dwarf":
        p_feat = ("Darkvision: 60ft\n" + "Dwarven Resilence: Advantage on saving throws against\n poison, and resistance against poison in combat.\n" + 
                  "Dwaven Combat Training: Proficiency with\nbattleaxe, handaxe, light hammer and warhammer\n" + "Tool Proficiency: Proficency with smith's tools, brewer's supplues, or mason's tools.\n"
                  + "Stonecunning: Proficiency x2 for history checks related to \nstone work\n" + "Languages: Common, Dwarvish\n" + "Sub Race: Hill Dwarf\n") 
    if player_race == "Elf":
        p_feat = ("Darkvision: 60ft\n" + "Keen Senses: Profiency in Perception skill.\n" + "Fey Ancestry: Advantage on saving throws against\n being charmed, and magic cant put you to sleep\n"
                  + "Trance: You don't sleep but instead go into a trance for 4 hours\n gaining the benifits of 8 hours  rest\n" + "Languages: Common, Elvish\n"
                  + "Subrace: High Elf\n" + "Elf Weapon Training: Proficiency with longswords, shortbows,\n shortswords, and longbows.\n" + "Cantrip: You know the firebolt (1d10) cantrip\n INT is your spellcasting ability.\n"
                  + "Extra Language: You can speak and read Celestrial\n")
    if player_race == "Halfling":
        p_feat = ("Lucky: When you roll a 1 on an attack, ability, or saving roll\n you can reroll the die and must keep the new roll\n" + "Brave: Advantage on saveing throws against being frieghtened.\n"
                  + "Halfling Nimbleness: You can move through the \nspace of any creature that is a size larger than you\n" + "Languages: Common and Halfling.\n"
                  + "Subrace: Lightfoot\n" + "Naturally Stealthy: You can hide \neven when being obscured by a creature larger then you.\n")
    if player_race == "Human":
        p_feat = "Languages: Common and Dwarvish or Elvish.\n"
    if player_race == "Gnome":
        p_feat = ("Darkvision: 60ft\n" + "Gnome Cunning: Advantage on INT, WIS, and CHA \nsaving throws against magic\n" + ":anguages: Common and Gnomish\n"
                  + "Subrace: Rock Gnome\n" + "Artificer's Lore: Profiency x2 for history checks\non magic items,  alchemical objects, or technological devices.\n"
                  + "Tinker: Using Tinker's Tools spending 1 hour and 10g:\nTiny Clockwork Device\nAC:5\nHp:1\nCan have up to 3 at a time.\nChoose one of the following:\n"
                  + "Clockwork Toy: A small clockwork animal, dragon or soldier.\nWhen placed on the ground, the toy moves 5 feet\nin a random direction per turn.\nIt makes noise.\n"
                  + "Fire Starter: Device produces a miniture flame which can light\ncandles, campfires, or torches.\n" + "Music Box: Plays a song while open and stops when closed or done playing.\n")
    if player_race == "Half-Elf":
        p_feat = ("Darkvision: 60ft\n" + "Fey Ancestry: Advantage on saving throws against\n being charmed, and magic cant put you to sleep\n" + "Languages: Common, Elvish\n")
    if player_race == "Half-Orc":
        p_feat = ("Darkvision: 60ft\n" + "Menacing: Proficiency with Intimidation skill.\n" + "Relentless Endurance: When you would be dropped to 0 hit points\nbut not outright killed, you instead drop to 1 hitpoint.\nYou can only use this\nfeature once a long rest.\n"
         +"Savage Attacks: When you score a critical hit with a melee\nweapon  attack, you can roll once of the weapon's damage\ndice one additiional time and add it to the\nextra damage of the critical hit.\n"
         + "Languages: Common and Orc.\n")
    if player_race == "Tiefling":
        p_feat = ("Darkvision: 60ft\n" + "Hellish Resistance: Resistance to fire damage.\n" + "Infernal Legacy:\nLevel 1: Thaumaturgy\nLevel 3: Hellish Rebuke\nLevel 5: Darkness, once a long rest\nCHA is your spellcasting ability.\n"
                  + "Languages: Common and Infernal")
    if player_class == "Fighter":
        c_feat = "Fighter Things \nHit Stuff \nMore Hitting"
        if level >= '2':
            c_feat += "Even More Fighter Things \n Armor Swords"
    return f"{p_feat}\n{c_feat}"
        
#Used for testing

if __name__=="__main__":
   while True:
    choice = input("mod test (mod/hp)")
    while choice == "mod":
        roll = int(input("roll"))
        print(MODIFIER(roll))
    while choice == "hp":
        player_class = input("player class")
        con_mod = int(input("con mod"))
        level = int(input("level"))
        print(HIT_POINTS(player_class, con_mod, level))
        

    
        
        
    
