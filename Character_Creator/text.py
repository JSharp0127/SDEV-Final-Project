"""
Author: John Sharp
File text.py

This module is used to store and import the larger text strings to the main program.
Using a separate module makes it easy to add any additional text and keeps from needing to add large swaths of code to the main program.

"""


def GLOSSARY():
    glossary_str = (
        "STR - Strength\n" +
        "DEX - Dexterity\n" +
        "CON - Constitution\n" +
        "INT - Intellegence\n" +
        "WIS - Wisdon\n" +
        "CHA - Charisma\n" +
        "DMG - Damage\n" +
        "AC - Armor Class\n" +
        "HP - Hit Points\n"
        )
    return glossary_str


def HELP_TEXT():
    help_str = (
        ":::To Complete a Character:::\n" +
        "1. In the name entry field type in you desired character name\n" +
        "2. Under Race choose the race for your character. \nTo see the race features click the Features button in the Features Box\n" +
        "3. Choose the Class for you character. \nTo see the class features click the Features button in the Features Box\n" +
        "4. Choose your characters Level (1-3)\n" +
        "5. For your characters stats click the D6 button for each stat. \nA value equating to 3d6 will be \"rolled\" at random. \nTalk with you DM if you wish to reroll\n" +
        "6. Skills will auto-populate based on Class and Stats\n" +
        "7. AC will auto-populate based on your stats\n" +
        "8. Click the HP button to \"roll\" your characters HP after choosing Class, Stats, Race and Level\n" +
        "9. To Save your character click the Save button. \nA file will be created using your characters name. \nIf a save file already exists it will override the previous one, \nso becarful not to name multiple characters the same name\n" +
        "10. To Load your character click the Load button. \nYou will be prompted to enter the name of the character to be loaded\n" +
        "11. To reset the character creator back to the starting state click the NEW button\n"
                )
    return help_str


def SPLASH_TEXT():
    splash_str = (
        "Welcome to \"Easy 5e Character Creator\"\n" +
        "This application is a solo project by JSharp0127\n" +
        "The Purpose of this application is to make creating a player character for the \nTTRPG Dungeons and Dragons 5th Edition\n" +
        "an easy and quick expirence for new and veterain players that want to quickly jump into playing with their friends.\n"  +
        "This application aids in creating a level 1-3 character following the SRD-OGL creation rules.\n" +
        "Meaning while the player can choose their race/class combination and roll their stats, there are parts of the\n" +
        "creation that are set by default.\n" +
        "Such things are:\n" +
        "Skills\nSub-Race\nSub-Class\nSpells\n" +
        "While the goal is to make this application more customizable in the future for the time being using these\n" +
        "restricted choice selections makes it so the application can be released in a stable condition so it can be\n" +
        "accessed asap for players to use.\n" +
        "\n"+
        "There is an  indepth How to Create a Character explanation under the Help menu, but the majority\n" +
        "of creation consists of player choices from the provided drop down menues, rolling and compilation\n" +
        "buttons, and name entry field.\n" +
        "Under the Help menu there is also a provided Glossary for explaining any abbriviated text.\n" +
        "(i.e. DMG = Damage or STR = Strength)\n" +
        "\n" +
        "Update Log:\n" +
        "11/31/23 - \"What Makes You....You\"\n" +
        "(Players have the ability to roll their main 6 stats and HP. AC, modifiers, and skills automatically update\n" +
        "using the results of the main stats.)\n" +
        "12/1/23 - \"Birth of a Hero\"\n" +
        "(Players now can choose their race and the race feature appear in the features block)\n" +
        "12/3/23 - \"Gods of Nature and Rage Music\"\n" +
        "(The first 4 classes (Barbarian, Bard, Cleric, and Druid) have been added and their class features\n" +
        "appear in the features block)\n" +
        "12/4/23  - \"Filed Under D.... for Doughnut\"\n" +
        "(Character sheets can now be saved and loaded using the characters name for the file name)\n" +
        "12/6/23 - \"Swords and Fists\"\n" +
        "(The Fighter and Monk class option are added)\n" +
        "12/11/23 - \"Swords and Bows\"\n" +
        "(Paladin and Ranger added to class options)\n" +
        "12/13/23 - \"Sneaky Spell Slingers\"\n" +
        "(Rogue and Sorcercer added to class options)\n" +
        "12/14/23 - \"Fire and Shadows\"\n" +
        "(Warlock and Wizard added to the class options. ALL CLASSES NOW ADDED!!)\n"
        )
    return splash_str

