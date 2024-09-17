from backend import create_app, db
from backend.models import RPGSystem, Class, Race, Skill, Item, Monster, Spell, ClassSpell, Feat, ClassProgression
import json

def seed_rpg_systems():
    # Define RPG systems data
    rpg_systems = [
    {
        "name": "Dungeons & Dragons 5th Edition",
        "description": "D&D 5th Edition is a high-fantasy roleplaying game known for its accessibility and streamlined rules. Players create characters from a variety of races and classes, exploring worlds filled with magic, monsters, and adventure. The system emphasizes roleplay, exploration, and combat, with a flexible set of rules that encourage creativity. Its advantage/disadvantage mechanic simplifies gameplay, allowing for quicker decision-making. D&D 5E is highly customizable, making it ideal for both new and experienced players. The game features a rich ecosystem of supplemental content, expanding the core rules.",
        "publisher": "Wizards of the Coast",
        "edition": "5th Edition",
        "core_rulebook": "Player's Handbook",
        "genre": "Fantasy",
        "popularity": 10,
        "default_settings": {
            "dice": "d20",
            "classes": ["Barbarian", "Wizard", "Rogue"],
            "races": ["Elf", "Dwarf", "Human"],
            "mechanics": ["Ability Scores", "Saving Throws", "Proficiency Bonus"],
            "ability_scores": ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"],
            "setting": "Forgotten Realms",
            "logo": "/systemLogos/DnDLogo.png",
        }
    },
    {
        "name": "Pathfinder",
        "description": "Pathfinder 2E is a fantasy roleplaying game known for its detailed and intricate mechanics. Building upon the rules of D&D 3.5, it offers a complex and tactical system where players can fine-tune their characters with various feats, abilities, and ancestries. Combat in Pathfinder 2E is strategic, with an action economy that offers players more flexibility in how they approach each turn. It caters to players who enjoy deep customization and mechanical depth, allowing for unique character builds. The system’s world, Golarion, is rich in lore, offering diverse settings and stories for campaigns.",
        "publisher": "Paizo Publishing",
        "edition": "2nd Edition",
        "core_rulebook": "Pathfinder Core Rulebook",
        "genre": "Fantasy",
        "popularity": 8,
        "default_settings": {
            "dice": "d20",
            "classes": ["Alchemist", "Fighter", "Sorcerer"],
            "races": ["Elf", "Goblin", "Halfling"],
            "mechanics": ["Action Economy", "Feats", "Ancestries"],
            "ability_scores": ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"],
            "setting": "Golarion",
            "logo": "/systemLogos/PathfinderLogo.png",
        }
    },
    {
        "name": "Call of Cthulhu",
        "description": "Call of Cthulhu is a horror-themed roleplaying game set in the worlds of H.P. Lovecraft. In the 7th edition, players take on the roles of investigators uncovering dark secrets, often leading to encounters with eldritch horrors beyond human comprehension. The system is known for its focus on investigation, mental strain, and the fragility of human sanity. Combat is often a last resort, with the emphasis on gathering clues, solving mysteries, and surviving the unknown. Call of Cthulhu uses a percentile-based system that rewards careful thinking and roleplay, rather than brute force.",
        "publisher": "Chaosium",
        "edition": "7th Edition",
        "core_rulebook": "Call of Cthulhu Investigator Handbook",
        "genre": "Horror",
        "popularity": 9,
        "default_settings": {
            "dice": "d100",
            "classes": ["Antiquarian", "Occultist", "Private Investigator"],
            "races": ["Human", "Deep One Hybrid", "Ghoul"],
            "skills": ["Spot Hidden", "Psychology", "Library Use"],
            "mechanics": ["Sanity", "Luck"],
            "ability_scores": ["Strength", "Dexterity", "Constitution", "Intelligence", "Power", "Appearance", "Size", "Education"],
            "setting": "1920s Lovecraftian Horror",
            "logo": "/systemLogos/CoCLogo.png",
        }
    },
    {
        "name": "Shadowrun",
        "description": "Shadowrun combines cyberpunk and fantasy elements, setting players in a dystopian future where magic and technology coexist. Players take on the roles of shadowrunners—mercenaries who work in the criminal underworld to complete dangerous missions for powerful corporations. The system is known for its complex mechanics, especially regarding hacking, magic, and combat, and it encourages teamwork to tackle multi-faceted challenges. Shadowrun’s world is gritty and dark, with themes of corporate greed, social inequality, and technological advancements clashing with traditional magic.",
        "publisher": "Catalyst Game Labs",
        "edition": "6th Edition",
        "core_rulebook": "Shadowrun Core Rulebook",
        "genre": "Cyberpunk",
        "popularity": 7,
        "default_settings": {
            "dice": "d6",
            "classes": ["Street Samurai", "Decker", "Mage"],
            "races": ["Human", "Elf", "Ork"],
            "mechanics": ["Augmentations", "Hacking", "Magic"],
            "ability_scores": ["Body", "Agility", "Reaction", "Strength", "Willpower", "Logic", "Intuition", "Charisma", "Edge"],
            "setting": "Dystopian future with magic",
            "logo": "/systemLogos/ShadowrunLogo.png",
        }
    },
    {
        "name": "Star Wars: Edge of the Empire",
        "description": "Edge of the Empire is set in the Star Wars universe, focusing on the seedy underbelly of the galaxy—smugglers, bounty hunters, and outlaws. The system uses narrative dice, which allow for more storytelling-driven outcomes beyond simple success or failure. Players must manage their obligations and relationships while navigating a galaxy controlled by the Empire. The game is known for its flexible storytelling and immersive world-building, allowing players to create their own Star Wars adventures, often with a focus on personal motivations and survival.",
        "publisher": "Fantasy Flight Games",
        "edition": "Edge of the Empire",
        "core_rulebook": "Edge of the Empire Core Rulebook",
        "genre": "Science Fiction",
        "popularity": 6,
        "default_settings": {
            "dice": "Custom Star Wars Dice",
            "classes": ["Bounty Hunter", "Smuggler", "Technician"],
            "races": ["Human", "Twi'lek", "Wookiee"],
            "mechanics": ["Obligation", "Destiny Points"],
            "ability_scores": ["Brawn", "Agility", "Intellect", "Cunning", "Willpower", "Presence"],
            "generation method": '',
            "setting": "Outer Rim Territories",
            "logo": "/systemLogos/StarWarsLogo.png",
        }
    },
    {
        "name": "Mothership RPG",
        "description": "Mothership is a sci-fi horror roleplaying game where players take on the roles of crewmembers aboard spaceships, exploring the unknown and facing existential threats. The system emphasizes player survival in a hostile and uncaring universe, with mechanics that focus on stress, fear, and the constant threat of death. Players must manage their resources carefully and work together to overcome both physical and psychological dangers. Mothership encourages a tense, atmospheric experience where the stakes are high, and failure can be catastrophic.",
        "publisher": "Tuesday Knight Games",
        "edition": "1st Edition",
        "core_rulebook": "Mothership Player's Survival Guide",
        "genre": "Sci-Fi Horror",
        "popularity": 7,
        "default_settings": {
            "dice": "d10/d100",
            "classes": ["Marine", "Scientist", "Android"],
            "races": ["Human"],
            "mechanics": ["Panic Rolls", "Stress and Trauma"],
            "ability_scores": ["Strength", "Speed", "Intellect", "Combat"],
            "setting": "Deep space exploration and survival",
            "logo": "/systemLogos/MothershipLogo.png",
        }
    }
]

    # Define classes, races, skills, items, and monsters (adjust as needed for the 5 popular systems)
    classes = {
        "Dungeons & Dragons 5th Edition": [
            {"name": "Barbarian", "description": "A fierce warrior of primitive background who can enter a battle rage.", "hit_die": "d12", "primary_ability": "Strength"},
            {"name": "Bard", "description": "An inspiring magician whose power echoes the music of creation.", "hit_die": "d8", "primary_ability": "Charisma"},
            {"name": "Cleric", "description": "A priestly champion who wields divine magic in service of a higher power.", "hit_die": "d8", "primary_ability": "Wisdom"},
            {"name": "Druid", "description": "A priest of the Old Faith, wielding the powers of nature and adopting animal forms.", "hit_die": "d8", "primary_ability": "Wisdom"},
            {"name": "Fighter", "description": "A master of martial combat, skilled with a variety of weapons and armor.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"},
            {"name": "Monk", "description": "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.", "hit_die": "d8", "primary_ability": "Dexterity & Wisdom"},
            {"name": "Paladin", "description": "A holy warrior bound to a sacred oath.", "hit_die": "d10", "primary_ability": "Strength & Charisma"},
            {"name": "Ranger", "description": "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.", "hit_die": "d10", "primary_ability": "Dexterity & Wisdom"},
            {"name": "Rogue", "description": "A scoundrel who uses stealth and trickery to overcome obstacles and enemies.", "hit_die": "d8", "primary_ability": "Dexterity"},
            {"name": "Sorcerer", "description": "A spellcaster who draws on inherent magic from a gift or bloodline.", "hit_die": "d6", "primary_ability": "Charisma"},
            {"name": "Warlock", "description": "A wielder of magic that is derived from a bargain with an extraplanar entity.", "hit_die": "d8", "primary_ability": "Charisma"},
            {"name": "Wizard", "description": "A scholarly magic-user capable of manipulating the structures of reality.", "hit_die": "d6", "primary_ability": "Intelligence"}
        ],
        "Pathfinder": [
            {"name": "Alchemist", "description": "A master of potions, bombs, and mutagens, blending magic and science.", "hit_die": "d8", "primary_ability": "Intelligence"},
            {"name": "Barbarian", "description": "A savage warrior who can enter a frenzy during battle.", "hit_die": "d12", "primary_ability": "Strength"},
            {"name": "Bard", "description": "A versatile performer whose music can inspire allies and manipulate foes.", "hit_die": "d8", "primary_ability": "Charisma"},
            {"name": "Champion", "description": "A divine warrior who defends the innocent and punishes the wicked.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"},
            {"name": "Cleric", "description": "A servant of the gods who channels divine power.", "hit_die": "d8", "primary_ability": "Wisdom"},
            {"name": "Druid", "description": "A protector of nature who can transform into animals and command the elements.", "hit_die": "d8", "primary_ability": "Wisdom"},
            {"name": "Fighter", "description": "A master of combat techniques who excels in physical confrontations.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"},
            {"name": "Monk", "description": "A martial artist who can strike with incredible speed and power.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"},
            {"name": "Ranger", "description": "A hunter of the wilds who can track and take down prey.", "hit_die": "d10", "primary_ability": "Dexterity or Strength"},
            {"name": "Rogue", "description": "A sneaky and nimble combatant who uses trickery to gain the upper hand.", "hit_die": "d8", "primary_ability": "Dexterity"},
            {"name": "Sorcerer", "description": "A spellcaster who draws magic from within, based on their bloodline.", "hit_die": "d6", "primary_ability": "Charisma"},
            {"name": "Wizard", "description": "A scholarly magic-user who can cast a wide array of spells.", "hit_die": "d6", "primary_ability": "Intelligence"}
        ],
        "Call of Cthulhu": [
            {"name": "Antiquarian", "description": "A scholar of ancient artifacts and texts, delving into forgotten lore.", "hit_die": "d6", "primary_ability": "Intelligence"},
            {"name": "Author", "description": "A writer and researcher who uncovers hidden truths.", "hit_die": "d6", "primary_ability": "Intelligence"},
            {"name": "Detective", "description": "An investigator who solves mysteries and uncovers secrets.", "hit_die": "d8", "primary_ability": "Intelligence or Perception"},
            {"name": "Doctor", "description": "A medical professional who can treat injuries and illnesses.", "hit_die": "d8", "primary_ability": "Intelligence or Medicine"},
            {"name": "Journalist", "description": "A reporter who digs into the underbelly of society to reveal the truth.", "hit_die": "d6", "primary_ability": "Charisma or Perception"},
            {"name": "Occultist", "description": "A practitioner of dark arts and forbidden knowledge.", "hit_die": "d6", "primary_ability": "Intelligence or Charisma"},
            {"name": "Parapsychologist", "description": "A scientist who studies supernatural phenomena.", "hit_die": "d6", "primary_ability": "Intelligence or Wisdom"},
            {"name": "Police Officer", "description": "A law enforcer who upholds justice and order.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"},
            {"name": "Private Investigator", "description": "A freelance detective who takes on dangerous cases.", "hit_die": "d8", "primary_ability": "Intelligence or Perception"},
            {"name": "Professor", "description": "An academic expert in a specific field of knowledge.", "hit_die": "d6", "primary_ability": "Intelligence"},
            {"name": "Soldier", "description": "A trained combatant skilled in warfare.", "hit_die": "d10", "primary_ability": "Strength or Dexterity"}
        ],
        "Shadowrun": [
            {"name": "Street Samurai", "description": "A cyber-enhanced warrior who follows a strict code of honor.", "hit_die": "d10", "primary_ability": "Strength or Agility"},
            {"name": "Decker", "description": "A hacker who can manipulate the digital world to their advantage.", "hit_die": "d8", "primary_ability": "Intelligence"},
            {"name": "Mage", "description": "A spellcaster who can manipulate mana to cast powerful spells.", "hit_die": "d6", "primary_ability": "Willpower or Charisma"},
            {"name": "Rigger", "description": "A tech-savvy specialist who controls drones and vehicles.", "hit_die": "d8", "primary_ability": "Intelligence or Agility"},
            {"name": "Shaman", "description": "A spiritual leader who can call upon spirits and nature for aid.", "hit_die": "d6", "primary_ability": "Charisma or Willpower"},
            {"name": "Adept", "description": "A mystic warrior who channels magic into physical abilities.", "hit_die": "d10", "primary_ability": "Strength or Willpower"},
            {"name": "Technomancer", "description": "A unique individual who can interface with and control technology using only their mind.", "hit_die": "d8", "primary_ability": "Intelligence or Willpower"},
            {"name": "Face", "description": "A charismatic negotiator and leader who can talk their way out of (or into) any situation.", "hit_die": "d8", "primary_ability": "Charisma"},
            {"name": "Weapon Specialist", "description": "A highly trained individual proficient in a wide range of weaponry.", "hit_die": "d10", "primary_ability": "Strength or Agility"}
        ],
        "Star Wars: Edge of the Empire": [
            {"name": "Bounty Hunter", "description": "A ruthless mercenary who captures or kills targets for money.", "hit_die": "d10", "primary_ability": "Agility or Strength"},
            {"name": "Colonist", "description": "A settler and entrepreneur seeking fortune and a new life in the Outer Rim.", "hit_die": "d8", "primary_ability": "Charisma or Intelligence"},
            {"name": "Explorer", "description": "An adventurer and scout who uncovers the unknown regions of the galaxy.", "hit_die": "d8", "primary_ability": "Intelligence or Agility"},
            {"name": "Hired Gun", "description": "A tough and seasoned warrior who fights for credits and glory.", "hit_die": "d10", "primary_ability": "Strength or Agility"},
            {"name": "Smuggler", "description": "A crafty and daring rogue who deals in illegal goods.", "hit_die": "d8", "primary_ability": "Agility or Charisma"},
            {"name": "Technician", "description": "A skilled engineer who creates and repairs advanced technology.", "hit_die": "d8", "primary_ability": "Intelligence or Agility"}
        ],
        "Mothership RPG": [
            {"name": "Marine", "description": "A soldier trained in combat and survival in hostile environments.", "hit_die": "d10", "primary_ability": "Strength or Combat"},
            {"name": "Scientist", "description": "An expert in various fields of science, using intellect to solve problems.", "hit_die": "d6", "primary_ability": "Intelligence"},
            {"name": "Teamster", "description": "A hardworking crew member skilled in technical and manual labor.", "hit_die": "d8", "primary_ability": "Strength or Agility"},
            {"name": "Android", "description": "An artificial lifeform with superior physical or intellectual capabilities.", "hit_die": "d6", "primary_ability": "Intelligence or Combat"}
        ],
    }

    races = {
        "Dungeons & Dragons 5th Edition": [
            {
                "name": "Elf",
                "description": "Elves are a magical people of otherworldly grace, living in the world but not entirely part of it.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Elvish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Ranger"
            },
            {
                "name": "Dwarf",
                "description": "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.",
                "size": "Medium",
                "speed": 25,
                "languages": ["Common", "Dwarvish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Fighter"
            },
            {
                "name": "Human",
                "description": "A versatile and adaptable race, excelling in various fields of life.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Any",
            },
            {
                "name": "Halfling",
                "description": "A small, nimble race known for their courage and resourcefulness.",
                "size": "Small",
                "speed": 25,
                "languages": ["Common", "Halfling"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Rogue",
            },
            {
                "name": "Dragonborn",
                "description": "A proud and honorable race with dragon ancestry, capable of breathing elemental energy.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Draconic"],
                "vision_type": "Normal",
                "natural_weapons": "Breath Weapon",
                "favored_class": "Paladin",
            },
            {
                "name": "Gnome",
                "description": "A small, curious race with a love for invention and discovery.",
                "size": "Small",
                "speed": 25,
                "languages": ["Common", "Gnomish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Artificer",
            },
            {
                "name": "Half-Elf",
                "description": "A race with both human and elven ancestry, combining the best traits of both.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Elvish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Bard",
            },
            {
                "name": "Half-Orc",
                "description": "A race with human and orc ancestry, known for their strength and resilience.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Orc"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Barbarian",
            },
            {
                "name": "Tiefling",
                "description": "A race with infernal heritage, marked by their demonic appearance and dark powers.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Infernal"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Warlock",
            },
        ],
        "Pathfinder": [
            {
                "name": "Elf",
                "description": "A race of scholars and archers, known for their long lifespan and connection to nature.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Elvish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Wizard",
            },
            {
                "name": "Dwarf",
                "description": "A sturdy race with a deep connection to the earth, excelling in mining and crafting.",
                "size": "Medium",
                "speed": 25,
                "languages": ["Common", "Dwarvish"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Cleric",
            },
            {
                "name": "Human",
                "description": "A race known for their adaptability and diversity, thriving in various environments.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Any",
            },
            {
                "name": "Halfling",
                "description": "A small and nimble race, known for their bravery and luck.",
                "size": "Small",
                "speed": 25,
                "languages": ["Common", "Halfling"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Rogue",
            },
            {
                "name": "Goblin",
                "description": "A mischievous and resourceful race, often underestimated due to their small size.",
                "size": "Small",
                "speed": 25,
                "languages": ["Common", "Goblin"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Rogue",
            },
            {
                "name": "Gnome",
                "description": "A curious and inventive race, deeply connected to the world of magic.",
                "size": "Small",
                "speed": 25,
                "languages": ["Common", "Gnomish"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Sorcerer",
            },
            {
                "name": "Half-Elf",
                "description": "A race that bridges the gap between humans and elves, possessing traits of both.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Elvish"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Bard",
            },
            {
                "name": "Half-Orc",
                "description": "A race that combines the strength of orcs with the versatility of humans.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common", "Orc"],
                "vision_type": "Darkvision",
                "natural_weapons": "None",
                "favored_class": "Barbarian",
            },
        ],
        "Call of Cthulhu": [
            {
                "name": "Human",
                "description": "The primary race in the world of Call of Cthulhu, driven by curiosity, fear, and resilience.",
                "size": "Medium",
                "speed": 30,
                "languages": ["English", "Varies"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Investigator",
            },
            {
                "name": "Deep One Hybrid",
                "description": "A human tainted by the blood of the Deep Ones, often showing signs of their aquatic ancestry.",
                "size": "Medium",
                "speed": 30,
                "languages": ["English", "Deep One"],
                "vision_type": "Darkvision",
                "natural_weapons": "Claws",
                "favored_class": "Cultist",
            },
            {
                "name": "Ghoul",
                "description": "A once-human creature transformed into a monstrous cannibal by the horrors of the Mythos.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Varies"],
                "vision_type": "Darkvision",
                "natural_weapons": "Claws",
                "favored_class": "None",
            },
        ],
        "Shadowrun": [
            {
                "name": "Human",
                "description": "The most common race, known for their adaptability and ambition.",
                "size": "Medium",
                "speed": 30,
                "languages": ["English", "Varies"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Technomancer",
            },
            {
                "name": "Elf",
                "description": "A graceful and agile race with an affinity for magic and technology.",
                "size": "Medium",
                "speed": 30,
                "languages": ["English", "Elvish"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Decker",
            },
            {
                "name": "Ork",
                "description": "A strong and resilient race, often marginalized in society but possessing great potential.",
                "size": "Medium",
                "speed": 30,
                "languages": ["English", "Or'zet"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Street Samurai",
            },
            {
                "name": "Dwarf",
                "description": "A short but sturdy race, excelling in technical fields and engineering.",
                "size": "Small",
                "speed": 25,
                "languages": ["English", "Dwarvish"],
                "vision_type": "Low-light vision",
                "natural_weapons": "None",
                "favored_class": "Rigger",
            },
            {
                "name": "Troll",
                "description": "A massive and powerful race, often feared due to their size and strength.",
                "size": "Large",
                "speed": 25,
                "languages": ["English", "Troll"],
                "vision_type": "Thermographic Vision",
                "natural_weapons": "None",
                "favored_class": "Heavy Weapons Specialist",
            },
        ],
        "Star Wars: Edge of the Empire":[
            {
                "name": "Human",
                "description": "The most widespread species in the galaxy, known for their diversity and ambition.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Galactic Basic"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Smuggler",
            },
            {
                "name": "Twi'lek",
                "description": "A race known for their distinctive head-tails and strong sense of community.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Galactic Basic", "Twi'leki"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Scoundrel",
            },
            {
                "name": "Wookiee",
                "description": "A tall and powerful species from the forested planet Kashyyyk, known for their strength and loyalty.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Shyriiwook"],
                "vision_type": "Normal",
                "natural_weapons": "Claws",
                "favored_class": "Warrior",
            },
            {
                "name": "Rodian",
                "description": "A green-skinned species known for their tracking and hunting skills.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Galactic Basic", "Rodese"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Bounty Hunter",
            },
            {
                "name": "Bothan",
                "description": "A furred species known for their intelligence and skills in espionage.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Galactic Basic", "Bothese"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Spy",
            },
        ],
        "Mothership RPG": [
            {
                "name": "Human",
                "description": "The standard race in the universe of Mothership, facing the dangers of deep space.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common"],
                "vision_type": "Normal",
                "natural_weapons": "None",
                "favored_class": "Scientist",
            },
            {
                "name": "Android",
                "description": "A synthetic lifeform designed to assist humans, often indistinguishable from their creators.",
                "size": "Medium",
                "speed": 30,
                "languages": ["Common"],
                "vision_type": "Infrared Vision",
                "natural_weapons": "None",
                "favored_class": "Marine",
            }
        ]
    }

    skills = {
        "Dungeons & Dragons 5th Edition": [
            {"name": "Acrobatics", "description": "Perform feats of agility, including dives, rolls, flips, and maintaining balance.", "associated_ability": "Dexterity"},
            {"name": "Animal Handling", "description": "Calm down domesticated animals, keep a mount from getting spooked, or intuit an animal's intentions.", "associated_ability": "Wisdom"},
            {"name": "Arcana", "description": "Recall lore about spells, magic items, eldritch symbols, magical traditions, and more.", "associated_ability": "Intelligence"},
            {"name": "Athletics", "description": "Perform physical activities such as climbing, jumping, or swimming.", "associated_ability": "Strength"},
            {"name": "Deception", "description": "Convince others of falsehoods, disguise your motives, or mislead others.", "associated_ability": "Charisma"},
            {"name": "History", "description": "Recall historical events, legends, and knowledge of civilizations.", "associated_ability": "Intelligence"},
            {"name": "Insight", "description": "Discern the true intentions of a creature, such as when searching for a lie or predicting someone's next move.", "associated_ability": "Wisdom"},
            {"name": "Intimidation", "description": "Use threats, physical power, or other means to influence others.", "associated_ability": "Charisma"},
            {"name": "Investigation", "description": "Search for clues and make deductions based on those clues.", "associated_ability": "Intelligence"},
            {"name": "Medicine", "description": "Diagnose illnesses, stabilize a dying creature, or treat wounds.", "associated_ability": "Wisdom"},
            {"name": "Nature", "description": "Recall knowledge about the natural world, such as terrain, plants, and animals.", "associated_ability": "Intelligence"},
            {"name": "Perception", "description": "Spot, hear, or otherwise detect the presence of something.", "associated_ability": "Wisdom"},
            {"name": "Performance", "description": "Entertain an audience with music, dance, acting, or other performing arts.", "associated_ability": "Charisma"},
            {"name": "Persuasion", "description": "Influence others with tact, social graces, or good nature.", "associated_ability": "Charisma"},
            {"name": "Religion", "description": "Recall lore about deities, rites, prayers, religious hierarchies, holy symbols, and practices.", "associated_ability": "Intelligence"},
            {"name": "Sleight of Hand", "description": "Pickpocket, plant something on someone, or perform other subtle hand movements.", "associated_ability": "Dexterity"},
            {"name": "Stealth", "description": "Move silently, hide, or otherwise avoid detection.", "associated_ability": "Dexterity"},
            {"name": "Survival", "description": "Track creatures, find food and water, or endure harsh environments.", "associated_ability": "Wisdom"}
        ],
        "Pathfinder": [
            {"name": "Acrobatics", "description": "Perform feats of agility, including jumps, flips, and maintaining balance.", "associated_ability": "Dexterity"},
            {"name": "Arcana", "description": "Identify spells and magic items, as well as recall knowledge about magical traditions.", "associated_ability": "Intelligence"},
            {"name": "Athletics", "description": "Perform physical activities such as climbing, jumping, or swimming.", "associated_ability": "Strength"},
            {"name": "Crafting", "description": "Create, repair, or identify items.", "associated_ability": "Intelligence"},
            {"name": "Deception", "description": "Lie, create diversions, or mislead others.", "associated_ability": "Charisma"},
            {"name": "Diplomacy", "description": "Influence others through negotiation, charm, or flattery.", "associated_ability": "Charisma"},
            {"name": "Intimidation", "description": "Coerce others through threats, displays of force, or physical power.", "associated_ability": "Charisma"},
            {"name": "Medicine", "description": "Provide medical care, such as treating wounds or illnesses.", "associated_ability": "Wisdom"},
            {"name": "Nature", "description": "Recall knowledge about the natural world, such as terrain, plants, and animals.", "associated_ability": "Wisdom"},
            {"name": "Occultism", "description": "Identify and understand occult rituals, symbols, and creatures.", "associated_ability": "Intelligence"},
            {"name": "Performance", "description": "Entertain others through music, dance, acting, or other performing arts.", "associated_ability": "Charisma"},
            {"name": "Religion", "description": "Recall knowledge about gods, holy rites, and religious customs.", "associated_ability": "Wisdom"},
            {"name": "Society", "description": "Understand social structures, laws, and history.", "associated_ability": "Intelligence"},
            {"name": "Stealth", "description": "Move silently, hide, or otherwise avoid detection.", "associated_ability": "Dexterity"},
            {"name": "Survival", "description": "Track creatures, find food and water, or endure harsh environments.", "associated_ability": "Wisdom"},
            {"name": "Thievery", "description": "Pick locks, disable traps, or perform sleight of hand.", "associated_ability": "Dexterity"}
        ],
        "Call of Cthulhu": [
            {"name": "Accounting", "description": "Track financial records and understand economic systems.", "associated_ability": "Intelligence"},
            {"name": "Anthropology", "description": "Study human cultures and societies.", "associated_ability": "Intelligence"},
            {"name": "Appraise", "description": "Determine the value of objects and artifacts.", "associated_ability": "Intelligence"},
            {"name": "Archaeology", "description": "Study ancient civilizations and artifacts.", "associated_ability": "Intelligence"},
            {"name": "Art/Craft", "description": "Create and understand various forms of art and craftsmanship.", "associated_ability": "Intelligence"},
            {"name": "Charm", "description": "Influence others through personal appeal.", "associated_ability": "Charisma"},
            {"name": "Climb", "description": "Scale walls, cliffs, and other vertical surfaces.", "associated_ability": "Strength"},
            {"name": "Credit Rating", "description": "Assess financial status and reputation.", "associated_ability": "Charisma"},
            {"name": "Cthulhu Mythos", "description": "Knowledge of forbidden lore and ancient evils.", "associated_ability": "Intelligence"},
            {"name": "Disguise", "description": "Alter appearance to conceal identity.", "associated_ability": "Charisma"},
            {"name": "Dodge", "description": "Avoid physical attacks and hazards.", "associated_ability": "Dexterity"},
            {"name": "Drive Auto", "description": "Operate motor vehicles.", "associated_ability": "Dexterity"},
            {"name": "Elec Repair", "description": "Repair and maintain electrical equipment.", "associated_ability": "Intelligence"},
            {"name": "Fast Talk", "description": "Convince others through quick and persuasive speech.", "associated_ability": "Charisma"},
            {"name": "Fighting", "description": "Engage in hand-to-hand combat.", "associated_ability": "Strength"},
            {"name": "Firearms", "description": "Use guns and other ranged weapons.", "associated_ability": "Dexterity"},
            {"name": "First Aid", "description": "Provide basic medical care and stabilize the wounded.", "associated_ability": "Intelligence"},
            {"name": "History", "description": "Understand and interpret historical events.", "associated_ability": "Intelligence"},
            {"name": "Intimidate", "description": "Coerce others through threats or displays of power.", "associated_ability": "Charisma"},
            {"name": "Jump", "description": "Leap over obstacles or across gaps.", "associated_ability": "Strength"},
            {"name": "Law", "description": "Understand legal systems and procedures.", "associated_ability": "Intelligence"},
            {"name": "Library Use", "description": "Research and find information in books and documents.", "associated_ability": "Intelligence"},
            {"name": "Listen", "description": "Detect sounds and overhear conversations.", "associated_ability": "Wisdom"},
            {"name": "Locksmith", "description": "Pick locks and work with mechanical security devices.", "associated_ability": "Dexterity"},
            {"name": "Mech Repair", "description": "Repair and maintain mechanical equipment.", "associated_ability": "Intelligence"},
            {"name": "Medicine", "description": "Diagnose and treat diseases and injuries.", "associated_ability": "Intelligence"},
            {"name": "Natural World", "description": "Understand natural environments and creatures.", "associated_ability": "Intelligence"},
            {"name": "Navigate", "description": "Determine your location and find your way.", "associated_ability": "Intelligence"},
            {"name": "Occult", "description": "Understand occult rituals, symbols, and beliefs.", "associated_ability": "Intelligence"},
            {"name": "Operate Heavy Machinery", "description": "Operate and maintain heavy machinery.", "associated_ability": "Strength"},
            {"name": "Persuade", "description": "Convince others with reason and logic.", "associated_ability": "Charisma"},
            {"name": "Pilot", "description": "Operate aircraft or watercraft.", "associated_ability": "Dexterity"},
            {"name": "Psychoanalysis", "description": "Treat mental disorders through therapy.", "associated_ability": "Intelligence"},
            {"name": "Psychology", "description": "Understand human behavior and motives.", "associated_ability": "Intelligence"},
            {"name": "Ride", "description": "Ride and control mounts.", "associated_ability": "Dexterity"},
            {"name": "Science", "description": "Specialize in a scientific discipline.", "associated_ability": "Intelligence"},
            {"name": "Sleight of Hand", "description": "Perform quick hand movements, such as tricks or theft.", "associated_ability": "Dexterity"},
            {"name": "Spot Hidden", "description": "Notice hidden objects or creatures.", "associated_ability": "Wisdom"},
            {"name": "Stealth", "description": "Move silently and avoid detection.", "associated_ability": "Dexterity"},
            {"name": "Survival", "description": "Endure and navigate wilderness environments.", "associated_ability": "Wisdom"},
            {"name": "Swim", "description": "Move through water effectively.", "associated_ability": "Strength"},
            {"name": "Throw", "description": "Accurately throw objects or weapons.", "associated_ability": "Dexterity"},
            {"name": "Track", "description": "Follow the trail of a creature or person.", "associated_ability": "Wisdom"}
        ],
        "Shadowrun": [
            {"name": "Athletics", "description": "Physical activities such as running, climbing, and swimming.", "associated_ability": "Strength/Agility"},
            {"name": "Con", "description": "Deceive others, create false identities, or manipulate social situations.", "associated_ability": "Charisma"},
            {"name": "Cybercombat", "description": "Engage in combat within the Matrix, targeting other deckers or IC.", "associated_ability": "Logic"},
            {"name": "Electronics", "description": "Understand and manipulate electronic devices.", "associated_ability": "Logic"},
            {"name": "Enchanting", "description": "Create and use magical items.", "associated_ability": "Magic"},
            {"name": "Etiquette", "description": "Understand and follow social protocols and customs.", "associated_ability": "Charisma"},
            {"name": "Hacking", "description": "Manipulate the Matrix, break into systems, and exploit software.", "associated_ability": "Logic"},
            {"name": "Negotiation", "description": "Influence others through bargaining and diplomacy.", "associated_ability": "Charisma"},
            {"name": "Perception", "description": "Spot details, detect hidden objects, and observe the environment.", "associated_ability": "Intuition"},
            {"name": "Pilot Ground Craft", "description": "Operate ground vehicles such as cars and motorcycles.", "associated_ability": "Reaction"},
            {"name": "Pilot Aircraft", "description": "Operate aerial vehicles such as planes and drones.", "associated_ability": "Reaction"},
            {"name": "Sneaking", "description": "Move silently and avoid detection.", "associated_ability": "Agility"},
            {"name": "Spellcasting", "description": "Cast and control magical spells.", "associated_ability": "Magic"},
            {"name": "Survival", "description": "Endure harsh environments and find sustenance.", "associated_ability": "Intuition"},
            {"name": "Tracking", "description": "Follow the trail of a creature or person.", "associated_ability": "Intuition"},
            {"name": "Unarmed Combat", "description": "Engage in hand-to-hand combat.", "associated_ability": "Agility"}
        ],
        "Star Wars: Edge of the Empire": [
            {"name": "Astrogation", "description": "Plot courses through hyperspace.", "associated_ability": "Intellect"},
            {"name": "Athletics", "description": "Perform physical feats of strength and endurance.", "associated_ability": "Brawn"},
            {"name": "Charm", "description": "Use personal appeal to sway others.", "associated_ability": "Presence"},
            {"name": "Coercion", "description": "Use threats or force to influence others.", "associated_ability": "Willpower"},
            {"name": "Computers", "description": "Manipulate and retrieve data using computer systems.", "associated_ability": "Intellect"},
            {"name": "Cool", "description": "Stay calm under pressure and act quickly.", "associated_ability": "Presence"},
            {"name": "Coordination", "description": "Balance and perform acrobatic maneuvers.", "associated_ability": "Agility"},
            {"name": "Deception", "description": "Convince others of lies or false information.", "associated_ability": "Cunning"},
            {"name": "Discipline", "description": "Resist mental and emotional influence.", "associated_ability": "Willpower"},
            {"name": "Leadership", "description": "Inspire and lead others.", "associated_ability": "Presence"},
            {"name": "Mechanics", "description": "Repair and maintain mechanical systems.", "associated_ability": "Intellect"},
            {"name": "Medicine", "description": "Treat wounds and illnesses.", "associated_ability": "Intellect"},
            {"name": "Melee", "description": "Engage in close combat with weapons.", "associated_ability": "Brawn"},
            {"name": "Negotiation", "description": "Bargain and trade with others.", "associated_ability": "Presence"},
            {"name": "Perception", "description": "Spot details and observe the environment.", "associated_ability": "Cunning"},
            {"name": "Piloting (Planetary)", "description": "Operate vehicles in planetary environments.", "associated_ability": "Agility"},
            {"name": "Piloting (Space)", "description": "Operate spacecraft in space.", "associated_ability": "Agility"},
            {"name": "Ranged (Heavy)", "description": "Operate heavy ranged weapons.", "associated_ability": "Agility"},
            {"name": "Ranged (Light)", "description": "Operate light ranged weapons.", "associated_ability": "Agility"},
            {"name": "Resilience", "description": "Endure physical strain and resist environmental hazards.", "associated_ability": "Brawn"},
            {"name": "Skulduggery", "description": "Perform criminal activities like lockpicking and smuggling.", "associated_ability": "Cunning"},
            {"name": "Stealth", "description": "Move silently and avoid detection.", "associated_ability": "Agility"},
            {"name": "Streetwise", "description": "Navigate urban environments and underworld networks.", "associated_ability": "Cunning"},
            {"name": "Survival", "description": "Endure harsh environments and find sustenance.", "associated_ability": "Cunning"},
            {"name": "Vigilance", "description": "Stay alert and react quickly.", "associated_ability": "Willpower"}
        ],
        "Mothership RPG": [
            {"name": "Athletics", "description": "Perform physical feats such as climbing and running.", "associated_ability": "Strength"},
            {"name": "Combat", "description": "Engage in armed or unarmed combat.", "associated_ability": "Combat"},
            {"name": "Command", "description": "Lead others and issue orders.", "associated_ability": "Charisma"},
            {"name": "Computers", "description": "Manipulate and retrieve data using computer systems.", "associated_ability": "Intellect"},
            {"name": "Engineering", "description": "Build, repair, and maintain machinery.", "associated_ability": "Intellect"},
            {"name": "Explosives", "description": "Handle, deploy, and disarm explosives.", "associated_ability": "Intellect"},
            {"name": "First Aid", "description": "Provide emergency medical treatment.", "associated_ability": "Intellect"},
            {"name": "Intimidation", "description": "Coerce others through threats or displays of force.", "associated_ability": "Charisma"},
            {"name": "Linguistics", "description": "Understand and translate languages.", "associated_ability": "Intellect"},
            {"name": "Mechanics", "description": "Operate and repair mechanical systems.", "associated_ability": "Intellect"},
            {"name": "Military Training", "description": "Specialized combat techniques and strategies.", "associated_ability": "Combat"},
            {"name": "Piloting", "description": "Operate spacecraft and other vehicles.", "associated_ability": "Agility"},
            {"name": "Psychology", "description": "Understand human behavior and motives.", "associated_ability": "Intellect"},
            {"name": "Research", "description": "Analyze data and conduct experiments.", "associated_ability": "Intellect"},
            {"name": "Survival", "description": "Endure harsh environments and find sustenance.", "associated_ability": "Intellect"},
            {"name": "Xenobiology", "description": "Understand and study alien life forms.", "associated_ability": "Intellect"}
        ],

    }

    items = {
        "Dungeons & Dragons 5th Edition": [
            # Simple Melee Weapons
            {"name": "Longsword", "description": "A versatile sword favored by many warriors.", "weight": 3, "rarity": "Common", "cost": 15, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Shortsword", "description": "A lightweight sword ideal for quick strikes.", "weight": 2, "rarity": "Common", "cost": 10, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Longbow", "description": "A powerful ranged weapon with great range.", "weight": 2, "rarity": "Common", "cost": 50, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Club", "description": "A simple bludgeoning weapon.", "weight": 2, "rarity": "Common", "cost": 1, "damage_type": "Bludgeoning", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Dagger", "description": "A small, easily concealed blade.", "weight": 1, "rarity": "Common", "cost": 2, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Greatclub", "description": "A large, heavy club.", "weight": 10, "rarity": "Common", "cost": 2, "damage_type": "Bludgeoning", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Handaxe", "description": "A small axe that can be thrown.", "weight": 2, "rarity": "Common", "cost": 5, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Javelin", "description": "A light spear designed to be thrown.", "weight": 2, "rarity": "Common", "cost": 5, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Light Hammer", "description": "A small hammer, balanced for throwing.", "weight": 2, "rarity": "Common", "cost": 2, "damage_type": "Bludgeoning", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Mace", "description": "A bludgeoning weapon with a heavy head.", "weight": 4, "rarity": "Common", "cost": 5, "damage_type": "Bludgeoning", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Quarterstaff", "description": "A sturdy pole, often used as a walking stick.", "weight": 4, "rarity": "Common", "cost": 2, "damage_type": "Bludgeoning", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Sickle", "description": "A curved blade used for harvesting crops.", "weight": 2, "rarity": "Common", "cost": 1, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Spear", "description": "A weapon with a long shaft and pointed tip.", "weight": 3, "rarity": "Common", "cost": 1, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            
            # Simple Ranged Weapons
            {"name": "Light Crossbow", "description": "A small, easy-to-use crossbow.", "weight": 5, "rarity": "Common", "cost": 25, "damage_type": "Piercing", "material": "Wood/Steel", "slot_type": "Weapon"},
            {"name": "Dart", "description": "A small throwing weapon.", "weight": 0.25, "rarity": "Common", "cost": 0.05, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Shortbow", "description": "A smaller, lighter bow.", "weight": 2, "rarity": "Common", "cost": 25, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Sling", "description": "A simple weapon that hurls stones.", "weight": 0, "rarity": "Common", "cost": 1, "damage_type": "Bludgeoning", "material": "Leather", "slot_type": "Weapon"},
            
            # Martial Melee Weapons
            {"name": "Battleaxe", "description": "A sturdy axe favored by warriors.", "weight": 4, "rarity": "Common", "cost": 10, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Flail", "description": "A weapon with a spiked ball on a chain.", "weight": 2, "rarity": "Common", "cost": 10, "damage_type": "Bludgeoning", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Glaive", "description": "A polearm with a long blade.", "weight": 6, "rarity": "Common", "cost": 20, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Greataxe", "description": "A large, double-bladed axe.", "weight": 7, "rarity": "Common", "cost": 30, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Greatsword", "description": "A massive two-handed sword.", "weight": 6, "rarity": "Common", "cost": 50, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Halberd", "description": "A polearm with an axe blade and spike.", "weight": 6, "rarity": "Common", "cost": 20, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Lance", "description": "A long weapon used by mounted warriors.", "weight": 6, "rarity": "Common", "cost": 10, "damage_type": "Piercing", "material": "Wood/Steel", "slot_type": "Weapon"},
            {"name": "Longsword", "description": "A versatile sword favored by many warriors.", "weight": 3, "rarity": "Common", "cost": 15, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Maul", "description": "A heavy hammer for smashing foes.", "weight": 10, "rarity": "Common", "cost": 10, "damage_type": "Bludgeoning", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Morningstar", "description": "A spiked mace that deals heavy damage.", "weight": 4, "rarity": "Common", "cost": 15, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Pike", "description": "A long weapon with a pointed tip.", "weight": 18, "rarity": "Common", "cost": 5, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Rapier", "description": "A slender sword for thrusting.", "weight": 2, "rarity": "Common", "cost": 25, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Scimitar", "description": "A curved blade favored in desert regions.", "weight": 3, "rarity": "Common", "cost": 25, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Shortsword", "description": "A lightweight sword ideal for quick strikes.", "weight": 2, "rarity": "Common", "cost": 10, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Trident", "description": "A three-pronged spear used in aquatic environments.", "weight": 4, "rarity": "Common", "cost": 5, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "War Pick", "description": "A weapon designed to penetrate armor.", "weight": 2, "rarity": "Common", "cost": 5, "damage_type": "Piercing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Warhammer", "description": "A hammer used for both construction and combat.", "weight": 2, "rarity": "Common", "cost": 15, "damage_type": "Bludgeoning", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Whip", "description": "A flexible weapon that can disarm opponents.", "weight": 3, "rarity": "Common", "cost": 2, "damage_type": "Slashing", "material": "Leather", "slot_type": "Weapon"},
            
            # Martial Ranged Weapons
            {"name": "Blowgun", "description": "A tube that shoots small darts.", "weight": 1, "rarity": "Common", "cost": 10, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Hand Crossbow", "description": "A small crossbow for one-handed use.", "weight": 3, "rarity": "Common", "cost": 75, "damage_type": "Piercing", "material": "Wood/Steel", "slot_type": "Weapon"},
            {"name": "Heavy Crossbow", "description": "A large crossbow that deals significant damage.", "weight": 18, "rarity": "Common", "cost": 50, "damage_type": "Piercing", "material": "Wood/Steel", "slot_type": "Weapon"},
            {"name": "Longbow", "description": "A powerful ranged weapon with great range.", "weight": 2, "rarity": "Common", "cost": 50, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Net", "description": "A weapon used to entangle foes.", "weight": 3, "rarity": "Common", "cost": 1, "damage_type": "None", "material": "Rope", "slot_type": "Weapon"},
            
            # Magical Weapons (Examples)
            {"name": "Flame Tongue", "description": "A sword that can burst into flame.", "weight": 3, "rarity": "Rare", "cost": None, "damage_type": "Slashing/Fire", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Frost Brand", "description": "A sword that deals cold damage.", "weight": 3, "rarity": "Very Rare", "cost": None, "damage_type": "Slashing/Cold", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Vorpal Sword", "description": "A sword that can decapitate its foes.", "weight": 3, "rarity": "Legendary", "cost": None, "damage_type": "Slashing", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Sunblade", "description": "A radiant blade that glows with sunlight.", "weight": 2, "rarity": "Rare", "cost": None, "damage_type": "Radiant", "material": "Steel", "slot_type": "Weapon"},
            {"name": "Oathbow", "description": "A bow that can swear an oath to slay a particular enemy.", "weight": 2, "rarity": "Very Rare", "cost": None, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            
            # Light Armor
            {"name": "Padded Armor", "description": "Light armor made from quilted layers of cloth.", "weight": 8, "rarity": "Common", "cost": 5, "material": "Cloth", "slot_type": "Armor"},
            {"name": "Leather Armor", "description": "Basic light armor made from leather.", "weight": 10, "rarity": "Common", "cost": 10, "material": "Leather", "slot_type": "Armor"},
            {"name": "Studded Leather Armor", "description": "Leather armor reinforced with small metal rivets.", "weight": 13, "rarity": "Common", "cost": 45, "material": "Leather/Metal", "slot_type": "Armor"},
            
            # Medium Armor
            {"name": "Hide Armor", "description": "Armor made from the hides of beasts.", "weight": 12, "rarity": "Common", "cost": 10, "material": "Hide", "slot_type": "Armor"},
            {"name": "Chain Shirt", "description": "A shirt made of interlocking metal rings.", "weight": 20, "rarity": "Common", "cost": 50, "material": "Metal", "slot_type": "Armor"},
            {"name": "Scale Mail", "description": "Armor made from overlapping metal scales.", "weight": 45, "rarity": "Common", "cost": 50, "material": "Metal", "slot_type": "Armor"},
            {"name": "Breastplate", "description": "A fitted metal chest piece that offers protection.", "weight": 20, "rarity": "Uncommon", "cost": 400, "material": "Metal", "slot_type": "Armor"},
            {"name": "Half Plate", "description": "Armor that covers most of the body, except for the limbs.", "weight": 40, "rarity": "Uncommon", "cost": 750, "material": "Metal", "slot_type": "Armor"},
            
            # Heavy Armor
            {"name": "Ring Mail", "description": "Armor made of metal rings sewn onto a leather backing.", "weight": 40, "rarity": "Common", "cost": 30, "material": "Metal/Leather", "slot_type": "Armor"},
            {"name": "Chain Mail", "description": "Armor made from interlocking metal rings, covering the whole body.", "weight": 55, "rarity": "Common", "cost": 75, "material": "Metal", "slot_type": "Armor"},
            {"name": "Splint Armor", "description": "Armor made from metal strips riveted to a leather backing.", "weight": 60, "rarity": "Uncommon", "cost": 200, "material": "Metal/Leather", "slot_type": "Armor"},
            {"name": "Plate Armor", "description": "The best protection money can buy, full-body armor made of metal plates.", "weight": 65, "rarity": "Rare", "cost": 1500, "material": "Metal", "slot_type": "Armor"},
            
            # Shields
            {"name": "Shield", "description": "A simple wooden or metal shield.", "weight": 6, "rarity": "Common", "cost": 10, "material": "Wood/Metal", "slot_type": "Shield"},
            
            # Magical Armors (Examples)
            {"name": "Mithral Armor", "description": "Light and flexible armor made from mithral.", "weight": 10, "rarity": "Rare", "cost": None, "material": "Mithral", "slot_type": "Armor"},
            {"name": "Adamantine Armor", "description": "Armor made from adamantine, making it nearly indestructible.", "weight": 55, "rarity": "Very Rare", "cost": None, "material": "Adamantine", "slot_type": "Armor"},
            {"name": "Dragon Scale Mail", "description": "Armor made from the scales of a dragon, offering resistance to the dragon's breath weapon.", "weight": 45, "rarity": "Very Rare", "cost": None, "material": "Dragon Scales", "slot_type": "Armor"},
            {"name": "Armor of Invulnerability", "description": "Magical armor that makes the wearer immune to nonmagical damage for a short time.", "weight": 60, "rarity": "Legendary", "cost": None, "material": "Metal", "slot_type": "Armor"},
            {"name": "Cloak of Protection", "description": "A magical cloak that offers protection to the wearer.", "weight": 1, "rarity": "Uncommon", "cost": None, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Robe of the Archmagi", "description": "A powerful robe that enhances the wearer's spellcasting abilities.", "weight": 1, "rarity": "Legendary", "cost": None, "material": "Cloth", "slot_type": "Robe"},
            
            # Potions
            {"name": "Potion of Healing", "description": "Heals 2d4 + 2 hit points.", "weight": 0.5, "rarity": "Common", "cost": 50, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Greater Healing", "description": "Heals 4d4 + 4 hit points.", "weight": 0.5, "rarity": "Uncommon", "cost": 150, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Superior Healing", "description": "Heals 8d4 + 8 hit points.", "weight": 0.5, "rarity": "Rare", "cost": 500, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Supreme Healing", "description": "Heals 10d4 + 20 hit points.", "weight": 0.5, "rarity": "Very Rare", "cost": 1350, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Fire Breath", "description": "After drinking this potion, you can use a bonus action to exhale fire at a target within 30 feet.", "weight": 0.5, "rarity": "Uncommon", "cost": 300, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Flying", "description": "Grants a flying speed equal to your walking speed for 1 hour.", "weight": 0.5, "rarity": "Very Rare", "cost": 5000, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Invisibility", "description": "Grants invisibility for 1 hour or until you attack or cast a spell.", "weight": 0.5, "rarity": "Very Rare", "cost": 5000, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Water Breathing", "description": "Allows you to breathe underwater for 1 hour.", "weight": 0.5, "rarity": "Uncommon", "cost": 180, "material": "Glass Vial", "slot_type": "Potion"},
            {"name": "Potion of Speed", "description": "Grants the effects of the haste spell for 1 minute.", "weight": 0.5, "rarity": "Very Rare", "cost": 3000, "material": "Glass Vial", "slot_type": "Potion"},
            
            # Scrolls
            {"name": "Spell Scroll (Cantrip)", "description": "Contains a cantrip from any spell list. A spellcaster can use it to cast the cantrip once.", "weight": 0.0, "rarity": "Common", "cost": 25, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (1st Level)", "description": "Contains a 1st-level spell from any spell list.", "weight": 0.0, "rarity": "Common", "cost": 75, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (2nd Level)", "description": "Contains a 2nd-level spell from any spell list.", "weight": 0.0, "rarity": "Uncommon", "cost": 150, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (3rd Level)", "description": "Contains a 3rd-level spell from any spell list.", "weight": 0.0, "rarity": "Uncommon", "cost": 300, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (4th Level)", "description": "Contains a 4th-level spell from any spell list.", "weight": 0.0, "rarity": "Rare", "cost": 500, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (5th Level)", "description": "Contains a 5th-level spell from any spell list.", "weight": 0.0, "rarity": "Rare", "cost": 1000, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (6th Level)", "description": "Contains a 6th-level spell from any spell list.", "weight": 0.0, "rarity": "Very Rare", "cost": 2000, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (7th Level)", "description": "Contains a 7th-level spell from any spell list.", "weight": 0.0, "rarity": "Very Rare", "cost": 5000, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (8th Level)", "description": "Contains an 8th-level spell from any spell list.", "weight": 0.0, "rarity": "Very Rare", "cost": 10000, "material": "Parchment", "slot_type": "Scroll"},
            {"name": "Spell Scroll (9th Level)", "description": "Contains a 9th-level spell from any spell list.", "weight": 0.0, "rarity": "Legendary", "cost": 50000, "material": "Parchment", "slot_type": "Scroll"},
            
            # Other Consumables
            {"name": "Bead of Nourishment", "description": "This spongy, flavorless bead dissolves on your tongue and provides nourishment as if you’d eaten a full day's rations.", "weight": 0.0, "rarity": "Common", "cost": 10, "material": "Magic Bead", "slot_type": "Miscellaneous"},
            {"name": "Bead of Refreshment", "description": "This spongy, flavorless bead dissolves on your tongue and provides hydration for a full day.", "weight": 0.0, "rarity": "Common", "cost": 10, "material": "Magic Bead", "slot_type": "Miscellaneous"},
            {"name": "Dust of Disappearance", "description": "Toss this dust in the air to become invisible for 2d4 minutes.", "weight": 0.0, "rarity": "Uncommon", "cost": 200, "material": "Magic Dust", "slot_type": "Miscellaneous"},
            {"name": "Dust of Dryness", "description": "You can sprinkle this dust over water to absorb it. Each pinch can absorb up to 15 cubic feet of water.", "weight": 0.0, "rarity": "Uncommon", "cost": 300, "material": "Magic Dust", "slot_type": "Miscellaneous"},
            {"name": "Feather Token", "description": "A small magical token that can turn into a bird to deliver messages.", "weight": 0.0, "rarity": "Rare", "cost": 500, "material": "Feather", "slot_type": "Miscellaneous"},

            # Common Wondrous Items
            {"name": "Alchemy Jug", "description": "A jug that can produce various liquids, such as water, wine, or acid.", "weight": 12, "rarity": "Uncommon", "cost": 2000, "material": "Ceramic", "slot_type": "Miscellaneous"},
            {"name": "Bag of Holding", "description": "A bag that holds far more than its outside dimensions suggest.", "weight": 15, "rarity": "Uncommon", "cost": 4000, "material": "Cloth", "slot_type": "Miscellaneous"},
            {"name": "Cloak of Elvenkind", "description": "While wearing this cloak with its hood up, Wisdom (Perception) checks to see you have disadvantage.", "weight": 1, "rarity": "Uncommon", "cost": 5000, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Cloak of Protection", "description": "You gain a +1 bonus to AC and saving throws while you wear this cloak.", "weight": 1, "rarity": "Uncommon", "cost": 3000, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Decanter of Endless Water", "description": "This decanter can produce a stream or geyser of water.", "weight": 2, "rarity": "Uncommon", "cost": 4000, "material": "Metal", "slot_type": "Miscellaneous"},
            {"name": "Driftglobe", "description": "A small orb that hovers and emits light when commanded.", "weight": 1, "rarity": "Uncommon", "cost": 750, "material": "Glass", "slot_type": "Orb"},
            {"name": "Eversmoking Bottle", "description": "A bottle that releases smoke, heavily obscuring the area around it.", "weight": 2, "rarity": "Uncommon", "cost": 2500, "material": "Metal", "slot_type": "Miscellaneous"},
            {"name": "Goggles of Night", "description": "While wearing these dark lenses, you have darkvision out to a range of 60 feet.", "weight": 0.1, "rarity": "Uncommon", "cost": 2000, "material": "Glass", "slot_type": "Eyewear"},

            # Rare Wondrous Items
            {"name": "Amulet of Health", "description": "Your Constitution score is 19 while you wear this amulet.", "weight": 1, "rarity": "Rare", "cost": 12000, "material": "Gold", "slot_type": "Amulet"},
            {"name": "Amulet of the Planes", "description": "This amulet allows you to use plane shift.", "weight": 1, "rarity": "Very Rare", "cost": 24000, "material": "Gold", "slot_type": "Amulet"},
            {"name": "Belt of Giant Strength", "description": "Wearing this belt raises your Strength score depending on the type of giant.", "weight": 1, "rarity": "Varies", "cost": 10000, "material": "Leather", "slot_type": "Belt"},
            {"name": "Boots of Levitation", "description": "While wearing these boots, you can cast levitate on yourself at will.", "weight": 2, "rarity": "Rare", "cost": 8000, "material": "Leather", "slot_type": "Boots"},
            {"name": "Boots of Speed", "description": "While you wear these boots, you can use a bonus action to double your walking speed.", "weight": 1, "rarity": "Rare", "cost": 10000, "material": "Leather", "slot_type": "Boots"},
            {"name": "Bracers of Defense", "description": "While wearing these bracers, you gain a +2 bonus to AC if you are wearing no armor.", "weight": 2, "rarity": "Rare", "cost": 12000, "material": "Leather", "slot_type": "Bracers"},
            {"name": "Cape of the Mountebank", "description": "While wearing this cape, you can use Dimension Door as an action.", "weight": 1, "rarity": "Rare", "cost": 15000, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Carpet of Flying", "description": "This magic carpet allows you to fly.", "weight": 5, "rarity": "Very Rare", "cost": 25000, "material": "Cloth", "slot_type": "Miscellaneous"},

            # Very Rare Wondrous Items
            {"name": "Cloak of Displacement", "description": "While wearing this cloak, it creates an illusion that makes you harder to hit.", "weight": 1, "rarity": "Very Rare", "cost": 30000, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Crystal Ball", "description": "This crystal ball allows you to scry.", "weight": 8, "rarity": "Very Rare", "cost": 25000, "material": "Crystal", "slot_type": "Orb"},
            {"name": "Ioun Stone (Various)", "description": "These stones float around your head and grant various effects.", "weight": 0, "rarity": "Varies", "cost": 5000, "material": "Stone", "slot_type": "Miscellaneous"},
            {"name": "Portable Hole", "description": "A portable extradimensional hole.", "weight": 0.5, "rarity": "Rare", "cost": 10000, "material": "Cloth", "slot_type": "Miscellaneous"},
            {"name": "Ring of Invisibility", "description": "While wearing this ring, you can turn invisible at will.", "weight": 0, "rarity": "Legendary", "cost": 50000, "material": "Metal", "slot_type": "Ring"},
            {"name": "Ring of Regeneration", "description": "While wearing this ring, you regain 1d6 hit points every 10 minutes.", "weight": 0, "rarity": "Very Rare", "cost": 30000, "material": "Metal", "slot_type": "Ring"},
            {"name": "Ring of Protection", "description": "You gain a +1 bonus to AC and saving throws while wearing this ring.", "weight": 0, "rarity": "Rare", "cost": 10000, "material": "Metal", "slot_type": "Ring"},
            {"name": "Wand of Fireballs", "description": "This wand allows you to cast the Fireball spell.", "weight": 1, "rarity": "Rare", "cost": 15000, "material": "Wood", "slot_type": "Wand"},
            {"name": "Wand of Lightning Bolts", "description": "This wand allows you to cast the Lightning Bolt spell.", "weight": 1, "rarity": "Rare", "cost": 15000, "material": "Wood", "slot_type": "Wand"},
            
            # Legendary Wondrous Items
            {"name": "Cloak of Invisibility", "description": "While wearing this cloak, you can become invisible for a total of 2 hours per day.", "weight": 1, "rarity": "Legendary", "cost": 60000, "material": "Cloth", "slot_type": "Cloak"},
            {"name": "Talisman of Ultimate Evil", "description": "An evil artifact that grants tremendous power to evil characters.", "weight": 1, "rarity": "Legendary", "cost": 100000, "material": "Metal", "slot_type": "Amulet"},
            {"name": "Talisman of Pure Good", "description": "A good artifact that grants tremendous power to good characters.", "weight": 1, "rarity": "Legendary", "cost": 100000, "material": "Metal", "slot_type": "Amulet"},
            {"name": "Rod of Lordly Might", "description": "This rod can transform into a variety of weapons and tools.", "weight": 5, "rarity": "Legendary", "cost": 75000, "material": "Metal", "slot_type": "Rod"},
            
            # Legendary Items
            {"name": "Vorpal Sword", "description": "This enchanted sword has a chance to instantly decapitate a foe.", "weight": 3, "rarity": "Legendary", "cost": 75000, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Holy Avenger", "description": "This sword provides immense power to paladins, dealing extra radiant damage to fiends and undead.", "weight": 4, "rarity": "Legendary", "cost": 90000, "damage_type": "Radiant", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Staff of the Magi", "description": "A staff that holds immense magical power, allowing a wizard to cast high-level spells.", "weight": 6, "rarity": "Legendary", "cost": 100000, "material": "Wood", "slot_type": "Staff"},
            {"name": "Sword of Sharpness", "description": "This sword can cut through armor and deals additional damage when rolling a critical hit.", "weight": 3, "rarity": "Legendary", "cost": 70000, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Ring of Three Wishes", "description": "This ring contains 1d3 charges, each of which allows you to cast the Wish spell.", "weight": 0, "rarity": "Legendary", "cost": 200000, "material": "Metal", "slot_type": "Ring"},
            {"name": "Robe of the Archmagi", "description": "This robe increases a wizard's AC and saving throws, and enhances spellcasting.", "weight": 1, "rarity": "Legendary", "cost": 80000, "material": "Cloth", "slot_type": "Robe"},
            {"name": "Hammer of Thunderbolts", "description": "A magical hammer that can stun enemies when thrown and deals additional thunder damage.", "weight": 10, "rarity": "Legendary", "cost": 95000, "damage_type": "Bludgeoning", "material": "Metal", "slot_type": "Weapon"},

            # Artifacts
            {"name": "The Book of Exalted Deeds", "description": "A holy book that grants immense power to good-aligned creatures.", "weight": 3, "rarity": "Artifact", "cost": 300000, "material": "Parchment", "slot_type": "Miscellaneous"},
            {"name": "The Book of Vile Darkness", "description": "A foul book that corrupts those who read it, granting them dark powers.", "weight": 3, "rarity": "Artifact", "cost": 300000, "material": "Parchment", "slot_type": "Miscellaneous"},
            {"name": "The Eye of Vecna", "description": "A powerful artifact that must be implanted in place of your own eye. Grants immense magical abilities but at a terrible cost.", "weight": 0.1, "rarity": "Artifact", "cost": 500000, "material": "Unknown", "slot_type": "Miscellaneous"},
            {"name": "The Hand of Vecna", "description": "A powerful artifact that must be grafted to replace your own hand. Grants immense dark powers at a great personal cost.", "weight": 1, "rarity": "Artifact", "cost": 500000, "material": "Unknown", "slot_type": "Miscellaneous"},
            {"name": "The Orb of Dragonkind", "description": "This powerful artifact can control dragons and summon them to your aid.", "weight": 5, "rarity": "Artifact", "cost": 600000, "material": "Crystal", "slot_type": "Orb"},
            {"name": "The Sword of Kas", "description": "A sentient sword that was created to destroy Vecna. It grants immense power but holds its own dark agenda.", "weight": 4, "rarity": "Artifact", "cost": 700000, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "The Talisman of Pure Good", "description": "A talisman that radiates holy power, granting immense benefits to good-aligned creatures.", "weight": 1, "rarity": "Artifact", "cost": 1000000, "material": "Metal", "slot_type": "Amulet"},
            {"name": "The Talisman of Ultimate Evil", "description": "A talisman that corrupts and grants power to evil-aligned creatures.", "weight": 1, "rarity": "Artifact", "cost": 1000000, "material": "Metal", "slot_type": "Amulet"},
            {"name": "The Deck of Many Things", "description": "A deck of cards that grants either great fortune or disaster to those who draw from it.", "weight": 0.5, "rarity": "Artifact", "cost": 500000, "material": "Paper", "slot_type": "Miscellaneous"},
            {"name": "The Blackrazor", "description": "A sentient sword that devours souls and grows stronger with each soul consumed.", "weight": 4, "rarity": "Artifact", "cost": 750000, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "The Axe of the Dwarvish Lords", "description": "A powerful weapon and symbol of authority among dwarves. Grants powers to shape stone and command dwarves.", "weight": 6, "rarity": "Artifact", "cost": 600000, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"}
        ],
        "Pathfinder 2nd Edition": [
            # Simple Weapons
            {"name": "Club", "description": "A simple wooden club.", "weight": 1, "rarity": "Common", "cost": 0, "damage_type": "Bludgeoning", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Dagger", "description": "A small blade used for close combat or throwing.", "weight": 0.5, "rarity": "Common", "cost": 2, "damage_type": "Piercing/Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Spear", "description": "A simple spear used for thrusting attacks.", "weight": 1.5, "rarity": "Common", "cost": 5, "damage_type": "Piercing", "material": "Wood/Metal", "slot_type": "Weapon"},
            
            # Martial Weapons
            {"name": "Longsword", "description": "A versatile sword used by warriors.", "weight": 1.5, "rarity": "Common", "cost": 15, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Greataxe", "description": "A large axe that deals significant damage.", "weight": 3, "rarity": "Common", "cost": 30, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Rapier", "description": "A lightweight sword used for piercing thrusts.", "weight": 1, "rarity": "Uncommon", "cost": 20, "damage_type": "Piercing", "material": "Metal", "slot_type": "Weapon"},
            
            # Ranged Weapons
            {"name": "Shortbow", "description": "A lightweight bow for long-distance combat.", "weight": 1, "rarity": "Common", "cost": 20, "damage_type": "Piercing", "material": "Wood", "slot_type": "Weapon"},
            {"name": "Crossbow", "description": "A mechanical ranged weapon that fires bolts.", "weight": 2, "rarity": "Common", "cost": 35, "damage_type": "Piercing", "material": "Wood/Metal", "slot_type": "Weapon"},
            
            # Advanced Weapons
            {"name": "Flail", "description": "A weapon with a spiked ball attached to a chain for versatile attacks.", "weight": 2, "rarity": "Uncommon", "cost": 10, "damage_type": "Bludgeoning", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Halberd", "description": "A pole weapon with an axe blade for cutting and thrusting attacks.", "weight": 3, "rarity": "Uncommon", "cost": 10, "damage_type": "Slashing/Piercing", "material": "Metal", "slot_type": "Weapon"},
            
            # Exotic Weapons
            {"name": "Kukri", "description": "A short blade with a curved edge, often used by exotic fighters.", "weight": 1, "rarity": "Rare", "cost": 10, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
            {"name": "Katana", "description": "A long curved sword known for its sharpness.", "weight": 1.5, "rarity": "Rare", "cost": 50, "damage_type": "Slashing", "material": "Metal", "slot_type": "Weapon"},
        
            # Light Armor
            {"name": "Padded Armor", "description": "Soft armor made from layers of fabric.", "weight": 8, "rarity": "Common", "cost": 5, "armor_class_bonus": 1, "max_dex_bonus": 4, "material": "Cloth", "slot_type": "Armor"},
            {"name": "Leather Armor", "description": "Simple armor made from toughened leather.", "weight": 10, "rarity": "Common", "cost": 10, "armor_class_bonus": 2, "max_dex_bonus": 3, "material": "Leather", "slot_type": "Armor"},
            {"name": "Studded Leather Armor", "description": "Leather armor reinforced with metal studs.", "weight": 13, "rarity": "Uncommon", "cost": 25, "armor_class_bonus": 3, "max_dex_bonus": 2, "material": "Leather/Metal", "slot_type": "Armor"},
            
            # Medium Armor
            {"name": "Hide Armor", "description": "Armor made from thick animal hides.", "weight": 25, "rarity": "Common", "cost": 20, "armor_class_bonus": 3, "max_dex_bonus": 2, "material": "Hide", "slot_type": "Armor"},
            {"name": "Chain Shirt", "description": "A shirt made of interlocking metal rings.", "weight": 20, "rarity": "Common", "cost": 50, "armor_class_bonus": 4, "max_dex_bonus": 2, "material": "Metal", "slot_type": "Armor"},
            
            # Heavy Armor
            {"name": "Scale Mail", "description": "Armor made of metal scales sewn to a fabric backing.", "weight": 45, "rarity": "Common", "cost": 50, "armor_class_bonus": 4, "max_dex_bonus": 1, "material": "Metal", "slot_type": "Armor"},
            {"name": "Breastplate", "description": "A fitted metal chestplate for protection.", "weight": 30, "rarity": "Uncommon", "cost": 200, "armor_class_bonus": 5, "max_dex_bonus": 1, "material": "Metal", "slot_type": "Armor"},
            {"name": "Full Plate", "description": "Armor that covers the entire body with interlocking plates.", "weight": 65, "rarity": "Rare", "cost": 1500, "armor_class_bonus": 6, "max_dex_bonus": 0, "material": "Metal", "slot_type": "Armor"},
            
            # Shields
            {"name": "Buckler", "description": "A small, lightweight shield used for deflecting attacks.", "weight": 2, "rarity": "Common", "cost": 5, "armor_class_bonus": 1, "material": "Wood/Metal", "slot_type": "Shield"},
            {"name": "Heavy Shield", "description": "A larger shield offering more protection.", "weight": 15, "rarity": "Uncommon", "cost": 20, "armor_class_bonus": 2, "material": "Wood/Metal", "slot_type": "Shield"},
            {"name": "Tower Shield", "description": "A massive shield that covers nearly the entire body.", "weight": 45, "rarity": "Rare", "cost": 100, "armor_class_bonus": 4, "material": "Wood/Metal", "slot_type": "Shield"},
        
            # Potions
            {"name": "Potion of Healing", "description": "Restores hit points to the drinker.", "weight": 0.1, "rarity": "Common", "cost": 50, "effect": "Restores 1d8 hit points", "slot_type": "Consumable"},
            {"name": "Greater Potion of Healing", "description": "Restores a greater amount of hit points.", "weight": 0.1, "rarity": "Uncommon", "cost": 250, "effect": "Restores 4d8 hit points", "slot_type": "Consumable"},
            {"name": "Potion of Invisibility", "description": "Grants the drinker temporary invisibility.", "weight": 0.1, "rarity": "Rare", "cost": 300, "effect": "Grants invisibility for 1 minute", "slot_type": "Consumable"},
            {"name": "Elixir of Life", "description": "Cures poisons and diseases.", "weight": 0.1, "rarity": "Rare", "cost": 500, "effect": "Removes poison and disease effects", "slot_type": "Consumable"},
            
            # Scrolls
            {"name": "Scroll of Fireball", "description": "Casts the Fireball spell.", "weight": 0.05, "rarity": "Common", "cost": 100, "effect": "Casts Fireball (3rd level)", "slot_type": "Consumable"},
            {"name": "Scroll of Teleportation", "description": "Casts the Teleport spell.", "weight": 0.05, "rarity": "Uncommon", "cost": 250, "effect": "Casts Teleport (5th level)", "slot_type": "Consumable"},
            
            # Alchemical Items
            {"name": "Alchemist's Fire", "description": "A flask of volatile liquid that ignites when thrown.", "weight": 1, "rarity": "Common", "cost": 20, "effect": "Deals 1d6 fire damage per round for 1 minute", "slot_type": "Consumable"},
            {"name": "Tanglefoot Bag", "description": "A bag of sticky substance that can entangle foes.", "weight": 1, "rarity": "Uncommon", "cost": 30, "effect": "Entangles target, reducing movement", "slot_type": "Consumable"},
            {"name": "Smokestick", "description": "Creates a cloud of smoke to obscure vision.", "weight": 0.5, "rarity": "Common", "cost": 10, "effect": "Creates a smoke cloud for 1 minute", "slot_type": "Consumable"},

            # Poisons
            {"name": "Drow Poison", "description": "A poison often used by the drow to incapacitate their foes.", "weight": 0.1, "rarity": "Rare", "cost": 200, "effect": "Target falls unconscious if they fail a Fortitude save", "slot_type": "Consumable"},
            {"name": "Wyvern Poison", "description": "A deadly poison harvested from wyvern stingers.", "weight": 0.1, "rarity": "Very Rare", "cost": 500, "effect": "Deals 7d6 poison damage over time", "slot_type": "Consumable"},
        
            # Amulets
            {"name": "Amulet of Natural Armor", "description": "Grants an enhancement bonus to natural armor.", "weight": 0.1, "rarity": "Uncommon", "cost": 300, "effect": "+1 to natural armor", "slot_type": "Neck"},
            {"name": "Amulet of Mighty Fists", "description": "Enhances unarmed strikes and natural weapons.", "weight": 0.1, "rarity": "Rare", "cost": 2000, "effect": "+1 to attack and damage rolls for unarmed strikes", "slot_type": "Neck"},
            
            # Belts
            {"name": "Belt of Giant Strength", "description": "Increases the wearer's Strength score.", "weight": 1, "rarity": "Rare", "cost": 5000, "effect": "Increases Strength by +2", "slot_type": "Waist"},
            {"name": "Belt of Physical Might", "description": "Increases two physical ability scores.", "weight": 1, "rarity": "Very Rare", "cost": 8000, "effect": "Increases Strength and Constitution by +2", "slot_type": "Waist"},
            
            # Cloaks
            {"name": "Cloak of Resistance", "description": "Grants a bonus on all saving throws.", "weight": 0.5, "rarity": "Uncommon", "cost": 1000, "effect": "+1 bonus on all saving throws", "slot_type": "Shoulders"},
            {"name": "Cloak of Invisibility", "description": "Grants temporary invisibility when activated.", "weight": 0.5, "rarity": "Very Rare", "cost": 6000, "effect": "Grants invisibility for up to 10 minutes", "slot_type": "Shoulders"},
            
            # Boots
            {"name": "Boots of Speed", "description": "Increases movement speed and grants a haste effect.", "weight": 1, "rarity": "Rare", "cost": 4000, "effect": "Grants haste for up to 10 rounds per day", "slot_type": "Feet"},
            {"name": "Boots of Levitation", "description": "Allows the wearer to levitate at will.", "weight": 1, "rarity": "Very Rare", "cost": 6000, "effect": "Allows levitation for up to 1 hour per day", "slot_type": "Feet"},
            
            # Headbands
            {"name": "Headband of Inspired Wisdom", "description": "Increases the wearer's Wisdom score.", "weight": 0.2, "rarity": "Rare", "cost": 5000, "effect": "Increases Wisdom by +2", "slot_type": "Head"},
            {"name": "Headband of Mental Superiority", "description": "Increases all mental ability scores.", "weight": 0.2, "rarity": "Very Rare", "cost": 12000, "effect": "Increases Intelligence, Wisdom, and Charisma by +2", "slot_type": "Head"},
            
            # Rings
            {"name": "Ring of Protection", "description": "Grants a deflection bonus to AC.", "weight": 0.05, "rarity": "Uncommon", "cost": 2000, "effect": "+1 deflection bonus to AC", "slot_type": "Ring"},
            {"name": "Ring of Regeneration", "description": "Slowly heals the wearer over time.", "weight": 0.05, "rarity": "Very Rare", "cost": 10000, "effect": "Heals 1 hit point every 10 minutes", "slot_type": "Ring"},
            
            # Bracers
            {"name": "Bracers of Archery", "description": "Improves proficiency with bows.", "weight": 0.5, "rarity": "Rare", "cost": 3000, "effect": "+1 to attack rolls with bows", "slot_type": "Arms"},
            {"name": "Bracers of Defense", "description": "Grants an armor bonus to AC.", "weight": 0.5, "rarity": "Very Rare", "cost": 8000, "effect": "+2 armor bonus to AC", "slot_type": "Arms"},
        
            # Legendary Weapons
            {"name": "Sunblade", "description": "A longsword that functions as a sunlamp and deals radiant damage.", "weight": 2, "rarity": "Legendary", "cost": 0, "damage_type": "Radiant", "effect": "Deals an extra 2d6 radiant damage to undead", "slot_type": "Hand"},
            {"name": "Vorpal Sword", "description": "A blade that can decapitate foes.", "weight": 3, "rarity": "Legendary", "cost": 0, "damage_type": "Slashing", "effect": "On a natural 20, decapitate target", "slot_type": "Hand"},
            
            # Legendary Armor
            {"name": "Armor of Invulnerability", "description": "Grants resistance to all damage types.", "weight": 25, "rarity": "Legendary", "cost": 0, "effect": "Immune to non-magical damage and resistant to all magical damage", "slot_type": "Body"},
            {"name": "Plate of the Dawnflower", "description": "Blessed plate armor that offers immense protection and radiant damage resistance.", "weight": 30, "rarity": "Legendary", "cost": 0, "effect": "+3 bonus to AC, resistance to radiant damage", "slot_type": "Body"},
            
            # Legendary Artifacts
            {"name": "Rod of Lordly Might", "description": "A powerful artifact that can transform into various weapons and tools.", "weight": 5, "rarity": "Artifact", "cost": 0, "effect": "Transforms into various weapons, provides bonuses to Strength", "slot_type": "Hand"},
            {"name": "Staff of the Magi", "description": "A legendary staff with powerful magical abilities.", "weight": 5, "rarity": "Artifact", "cost": 0, "effect": "Stores spell slots, can absorb spells, and cast high-level spells", "slot_type": "Hand"},
            
            # Legendary Wondrous Items
            {"name": "Cloak of the Phoenix", "description": "A cloak that grants the wearer the ability to rise from the ashes after death.", "weight": 1, "rarity": "Legendary", "cost": 0, "effect": "Once per day, rise from death with full hit points", "slot_type": "Shoulders"},
            {"name": "Belt of Dwarvenkind", "description": "A belt that grants dwarven resilience and physical fortitude.", "weight": 1, "rarity": "Legendary", "cost": 0, "effect": "Grants +2 Constitution, advantage on saving throws against poison, and resistance to poison damage", "slot_type": "Waist"},
            
            # Legendary Rings
            {"name": "Ring of Three Wishes", "description": "A ring with the power to grant three wishes.", "weight": 0.05, "rarity": "Legendary", "cost": 0, "effect": "Grants three wishes, one per activation", "slot_type": "Ring"},
            {"name": "Ring of Elemental Command", "description": "Allows control over one of the four elements (fire, water, earth, air).", "weight": 0.05, "rarity": "Legendary", "cost": 0, "effect": "Grants control over a specific element, such as summoning or manipulating elemental forces", "slot_type": "Ring"},
            
            # Legendary Amulets
            {"name": "Amulet of the Planes", "description": "Allows the wearer to shift between planes of existence.", "weight": 0.1, "rarity": "Legendary", "cost": 0, "effect": "Teleport to other planes of existence", "slot_type": "Neck"},
            {"name": "Amulet of Perfect Health", "description": "Grants immunity to diseases and poison, and restores hit points.", "weight": 0.1, "rarity": "Legendary", "cost": 0, "effect": "Immunity to disease, poison, and full restoration of hit points once per day", "slot_type": "Neck"}
        ],
    }

    monsters = {
        "Dungeons & Dragons 5th Edition": [
            {"name": "Goblin", "description": "A small, sneaky creature...", "size": "Small", "hit_points": 7, "armor_class": 15},
            {"name": "Dragon", "description": "A powerful, fire-breathing beast...", "size": "Large", "hit_points": 200, "armor_class": 18},
        ],
    }

    feats = {
        "Dungeons & Dragons 5th Edition": [
            {"name": "Alert", "description": "Always on the lookout for danger. Gain a +5 bonus to initiative and can't be surprised while conscious."},
            {"name": "Athlete", "description": "You have undergone extensive physical training. Increase either your Strength or Dexterity by 1."},
            {"name": "Tough", "description": "Your hit point maximum increases by an amount equal to twice your level."}
        ],
        "Pathfinder": [
            {"name": "Power Attack", "description": "Take a penalty on attack rolls to gain a bonus on damage rolls."},
            {"name": "Toughness", "description": "Gain a flat bonus to hit points."},
            {"name": "Improved Initiative", "description": "Gain a +4 bonus to initiative checks."}
        ],
        "Call of Cthulhu": [
            {"name": "Resilient", "description": "You are naturally tough and recover from mental or physical trauma more quickly."},
            {"name": "Sharp Shooter", "description": "Gain a bonus when firing ranged weapons."}
        ],
        "Shadowrun": [
            {"name": "Ambidextrous", "description": "You can use either hand equally well for any task."},
            {"name": "Toughness", "description": "Gain bonus hit points or resistances."},
            {"name": "Lightning Reflexes", "description": "Improve reaction times in combat."}
        ],
        "Star Wars: Edge of the Empire": [
            {"name": "Quick Draw", "description": "You can draw or holster a weapon as an incidental action."},
            {"name": "Deadly Accuracy", "description": "When you choose a combat skill, your attacks with it deal increased damage."}
        ],
        "Mothership RPG": [
            {"name": "Fearless", "description": "You are immune to fear effects."},
            {"name": "Hardened", "description": "Gain a bonus to resist physical trauma."}
        ]
    }

    spells = {
        "Dungeons & Dragons 5th Edition": [
            {
                "name": "Acid Splash",
                "description": "You hurl a bubble of acid. Choose one creature you can see within range, or choose two creatures within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Blade Ward",
                "description": "You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks.",
                "level": 0,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 round",
                "components": "V, S"
            },
            {
                "name": "Booming Blade",
                "description": "As part of the action used to cast this spell, you must make a melee attack with a weapon against one creature within the spell's range, otherwise the spell fails. On a hit, the target suffers the weapon attack’s normal effects and becomes sheathed in booming energy until the start of your next turn.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "1 round",
                "components": "V, M (a weapon)"
            },
            {
                "name": "Chill Touch",
                "description": "You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "1 round",
                "components": "V, S"
            },
            {
                "name": "Control Flames",
                "description": "You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways: expand the flame, extinguish it, change its brightness or color, or create simple shapes.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "S"
            },
            {
                "name": "Create Bonfire",
                "description": "You create a bonfire on the ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire’s space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Dancing Lights",
                "description": "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can combine the four lights into one glowing, vaguely humanoid form of Medium size.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a bit of phosphorus or wychwood, or a glowworm)"
            },
            {
                "name": "Druidcraft",
                "description": "Whispering to the spirits of nature, you create one of the following effects within range: instantly lighting or snuffing out a candle, predicting the weather, making a flower bloom, or creating harmless sensory effects.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Eldritch Blast",
                "description": "A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Fire Bolt",
                "description": "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Frostbite",
                "description": "You cause numbing frost to form on one creature that you can see within range. The target must make a Constitution saving throw. On a failed save, the target takes 1d6 cold damage, and it has disadvantage on the next weapon attack roll it makes before the end of its next turn.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Green-Flame Blade",
                "description": "As part of the action used to cast this spell, you must make a melee attack with a weapon against one creature within the spell's range. On a hit, the target suffers the weapon attack's normal effects, and green fire leaps from the target to a different creature of your choice within 5 feet of it.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "V, M (a weapon)"
            },
            {
                "name": "Guidance",
                "description": "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the ability check.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Infestation",
                "description": "You cause a cloud of mites, fleas, and other parasites to appear momentarily on one creature you can see within range. The target must succeed on a Constitution saving throw or take 1d6 poison damage and move 5 feet in a random direction.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a living flea)"
            },
            {
                "name": "Light",
                "description": "You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, M (a firefly or phosphorescent moss)"
            },
            {
                "name": "Mage Hand",
                "description": "A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it. You can use the hand to manipulate objects, open doors, retrieve items, or perform other simple tasks.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "1 minute",
                "components": "V, S"
            },
            {
                "name": "Mending",
                "description": "This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, or a torn cloak. As long as the break is no larger than 1 foot in any dimension, you can mend it, leaving no trace of the former damage.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (two lodestones)"
            },
            {
                "name": "Message",
                "description": "You point your finger toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "1 round",
                "components": "V, S, M (a short piece of copper wire)"
            },
            {
                "name": "Minor Illusion",
                "description": "You create a sound or an image of an object within range that lasts for the duration. The illusion ends if you dismiss it or cast this spell again. If you create a sound, its volume can range from a whisper to a scream. The image must fit within a 5-foot cube.",
                "level": 0,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "1 minute",
                "components": "S, M (a bit of fleece)"
            },
            {
                "name": "Mold Earth",
                "description": "You choose a portion of dirt or stone that you can see within range and that fits within a 5-foot cube. You manipulate it in one of the following ways: move earth, cause shapes, or create difficult terrain.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous or 1 hour",
                "components": "S"
            },
            {
                "name": "Poison Spray",
                "description": "You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "10 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Prestidigitation",
                "description": "This spell is a minor magical trick that novice spellcasters use for practice. You create one of the following magical effects: clean or soil an object, chill or warm food, create a sensory effect, or light/extinguish a small fire.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "10 feet",
                "duration": "Up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Produce Flame",
                "description": "A flickering flame appears in your hand. The flame remains there for the duration and harms neither you nor your equipment. You can also hurl the flame at a creature within range, making a ranged spell attack.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "10 minutes",
                "components": "V, S"
            },
            {
                "name": "Ray of Frost",
                "description": "A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Resistance",
                "description": "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one saving throw of its choice. It can roll the die before or after making the saving throw.",
                "level": 0,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a miniature cloak)"
            },
            {
                "name": "Sacred Flame",
                "description": "Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 radiant damage. The target gains no benefit from cover for this saving throw.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Shape Water",
                "description": "You choose an area of water that you can see within range and that fits within a 5-foot cube. You can manipulate it in various ways, such as moving it, changing its shape or color, or freezing it for 1 hour.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous or 1 hour",
                "components": "S"
            },
            {
                "name": "Shocking Grasp",
                "description": "Lightning springs from your hand to deliver a shock to a creature you try to touch. Make a melee spell attack against the target. On a hit, the target takes 1d8 lightning damage, and it can’t take reactions until the start of its next turn.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Spare the Dying",
                "description": "You touch a living creature that has 0 hit points. The creature becomes stable. This spell has no effect on undead or constructs.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Sword Burst",
                "description": "You create a momentary circle of spectral blades that sweep around you. Each creature within 5 feet of you, other than you, must succeed on a Dexterity saving throw or take 1d6 force damage.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Thaumaturgy",
                "description": "You manifest a minor wonder, a sign of supernatural power, within range. You create one of the following magical effects: your voice booms, flames flicker, tremors, an unlocked door opens, or harmless sensory effects.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Up to 1 minute",
                "components": "V"
            },
            {
                "name": "Thorn Whip",
                "description": "You create a long, vine-like whip covered in thorns that lashes out at a creature in range. Make a melee spell attack. On a hit, the creature takes 1d6 piercing damage, and if it's Large or smaller, you pull the creature up to 10 feet closer to you.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (the stem of a plant with thorns)"
            },
            {
                "name": "Thunderclap",
                "description": "You create a burst of thunderous sound, which can be heard 100 feet away. Each creature other than you within 5 feet must succeed on a Constitution saving throw or take 1d6 thunder damage.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "S"
            },
            {
                "name": "Toll the Dead",
                "description": "You point at one creature you can see within range, and the sound of a dolorous bell fills the air around it for a moment. The target must succeed on a Wisdom saving throw or take necrotic damage. If the target is missing hit points, it takes additional damage.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "True Strike",
                "description": "You extend your hand and point a finger at a target in range. Your magic grants you a brief insight into the target’s defenses. On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn’t ended.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 round",
                "components": "S"
            },
            {
                "name": "Vicious Mockery",
                "description": "You unleash a string of insults laced with subtle enchantments at a creature within range. If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on its next attack roll.",
                "level": 0,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Word of Radiance",
                "description": "You utter a divine word, and burning radiance erupts from you. Each creature of your choice that you can see within 5 feet of you must succeed on a Constitution saving throw or take 1d6 radiant damage.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "V, M (a holy symbol)"
            },
            {
                "name": "Alarm",
                "description": "You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (a tiny bell and a piece of fine silver wire)"
            },
            {
                "name": "Animal Friendship",
                "description": "This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "24 hours",
                "components": "V, S, M (a morsel of food)"
            },
            {
                "name": "Armor of Agathys",
                "description": "A protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 cold damage.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V, S, M (a cup of water)"
            },
            {
                "name": "Bane",
                "description": "Up to three creatures of your choice that you can see within range must make Charisma saving throws. Whenever a target that fails this saving throw makes an attack roll or a saving throw before the spell ends, the target must roll a d4 and subtract the number rolled from the attack roll or saving throw.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a drop of blood)"
            },
            {
                "name": "Bless",
                "description": "You bless up to three creatures of your choice within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a sprinkling of holy water)"
            },
            {
                "name": "Burning Hands",
                "description": "As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (15-foot cone)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Charm Person",
                "description": "You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Chromatic Orb",
                "description": "You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range. You choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and then make a ranged spell attack against the target.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a diamond worth at least 50 gp)"
            },
            {
                "name": "Color Spray",
                "description": "A dazzling array of flashing, colored light springs from your hand. Roll 6d10; the total is how many hit points of creatures this spell can affect.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self (15-foot cone)",
                "duration": "1 round",
                "components": "V, S, M (a pinch of powder or sand colored red, yellow, and blue)"
            },
            {
                "name": "Command",
                "description": "You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "1 round",
                "components": "V"
            },
            {
                "name": "Compelled Duel",
                "description": "You attempt to compel a creature into a duel. One creature that you can see within range must make a Wisdom saving throw.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 bonus action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Comprehend Languages",
                "description": "For the duration, you understand the literal meaning of any spoken language that you hear. You also understand any written language that you see.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V, S, M (a pinch of soot and salt)"
            },
            {
                "name": "Create or Destroy Water",
                "description": "You either create or destroy water. Create Water: You create up to 10 gallons of clean water within range in an open container. Destroy Water: You destroy up to 10 gallons of water in an open container within range.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a drop of water if creating water or a few grains of sand if destroying it)"
            },
            {
                "name": "Cure Wounds",
                "description": "A creature you touch regains hit points equal to 1d8 + your spellcasting ability modifier.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Detect Evil and Good",
                "description": "For the duration, you know if there is an aberration, celestial, elemental, fey, fiend, or undead within 30 feet of you.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Detect Magic",
                "description": "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Detect Poison and Disease",
                "description": "For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a yew leaf)"
            },
            {
                "name": "Disguise Self",
                "description": "You make yourself—including your clothing, armor, weapons, and other belongings on your person—look different.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Divine Favor",
                "description": "Your prayer empowers you with divine radiance. Until the spell ends, your weapon attacks deal an extra 1d4 radiant damage on a hit.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Ensnaring Strike",
                "description": "The next time you hit a creature with a weapon attack before this spell ends, writhing mass of thorny vines appears at the point of impact, and the target must succeed on a Strength saving throw or be restrained by the magical vines.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Faerie Fire",
                "description": "Each object in a 20-foot cube within range is outlined in blue, green, or violet light (your choice). Any creature in the area when the spell is cast is also outlined in light if it fails a Dexterity saving throw.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "False Life",
                "description": "Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 temporary hit points for the duration.",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V, S, M (a small amount of alcohol)"
            },
            {
                "name": "Feather Fall",
                "description": "Choose up to five falling creatures within range. A falling creature’s rate of descent slows to 60 feet per round until the spell ends.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 reaction",
                "range": "60 feet",
                "duration": "1 minute",
                "components": "V, M (a small feather or piece of down)"
            },
            {
                "name": "Fog Cloud",
                "description": "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed disperses it.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Goodberry",
                "description": "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry and regain 1 hit point, and the berry provides enough nourishment to sustain a creature for one day.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a sprig of mistletoe)"
            },
            {
                "name": "Grease",
                "description": "Slick grease covers the ground in a 10-foot square centered on a point within range and turns it into difficult terrain for the duration. When the grease appears, each creature standing in its area must succeed on a Dexterity saving throw or fall prone.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "1 minute",
                "components": "V, S, M (a bit of pork rind or butter)"
            },
            {
                "name": "Guiding Bolt",
                "description": "A flash of light streaks toward a creature of your choice within range. Make a ranged spell attack against the target. On a hit, the target takes 4d6 radiant damage, and the next attack roll made against this target before the end of your next turn has advantage.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "1 round",
                "components": "V, S"
            },
            {
                "name": "Healing Word",
                "description": "A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Hellish Rebuke",
                "description": "You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 reaction",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Heroism",
                "description": "A willing creature you touch is imbued with bravery. Until the spell ends, the creature is immune to being frightened and gains temporary hit points equal to your spellcasting ability modifier at the start of each of its turns.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Hunter's Mark",
                "description": "You choose a creature you can see within range and mystically mark it as your quarry. Until the spell ends, you deal an extra 1d6 damage to the target whenever you hit it with a weapon attack.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 bonus action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V"
            },
            {
                "name": "Identify",
                "description": "You choose one object that you must touch throughout the casting of the spell. If it is a magic item or some other magic-imbued object, you learn its properties and how to use them.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a pearl worth at least 100 gp and an owl feather)"
            },
            {
                "name": "Illusory Script",
                "description": "You write on parchment, paper, or some other suitable writing material and imbue it with a potent illusion that lasts for the duration. To you and any creatures you designate, the writing appears normal, written in your hand, and conveys whatever meaning you intended when you wrote it.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "10 days",
                "components": "V, S, M (a lead-based ink worth at least 10 gp, which the spell consumes)"
            },
            {
                "name": "Aid",
                "description": "Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range. Each target’s hit point maximum and current hit points increase by 5 for the duration.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (a tiny strip of white cloth)"
            },
            {
                "name": "Alter Self",
                "description": "You assume a different form. When you cast the spell, choose one of the following options: Aquatic Adaptation, Change Appearance, or Natural Weapons.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Animal Messenger",
                "description": "By means of this spell, you use an animal to deliver a message. Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat. You specify a location and a recipient.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "24 hours",
                "components": "V, S, M (a morsel of food)"
            },
            {
                "name": "Arcane Lock",
                "description": "You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate can open the object normally.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (gold dust worth at least 25 gp, which the spell consumes)"
            },
            {
                "name": "Augury",
                "description": "By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or employing some other divining tool, you receive an omen from an otherworldly entity about the results of a specific course of action.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V, S, M (specially marked sticks, bones, or similar tokens worth at least 25 gp)"
            },
            {
                "name": "Barkskin",
                "description": "You touch a willing creature. Until the spell ends, the target’s skin has a rough, bark-like appearance, and the target’s AC can’t be less than 16, regardless of what kind of armor it is wearing.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a handful of oak bark)"
            },
            {
                "name": "Blindness/Deafness",
                "description": "You can blind or deafen a foe. Choose one creature that you can see within range to make a Constitution saving throw. If it fails, the target is either blinded or deafened (your choice) for the duration.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "1 minute",
                "components": "V"
            },
            {
                "name": "Blur",
                "description": "Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on attack rolls against you.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Branding Smite",
                "description": "The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it’s invisible.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Calm Emotions",
                "description": "You attempt to suppress strong emotions in a group of people. Each humanoid in a 20-foot-radius sphere centered on a point you choose within range must make a Charisma saving throw.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Cloud of Daggers",
                "description": "You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell’s area for the first time on a turn or starts its turn there.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a sliver of glass)"
            },
            {
                "name": "Continual Flame",
                "description": "A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn’t use oxygen. The flame can be covered or hidden but not smothered or quenched.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (ruby dust worth 50 gp, which the spell consumes)"
            },
            {
                "name": "Cordon of Arrows",
                "description": "You plant four pieces of nonmagical ammunition—arrows or crossbow bolts—in the ground within range and lay magic upon them to protect an area. Until the spell ends, whenever a creature other than you comes within 30 feet of the ammunition for the first time on a turn or ends its turn there, one piece of ammunition flies up to strike it.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "8 hours",
                "components": "V, S, M (four or more arrows or bolts)"
            },
            {
                "name": "Crown of Madness",
                "description": "One humanoid of your choice that you can see within range must succeed on a Wisdom saving throw or become charmed by you for the duration. While the target is charmed, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Darkness",
                "description": "Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can’t see through this darkness, and nonmagical light can’t illuminate it.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, M (bat fur and a drop of pitch or piece of coal)"
            },
            {
                "name": "Darkvision",
                "description": "You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S, M (either a pinch of dried carrot or an agate)"
            },
            {
                "name": "Detect Thoughts",
                "description": "For the duration, you can read the thoughts of certain creatures. When you cast the spell and as your action on each turn until the spell ends, you can focus your mind on any one creature that you can see within 30 feet of you.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a copper piece)"
            },
            {
                "name": "Dragon's Breath",
                "description": "You touch one willing creature and imbue it with the power to spew magical energy from its mouth, provided it has one. Choose acid, cold, fire, lightning, or poison. Until the spell ends, the creature can use an action to exhale energy of the chosen type in a 15-foot cone.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 bonus action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a hot pepper)"
            },
            {
                "name": "Dust Devil",
                "description": "Choose an unoccupied 5-foot cube of air that you can see within range. An elemental force that resembles a dust devil appears in the cube and lasts for the spell’s duration.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of dust)"
            },
            {
                "name": "Earthbind",
                "description": "Choose one creature you can see within range. Yellow strips of magical energy loop around the creature. The target must succeed on a Strength saving throw or its flying speed (if any) is reduced to 0 feet for the spell’s duration.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Enhance Ability",
                "description": "You touch a creature and bestow upon it a magical enhancement. Choose one of the following effects: Bear’s Endurance, Bull’s Strength, Cat’s Grace, Eagle’s Splendor, Fox’s Cunning, or Owl’s Wisdom.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (fur or a feather from a beast)"
            },
            {
                "name": "Enlarge/Reduce",
                "description": "You cause a creature or object you can see within range to grow larger or smaller for the duration. Choose either a creature or an object that is neither worn nor carried.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of powdered iron)"
            },
            {
                "name": "Find Steed",
                "description": "You summon a spirit that assumes the form of an unusually intelligent, strong, and loyal steed, creating a long-lasting bond with it.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Flame Blade",
                "description": "You evoke a fiery blade in your free hand. The blade is similar in size and shape to a scimitar, and it lasts for the duration. You can use your action to make a melee spell attack with the fiery blade.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (leaf of sumac)"
            },
            {
                "name": "Flaming Sphere",
                "description": "A 5-foot-diameter sphere of fire appears in an unoccupied space of your choice within range and lasts for the duration.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a bit of tallow, a pinch of brimstone, and a dusting of powdered iron)"
            },
            {
                "name": "Gentle Repose",
                "description": "You touch a corpse or other remains. For the duration, the target is protected from decay and can’t become undead.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "10 days",
                "components": "V, S, M (a pinch of salt and one copper piece placed on each of the corpse’s eyes)"
            },
            {
                "name": "Gust of Wind",
                "description": "A line of strong wind 60 feet long and 10 feet wide blasts from you in a direction you choose for the spell’s duration.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (60-foot line)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a legume seed)"
            },
            {
                "name": "Heat Metal",
                "description": "Choose a manufactured metal object, such as a metal weapon or a suit of heavy or medium metal armor, that you can see within range. You cause the object to glow red-hot.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a piece of iron and a flame)"
            },
            {
                "name": "Hold Person",
                "description": "Choose a humanoid that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a small, straight piece of iron)"
            },
            {
                "name": "Invisibility",
                "description": "A creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target’s person.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (an eyelash encased in gum arabic)"
            },
            {
                "name": "Knock",
                "description": "Choose an object that you can see within range. The object can be a door, a box, a chest, a set of manacles, a padlock, or another object that contains a mundane or magical means that prevents access. A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Lesser Restoration",
                "description": "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Levitate",
                "description": "One creature or object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (either a small leather loop or a piece of golden wire bent into a cup shape with a long shank on one end)"
            },
            {
                "name": "Locate Object",
                "description": "Describe or name an object that is familiar to you. You sense the direction to the object’s location, as long as that object is within 1,000 feet of you. If the object is in motion, you know the direction of its movement.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a forked twig)"
            },
            {
                "name": "Magic Mouth",
                "description": "You implant a message within an object in range, a message that is uttered when a trigger condition is met. Choose an object that you can see and that isn’t being worn or carried by another creature. Then speak the message, which must be 25 words or less.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "Until dispelled",
                "components": "V, S, M (a small bit of honeycomb and jade dust worth at least 10 gp, which the spell consumes)"
            },
            {
                "name": "Magic Weapon",
                "description": "You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +1 bonus to attack rolls and damage rolls.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 bonus action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Melf's Acid Arrow",
                "description": "A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (powdered rhubarb leaf and an adder’s stomach)"
            },
            {
                "name": "Mirror Image",
                "description": "Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting position so it’s impossible to track which image is real. Each time a creature targets you with an attack during the spell’s duration, roll a d20 to determine whether the attack instead targets one of your duplicates.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 minute",
                "components": "V, S"
            },
            {
                "name": "Misty Step",
                "description": "Briefly surrounded by silvery mist, you teleport up to 30 feet to an unoccupied space that you can see.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Moonbeam",
                "description": "A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high cylinder centered on a point within range. Until the spell ends, dim light fills the cylinder.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (several seeds of any moonseed plant and a piece of opalescent feldspar)"
            },
            {
                "name": "Nystul's Magic Aura",
                "description": "You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn’t being carried or worn by another creature.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "24 hours",
                "components": "V, S, M (a small square of silk)"
            },
            {
                "name": "Pass Without Trace",
                "description": "A veil of shadows and silence radiates from you, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you has a +10 bonus to Dexterity (Stealth) checks and can’t be tracked except by magical means.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (ashes from a burned leaf of mistletoe and a sprig of spruce)"
            },
            {
                "name": "Phantasmal Force",
                "description": "You craft an illusion that takes root in the mind of a creature that you can see within range. The target must make an Intelligence saving throw. On a failed save, you create a phantasmal object, creature, or other visible phenomenon of your choice that is no larger than a 10-foot cube and that is perceivable only to the target.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a bit of fleece)"
            },
            {
                "name": "Prayer of Healing",
                "description": "Up to six creatures of your choice that you can see within range each regain hit points equal to 2d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "10 minutes",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Protection from Poison",
                "description": "You touch a creature. If it is poisoned, you neutralize the poison. If more than one poison afflicts the target, you neutralize one poison that you know is present, or you neutralize one at random.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Ray of Enfeeblement",
                "description": "A black beam of enervating energy springs from your finger toward a creature within range. Make a ranged spell attack against the target. On a hit, the target deals only half damage with weapon attacks that use Strength until the spell ends.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Rope Trick",
                "description": "You touch a length of rope that is up to 60 feet long. One end of the rope then rises into the air until the whole rope hangs perpendicular to the ground. At the upper end of the rope, an invisible entrance opens to an extradimensional space that lasts until the spell ends.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (powdered corn extract and a twisted loop of parchment)"
            },
            {
                "name": "See Invisibility",
                "description": "For the duration, you see invisible creatures and objects as if they were visible, and you can see into the Ethereal Plane.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V, S, M (a pinch of talc and a small sprinkling of powdered silver)"
            },
            {
                "name": "Shatter",
                "description": "A sudden loud ringing noise, painfully intense, erupts from a point of your choice within range. Each creature in a 10-foot-radius sphere centered on that point must make a Constitution saving throw. A creature takes 3d8 thunder damage on a failed save, or half as much damage on a successful one.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a chip of mica)"
            },
            {
                "name": "Silence",
                "description": "For the duration, no sound can be created within or pass through a 20-foot-radius sphere centered on a point you choose within range.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Spider Climb",
                "description": "Until the spell ends, one willing creature you touch gains the ability to move up, down, and across vertical surfaces and upside down along ceilings, while leaving its hands free.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a drop of bitumen and a spider)"
            },
            {
                "name": "Spike Growth",
                "description": "The ground in a 20-foot radius centered on a point within range twists and sprouts hard spikes and thorns. The area becomes difficult terrain for the duration.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (seven sharp thorns or seven small twigs, each sharpened to a point)"
            },
            {
                "name": "Spiritual Weapon",
                "description": "You create a floating, spectral weapon within range that lasts for the duration or until you cast this spell again. When you cast the spell, you can make a melee spell attack against a creature within 5 feet of the weapon.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "60 feet",
                "duration": "1 minute",
                "components": "V, S"
            },
            {
                "name": "Suggestion",
                "description": "You suggest a course of activity (limited to a sentence or two) and magically influence a creature you can see within range that can hear and understand you.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 8 hours",
                "components": "V, M (a snake’s tongue and either a bit of honeycomb or a drop of sweet oil)"
            },
            {
                "name": "Warding Bond",
                "description": "This spell wards a willing creature you touch and creates a mystic connection between you and the target until the spell ends. While the target is within 60 feet of you, it gains a +1 bonus to AC and saving throws, and it has resistance to all damage.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (a pair of platinum rings worth at least 50 gp each, which you and the target must wear for the duration)"
            },
            {
                "name": "Zone of Truth",
                "description": "You create a magical zone that guards against deception in a 15-foot-radius sphere centered on a point of your choice within range.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "10 minutes",
                "components": "V, S"
            },
            {
                "name": "Animate Dead",
                "description": "This spell creates an undead servant. Choose a pile of bones or a corpse of a Medium or Small humanoid within range. Your spell imbues the target with a foul mimicry of life, raising it as an undead creature.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 minute",
                "range": "10 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a drop of blood, a piece of flesh, and a pinch of bone dust)"
            },
            {
                "name": "Bestow Curse",
                "description": "You touch a creature, and that creature must succeed on a Wisdom saving throw or become cursed for the duration of the spell.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Blink",
                "description": "Roll a d20 at the end of each of your turns for the duration of the spell. On a roll of 11 or higher, you vanish from your current plane of existence and appear in the Ethereal Plane.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 minute",
                "components": "V, S"
            },
            {
                "name": "Call Lightning",
                "description": "A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see 100 feet directly above you. Until the spell ends, you can use your action to call down lightning bolts from the cloud to strike targets below.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Clairvoyance",
                "description": "You create an invisible sensor within range in a location familiar to you or in an obvious location that is unfamiliar to you. The sensor remains in place for the duration, and it can’t be attacked or otherwise interacted with.",
                "level": 3,
                "school": "Divination",
                "casting_time": "10 minutes",
                "range": "1 mile",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing)"
            },
            {
                "name": "Counterspell",
                "description": "You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 reaction",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "S"
            },
            {
                "name": "Create Food and Water",
                "description": "You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Daylight",
                "description": "A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet. If you choose a point on an object you are holding or one that isn’t being worn or carried, the light shines from the object and moves with it.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Dispel Magic",
                "description": "Choose one creature, object, or magical effect within range. Any spell of 3rd level or lower on the target ends. For each spell of 4th level or higher on the target, make an ability check using your spellcasting ability.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Elemental Weapon",
                "description": "A nonmagical weapon you touch becomes a magic weapon. Choose one of the following damage types: acid, cold, fire, lightning, or thunder. For the duration, the weapon has a +1 bonus to attack rolls and deals an extra 1d4 damage of the chosen type.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Fear",
                "description": "You project a phantasmal image of the most fearsome creature imaginable. Each creature in a 30-foot cone must succeed on a Wisdom saving throw or drop whatever it is holding and become frightened for the duration.",
                "level": 3,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self (30-foot cone)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a white feather or the heart of a hen)"
            },
            {
                "name": "Fireball",
                "description": "A bright streak flashes from your pointing finger to a point you choose within range, then blossoms with a low roar into an explosion of flame.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a tiny ball of bat guano and sulfur)"
            },
            {
                "name": "Fly",
                "description": "You touch a willing creature. The target gains a flying speed of 60 feet for the duration.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a wing feather from any bird)"
            },
            {
                "name": "Gaseous Form",
                "description": "You transform a willing creature you touch, along with everything it’s wearing and carrying, into a misty cloud for the duration.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a bit of gauze and a wisp of smoke)"
            },
            {
                "name": "Glyph of Warding",
                "description": "When you cast this spell, you inscribe a glyph that harms other creatures, either upon a surface or within an object that can be closed to conceal the glyph. If you choose a surface, the glyph can cover an area no larger than 10 feet in diameter.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Until dispelled or triggered",
                "components": "V, S, M (incense and powdered diamond worth at least 200 gp, which the spell consumes)"
            },
            {
                "name": "Haste",
                "description": "Choose a willing creature that you can see within range. Until the spell ends, the target’s speed is doubled, it gains a +2 bonus to AC, it has advantage on Dexterity saving throws, and it gains an additional action on each of its turns.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a shaving of licorice root)"
            },
            {
                "name": "Hypnotic Pattern",
                "description": "You create a twisting pattern of colors that weaves through the air inside a 30-foot cube within range. The pattern appears for a moment and vanishes. Each creature in the area who sees the pattern must make a Wisdom saving throw.",
                "level": 3,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a glowing stick of incense or a crystal vial filled with phosphorescent material)"
            },
            {
                "name": "Leomund's Tiny Hut",
                "description": "A 10-foot-radius immobile dome of force springs into existence around and above you and remains stationary for the duration. The spell ends if you leave its area.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 minute",
                "range": "Self (10-foot radius)",
                "duration": "8 hours",
                "components": "V, S, M (a small crystal bead)"
            },
            {
                "name": "Lightning Bolt",
                "description": "A stroke of lightning forming a line 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line must make a Dexterity saving throw. A creature takes 8d6 lightning damage on a failed save, or half as much damage on a successful one.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (100-foot line)",
                "duration": "Instantaneous",
                "components": "V, S, M (a bit of fur and a rod of amber, crystal, or glass)"
            },
            {
                "name": "Magic Circle",
                "description": "You create a 10-foot-radius, 20-foot-tall cylinder of magical energy centered on a point on the ground that you can see within range. Glowing runes appear wherever the cylinder intersects with the floor or other surface.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 minute",
                "range": "10 feet",
                "duration": "1 hour",
                "components": "V, S, M (holy water or powdered silver and iron worth at least 100 gp, which the spell consumes)"
            },
            {
                "name": "Major Image",
                "description": "You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 20-foot cube. The image appears at a spot within range and lasts for the duration.",
                "level": 3,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a bit of fleece)"
            },
            {
                "name": "Mass Healing Word",
                "description": "As you call out words of restoration, up to six creatures of your choice that you can see within range regain hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Meld into Stone",
                "description": "You step into a stone object or surface large enough to fully contain your body, melding yourself and all the equipment you carry with the stone for the duration.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S"
            },
            {
                "name": "Nondetection",
                "description": "For the duration, you hide a target that you touch from divination magic. The target can be a willing creature, a place, or an object no larger than 10 feet in any dimension.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S, M (a pinch of diamond dust worth 25 gp sprinkled over the target, which the spell consumes)"
            },
            {
                "name": "Phantom Steed",
                "description": "A Large quasi-real, horselike creature appears on the ground in an unoccupied space of your choice within range. You decide the creature’s appearance, but it has the statistics of a riding horse.",
                "level": 3,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Plant Growth",
                "description": "This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action or 8 hours",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Protection from Energy",
                "description": "For the duration, the willing creature you touch has resistance to one damage type of your choice: acid, cold, fire, lightning, or thunder.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Remove Curse",
                "description": "At your touch, all curses affecting one creature or object end. If the object is a cursed magic item, its curse remains, but the spell breaks its owner’s attunement to the object so it can be removed or discarded.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Revivify",
                "description": "You touch a creature that has died within the last minute. That creature returns to life with 1 hit point. This spell can’t return to life a creature that has died of old age, nor can it restore any missing body parts.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (diamonds worth 300 gp, which the spell consumes)"
            },
            {
                "name": "Sending",
                "description": "You send a short message of twenty-five words or less to a creature with which you are familiar. The creature hears the message in its mind, recognizes you as the sender if it knows you, and can answer in a like manner immediately.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Unlimited",
                "duration": "1 round",
                "components": "V, S, M (a short piece of fine copper wire)"
            },
            {
                "name": "Sleet Storm",
                "description": "Until the spell ends, freezing rain and sleet fall in a 20-foot-tall cylinder with a 40-foot radius centered on a point you choose within range. The area is heavily obscured, and exposed flames in the area are doused.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of dust and a few drops of water)"
            },
            {
                "name": "Slow",
                "description": "You alter time around up to six creatures of your choice in a 40-foot cube within range. Each target must succeed on a Wisdom saving throw or be affected by this spell for the duration.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a drop of molasses)"
            },
            {
                "name": "Spirit Guardians",
                "description": "You call forth spirits to protect you. They flit around you to a distance of 15 feet for the duration. If you are good or neutral, their spectral form appears angelic or fey (your choice).",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Self (15-foot radius)",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a holy symbol)"
            },
            {
                "name": "Stinking Cloud",
                "description": "You create a 20-foot-radius sphere of yellow, nauseating gas centered on a point within range. The cloud spreads around corners, and its area is heavily obscured. The cloud lingers in the air for the duration.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a rotten egg or several skunk cabbage leaves)"
            },
            {
                "name": "Thunder Step",
                "description": "You teleport yourself to an unoccupied space you can see within range. Immediately after you disappear, a thunderous boom sounds, and each creature within 10 feet of the space you left must make a Constitution saving throw.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Tidal Wave",
                "description": "You conjure up a wave of water that crashes down on an area within range. The area can be up to 30 feet long, up to 10 feet wide, and up to 10 feet tall. Each creature in that area must make a Dexterity saving throw.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a drop of water)"
            },
            {
                "name": "Tiny Servant",
                "description": "You touch one Tiny, nonmagical object that isn’t attached to another object or a surface and isn’t being carried by another creature. The target animates and sprouts legs, becoming a creature under your control until the spell ends or until it drops to 0 hit points.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S"
            },
            {
                "name": "Tongues",
                "description": "This spell grants the creature you touch the ability to understand any spoken language it hears. Moreover, when the target speaks, any creature that knows at least one language and can hear the target understands what it says.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, M (a small clay model of a ziggurat)"
            },
            {
                "name": "Vampiric Touch",
                "description": "The touch of your shadow-wreathed hand can siphon life force from others to heal your wounds. Make a melee spell attack against a creature within your reach. On a hit, the target takes 3d6 necrotic damage, and you regain hit points equal to half the amount of necrotic damage dealt.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Wall of Water",
                "description": "You conjure up a wall of water on the ground at a point you can see within range. You can make the wall up to 30 feet long, 10 feet high, and 1 foot thick, or you can make a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a drop of water)"
            },
            {
                "name": "Arcane Eye",
                "description": "You create an invisible, magical eye within range that hovers in the air for the duration. You mentally receive visual information from the eye, which has normal vision and darkvision out to 30 feet.",
                "level": 4,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a bit of bat fur)"
            },
            {
                "name": "Banishment",
                "description": "You attempt to send one creature that you can see within range to another plane of existence. The target must succeed on a Charisma saving throw or be banished.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (an item distasteful to the target)"
            },
            {
                "name": "Blight",
                "description": "Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality. The target must make a Constitution saving throw, taking 8d8 necrotic damage on a failed save, or half as much on a successful one.",
                "level": 4,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Compulsion",
                "description": "Creatures of your choice that you can see within range and that can hear you must make a Wisdom saving throw. On a failed save, a target is affected by this spell. Until the spell ends, you can use a bonus action on each of your turns to designate a direction that is horizontal to you.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Confusion",
                "description": "This spell assaults and twists creatures’ minds, spawning delusions and provoking uncontrolled actions. Each creature in a 10-foot-radius sphere centered on a point you choose within range must succeed on a Wisdom saving throw when you cast this spell or be affected by it.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (three nut shells)"
            },
            {
                "name": "Conjure Minor Elementals",
                "description": "You summon elementals that appear in unoccupied spaces that you can see within range. You choose one of the following options for what appears: one elemental of challenge rating 2 or lower, two elementals of challenge rating 1 or lower, or four elementals of challenge rating 1/2 or lower.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "90 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Control Water",
                "description": "Until the spell ends, you can control any freestanding water inside an area you choose that is a cube up to 100 feet on each side. You can choose from any of the following effects when you cast this spell.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a drop of water and a pinch of dust)"
            },
            {
                "name": "Dimension Door",
                "description": "You teleport yourself from your current location to any other spot within range. You arrive exactly at the spot desired. It can be a place you can see, one you can visualize, or one you can describe by stating distance and direction.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "500 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Divination",
                "description": "Your magic and an offering put you in contact with a god or a god’s servants. You ask a single question concerning a specific goal, event, or activity to occur within 7 days.",
                "level": 4,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V, S, M (incense and a sacrificial offering appropriate to your religion worth at least 25 gp)"
            },
            {
                "name": "Dominate Beast",
                "description": "You attempt to beguile a beast that you can see within range. It must succeed on a Wisdom saving throw or be charmed by you for the duration. If you or creatures that are friendly to you are fighting it, it has advantage on the saving throw.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Evard’s Black Tentacles",
                "description": "Squirming, ebony tentacles fill a 20-foot square on ground that you can see within range. For the duration, these tentacles turn the ground in the area into difficult terrain.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a piece of tentacle from a giant octopus or a giant squid)"
            },
            {
                "name": "Fabricate",
                "description": "You convert raw materials into products of the same material. For example, you can fabricate a wooden bridge from a clump of trees, a rope from a patch of hemp, and clothes from flax or wool.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "10 minutes",
                "range": "120 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Faithful Hound",
                "description": "You conjure a phantom watchdog in an unoccupied space that you can see within range, where it remains for the duration, until you dismiss it as an action, or until you move more than 100 feet away from it.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (a tiny silver whistle, a piece of bone, and a thread)"
            },
            {
                "name": "Fire Shield",
                "description": "Thin and wispy flames wreathe your body for the duration, shedding bright light in a 10-foot radius and dim light for an additional 10 feet. The flames provide you with a warm shield or a chill shield, as you choose.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "10 minutes",
                "components": "V, S, M (a bit of phosphorus or a firefly)"
            },
            {
                "name": "Freedom of Movement",
                "description": "For the duration, the target’s movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target’s speed nor cause the target to be paralyzed or restrained.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (a leather strap, bound around the arm or a similar appendage)"
            },
            {
                "name": "Giant Insect",
                "description": "You transform up to ten centipedes, three spiders, five wasps, or one scorpion within range into giant versions of their natural forms for the duration.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Greater Invisibility",
                "description": "You or a creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target’s person.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Guardian of Faith",
                "description": "A Large spectral guardian appears and hovers for the duration in an unoccupied space of your choice that you can see within range. The guardian occupies that space and is indistinct except for a gleaming sword and shield emblazoned with the symbol of your deity.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V"
            },
            {
                "name": "Hallucinatory Terrain",
                "description": "You make natural terrain in a 150-foot cube in range look, sound, and smell like some other sort of natural terrain. Open fields or a road could be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "10 minutes",
                "range": "300 feet",
                "duration": "24 hours",
                "components": "V, S, M (a stone, a twig, and a bit of green plant)"
            },
            {
                "name": "Ice Storm",
                "description": "A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high cylinder centered on a point within range. Each creature in the cylinder must make a Dexterity saving throw. A creature takes 2d8 bludgeoning damage and 4d6 cold damage on a failed save, or half as much damage on a successful one.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a pinch of dust and a few drops of water)"
            },
            {
                "name": "Leomund’s Secret Chest",
                "description": "You hide a chest, and all its contents, on the Ethereal Plane. You must touch the chest and the miniature replica that serves as a material component for the spell. The chest can contain up to 12 cubic feet of nonliving material.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (the chest (3 ft. by 2 ft. by 2 ft.) constructed from rare materials worth at least 5,000 gp, and a tiny replica made from the same materials worth at least 50 gp)"
            },
            {
                "name": "Locate Creature",
                "description": "Describe or name a creature that is familiar to you. You sense the direction to the creature’s location, as long as that creature is within 1,000 feet of you. If the creature is moving, you know the direction of its movement.",
                "level": 4,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a bit of fur from a bloodhound)"
            },
            {
                "name": "Mordenkainen’s Faithful Hound",
                "description": "You conjure a phantom watchdog in an unoccupied space that you can see within range, where it remains for the duration. The hound is invisible to all creatures except you and can’t be harmed.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (a tiny silver whistle, a piece of bone, and a thread)"
            },
            {
                "name": "Mordenkainen’s Private Sanctum",
                "description": "You make an area within range magically secure. The area is a cube that can be as small as 5 feet or as large as 100 feet on each side. The spell lasts for the duration or until you use an action to dismiss it.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "10 minutes",
                "range": "120 feet",
                "duration": "24 hours",
                "components": "V, S, M (a thin sheet of lead, a piece of opaque glass, a wad of cotton, and powdered chrysolite)"
            },
            {
                "name": "Otiluke’s Resilient Sphere",
                "description": "A sphere of shimmering force encloses a creature or object of Large size or smaller within range. An unwilling creature must make a Dexterity saving throw. On a failed save, the creature is enclosed for the duration.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic)"
            },
            {
                "name": "Phantasmal Killer",
                "description": "You tap into the nightmares of a creature you can see within range and create an illusory manifestation of its deepest fears, visible only to that creature. The target must make a Wisdom saving throw. On a failed save, the target becomes frightened for the duration.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Polymorph",
                "description": "This spell transforms a creature that you can see within range into a new form. An unwilling creature must make a Wisdom saving throw to avoid the effect. The transformation lasts for the duration, or until the target drops to 0 hit points or dies.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a caterpillar cocoon)"
            },
            {
                "name": "Staggering Smite",
                "description": "The next time you hit a creature with a melee weapon attack during this spell’s duration, your weapon pierces both body and mind, and the attack deals an extra 4d6 psychic damage to the target.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Stone Shape",
                "description": "You touch a stone object of Medium size or smaller or a section of stone no more than 5 feet in any dimension and form it into any shape that suits your purpose.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (soft clay, which must be worked into roughly the desired shape of the stone object)"
            },
            {
                "name": "Stoneskin",
                "description": "This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (diamond dust worth 100 gp, which the spell consumes)"
            },
            {
                "name": "Summon Greater Demon",
                "description": "You utter foul words, summoning one demon from the chaos of the Abyss. You choose the demon’s type, which must be of challenge rating 5 or lower, such as a shadow demon or a barlgura. The demon appears in an unoccupied space you can see within range, and the demon disappears when it drops to 0 hit points or when the spell ends.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a vial of blood from a humanoid killed within the past 24 hours)"
            },
            {
                "name": "Wall of Fire",
                "description": "You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a small piece of phosphorus)"
            },
            {
                "name": "Watery Sphere",
                "description": "You conjure up a sphere of water with a 10-foot radius at a point you can see within range. The sphere can hover but no more than 10 feet off the ground. The sphere remains for the spell’s duration.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a droplet of water)"
            },
            {
                "name": "Arcane Hand",
                "description": "You create a Large hand of shimmering, translucent force in an unoccupied space that you can see within range. The hand lasts for the spell’s duration and moves at your command, mimicking the movements of your own hand.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (an eggshell and a snake scale)"
            },
            {
                "name": "Freedom of Movement",
                "description": "For the duration, the target’s movement is unaffected by difficult terrain, and spells and other magical effects can neither reduce the target’s speed nor cause the target to be paralyzed or restrained.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (a leather strap, bound around the arm or a similar appendage)"
            },
            {
                "name": "Phantasmal Killer",
                "description": "You tap into the nightmares of a creature you can see within range and create an illusory manifestation of its deepest fears, visible only to that creature. The target must make a Wisdom saving throw. On a failed save, the target becomes frightened for the duration.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Guardian of Faith",
                "description": "A Large spectral guardian appears and hovers for the duration in an unoccupied space of your choice that you can see within range. The guardian occupies that space and is indistinct except for a gleaming sword and shield emblazoned with the symbol of your deity.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V"
            },
            {
                "name": "Death Ward",
                "description": "You touch a creature and grant it a measure of protection from death. The first time the target would drop to 0 hit points as a result of taking damage, the target instead drops to 1 hit point, and the spell ends.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S"
            },
            {
                "name": "Control Water",
                "description": "Until the spell ends, you can control any freestanding water inside an area you choose that is a cube up to 100 feet on each side. You can choose from any of the following effects when you cast this spell.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a drop of water and a pinch of dust)"
            },
            {
                "name": "Conjure Woodland Beings",
                "description": "You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears: one fey creature of challenge rating 2 or lower, two fey creatures of challenge rating 1 or lower, or four fey creatures of challenge rating 1/2 or lower.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (one holly berry per creature summoned)"
            },
            {
                "name": "Animate Objects",
                "description": "Objects come to life at your command. Choose up to ten nonmagical objects within range that are not being worn or carried. Medium targets count as two objects, Large targets count as four objects, Huge targets count as eight objects.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Antilife Shell",
                "description": "A shimmering barrier extends out from you in a 10-foot radius and moves with you, remaining centered on you and hedging out creatures other than undead and constructs. The barrier lasts for the duration.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self (10-foot radius)",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Awaken",
                "description": "After spending the casting time tracing magical pathways within a precious gemstone, you touch a Huge or smaller beast or plant. The target must have either no Intelligence score or an Intelligence of 3 or less.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "8 hours",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (an agate worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Banishing Smite",
                "description": "The next time you hit a creature with a weapon attack before this spell ends, your weapon crackles with force, and the attack deals an extra 5d10 force damage to the target. If this attack reduces the target to 50 hit points or fewer, you banish it.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 bonus action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Bigby's Hand",
                "description": "You create a Large hand of shimmering, translucent force in an unoccupied space that you can see within range. The hand lasts for the spell’s duration, and it moves at your command, mimicking the movements of your own hand.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (an eggshell and a snake scale)"
            },
            {
                "name": "Circle of Power",
                "description": "Divine energy radiates from you, distorting and diffusing magical energy within a 30-foot radius around you. Until the spell ends, the sphere moves with you, centered on you.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self (30-foot radius)",
                "duration": "Concentration, up to 10 minutes",
                "components": "V"
            },
            {
                "name": "Cloudkill",
                "description": "You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a point you choose within range. The fog spreads around corners. It lasts for the duration or until strong wind disperses it.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Commune",
                "description": "You contact your deity or a divine proxy and ask up to three questions that can be answered with a yes or no. You must ask your questions before the spell ends.",
                "level": 5,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "1 minute",
                "components": "V, S, M (incense and a vial of holy or unholy water)"
            },
            {
                "name": "Commune with Nature",
                "description": "You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you.",
                "level": 5,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Cone of Cold",
                "description": "A blast of cold air erupts from your hands. Each creature in a 60-foot cone must make a Constitution saving throw. A creature takes 8d8 cold damage on a failed save, or half as much damage on a successful one.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (60-foot cone)",
                "duration": "Instantaneous",
                "components": "V, S, M (a small crystal or glass cone)"
            },
            {
                "name": "Conjure Elemental",
                "description": "You call forth an elemental servant. Choose an area of air, earth, fire, or water that fills a 10-foot cube within range. An elemental of challenge rating 5 or lower appropriate to the area you chose appears in an unoccupied space within 10 feet of it.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "90 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (burning incense for air, soft clay for earth, sulfur and phosphorus for fire, and water and sand for water)"
            },
            {
                "name": "Contact Other Plane",
                "description": "You mentally contact a demigod, the spirit of a long-dead sage, or some other mysterious entity from another plane. Contacting this extraplanar intelligence can strain or even break your mind.",
                "level": 5,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "1 minute",
                "components": "V"
            },
            {
                "name": "Contagion",
                "description": "Your touch inflicts disease. Make a melee spell attack against a creature within your reach. On a hit, you infect the target with a disease of your choice, such as blinding sickness, filth fever, flesh rot, mindfire, seizure, or slimy doom.",
                "level": 5,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "7 days",
                "components": "V, S"
            },
            {
                "name": "Control Winds",
                "description": "You take control of the air in a 100-foot cube that you can see within range. Choose one of the following effects when you cast the spell: gusts, downdraft, or updraft. You can change the effect as an action on subsequent turns.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Creation",
                "description": "You pull wisps of shadow material from the Shadowfell to create a nonliving object of vegetable matter within range: soft goods, rope, wood, or something similar. You can also use the spell to create mineral objects such as stone, crystal, or metal.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "Special",
                "components": "V, S, M (a tiny piece of matter of the same type of the item you plan to create)"
            },
            {
                "name": "Destructive Wave",
                "description": "You strike the ground, creating a burst of divine energy that ripples outward from you. Each creature you choose within 30 feet of you must succeed on a Constitution saving throw or take 5d6 thunder damage, as well as 5d6 radiant or necrotic damage (your choice).",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (30-foot radius)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Dispel Evil and Good",
                "description": "Shimmering energy surrounds and protects you from fey, undead, and creatures originating from beyond the Material Plane. For the duration, celestials, elementals, fey, fiends, and undead have disadvantage on attack rolls against you.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (holy water or powdered silver and iron)"
            },
            {
                "name": "Dominate Person",
                "description": "You attempt to beguile a humanoid that you can see within range. It must succeed on a Wisdom saving throw or be charmed by you for the duration. While the target is charmed, you have a telepathic link with it.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Dream",
                "description": "This spell shapes a creature’s dreams. Choose a creature known to you as the target of this spell. The target must be on the same plane of existence as you.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "Special",
                "duration": "8 hours",
                "components": "V, S, M (a handful of sand, a dab of ink, and a writing quill plucked from a sleeping bird)"
            },
            {
                "name": "Flame Strike",
                "description": "A vertical column of divine fire roars down from the heavens in a location you specify. Each creature in a 10-foot-radius, 40-foot-high cylinder centered on a point within range must make a Dexterity saving throw.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a pinch of sulfur)"
            },
            {
                "name": "Geas",
                "description": "You place a magical command on a creature that you can see within range, forcing it to carry out some service or refrain from some action or course of activity as you decide.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 minute",
                "range": "60 feet",
                "duration": "30 days",
                "components": "V"
            },
            {
                "name": "Greater Restoration",
                "description": "You imbue a creature you touch with positive energy to undo a debilitating effect. You can reduce the target’s exhaustion level by one, or end one of the following effects on the target: one charm, one curse, any reduction to ability scores, or one effect reducing hit point maximum.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (diamond dust worth at least 100 gp, which the spell consumes)"
            },
            {
                "name": "Hallow",
                "description": "You touch a point and infuse an area around it with holy (or unholy) power. The area can have a radius up to 60 feet, and the spell lasts for the duration.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "24 hours",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (herbs, oils, and incense worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Hold Monster",
                "description": "Choose a creature that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. This spell has no effect on undead.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a small, straight piece of iron)"
            },
            {
                "name": "Immolation",
                "description": "Flames wreathe one creature that you can see within range. The target must make a Dexterity saving throw. It takes 8d6 fire damage on a failed save, or half as much damage on a successful one. On a failed save, the target also burns for the spell’s duration.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Insect Plague",
                "description": "Swarming, biting locusts fill a 20-foot-radius sphere centered on a point you choose within range. The sphere spreads around corners. The sphere remains for the duration, and its area is lightly obscured.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a few grains of sugar, some kernels of grain, and a smear of fat)"
            },
            {
                "name": "Legend Lore",
                "description": "Name or describe a person, place, or object. The spell brings to your mind a brief summary of the significant lore about the thing you named. The lore might consist of current tales, forgotten stories, or even secret lore that has never been widely known.",
                "level": 5,
                "school": "Divination",
                "casting_time": "10 minutes",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V, S, M (incense worth at least 250 gp, which the spell consumes, and four ivory strips worth at least 50 gp each)"
            },
            {
                "name": "Mass Cure Wounds",
                "description": "A wave of healing energy washes out from a point of your choice within range. Choose up to six creatures in a 30-foot-radius sphere centered on that point. Each target regains hit points equal to 3d8 + your spellcasting ability modifier.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Mislead",
                "description": "You become invisible at the same time that an illusory double of you appears where you are standing. The double lasts for the duration, but the invisibility ends if you attack or cast a spell.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 hour",
                "components": "S"
            },
            {
                "name": "Modify Memory",
                "description": "You attempt to reshape another creature’s memories. One creature that you can see must make a Wisdom saving throw. If you are fighting the creature, it has advantage on the saving throw. On a failed save, the target becomes charmed by you for the duration.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Passwall",
                "description": "A passage appears at a point of your choice that you can see on a wooden, plaster, or stone surface (such as a wall, a ceiling, or a floor) within range, and lasts for the duration. You choose the opening’s dimensions: up to 5 feet wide, 8 feet tall, and 20 feet deep.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "1 hour",
                "components": "V, S, M (a pinch of sesame seeds)"
            },
            {
                "name": "Planar Binding",
                "description": "With this spell, you attempt to bind a celestial, an elemental, a fey, or a fiend to your service. The creature must be within range for the entire casting of the spell. The target must make a Charisma saving throw or be bound to your service for the duration.",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 hour",
                "range": "60 feet",
                "duration": "24 hours",
                "components": "V, S, M (a jewel worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Raise Dead",
                "description": "You return a dead creature you touch to life, provided that it has been dead no longer than 10 days. If the creature’s soul is both willing and at liberty to rejoin the body, the creature returns to life with 1 hit point.",
                "level": 5,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a diamond worth at least 500 gp, which the spell consumes)"
            },
            {
                "name": "Reincarnate",
                "description": "You touch a dead humanoid or a piece of a dead humanoid. Provided that the creature has been dead no longer than 10 days, the spell forms a new adult body for it and then calls the soul to enter that body. If the target’s soul isn’t free or willing, the spell fails.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (rare oils and unguents worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Scrying",
                "description": "You can see and hear a particular creature you choose that is on the same plane of existence as you. The target must make a Wisdom saving throw, which is modified by how well you know the target and the sort of physical connection you have to it.",
                "level": 5,
                "school": "Divination",
                "casting_time": "10 minutes",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water)"
            },
            {
                "name": "Seeming",
                "description": "This spell allows you to change the appearance of any number of creatures that you can see within range. You give each target you choose a new, illusory appearance.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S"
            },
            {
                "name": "Swift Quiver",
                "description": "You transmute your quiver so it produces an endless supply of nonmagical ammunition, which seems to leap into your hand when you reach for it. On each of your turns until the spell ends, you can use a bonus action to make two attacks with a weapon that uses ammunition from the quiver.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 bonus action",
                "range": "Touch",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a quiver containing at least one piece of ammunition)"
            },
            {
                "name": "Telekinesis",
                "description": "You gain the ability to move or manipulate creatures or objects by thought. When you cast the spell, and as your action each round for the duration, you can exert your will on one creature or object that you can see within range, causing the appropriate effect below.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Teleportation Circle",
                "description": "As you cast the spell, you draw a 10-foot-diameter circle on the ground inscribed with sigils that link your location to a permanent teleportation circle of your choice whose sigil sequence you know and that is on the same plane of existence as you.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "10 feet",
                "duration": "1 round",
                "components": "V, M (rare chalks and inks infused with precious gems worth 50 gp, which the spell consumes)"
            },
            {
                "name": "Tree Stride",
                "description": "You gain the ability to enter a tree and move from inside it to inside another tree of the same kind within 500 feet. Both trees must be living and at least the same size as you. You must use 5 feet of movement to enter a tree.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Arcane Gate",
                "description": "You create linked teleportation portals that remain open for the duration. Choose two points on the ground that you can see, one point within 10 feet of you and one point within 500 feet of you.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "500 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Blade Barrier",
                "description": "You create a vertical wall of whirling, razor-sharp blades made of magical energy. The wall appears within range and lasts for the duration. You can make a straight wall up to 100 feet long, 20 feet high, and 5 feet thick, or a ringed wall up to 60 feet in diameter.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "90 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Chain Lightning",
                "description": "You create a bolt of lightning that arcs toward a target of your choice that you can see within range. Three bolts then leap from that target to as many as three other targets, each of which must be within 30 feet of the first target.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a bit of fur; a piece of amber, crystal, or glass; and three silver pins)"
            },
            {
                "name": "Circle of Death",
                "description": "A sphere of negative energy ripples out in a 60-foot-radius sphere from a point within range. Each creature in that area must make a Constitution saving throw, taking 8d6 necrotic damage on a failed save, or half as much damage on a successful one.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (the powder of a crushed black pearl worth at least 500 gp)"
            },
            {
                "name": "Conjure Fey",
                "description": "You summon a fey creature of challenge rating 6 or lower, or a fey spirit that takes the form of a beast of challenge rating 6 or lower. It appears in an unoccupied space that you can see within range. The fey creature disappears when it drops to 0 hit points or when the spell ends.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "90 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Contingency",
                "description": "Choose a spell of 5th level or lower that you can cast, that has a casting time of 1 action, and that can target you. You cast that spell—called the contingent spell—as part of casting contingency, expending spell slots for both, but the contingent spell doesn’t come into effect.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "10 minutes",
                "range": "Self",
                "duration": "10 days",
                "components": "V, S, M (a statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp)"
            },
            {
                "name": "Create Undead",
                "description": "You can cast this spell only at night. Choose up to three corpses of Medium or Small humanoids within range. Each corpse becomes a ghoul under your control.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 minute",
                "range": "10 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (one black onyx stone for each corpse worth at least 150 gp, which the spell consumes)"
            },
            {
                "name": "Disintegrate",
                "description": "A thin green ray springs from your pointing finger to a target that you can see within range. The target can be a creature, an object, or a creation of magical force, such as the wall created by wall of force.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a lodestone and a pinch of dust)"
            },
            {
                "name": "Drawmij’s Instant Summons",
                "description": "You touch an object weighing 10 pounds or less whose longest dimension is 6 feet or less, and mark it with a distinctive rune. If the object is on the same plane of existence as you, you can summon it to your hand at any time.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (a sapphire worth 1,000 gp)"
            },
            {
                "name": "Eyebite",
                "description": "For the spell’s duration, your eyes become an inky void imbued with dread power. One creature of your choice within 60 feet of you that you can see must succeed on a Wisdom saving throw or be affected by one of the following effects of your choice for the duration.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Flesh to Stone",
                "description": "You attempt to turn one creature that you can see within range into stone. If the target’s body is made of flesh, the creature must make a Constitution saving throw. On a failed save, it is restrained as its flesh begins to harden.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of lime, water, and earth)"
            },
            {
                "name": "Find the Path",
                "description": "This spell allows you to find the shortest, most direct physical route to a specific fixed location that you are familiar with on the same plane of existence.",
                "level": 6,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Concentration, up to 1 day",
                "components": "V, S, M (a set of divinatory tools—such as bones, ivory sticks, cards, teeth, or carved runes—worth 100 gp and an object from the location you wish to find)"
            },
            {
                "name": "Globe of Invulnerability",
                "description": "An immobile, faintly shimmering barrier springs into existence in a 10-foot radius around you and remains for the duration. Any spell of 5th level or lower cast from outside the barrier can’t affect creatures or objects within it, even if the spell is cast using a higher-level spell slot.",
                "level": 6,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self (10-foot radius)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a glass or crystal bead that shatters when the spell ends)"
            },
            {
                "name": "Guards and Wards",
                "description": "You create a ward that protects up to 2,500 square feet of floor space (an area 50 feet on each side) for the duration. Corridors in the warded area are filled with fog, and doors are locked, among other effects.",
                "level": 6,
                "school": "Abjuration",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "24 hours",
                "components": "V, S, M (burning incense, a small measure of brimstone and oil, a knotted string, a small amount of blood, and a small silver rod worth at least 10 gp)"
            },
            {
                "name": "Harm",
                "description": "You unleash a virulent disease on a creature that you can see within range. The target must make a Constitution saving throw. On a failed save, it takes 14d6 necrotic damage, or half as much damage on a successful one. The damage can’t reduce the target’s hit points below 1.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Heal",
                "description": "Choose a creature that you can see within range. A surge of positive energy washes through the creature, causing it to regain 70 hit points. This spell also ends blindness, deafness, and any diseases affecting the target.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Heroes’ Feast",
                "description": "You bring forth a great feast, including magnificent food and drink. The feast takes 1 hour to consume and disappears at the end of that time, and the beneficial effects don’t set in until this hour is over.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a gem-encrusted bowl worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Magic Jar",
                "description": "Your body falls into a catatonic state as your soul leaves it and enters the container you used for the spell’s material component. While your soul inhabits the container, you are aware of your surroundings as if you were in the container’s space.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Until dispelled",
                "components": "V, S, M (a gem, crystal, reliquary, or some other ornamental container worth at least 500 gp)"
            },
            {
                "name": "Mass Suggestion",
                "description": "You suggest a course of activity (limited to a sentence or two) and magically influence up to twelve creatures of your choice that you can see within range and that can hear and understand you.",
                "level": 6,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "24 hours",
                "components": "V, M (a snake’s tongue and either a bit of honeycomb or a drop of sweet oil)"
            },
            {
                "name": "Move Earth",
                "description": "You can reshape dirt, sand, or clay in the area in any manner you choose for the duration. You can raise or lower the area’s elevation, create or fill in a trench, erect or flatten a wall, or form a pillar.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 2 hours",
                "components": "V, S, M (an iron blade and a small bag containing a mixture of soils—clay, loam, and sand)"
            },
            {
                "name": "Otiluke’s Freezing Sphere",
                "description": "A frigid globe of cold energy streaks from your fingertips to a point of your choice within range, where it explodes in a 60-foot-radius sphere. Each creature within the area must make a Constitution saving throw.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a small crystal sphere)"
            },
            {
                "name": "Otto’s Irresistible Dance",
                "description": "Choose one creature that you can see within range. The target begins a comic dance in place, shuffling, tapping its feet, and capering for the duration. Creatures that can’t be charmed are immune to this spell.",
                "level": 6,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V"
            },
            {
                "name": "Programmed Illusion",
                "description": "You create an illusion of an object, a creature, or some other visible phenomenon within range that activates when a specific condition occurs. The illusion is imperceptible until then. It must be no larger than a 30-foot cube.",
                "level": 6,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Until dispelled",
                "components": "V, S, M (a bit of fleece and jade dust worth at least 25 gp)"
            },
            {
                "name": "Sunbeam",
                "description": "A beam of brilliant light flashes out from your hand in a 5-foot-wide, 60-foot-long line. Each creature in the line must make a Constitution saving throw. On a failed save, a creature takes 6d8 radiant damage and is blinded until your next turn.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (60-foot line)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a magnifying glass)"
            },
            {
                "name": "Sunbeam",
                "description": "A beam of brilliant light flashes out from your hand in a 5-foot-wide, 60-foot-long line. Each creature in the line must make a Constitution saving throw. On a failed save, a creature takes 6d8 radiant damage and is blinded until your next turn.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (60-foot line)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a magnifying glass)"
            },
            {
                "name": "True Seeing",
                "description": "This spell gives the willing creature you touch the ability to see things as they actually are. For the duration, the creature has truesight, notices secret doors hidden by magic, and can see into the Ethereal Plane, all out to a range of 120 feet.",
                "level": 6,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (an ointment for the eyes that is made from mushroom powder, saffron, and fat)"
            },
            {
                "name": "Wind Walk",
                "description": "You and up to ten willing creatures you can see within range assume a gaseous form for the duration, appearing as wisps of cloud. While in this cloud form, a creature has a flying speed of 300 feet and has resistance to nonmagical damage.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (fire and holy water)"
            },
            {
                "name": "Word of Recall",
                "description": "You and up to five willing creatures within 5 feet of you instantly teleport to a previously designated sanctuary. You and any creatures that teleport with you appear in the nearest unoccupied space to the spot you designated when you prepared your sanctuary.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Tenser’s Transformation",
                "description": "You endow yourself with endurance and martial prowess fueled by magic. For the duration, you gain the following benefits: 50 temporary hit points, advantage on weapon attacks, proficiency with all weapons, and two weapon attacks per turn.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a weapon)"
            },
            {
                "name": "Transport via Plants",
                "description": "This spell creates a magical link between a Large or larger inanimate plant within range and another plant, at any distance, on the same plane of existence. You must have seen or touched the destination plant at least once before.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "10 feet",
                "duration": "1 round",
                "components": "V, S"
            },
            {
                "name": "Find the Path",
                "description": "This spell allows you to find the shortest, most direct physical route to a specific fixed location that you are familiar with on the same plane of existence.",
                "level": 6,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Concentration, up to 1 day",
                "components": "V, S, M (a set of divinatory tools—such as bones, ivory sticks, cards, teeth, or carved runes—worth 100 gp, and an object from the location you wish to find)"
            },
            {
                "name": "Flesh to Stone",
                "description": "You attempt to turn one creature that you can see within range into stone. If the target’s body is made of flesh, the creature must make a Constitution saving throw. On a failed save, it is restrained as its flesh begins to harden.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of lime, water, and earth)"
            },
            {
                "name": "Heroes’ Feast",
                "description": "You bring forth a great feast, including magnificent food and drink. The feast takes 1 hour to consume and disappears at the end of that time, and the beneficial effects don’t set in until this hour is over.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a gem-encrusted bowl worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Harm",
                "description": "You unleash a virulent disease on a creature that you can see within range. The target must make a Constitution saving throw. On a failed save, it takes 14d6 necrotic damage, or half as much damage on a successful one.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Mass Suggestion",
                "description": "You suggest a course of activity (limited to a sentence or two) and magically influence up to twelve creatures of your choice that you can see within range and that can hear and understand you.",
                "level": 6,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "24 hours",
                "components": "V, S, M (a snake’s tongue and either a bit of honeycomb or a drop of sweet oil)"
            },
            {
                "name": "Move Earth",
                "description": "You can reshape dirt, sand, or clay in the area in any manner you choose for the duration. You can raise or lower the area’s elevation, create or fill in a trench, erect or flatten a wall, or form a pillar.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 2 hours",
                "components": "V, S, M (an iron blade and a small bag containing a mixture of soils—clay, loam, and sand)"
            },
            {
                "name": "Soul Cage",
                "description": "This spell snatches the soul of a humanoid as it dies and traps it inside a tiny cage you use for the material component. While you have a soul inside the cage, you can exploit it in different ways.",
                "level": 6,
                "school": "Necromancy",
                "casting_time": "1 reaction, which you take when a humanoid you can see within 60 feet of you dies",
                "range": "60 feet",
                "duration": "8 hours",
                "components": "V, S, M (a tiny silver cage worth 100 gp)"
            },
            {
                "name": "True Seeing",
                "description": "This spell gives the willing creature you touch the ability to see things as they actually are. For the duration, the creature has truesight, notices secret doors hidden by magic, and can see into the Ethereal Plane, all out to a range of 120 feet.",
                "level": 6,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (an ointment for the eyes that is made from mushroom powder, saffron, and fat)"
            },
            {
                "name": "Wind Walk",
                "description": "You and up to ten willing creatures you can see within range assume a gaseous form for the duration, appearing as wisps of cloud. While in this cloud form, a creature has a flying speed of 300 feet and has resistance to nonmagical damage.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "8 hours",
                "components": "V, S, M (fire and holy water)"
            },
            {
                "name": "Word of Recall",
                "description": "You and up to five willing creatures within 5 feet of you instantly teleport to a previously designated sanctuary. You and any creatures that teleport with you appear in the nearest unoccupied space to the spot you designated when you prepared your sanctuary.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "5 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Arcane Sword",
                "description": "You create a sword-shaped plane of force that hovers within range. It lasts for the duration. When the sword appears, you make a melee spell attack against a target of your choice within 5 feet of the sword.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a miniature platinum sword with a grip and pommel of copper and zinc, worth 250 gp)"
            },
            {
                "name": "Conjure Celestial",
                "description": "You summon a celestial of challenge rating 4 or lower, which appears in an unoccupied space that you can see within range. The celestial disappears when it drops to 0 hit points or when the spell ends.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "90 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Delayed Blast Fireball",
                "description": "A beam of yellow light flashes from your pointing finger, then condenses to linger at a chosen point within range as a glowing bead for the duration. When the spell ends, either because your concentration is broken or because you decide to end it, the bead blossoms with a low roar into an explosion of flame.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a tiny ball of bat guano and sulfur)"
            },
            {
                "name": "Divine Word",
                "description": "You utter a divine word, imbued with the power that shaped the world at the dawn of creation. Choose any number of creatures you can see within range. Each creature that can hear you must make a Charisma saving throw.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 bonus action",
                "range": "30 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Etherealness",
                "description": "You step into the border regions of the Ethereal Plane, in the area where it overlaps with your current plane. You remain in the Border Ethereal for the duration or until you use your action to dismiss the spell.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Up to 8 hours",
                "components": "V, S"
            },
            {
                "name": "Finger of Death",
                "description": "You send negative energy coursing through a creature that you can see within range, causing it searing pain. The target must make a Constitution saving throw. It takes 7d8 + 30 necrotic damage on a failed save, or half as much damage on a successful one.",
                "level": 7,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Fire Storm",
                "description": "A storm made up of sheets of roaring flame appears in a location you choose. The area of the storm consists of up to ten 10-foot cubes, which you can arrange as you wish. Each cube must have at least one face adjacent to the face of another cube.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Forcecage",
                "description": "An immobile, invisible, cube-shaped prison composed of magical force springs into existence around an area you choose within range. The prison can be a cage or a solid box, as you choose.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "100 feet",
                "duration": "1 hour",
                "components": "V, S, M (ruby dust worth 1,500 gp, which the spell consumes)"
            },
            {
                "name": "Mirage Arcane",
                "description": "You make terrain in an area up to 1 mile square look, sound, smell, and even feel like some other sort of terrain. The terrain’s general shape remains the same, however. Open fields or a road could be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain.",
                "level": 7,
                "school": "Illusion",
                "casting_time": "10 minutes",
                "range": "Sight",
                "duration": "10 days",
                "components": "V, S"
            },
            {
                "name": "Plane Shift",
                "description": "You and up to eight willing creatures who link hands in a circle are transported to a different plane of existence. You can specify a destination in general terms, such as the City of Brass on the Elemental Plane of Fire or the palace of Dispater on the second level of the Nine Hells.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a forked, metal rod worth at least 250 gp, attuned to a particular plane of existence)"
            },
            {
                "name": "Power Word Pain",
                "description": "You speak a word of power that causes waves of intense pain to assail one creature you can see within range. If the target has 100 hit points or fewer, it is subject to crippling pain. Otherwise, the spell has no effect.",
                "level": 7,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Prismatic Spray",
                "description": "Eight multicolored rays of light flash from your hand. Each ray is a different color and has a different power. Each creature in a 60-foot cone must make a Dexterity saving throw. For each target, roll a d8 to determine which color ray affects it.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Self (60-foot cone)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Project Image",
                "description": "You create an illusory copy of yourself that lasts for the duration. The copy can appear at any location within range that you have seen before, regardless of intervening obstacles.",
                "level": 7,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "500 miles",
                "duration": "Concentration, up to 24 hours",
                "components": "V, S, M (a small replica of you made from materials worth at least 5 gp)"
            },
            {
                "name": "Regenerate",
                "description": "You touch a creature and stimulate its natural healing ability. The target regains 4d8 + 15 hit points. For the duration of the spell, the target regains 1 hit point at the start of each of its turns (10 hit points each minute).",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "1 hour",
                "components": "V, S, M (a prayer wheel and holy water)"
            },
            {
                "name": "Resurrection",
                "description": "You touch a dead creature that has been dead for no more than a century, that didn’t die of old age, and that isn’t undead. If its soul is free and willing, the target returns to life with all its hit points restored.",
                "level": 7,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a diamond worth at least 1,000 gp, which the spell consumes)"
            },
            {
                "name": "Reverse Gravity",
                "description": "This spell reverses gravity in a 50-foot-radius, 100-foot-high cylinder centered on a point within range. All creatures and objects that aren’t anchored to the ground fall upward and reach the top of the area when you cast this spell.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "100 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a lodestone and iron filings)"
            },
            {
                "name": "Sequester",
                "description": "By means of this spell, a willing creature or an object can be hidden away, safe from detection for the duration. When you cast the spell and touch the target, it becomes invisible and can’t be targeted by any divination spells.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (a powder composed of diamond, emerald, ruby, and sapphire dust worth at least 5,000 gp)"
            },
            {
                "name": "Simulacrum",
                "description": "You shape an illusory duplicate of one beast or humanoid that is within range for the entire casting time of the spell. The duplicate is a creature, partially real and formed from ice or snow, and it can take actions and otherwise be affected as a normal creature.",
                "level": 7,
                "school": "Illusion",
                "casting_time": "12 hours",
                "range": "Touch",
                "duration": "Until dispelled",
                "components": "V, S, M (snow or ice in quantities sufficient to make a life-size copy of the duplicated creature; some hair, fingernail clippings, or other piece of that creature’s body placed inside the snow or ice; powdered ruby worth 1,500 gp, sprinkled over the duplicate)"
            },
            {
                "name": "Symbol",
                "description": "When you cast this spell, you inscribe a harmful glyph either on a surface (such as a section of floor, a wall, or a table) or within an object that can be closed to conceal the glyph (a book, a scroll, or a treasure chest).",
                "level": 7,
                "school": "Abjuration",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Until dispelled or triggered",
                "components": "V, S, M (mercury, phosphorus, and powdered diamond and opal worth at least 1,000 gp)"
            },
            {
                "name": "Teleport",
                "description": "This spell instantly transports you and up to eight willing creatures of your choice, or a single object that you can see within range, to a destination you specify. If you target an object, it must be able to fit entirely inside a 10-foot cube.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "10 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Whirlwind",
                "description": "A whirlwind howls down to a point that you can see on the ground within range. The whirlwind is a 10-foot-radius, 30-foot-high cylinder centered on that point. Until the spell ends, you can use your action to move the whirlwind up to 30 feet in any direction along the ground.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "300 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a piece of straw)"
            },
            {
                "name": "Plane Shift",
                "description": "You and up to eight willing creatures who link hands in a circle are transported to a different plane of existence. You can specify a destination in general terms, such as the City of Brass on the Elemental Plane of Fire or the palace of Dispater on the second level of the Nine Hells.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a forked, metal rod worth at least 250 gp, attuned to a particular plane of existence)"
            },
            {
                "name": "Etherealness",
                "description": "You step into the border regions of the Ethereal Plane, in the area where it overlaps with your current plane. You remain in the Border Ethereal for the duration or until you use your action to dismiss the spell.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Up to 8 hours",
                "components": "V, S"
            },
            {
                "name": "Crown of Stars",
                "description": "Seven star-like motes of light appear and orbit your head. You can make one of these motes shoot toward a creature within range to deal radiant damage, and you can hurl another mote on each of your turns as a bonus action.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Symbol",
                "description": "When you cast this spell, you inscribe a harmful glyph either on a surface or within an object. When triggered, the glyph can produce effects like stunning, fear, or even instant death, depending on the type of glyph you select.",
                "level": 7,
                "school": "Abjuration",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Until dispelled or triggered",
                "components": "V, S, M (mercury, phosphorus, and powdered diamond and opal worth at least 1,000 gp)"
            },
            {
                "name": "Project Image",
                "description": "You create an illusory duplicate of yourself that lasts for the duration. The copy can appear at any location within range that you have seen before, regardless of intervening obstacles.",
                "level": 7,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "500 miles",
                "duration": "Concentration, up to 24 hours",
                "components": "V, S, M (a small replica of you made from materials worth at least 5 gp)"
            },
            {
                "name": "Power Word Pain",
                "description": "You speak a word of power that causes waves of intense pain to assail one creature you can see within range. If the target has 100 hit points or fewer, it is subject to crippling pain. Otherwise, the spell has no effect.",
                "level": 7,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Abi-Dalzim’s Horrid Wilting",
                "description": "You draw the moisture from every creature in a 30-foot cube centered on a point you choose within range. Each creature in that area must make a Constitution saving throw, taking 12d8 necrotic damage on a failed save, or half as much damage on a successful one.",
                "level": 8,
                "school": "Necromancy",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a bit of sponge)"
            },
            {
                "name": "Antimagic Field",
                "description": "A 10-foot-radius invisible sphere of antimagic surrounds you. This area is divorced from the magical energy that suffuses the multiverse. Within the sphere, spells can't be cast, summoned creatures disappear, and even magic items become mundane.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self (10-foot radius)",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a pinch of powdered iron or iron filings)"
            },
            {
                "name": "Antipathy/Sympathy",
                "description": "This spell attracts or repels creatures of your choice. The target must succeed on a Wisdom saving throw or be affected. You set the conditions for which creatures this effect applies to, depending on whether you choose antipathy or sympathy.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 hour",
                "range": "60 feet",
                "duration": "10 days",
                "components": "V, S, M (either a drop of honey or a bit of rotten meat)"
            },
            {
                "name": "Clone",
                "description": "This spell grows an inert duplicate of a living creature as a safeguard against death. This clone forms inside a sealed vessel and grows to full size and maturity after 120 days. You can create a clone of a creature that has died.",
                "level": 8,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a diamond worth at least 1,000 gp and at least 1 cubic inch of flesh)"
            },
            {
                "name": "Control Weather",
                "description": "You take control of the weather within a 5-mile radius centered on a point you can see. You can change precipitation, temperature, and wind conditions. It takes 1d4 x 10 minutes for the new conditions to take effect.",
                "level": 8,
                "school": "Transmutation",
                "casting_time": "10 minutes",
                "range": "Self (5-mile radius)",
                "duration": "Concentration, up to 8 hours",
                "components": "V, S, M (burning incense and bits of earth and wood mixed in water)"
            },
            {
                "name": "Demiplane",
                "description": "You create a shadowy door on a flat solid surface that you can see within range. The door is large enough to allow Medium creatures to pass through. When opened, the door leads to a demiplane that appears to be an empty room 30 feet in each dimension.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "1 hour",
                "components": "S"
            },
            {
                "name": "Dominate Monster",
                "description": "You attempt to beguile a creature that you can see within range. It must succeed on a Wisdom saving throw or be charmed by you for the duration. While charmed, you have a telepathic link with it, and you can issue commands to the creature.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S"
            },
            {
                "name": "Earthquake",
                "description": "You create a seismic disturbance at a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point and shakes creatures and structures in contact with the ground in that area.",
                "level": 8,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "500 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a pinch of dirt, a piece of rock, and a lump of clay)"
            },
            {
                "name": "Feeblemind",
                "description": "You blast the mind of a creature that you can see within range, attempting to shatter its intellect and personality. The target takes 4d6 psychic damage and must make an Intelligence saving throw or its Intelligence and Charisma scores become 1.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (a handful of clay, crystal, glass, or mineral spheres)"
            },
            {
                "name": "Glibness",
                "description": "Until the spell ends, when you make a Charisma check, you can replace the number you roll with a 15. Additionally, no magic can determine whether you are telling the truth, as you appear perfectly truthful to all.",
                "level": 8,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 hour",
                "components": "V"
            },
            {
                "name": "Holy Aura",
                "description": "Divine light washes out from you and coalesces in a soft radiance in a 30-foot radius around you. Creatures of your choice in that radius when you cast this spell shed dim light in a 5-foot radius and have advantage on all saving throws.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Self (30-foot radius)",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a tiny reliquary worth at least 1,000 gp containing a sacred relic)"
            },
            {
                "name": "Illusory Dragon",
                "description": "By gathering threads of shadow material from the Shadowfell, you create a Huge shadowy dragon in an unoccupied space that you can see within range. The illusion lasts for the spell’s duration and can be commanded to attack.",
                "level": 8,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "S"
            },
            {
                "name": "Incendiary Cloud",
                "description": "A cloud of roiling smoke shot through with white-hot embers appears in a 20-foot-radius sphere centered on a point within range. The cloud spreads around corners and is heavily obscured. The cloud lasts for the duration or until strong wind disperses it.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Maddening Darkness",
                "description": "Magical darkness spreads from a point you choose within range to fill a 60-foot-radius sphere until the spell ends. The darkness spreads around corners. A creature with darkvision can’t see through this darkness, and nonmagical light can’t illuminate it.",
                "level": 8,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S, M (a drop of pitch mixed with a pinch of sulfur)"
            },
            {
                "name": "Maze",
                "description": "You banish a creature that you can see within range into a labyrinthine demiplane. The target remains there for the duration or until it escapes the maze. While in the maze, the target is incapacitated.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 10 minutes",
                "components": "V, S"
            },
            {
                "name": "Mind Blank",
                "description": "Until the spell ends, one willing creature you touch is immune to psychic damage, any effect that would sense its emotions or read its thoughts, divination spells, and the charmed condition.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "24 hours",
                "components": "V, S"
            },
            {
                "name": "Power Word Stun",
                "description": "You speak a word of power that can overwhelm the mind of one creature you can see within range, leaving it dumbfounded. If the target has 150 hit points or fewer, it is stunned. Otherwise, the spell has no effect.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Sunburst",
                "description": "Brilliant sunlight flashes in a 60-foot radius centered on a point you choose within range. Each creature in that light must make a Constitution saving throw, taking 12d6 radiant damage on a failed save, or half as much on a successful one.",
                "level": 8,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "150 feet",
                "duration": "Instantaneous",
                "components": "V, S, M (fire and a piece of sunstone)"
            },
            {
                "name": "Telepathy",
                "description": "You create a telepathic link between yourself and a creature with which you are familiar. The creature can be anywhere on the same plane of existence as you. The spell fails if the creature has an Intelligence of 2 or lower.",
                "level": 8,
                "school": "Divination",
                "casting_time": "1 action",
                "range": "Unlimited",
                "duration": "24 hours",
                "components": "V, S, M (a pair of linked silver rings)"
            },
            {
                "name": "Tsunami",
                "description": "A wall of water springs into existence at a point you choose within range. You can make the wall up to 300 feet long, 300 feet high, and 50 feet thick. The wall lasts for the duration.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "Sight",
                "duration": "Concentration, up to 6 rounds",
                "components": "V, S"
            },
            {
                "name": "Astral Projection",
                "description": "You and up to eight willing creatures project your astral bodies into the Astral Plane. The material body you leave behind is unconscious and in a state of suspended animation.",
                "level": 9,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "10 feet",
                "duration": "Special",
                "components": "V, S, M (for each creature, a jacinth worth at least 1,000 gp and one ornately carved silver bar worth at least 100 gp)"
            },
            {
                "name": "Foresight",
                "description": "You touch a willing creature and bestow a limited ability to see into the immediate future. For the duration, the target can’t be surprised, has advantage on attack rolls, ability checks, and saving throws, and other creatures have disadvantage on attack rolls against it.",
                "level": 9,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "8 hours",
                "components": "V, S, M (a hummingbird feather)"
            },
            {
                "name": "Gate",
                "description": "You conjure a portal linking an unoccupied space you can see within range to a precise location on a different plane of existence. The portal is a circular opening, which you can make 5 to 20 feet in diameter.",
                "level": 9,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S, M (a diamond worth at least 5,000 gp)"
            },
            {
                "name": "Imprisonment",
                "description": "You create a magical restraint to hold a creature you can see within range. The target must succeed on a Wisdom saving throw or be bound by the spell; if it succeeds, it is immune to this spell if you cast it again. The spell offers multiple forms of imprisonment, like burial or slumber.",
                "level": 9,
                "school": "Abjuration",
                "casting_time": "1 minute",
                "range": "30 feet",
                "duration": "Until dispelled",
                "components": "V, S, M (a vellum depiction or a carved statuette of the target and a special component depending on the version of imprisonment you choose)"
            },
            {
                "name": "Mass Heal",
                "description": "A flood of healing energy flows from you into injured creatures around you. You restore up to 700 hit points, divided as you choose among any number of creatures that you can see within range. Creatures you heal are also cured of diseases and mental conditions.",
                "level": 9,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Meteor Swarm",
                "description": "Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius sphere centered on each point must make a Dexterity saving throw, taking 20d6 fire damage and 20d6 bludgeoning damage on a failed save, or half as much on a successful one.",
                "level": 9,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "1 mile",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Power Word Kill",
                "description": "You utter a word of power that can compel one creature you can see within range to die instantly. If the creature you choose has 100 hit points or fewer, it dies. Otherwise, the spell has no effect.",
                "level": 9,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Prismatic Wall",
                "description": "A shimmering, multicolored plane of light forms a vertical wall up to 90 feet long, 30 feet high, and 1 inch thick, or a sphere up to 30 feet in diameter, centered on a point you choose within range. The wall remains for the duration and affects creatures passing through it depending on its color.",
                "level": 9,
                "school": "Abjuration",
                "casting_time": "1 action",
                "range": "60 feet",
                "duration": "10 minutes",
                "components": "V, S"
            },
            {
                "name": "Shapechange",
                "description": "You assume the form of a different creature for the duration. The new form can be of any creature with a challenge rating equal to or less than your level. You can assume the form of a beast, a dragon, an elemental, a fey, a giant, a humanoid, a monstrosity, a plant, or an undead.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a jade circlet worth at least 1,500 gp, which you must place on your head)"
            },
            {
                "name": "Storm of Vengeance",
                "description": "A churning storm cloud forms, centered on a point you can see within range and spreading to a radius of 360 feet. Lightning flashes in the area, thunder booms, and strong winds roar. Each creature under the cloud takes varying effects over the course of the spell’s duration.",
                "level": 9,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Sight",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Time Stop",
                "description": "You briefly stop the flow of time for everyone but yourself. No time passes for other creatures, while you take 1d4 + 1 turns in a row, during which you can use actions and move as normal. This effect ends if one of your actions directly affects another creature or object.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "True Polymorph",
                "description": "Choose one creature or nonmagical object that you can see within range. You transform the creature into a different creature, or the object into a creature. Alternatively, you can transform the creature into an object. The transformation lasts for the duration, or until the target drops to 0 hit points or dies.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 action",
                "range": "30 feet",
                "duration": "Concentration, up to 1 hour",
                "components": "V, S, M (a drop of mercury, a dollop of gum arabic, and a wisp of smoke)"
            },
            {
                "name": "True Resurrection",
                "description": "You touch a creature that has been dead for no longer than 200 years and that died for any reason except old age. If its soul is free and willing, the creature is restored to life with all its hit points. This spell can even provide a new body if the original no longer exists.",
                "level": 9,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes)"
            },
            {
                "name": "Weird",
                "description": "Drawing on the deepest fears of a group of creatures, you create illusory creatures in their minds, visible only to them. Each creature in a 30-foot-radius sphere centered on a point of your choice within range must make a Wisdom saving throw. On a failed save, a creature is frightened.",
                "level": 9,
                "school": "Illusion",
                "casting_time": "1 action",
                "range": "120 feet",
                "duration": "Concentration, up to 1 minute",
                "components": "V, S"
            },
            {
                "name": "Wish",
                "description": "Wish is the mightiest spell a mortal creature can cast. By simply speaking aloud, you can alter the very foundations of reality in accord with your desires.",
                "level": 9,
                "school": "Conjuration",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Power Word Heal",
                "description": "A word of power restores a creature to full health. The creature you touch regains all its hit points. If the creature is charmed, frightened, paralyzed, or stunned, those conditions end. If the creature is prone, it can use its reaction to stand up.",
                "level": 9,
                "school": "Evocation",
                "casting_time": "1 action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Power Word Power",
                "description": "You speak a word of immense magical energy that greatly increases your power, allowing you to cast any spell without material or verbal components for 1 minute.",
                "level": 9,
                "school": "Enchantment",
                "casting_time": "1 action",
                "range": "Self",
                "duration": "1 minute",
                "components": "None"
            }
        ],
        "Pathfinder": [
            {"name": "Magic Missile", "description": "You fire unerring bolts of magical force at your foes.", "level": 1, "school": "Evocation", "casting_time": "1 action", "range": "120 feet", "duration": "Instantaneous", "components": "V, S"},
            {"name": "Shield", "description": "An invisible barrier of force appears and protects you.", "level": 1, "school": "Abjuration", "casting_time": "1 reaction", "range": "Self", "duration": "1 round", "components": "V, S"}
        ],
        "Call of Cthulhu": [
            {"name": "Shriveling", "description": "You project dark energy towards a target, causing damage.", "level": 1, "school": "Necromancy", "casting_time": "1 action", "range": "30 feet", "duration": "Instantaneous", "components": "V, S, M (a withered leaf)"}
        ],
        "Shadowrun": [
            {"name": "Stun Bolt", "description": "A non-lethal magical attack that causes mental strain.", "level": 1, "school": "Combat", "casting_time": "1 action", "range": "Line of Sight", "duration": "Instantaneous", "components": "S"}
        ],
        "Star Wars: Edge of the Empire": [
            {"name": "Force Push", "description": "You push objects or creatures using the Force.", "level": 1, "school": "Telekinesis", "casting_time": "1 action", "range": "30 feet", "duration": "Instantaneous", "components": "S"}
        ],
        "Mothership RPG": [
            {"name": "EMP Pulse", "description": "A pulse that disables nearby electronic devices.", "level": 1, "school": "Tech", "casting_time": "1 action", "range": "10 feet", "duration": "Instantaneous", "components": "S"}
        ]
    }

    class_spells = {
        "Dungeons & Dragons 5th Edition": {
            "Druid": ["Cure Wounds"],
            "Wizard": ["Fireball"]
        },
        "Pathfinder": {
            "Wizard": ["Magic Missile", "Shield"]
        },
        "Call of Cthulhu": {
            "Occultist": ["Shriveling"]
        },
        "Shadowrun": {
            "Mage": ["Stun Bolt"]
        },
        "Star Wars: Edge of the Empire": {
            "Technician": ["Force Push"]
        },
        "Mothership RPG": {
            "Scientist": ["EMP Pulse"]
        }
    }

    class_progression_spells = {
        "Dungeons & Dragons 5th Edition": {
            "Druid": {
                1: {"cantrips": 2, "spells": 2},
                2: {"cantrips": 2, "spells": 3},
                3: {"cantrips": 2, "spells": 4},
                4: {"cantrips": 3, "spells": 5},
                5: {"cantrips": 3, "spells": 6}
            },
            "Wizard": {
                1: {"cantrips": 3, "spells": 2},
                2: {"cantrips": 3, "spells": 3},
                3: {"cantrips": 3, "spells": 4},
                4: {"cantrips": 4, "spells": 5},
                5: {"cantrips": 4, "spells": 6}
            }
        },
        "Pathfinder": {
            "Wizard": {
                1: {"cantrips": 4, "spells": 2},
                2: {"cantrips": 4, "spells": 3},
                3: {"cantrips": 4, "spells": 4},
                4: {"cantrips": 5, "spells": 5},
                5: {"cantrips": 5, "spells": 6}
            }
        },
        "Call of Cthulhu": {
            "Occultist": {
                1: {"spells": 3},
                2: {"spells": 4},
                3: {"spells": 5}
            }
        },
        "Shadowrun": {
            "Mage": {
                1: {"spells": 2},
                2: {"spells": 3},
                3: {"spells": 4}
            }
        },
        "Star Wars: Edge of the Empire": {
            "Technician": {
                1: {"abilities": 2},
                2: {"abilities": 3},
                3: {"abilities": 4}
            }
        },
        "Mothership RPG": {
            "Scientist": {
                1: {"spells": 1},
                2: {"spells": 2},
                3: {"spells": 3}
            }
        }
    }


    # Seeding data
    for system_data in rpg_systems:
        # Create and save the RPG system
        system = RPGSystem(
            name=system_data["name"],
            description=system_data["description"],
            publisher=system_data["publisher"],
            edition=system_data["edition"],
            core_rulebook=system_data["core_rulebook"],
            genre=system_data["genre"],
            popularity=system_data["popularity"],
            default_settings=system_data["default_settings"]
        )
        db.session.add(system)
        db.session.commit()

        # Seed classes
        if system_data["name"] in classes:
            for class_data in classes[system_data["name"]]:
                new_class = Class(
                    name=class_data["name"],
                    description=class_data["description"],
                    hit_die=class_data["hit_die"],
                    primary_ability=class_data["primary_ability"],
                    rpg_system_id=system.id  # Ensure this class is linked to the correct RPG system
                )
                db.session.add(new_class)
                db.session.commit()

                # Seed class progression for each class
                if system_data["name"] in class_progression_spells and new_class.name in class_progression_spells[system_data["name"]]:
                    progression_data = class_progression_spells[system_data["name"]][new_class.name]
                    
                    # Iterate over each level and the corresponding progression data
                    for level, progression in progression_data.items():
                        class_progression = ClassProgression(
                            class_id=new_class.id,
                            level=level,
                            available_spell=progression  # Assign the available_spell field directly from the progression data
                        )
                        db.session.add(class_progression)


        # Seed feats
        if system_data["name"] in feats:
            for feat_data in feats[system_data["name"]]:
                new_feat = Feat(
                    name=feat_data["name"],
                    description=feat_data["description"],
                    rpg_system_id=system.id  # Ensure this feat is linked to the correct RPG system
                )
                db.session.add(new_feat)

        # Seed spells
        if system_data["name"] in spells:
            for spell_data in spells[system_data["name"]]:
                new_spell = Spell(
                    name=spell_data["name"],
                    description=spell_data["description"],
                    level=spell_data["level"],
                    school=spell_data["school"],
                    casting_time=spell_data["casting_time"],
                    range=spell_data["range"],
                    duration=spell_data["duration"],
                    components=spell_data["components"],
                    rpg_system_id=system.id
                )
                db.session.add(new_spell)
            db.session.commit()

        # Seed class-spells relationships
        if system_data["name"] in class_spells:
            for class_name, spell_names in class_spells[system_data["name"]].items():
                class_obj = Class.query.filter_by(name=class_name, rpg_system_id=system.id).first()
                for spell_name in spell_names:
                    spell_obj = Spell.query.filter_by(name=spell_name, rpg_system_id=system.id).first()
                    if class_obj and spell_obj:
                        class_spell = ClassSpell(class_id=class_obj.id, spell_id=spell_obj.id)
                        db.session.add(class_spell)

        # Seed races
        if system_data["name"] in races:
            for race_data in races[system_data["name"]]:
                new_race = Race(
                    name=race_data["name"],
                    description=race_data["description"],
                    size=race_data["size"],
                    speed=race_data["speed"],
                    languages=json.dumps(race_data["languages"]),
                    vision_type=race_data["vision_type"],
                    natural_weapons=race_data["natural_weapons"],
                    favored_class=race_data["favored_class"],
                    rpg_system_id=system.id  # Ensure this race is linked to the correct RPG system
                )
                db.session.add(new_race)

        # Seed skills
        if system_data["name"] in skills:
            for skill_data in skills[system_data["name"]]:
                new_skill = Skill(
                    name=skill_data["name"],
                    description=skill_data["description"],
                    associated_ability=skill_data["associated_ability"],
                    rpg_system_id=system.id  # Ensure this skill is linked to the correct RPG system
                )
                db.session.add(new_skill)

        # Seed items
        if system_data["name"] in items:
            for item_data in items[system_data["name"]]:
                new_item = Item(
                    name=item_data["name"],
                    description=item_data["description"],
                    weight=item_data["weight"],
                    rarity=item_data["rarity"],
                    cost=item_data["cost"],
                    damage_type=item_data.get("damage_type"),
                    rpg_system_id=system.id  # Ensure this item is linked to the correct RPG system
                )
                db.session.add(new_item)

        # Seed monsters
        if system_data["name"] in monsters:
            for monster_data in monsters[system_data["name"]]:
                new_monster = Monster(
                    name=monster_data["name"],
                    description=monster_data["description"],
                    size=monster_data["size"],
                    hit_points=monster_data["hit_points"],
                    armor_class=monster_data["armor_class"],
                    rpg_system_id=system.id  # Ensure this monster is linked to the correct RPG system
                )
                db.session.add(new_monster)


    db.session.commit()
    print("Database seeded successfully!")

def run_seed():
    app = create_app()
    with app.app_context():
        db.session.query(Monster).delete()
        db.session.query(Item).delete()
        db.session.query(Skill).delete()
        db.session.query(Race).delete()
        db.session.query(Class).delete()
        db.session.query(RPGSystem).delete()
        db.session.query(Spell).delete()
        db.session.query(ClassSpell).delete()
        db.session.query(Feat).delete()
        db.session.query(ClassProgression).delete()
        db.session.commit()
        seed_rpg_systems()


if __name__ == '__main__':
    run_seed()