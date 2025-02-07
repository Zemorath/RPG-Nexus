from backend import create_app, db
from backend.models import RPGSystem, Class, Race, Skill, Item, Monster, Spell, ClassSpell, Feat, ClassProgression, Background, Alignment
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
        "Pathfinder": [
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
            {
                "name": "Acid Splash",
                "description": "You fire a small orb of acid at the target. You must succeed on a ranged touch attack to hit your target. The orb deals 1d3 points of acid damage.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Arcane Mark",
                "description": "This spell allows you to inscribe your personal rune or mark, which can consist of no more than six characters. The writing can be visible or invisible.",
                "level": 0,
                "school": "Universal",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S"
            },
            {
                "name": "Bleed",
                "description": "You cause a living creature that is below 0 hit points but stabilized to resume dying. Upon casting this spell, you target a living creature that has –1 or fewer hit points. That creature begins dying, taking 1 point of damage per round.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Create Water",
                "description": "This spell generates wholesome, drinkable water, just like clean rain water. Water can be created in an area as small as will actually contain the liquid, or in an area three times as large—possibly creating a downpour or filling many small receptacles.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Daze",
                "description": "This spell clouds the mind of a humanoid creature with 4 or fewer Hit Dice so that it takes no actions. Humanoids of 5 or more HD are not affected. A dazed subject is not stunned, so attackers get no special advantage against it.",
                "level": 0,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round",
                "components": "V, S, M (a pinch of wool or similar substance)"
            },
            {
                "name": "Detect Magic",
                "description": "You detect magical auras. The amount of information revealed depends on how long you study a particular area or subject.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Concentration, up to 1 min./level",
                "components": "V, S"
            },
            {
                "name": "Detect Poison",
                "description": "You determine whether a creature, object, or area has been poisoned or is poisonous. You can determine the exact type of poison with a DC 20 Wisdom check.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Flare",
                "description": "This cantrip creates a burst of light. If you cause the light to burst in front of a single creature, that creature is dazzled for 1 minute unless it makes a successful Fortitude save.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Ghost Sound",
                "description": "Ghost sound allows you to create a volume of sound that rises, recedes, approaches, or remains at a fixed place. You choose what type of sound ghost sound creates when casting it and cannot thereafter change the sound's basic character.",
                "level": 0,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S, M (a bit of wool or a small lump of wax)"
            },
            {
                "name": "Guidance",
                "description": "This spell imbues the subject with a touch of divine guidance. The creature gets a +1 competence bonus on a single attack roll, saving throw, or skill check.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute or until discharged",
                "components": "V, S"
            },
            {
                "name": "Light",
                "description": "This spell causes a touched object to glow like a torch, shedding normal light in a 20-foot radius from the point touched, and increasing the light level for an additional 20 feet by one step, up to normal light (darkness becomes dim light, and dim light becomes normal light).",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, M/DF (a firefly)"
            },
            {
                "name": "Mage Hand",
                "description": "You point your finger at an object and can lift it and move it at will from a distance. As a move action, you can propel the object as far as 15 feet in any direction, though the spell ends if the distance between you and the object ever exceeds the spell's range.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Concentration",
                "components": "V, S"
            },
            {
                "name": "Mending",
                "description": "This spell repairs damaged objects, restoring 1d4 hit points to the object. If the object has the broken condition, this condition is removed if the object is restored to at least half its original hit points.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "10 minutes",
                "range": "10 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Brand",
                "description": "You mark a creature or object with a personal rune or mark. The writing can be visible or invisible, and it causes no harm to the target. At any time, you can focus on the brand from any distance to learn the direction and approximate distance of the branded subject relative to you.",
                "level": 0,
                "school": "Universal",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S, M (a drop of ink)"
            },
            {
                "name": "Detect Chaos",
                "description": "You can sense the presence of chaos. The amount of information revealed depends on how long you study a particular area or subject: 1st round - presence or absence of chaos; 2nd round - number of chaotic auras and strength of strongest; 3rd round - strength and location of each aura.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft. cone",
                "duration": "Concentration, up to 10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Detect Good",
                "description": "This spell functions like detect chaos, except that it detects the auras of good creatures, clerics or paladins of good deities, good spells, and good magic items.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft. cone",
                "duration": "Concentration, up to 10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Detect Law",
                "description": "This spell functions like detect chaos, except that it detects the auras of lawful creatures, clerics of lawful deities, lawful spells, and lawful magic items.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft. cone",
                "duration": "Concentration, up to 10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Putrefy Food and Drink",
                "description": "This spell causes otherwise edible food or drink to become putrid and spoiled. The food turns to a foul-smelling, rotten mush. Unholy water and similar food and drink items are spoiled by purify food and drink, while food and drink with opposite alignments or effects are unaffected.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Sift",
                "description": "You can sift through earth, sand, or dirt to locate small items. You can search a 5-foot-square area as a standard action, gaining a +5 bonus on Perception checks to find items buried or concealed in that area. This spell does not give you the ability to find items hidden by magic.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "5 ft.",
                "duration": "Concentration, up to 1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Message",
                "description": "You can whisper messages and receive whispered replies. Those nearby can hear these messages with a DC 25 Perception check. You point your finger at each creature you want to receive the message.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "10 min./level",
                "components": "V, S, F (a piece of copper wire)"
            },
            {
                "name": "Open/Close",
                "description": "You can open or close (your choice) a door, chest, box, window, bag, pouch, bottle, barrel, or other container. If anything resists this activity (such as a bar on a door or a lock on a chest), the spell fails.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, F (a brass key)"
            },
            {
                "name": "Prestidigitation",
                "description": "Prestidigitations are minor tricks that novice spellcasters use for practice. Once cast, a prestidigitation spell enables you to perform simple magical effects for 1 hour.",
                "level": 0,
                "school": "Universal",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "1 hour",
                "components": "V, S"
            },
            {
                "name": "Purify Food and Drink",
                "description": "This spell makes spoiled, rotten, diseased, poisonous, or otherwise contaminated food and water pure and suitable for eating and drinking. This spell does not prevent subsequent natural decay or spoilage.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Read Magic",
                "description": "You can decipher magical inscriptions on objects—books, scrolls, weapons, and the like—that would otherwise be unintelligible. This deciphering does not normally invoke the magic contained in the writing, although it may do so in the case of a cursed or trapped scroll.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level",
                "components": "V, S, F (a clear crystal or mineral prism)"
            },
            {
                "name": "Resistance",
                "description": "You imbue the subject with magical energy that protects it from harm, granting it a +1 resistance bonus on saves.",
                "level": 0,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute",
                "components": "V, S, M (a miniature cloak)"
            },
            {
                "name": "Spark",
                "description": "You can make an unattended flammable object no larger than a Huge creature burst into flames. This spell can target one Fine object or up to a 5-foot cube of loose material.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V or S"
            },
            {
                "name": "Stabilize",
                "description": "Upon casting this spell, you target a living creature that has –1 or fewer hit points. That creature is automatically stabilized and does not lose any more hit points. If the creature later takes damage, it continues dying normally.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Dancing Lights",
                "description": "You create up to four lights that resemble lanterns or torches, or four glowing spheres of light, or one faintly glowing, vaguely humanoid shape. The dancing lights must stay within a 10-foot-radius area in relation to each other but otherwise move as you desire.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 minute (D)",
                "components": "V, S"
            },
            {
                "name": "Disrupt Undead",
                "description": "You direct a ray of positive energy. You must make a ranged touch attack to hit, and if the ray hits an undead creature, it deals 1d6 points of damage to it.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Know Direction",
                "description": "When you cast this spell, you instantly know the direction of north from your current position. The spell is effective in any environment in which 'north' exists, but it may not work in extraplanar settings.",
                "level": 0,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Lullaby",
                "description": "Any creature within the area that fails a Will save becomes drowsy and inattentive, taking a –5 penalty on Perception checks and a –2 penalty on Will saves against sleep effects while the lullaby is in effect.",
                "level": 0,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Concentration + 1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Ray of Frost",
                "description": "A ray of freezing air and ice projects from your pointing finger. You must succeed on a ranged touch attack with the ray to deal damage to a target. The ray deals 1d3 points of cold damage.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Spark",
                "description": "You can make an unattended Fine flammable object catch on fire. This works as if you were using flint and steel except that you can use spark in any sort of weather and it takes much less time to actually ignite an object.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V or S"
            },
            {
                "name": "Summon Instrument",
                "description": "This spell summons one handheld musical instrument of your choice. This instrument appears in your hands or at your feet (your choice). The instrument is typical for its type. Only one instrument appears per casting, and it will play only for you.",
                "level": 0,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "0 ft.",
                "duration": "1 minute/level (D)",
                "components": "V, S"
            },
            {
                "name": "Touch of Fatigue",
                "description": "You channel negative energy through your touch that fatigues the target. You must succeed on a touch attack to strike a target, and the subject becomes fatigued for the spell's duration.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 round/level",
                "components": "V, S, M (a drop of sweat)"
            },
            {
                "name": "Virtue",
                "description": "The subject gains 1 temporary hit point for the duration of the spell.",
                "level": 0,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute",
                "components": "V, S, DF"
            },

            {
                "name": "Abundant Ammunition",
                "description": "This spell creates copies of ammunition fired from a projectile weapon. When used on a loaded projectile weapon, the ammunition fired creates a duplicate that also fires at the same target. This counts as one attack.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, M (a single piece of ammunition)"
            },
            {
                "name": "Air Bubble",
                "description": "Creates a small pocket of breathable air around the target's head or a small air bubble in water. This does not provide the ability to speak normally while underwater.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, M (a small glass bead)"
            },
            {
                "name": "Adhesive Spittle",
                "description": "You create a patch of sticky goo that covers one 5-foot square. Any creature moving through the square takes a -20 penalty to Acrobatics checks and must make a Reflex save or become entangled. A successful save means the creature can move through the square at half speed.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 minute/level",
                "components": "V, S"
            },
            {
                "name": "Cause Fear",
                "description": "The affected creature becomes frightened. If the subject succeeds on a Will save, it is shaken for 1 round. Creatures with 6 or more Hit Dice are immune to this effect.",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1d4 rounds or 1 round; see text",
                "components": "V, S"
            },
            {
                "name": "Corrosive Touch",
                "description": "Your successful melee touch attack deals 1d4 points of acid damage per level (maximum 5d4). If you hold the charge for multiple rounds, each round that passes reduces the damage by 1d4 (minimum 1d4).",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Deathwatch",
                "description": "Using the powers of necromancy, you can determine the condition of creatures near death within the spell's range. You instantly know whether each creature within the area is dead, fragile (alive and wounded, with 3 or fewer hit points left), fighting off death (alive with 4 or more hit points), undead, or neither alive nor dead (such as a construct).",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "10 minutes/level",
                "components": "V, S"
            },
            {
                "name": "Detect Undead",
                "description": "You can detect the aura that surrounds undead creatures. The amount of information revealed depends on how long you study a particular area: 1st round - presence or absence of undead auras; 2nd round - number of undead auras and the strength of the strongest aura; 3rd round - the strength and location of each undead aura.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft. cone",
                "duration": "Concentration, up to 1 minute/level (D)",
                "components": "V, S, M/DF (earth from a grave)"
            },
            {
                "name": "Divine Favor",
                "description": "Calling upon the strength and wisdom of a deity, you gain a +1 luck bonus on attack and weapon damage rolls for every three caster levels you have (at least +1, maximum +3). The bonus doesn't apply to spell damage.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute",
                "components": "V, S, DF"
            },
            {
                "name": "Endure Elements",
                "description": "A creature protected by endure elements suffers no harm from being in a hot or cold environment. It can exist comfortably in conditions between -50 and 140 degrees Fahrenheit without having to make Fortitude saves. The creature's equipment is likewise protected.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "24 hours",
                "components": "V, S"
            },
            {
                "name": "Entropic Shield",
                "description": "A magical field appears around you, glowing with a chaotic blast of multicolored hues. This field deflects incoming arrows, rays, and other ranged attacks. Each ranged attack directed at you for which the attacker must make an attack roll has a 20% miss chance.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Hide from Animals",
                "description": "Animals cannot see, hear, or smell you or your companions. Even extraordinary or supernatural sensory capabilities cannot detect you. Animals simply act as though you aren't there. If you touch or attack an animal, the spell ends for all recipients.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level (D)",
                "components": "S, DF"
            },
            {
                "name": "Hide from Undead",
                "description": "Undead cannot see, hear, or smell the warded creatures. Even extraordinary or supernatural sensory capabilities cannot detect the warded creatures. Undead simply act as though the warded creatures are not there. If a warded creature attempts to turn or command undead, touches an undead creature, or attacks any creature, the spell ends for all recipients.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Ill Omen",
                "description": "You afflict the target with bad luck. On the next d20 roll the target makes, it must roll twice and take the less favorable result. For every five caster levels you possess, the target must roll twice and take the less favorable result on an additional d20 roll (maximum 4 rolls at 20th level).",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level or until discharged",
                "components": "V, S, M (hair from a black cat)"
            },
            {
                "name": "Magic Stone",
                "description": "You transmute as many as three pebbles, which can be no larger than sling bullets, so that they strike with great force when thrown or slung. If thrown, they have a range increment of 20 feet. Each stone deals 1d6+1 points of damage (including the spell's enhancement bonus). Against undead, each stone deals 2d6+2 points of damage.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "30 minutes or until discharged",
                "components": "V, S, DF"
            },
            {
                "name": "Obscure Object",
                "description": "This spell hides an object from location by divination (scrying) effects, such as the detect spells, locate object, and detect magic. It also prevents the object from being detected by crystal balls and other scrying devices. Attempts to view the object through scrying automatically fail.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "8 hours (D)",
                "components": "V, S, M/DF (chameleon skin)"
            },
            {
                "name": "Protection from Good",
                "description": "This spell functions like protection from evil, except that the deflection and resistance bonuses apply to attacks made by good creatures. The target receives a +2 bonus on saving throws against effects created by good creatures, and blocks possession and mental influence just as protection from evil does.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, S, M/DF"
            },
            {
                "name": "Protection from Law",
                "description": "This spell functions like protection from evil, except that the deflection and resistance bonuses apply to attacks made by lawful creatures. The target receives a +2 bonus on saving throws against effects created by lawful creatures, and blocks possession and mental influence just as protection from evil does.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, S, M/DF"
            },
            {
                "name": "Detect Animals or Plants",
                "description": "You can detect a particular kind of animal or plant in a cone emanating out from you in whatever direction you face. You must think of a kind of animal or plant when using the spell, but you can change the animal or plant kind each round. The amount of information revealed depends on how long you search a particular area.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Concentration, up to 10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Detect Snares and Pits",
                "description": "You can detect simple and complex snares, pits, and other outdoor traps. The spell does not detect magical traps (except those that operate by pit, thread, or similar mechanical triggers), nor does it detect traps that have been rendered safe or inactive.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Concentration, up to 10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Remove Fear",
                "description": "You instill courage in the subject, granting it a +4 morale bonus against fear effects for 10 minutes. If the subject is under the influence of a fear effect when receiving the spell, that effect is suppressed for the duration of the spell.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "10 minutes; see text",
                "components": "V, S"
            },
            {
                "name": "Sanctify Corpse",
                "description": "This spell preserves a corpse from decay and prevents it from being turned into an undead creature. The corpse is protected as if by gentle repose. If cast on a corpse that has already been animated as an undead, the creature must make a Will save or be destroyed.",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "24 hours",
                "components": "V, S, M/DF (a pinch of silver dust)"
            },
            {
                "name": "Shield of Faith",
                "description": "This spell creates a shimmering, magical field around the target that averts and deflects attacks. The spell grants the subject a +2 deflection bonus to AC, with an additional +1 to the bonus for every six levels you have (maximum +5 deflection bonus at 18th level).",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M (a small parchment with a bit of holy text written on it)"
            },
            {
                "name": "Touch of Gracelessness",
                "description": "With a touch, you reduce a target's grace and coordination. The target takes a -2 penalty to its Dexterity, and is knocked prone whenever it attempts to move more than half its speed during its turn. A successful Fortitude save negates the prone effect but not the Dexterity penalty.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Undetectable Alignment",
                "description": "This spell conceals the alignment of an object or creature from all forms of divination. When cast on a creature, the spell also prevents the creature's alignment from being detected through any magical effects or abilities that would do so.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "24 hours",
                "components": "V, S"
            },
            {
                "name": "Vision of Hell",
                "description": "You fill your target's mind with visions of Hell, causing them to become shaken. Evil creatures are immune to this effect. If the target fails their save, they are shaken for the duration of the spell and take a -2 penalty on saving throws against fear effects.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Pass Without Trace",
                "description": "The subject or subjects of this spell can move through any type of terrain and leave neither footprints nor scent. Tracking the subjects is impossible by nonmagical means.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Ray of Enfeeblement",
                "description": "A coruscating ray springs from your hand. You must succeed on a ranged touch attack to strike a target. The subject takes a penalty to Strength equal to 1d6+1 per two caster levels (maximum 1d6+5). The subject's Strength score cannot drop below 1.",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Summon Nature's Ally I",
                "description": "This spell summons a natural creature. It appears where you designate and acts immediately, on your turn. It attacks your opponents to the best of its ability. The creature summoned must be from the 1st-level list on the Summon Nature's Ally table.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Longstrider",
                "description": "This spell increases your base land speed by 10 feet. This enhancement bonus stacks with other effects that increase your speed.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 hour/level (D)",
                "components": "V, S, M (a pinch of dirt)"
            },
            {
                "name": "Alter Winds",
                "description": "You can alter the strength and direction of the winds within the area of effect. You can make the winds blow in a certain direction or manner, increase its strength, or decrease its strength.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "1 hour/level",
                "components": "V, S"
            },
            {
                "name": "Ant Haul",
                "description": "The target's carrying capacity triples. This does not affect the creature's actual Strength in any way, just the amount of material it can carry.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "2 hours/level",
                "components": "V, S, M (a small rope)"
            },
            {
                "name": "Aspect of the Falcon",
                "description": "You take on an aspect of a falcon. Your eyes become wide and raptor-like, and you gain a +3 competence bonus on Perception checks, a +1 competence bonus on ranged attacks, and the ability to ignore the first range increment penalty when making ranged attacks.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level",
                "components": "V, S, DF"
            },
            {
                "name": "Beguiling Gift",
                "description": "You offer an object to an adjacent creature who must make a Will save or be compelled to accept your gift and immediately put it to use, dropping whatever it was holding if necessary. The creature may still recognize the item as dangerous, and will not automatically use an item it knows to be harmful.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "5 ft.",
                "duration": "1 round",
                "components": "V, S, M (the object to be offered)"
            },
            {
                "name": "Burst Bonds",
                "description": "With a burst of strength, you break the bonds that hold you. You gain a +20 enhancement bonus on a single Strength check attempted to break bindings, break free of grapples, or escape from manacles. This bonus applies to your combat maneuver check when attempting to break free from a grapple.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Dancing Lantern",
                "description": "You can animate a lantern to follow you and provide light. The lantern sheds light as a normal lantern, hovers 3 feet above the ground, and moves with you, remaining within 5 feet of you at all times.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, F (a lantern)"
            },
            {
                "name": "Ear-Piercing Scream",
                "description": "You unleash a powerful scream, inaudible to all but a single target. The target is dazed for 1 round and takes 1d6 points of sonic damage per two caster levels (maximum 5d6).",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Floating Disk",
                "description": "You create a slightly concave, circular plane of force that follows you about and carries loads for you. The disk is 3 feet in diameter and 1 inch deep at its center. It can hold 100 pounds of weight per caster level.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level",
                "components": "V, S, M (a drop of mercury)"
            },
            {
                "name": "Force Hook Charge",
                "description": "You create a hook of force that you can use to make a charge attack. When you cast this spell, you choose a point of origin for the hook within medium range. As part of casting this spell, you can move up to twice your speed in a straight line to a space adjacent to the hook's origin.",
                "level": 1,
                "school": "Force",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Frostbite",
                "description": "Your touch causes a creature's blood to freeze. The target takes 1d6 points of nonlethal cold damage + 1 point per level, and is fatigued. A successful Fortitude save negates the fatigue.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Hero's Defiance",
                "description": "This spell cures 1d8 points of damage + 1 point per caster level (maximum +5). Unlike other cure spells, hero's defiance can be cast even if you've used your last spell slot of that level, but if you do so, you cannot cast any spells for 1 round.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Hold Portal",
                "description": "This spell magically holds shut a door, gate, window, or shutter of wood, metal, or stone. The magic affects the portal just as if it were securely closed and normally locked.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 min./level (D)",
                "components": "V"
            },
            {
                "name": "Instant Armor",
                "description": "You instantly wrap your body in a suit of armor made from force. This armor grants you an armor bonus of +4. It has no armor check penalty, arcane spell failure chance, or speed reduction. Since instant armor is made of force, incorporeal creatures can't bypass it the way they do normal armor.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S, F (a masterwork suit of armor)"
            },
            {
                "name": "Bless Water",
                "description": "This transmutation imbues a flask (1 pint) of water with positive energy, turning it into holy water. Holy water damages undead creatures and evil outsiders as though it were acid.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (5 pounds of powdered silver worth 25 gp)"
            },
            {
                "name": "Summon Minor Ally",
                "description": "This spell functions as summon nature's ally I, except you can summon 1d3 Tiny or smaller animals, such as bats, lizards, monkeys, rats, ravens, toads, or weasels. The summoned animals must all be the same type of creature.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Vanish",
                "description": "This spell functions like invisibility, except the duration is only a few rounds. The subject vanishes from sight, even from darkvision. If the creature attacks or casts a spell, this spell ends just as invisibility does.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 round/level (up to 5 rounds) (D)",
                "components": "V, S"
            },
            {
                "name": "Wrath",
                "description": "You fill a single target with divine fury. The target gains a +2 morale bonus on melee attack rolls, melee weapon damage rolls, and saving throws against fear effects. It gains 5 temporary hit points per caster level (maximum 5).",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute",
                "components": "V, S"
            },
            {
                "name": "Lock Gaze",
                "description": "You compel the target to constantly meet your gaze for the duration of the spell. The target can attempt to break eye contact as a move action by succeeding at a Will save, but it must succeed at a second Will save during the same round or immediately reestablish eye contact.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Magic Aura",
                "description": "You alter an item's aura so that it registers to detect spells as though it were non-magical, or as a magic item of a kind you specify, or as the subject of a spell you specify.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 day/level (D)",
                "components": "V, S, F (a small square of silk)"
            },
            {
                "name": "Restore Virtue",
                "description": "You restore the target's lost honor and dignity, granting them a +4 sacred bonus on saving throws against charm and compulsion effects for the duration of the spell.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, DF"
            },
            {
                "name": "Sacrifice",
                "description": "You transfer some of your life force to heal another creature. You take 1d4 points of damage and the target regains a number of hit points equal to double the damage you take. This damage cannot be reduced in any way.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Shillelagh",
                "description": "Your wooden weapon transforms into a weapon with greater power. The weapon gains a +1 enhancement bonus on attack and damage rolls. A quarterstaff gains this enhancement for both ends. The spell can affect any club, quarterstaff, or other wooden weapon.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Alarm",
                "description": "Alarm creates a subtle ward on an area you select. When a creature enters the warded area, the alarm alerts you.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level",
                "components": "V, S, F/DF (a tiny bell and a piece of very fine silver wire)"
            },
            {
                "name": "Animate Rope",
                "description": "You can animate a rope-like object. The maximum length assumes a rope with a 1-inch diameter.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Burning Hands",
                "description": "A cone of searing flame shoots from your fingertips. Any creature in the area of the flames takes 1d4 points of fire damage per caster level (maximum 5d4).",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "15 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Charm Person",
                "description": "This charm makes a humanoid creature regard you as its trusted friend and ally. If the creature is currently being threatened or attacked by you or your allies, however, it receives a +5 bonus on its saving throw.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level",
                "components": "V, S"
            },
            {
                "name": "Color Spray",
                "description": "A vivid cone of clashing colors springs forth from your hand, causing creatures to become stunned, perhaps also blinded, and possibly knocking them unconscious.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "15 ft.",
                "duration": "Instantaneous; see text",
                "components": "V, S, M (red, yellow, and blue powder or colored sand)"
            },
            {
                "name": "Comprehend Languages",
                "description": "You can understand the spoken words of creatures or read otherwise incomprehensible written messages.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level",
                "components": "V, S, M (a pinch of soot and salt)"
            },
            {
                "name": "Cure Light Wounds",
                "description": "When laying your hand upon a living creature, you channel positive energy that cures 1d8 points of damage + 1 point per caster level (maximum +5).",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Detect Secret Doors",
                "description": "You can detect secret doors, compartments, caches, and so forth.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Concentration, up to 1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Disguise Self",
                "description": "You make yourself—including clothing, armor, weapons, and equipment—look different.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Erase",
                "description": "Erase removes writings of either magical or mundane nature from a scroll or from one or two pages of paper, parchment, or similar surfaces.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Expeditious Retreat",
                "description": "This spell increases your base land speed by 30 feet. This adjustment is treated as an enhancement bonus.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Feather Fall",
                "description": "The affected creatures or objects fall slowly. Feather fall instantly changes the rate at which the targets fall to a mere 60 feet per round (equivalent to the end of a fall from a few feet), and the subjects take no damage upon landing while the spell is in effect.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 immediate action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Until landing or 1 round/level",
                "components": "V"
            },
            {
                "name": "Grease",
                "description": "A grease spell covers a solid surface with a layer of slippery grease. Any creature in the area when the spell is cast must make a successful Reflex save or fall.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level (D)",
                "components": "V, S, M (butter)"
            },
            {
                "name": "Identify",
                "description": "This spell functions as detect magic, except that it gives you a +10 enhancement bonus on Spellcraft checks made to identify the properties and command words of magic items in your possession.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "3 rounds/level (D)",
                "components": "V, S, M (wine stirred with an owl's feather)"
            },
            {
                "name": "Magic Missile",
                "description": "A missile of magical energy darts forth from your fingertip and strikes its target, dealing 1d4+1 points of force damage.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Mage Armor",
                "description": "An invisible but tangible field of force surrounds the subject of a mage armor spell, providing a +4 armor bonus to AC.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, F (a piece of cured leather)"
            },
            {
                "name": "Protection from Evil",
                "description": "This spell wards a creature from attacks by evil creatures, from mental control, and from summoned creatures.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, S, M/DF"
            },
            {
                "name": "Shield",
                "description": "Shield creates an invisible shield of force that hovers in front of you. It negates magic missile attacks directed at you.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Silent Image",
                "description": "This spell creates the visual illusion of an object, creature, or force, as visualized by you.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Concentration",
                "components": "V, S, F (a bit of fleece)"
            },
            {
                "name": "Sleep",
                "description": "A sleep spell causes a magical slumber to come upon 4 HD of creatures.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 round",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 min./level",
                "components": "V, S, M (fine sand, rose petals, or a live cricket)"
            },
            {
                "name": "Curse Water",
                "description": "This spell imbues a flask (1 pint) of water with negative energy, turning it into unholy water. Unholy water damages good outsiders as if it were acid. A cleric of an evil deity must cast this spell.",
                "level": 1,
                "school": "Necromancy",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (5 pounds of powdered silver worth 25 gp)"
            },
            {
                "name": "True Strike",
                "description": "You gain temporary, intuitive insight into the immediate future during your next attack. Your next single attack roll (if it is made before the end of the next round) gains a +20 insight bonus. Additionally, you are not affected by the miss chance that applies to attackers trying to strike a concealed target.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "See text",
                "components": "V, F (small wooden replica of an archery target)"
            },
            {
                "name": "Bless Water",
                "description": "This transmutation imbues a flask (1 pint) of water with positive energy, turning it into holy water. Holy water damages undead creatures and evil outsiders as if it were acid.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (5 pounds of powdered silver worth 25 gp)"
            },
            {
                "name": "Hypnotism",
                "description": "Your gestures and droning incantation fascinate nearby creatures, causing them to stop and stare blankly at you. In addition, you can use their rapt attention to make your suggestions and requests seem more reasonable. Roll 2d4 to see how many total HD of creatures you affect.",
                "level": 1,
                "school": "Enchantment",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2d4 rounds (D)",
                "components": "V, S"
            },
            {
                "name": "Magic Weapon",
                "description": "Magic weapon gives a weapon a +1 enhancement bonus on attack and damage rolls. An enhancement bonus does not stack with a masterwork weapon's +1 bonus on attack rolls.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Mount",
                "description": "You summon a light horse or a pony (your choice) to serve you as a mount. The steed serves willingly and well. The mount comes with a bit and bridle and a riding saddle.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (a bit of horse hair)"
            },
            {
                "name": "Obscuring Mist",
                "description": "A misty vapor arises around you. It is stationary. The vapor obscures all sight, including darkvision, beyond 5 feet. A creature 5 feet away has concealment (20% miss chance). Creatures farther away have total concealment (50% miss chance, and the attacker cannot use sight to locate the target).",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "20 ft.",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Ventriloquism",
                "description": "You can make your voice (or any sound that you can normally make vocally) seem to issue from someplace else. You can speak in any language you know. With respect to such voices and sounds, anyone who hears the sound and rolls a successful save recognizes it as illusory (but still hears it).",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level (D)",
                "components": "V, F (parchment rolled into cone)"
            },
            {
                "name": "Dancing Lights",
                "description": "Depending on version chosen, you create up to four lights that resemble lanterns or torches, up to four glowing spheres of light, or one faintly glowing, humanoid-shaped form. The dancing lights must stay within a 10-foot-radius area in relation to each other but otherwise move as you desire.",
                "level": 0,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 minute (D)",
                "components": "V, S"
            },
            {
                "name": "Disrupt Undead",
                "description": "You direct a ray of positive energy. You must make a ranged touch attack to hit, and if the ray hits an undead creature, it deals 1d6 points of damage to it.",
                "level": 0,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Nystul's Magic Aura",
                "description": "You alter an item's aura so that it registers to detect spells as though it were nonmagical, or a magic item of a kind you specify, or the subject of a spell you specify. If the object bearing the aura has identify cast on it or is similarly examined, the examiner recognizes that the aura is false.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 day/level (D)",
                "components": "V, S, F (a small square of silk that must be passed over the object)"
            },
            {
                "name": "Summon Monster I",
                "description": "This spell summons an extraplanar creature (typically an outsider, elemental, or magical beast native to another plane). It appears where you designate and acts immediately, on your turn. It attacks your opponents to the best of its ability. The monster summoned must be from the 1st-level list in the Summon Monster table.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S, F/DF (a tiny bag and a small candle)"
            },
            {
                "name": "Heightened Awareness",
                "description": "You enter a heightened state of awareness that allows you to notice more about your surroundings and recall information more easily. You gain a +2 competence bonus on Perception checks and Knowledge checks for the duration of the spell.",
                "level": 1,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 minutes/level",
                "components": "V, S"
            },
            {
                "name": "Targeted Bomb Admixture",
                "description": "Upon drinking this extract, you can choose to have your next bomb deal its damage as a single type: acid, cold, electricity, or fire. Additionally, the bomb's damage increases by 1d6 points and ignores resistance (but not immunity) to the chosen energy type.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level or until discharged",
                "components": "V, S"
            },
            {
                "name": "Dancing Lantern",
                "description": "You can animate a lantern to follow you. The lantern floats at shoulder height and remains within 5 feet of you, moving as you move. The lantern can't attack in any way, but it can use its own light as a light source. The lantern is made of force, even if it looks like a real lantern.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, F (a common lantern)"
            },
            {
                "name": "Disguise Self",
                "description": "You make yourself—including clothing, armor, weapons, and equipment—look different. You can seem 1 foot shorter or taller, thin, fat, or in between. You cannot change your creature type. Otherwise, the extent of the apparent change is up to you.",
                "level": 1,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Divine Favor",
                "description": "You gain a +1 luck bonus on attack and weapon damage rolls for every three caster levels you have (at least +1, maximum +3). The bonus doesn't apply to spell damage.",
                "level": 1,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute",
                "components": "V, S, DF"
            },
            {
                "name": "Shield of Faith",
                "description": "This spell creates a shimmering, magical field around the touched creature that averts and deflects attacks. The spell grants the subject a +2 deflection bonus to AC, with an additional +1 to the bonus for every six levels you have (maximum +5 deflection bonus at 18th level).",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M (a small parchment with a bit of holy text written on it)"
            },
            {
                "name": "Expeditious Excavation",
                "description": "You can excavate and move earth, dust, and sand up to the size of a 5-foot cube. If you excavate a wall, objects on that wall do not fall. The excavation does not create walls of loose soil, since the sides of the excavation are packed tight.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, M (tiny shovel)"
            },
            {
                "name": "Guardian Shell",
                "description": "You create a magical shell around yourself that turns aside ranged attacks. You gain a +4 deflection bonus to AC against ranged attacks. The shell has no effect on melee attacks.",
                "level": 1,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Liberating Command",
                "description": "Target creature can immediately attempt to break free from a grapple, pin, or entanglement effect that is hindering its movement with a +4 bonus on the check. The target can attempt this check even if it would not normally be able to take actions.",
                "level": 1,
                "school": "Transmutation",
                "casting_time": "1 immediate action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Stone Shield",
                "description": "You create a stone barrier that springs up from the ground, protecting you against one attack. The barrier provides cover (+4 AC), and grants you a +2 bonus to AC against the triggering attack.",
                "level": 1,
                "school": "Conjuration",
                "casting_time": "1 immediate action",
                "range": "Personal",
                "duration": "1 round or until discharged",
                "components": "V, S"
            },
            {
                "name": "Ablative Barrier",
                "description": "You create a protective barrier that absorbs damage from attacks. The barrier provides DR 5/— until its hit points are depleted. The barrier has 5 hit points per caster level (maximum 50).",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level or until depleted",
                "components": "V, S, M (a piece of metal)"
            },
            {
                "name": "Frigid Touch",
                "description": "Your touch causes ice to form on your target, dealing 4d6 points of cold damage and possibly entangling it. The target must make a Fortitude save or become entangled for 1 round per caster level.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous and 1 round/level (see text)",
                "components": "V, S"
            },
            {
                "name": "Levitate",
                "description": "Levitate allows you to move yourself, another creature, or an object up and down as you wish. A creature must be willing to be levitated, and an object must be unattended or possessed by a willing creature.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal or close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level (D)",
                "components": "V, S, F (either a small leather loop or a piece of golden wire bent into a cup shape)"
            },
            {
                "name": "Ant Haul, Communal",
                "description": "This spell functions like ant haul, except you divide the duration in 2-hour increments among the creatures touched. Each creature must receive at least a 2-hour duration increment.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "2 hours/level",
                "components": "V, S, M (a small pulley)"
            },
            {
                "name": "Protection from Arrows, Communal",
                "description": "This spell functions like protection from arrows, except you divide the duration in 1-hour increments among the creatures touched. Each creature must receive at least a 1-hour duration increment.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, F (a piece of tortoise shell or turtle shell)"
            },
            {
                "name": "Warding Weapon",
                "description": "You enchant a weapon to defend you while you cast spells. The weapon gains a +1 enhancement bonus per four caster levels (maximum +5) and hovers near you, automatically interposing itself between you and any attacks made against you.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 round/level",
                "components": "V, S, F (weapon to be enchanted)"
            },
            {
                "name": "Ghostbane Dirge",
                "description": "The target incorporeal creature takes half damage from nonmagical weapons and full damage from magic weapons and spells. The subject also loses its own incorporeal miss chance, and takes full damage from corporeal creatures' attacks.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, M/DF (a pinch of salt)"
            },
            {
                "name": "Pilfering Hand",
                "description": "You create and control an invisible telekinetic force that can manipulate objects weighing up to 5 pounds. You can use this force to steal small items from other creatures or to pick up and move objects at range.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Concentration",
                "components": "V, S"
            },
            {
                "name": "Share Memory",
                "description": "You transfer a specific memory of yours to the target. This memory must be no longer than 1 minute in length. The target experiences this memory as if it were one of their own memories, including any emotions or sensations associated with the memory.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Continual Flame",
                "description": "A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A continual flame can be covered and hidden but not smothered or quenched.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S, M (ruby dust worth 50 gp)"
            },
            {
                "name": "Daze Monster",
                "description": "This spell functions like daze, but daze monster can affect any one living creature of any type. Creatures of 7 or more HD are immune to this effect.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round",
                "components": "V, S, M (a pinch of wool or similar substance)"
            },
            {
                "name": "Fog Cloud",
                "description": "A bank of fog billows out from the point you designate. The fog obscures all sight, including darkvision, beyond 5 feet. A creature within 5 feet has concealment. Creatures farther away have total concealment.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Gust of Wind",
                "description": "This spell creates a severe blast of air that originates from you, affecting all creatures in its path. A Tiny or smaller creature must succeed on a Fortitude save or be thrown back 1d4×10 feet. Small creatures are knocked prone by the force of the wind unless they succeed on a Fortitude save.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "1 round",
                "components": "V, S"
            },
            {
                "name": "Shatter",
                "description": "Shatter creates a loud, ringing noise that breaks brittle, nonmagical objects; sunders a single solid, nonmagical object; or damages a crystalline creature. Used as an area attack, shatter destroys nonmagical objects of crystal, glass, ceramic, or porcelain.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (a chip of mica)"
            },
            {
                "name": "Spider Climb",
                "description": "The subject can climb and travel on vertical surfaces or even traverse ceilings as well as a spider does. The affected creature must have its hands free to climb in this manner. The subject gains a climb speed of 20 feet and a +8 racial bonus on Climb skill checks.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M (a drop of bitumen and a live spider)"
            },
            {
                "name": "Summon Swarm",
                "description": "You summon a swarm of bats, rats, or spiders (your choice), which attacks all other creatures within its area. The swarm does not attack creatures that fill its entire space but surrounds them, attacking any creature that enters or leaves the swarm.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Concentration + 2 rounds",
                "components": "V, S, M/DF (a square of red cloth)"
            },
            {
                "name": "Whispering Wind",
                "description": "You send a message or sound on the wind to a designated spot. The whispering wind travels to a specific location within range that is familiar to you, provided that it can find a way to the location. The message is clearly heard by any creatures within a 10-foot radius.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "1 mile/level",
                "duration": "No more than 1 hour/level or until discharged (destination is reached)",
                "components": "V, S"
            },
            {
                "name": "Align Weapon",
                "description": "Align weapon makes a weapon good, evil, lawful, or chaotic, as you choose. A weapon that is aligned can bypass the damage reduction of certain creatures. This spell has no effect on a weapon that already has an alignment.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Augury",
                "description": "An augury can tell you whether a particular action will bring good or bad results for you in the immediate future. The base chance for receiving a meaningful reply is 70% + 1% per caster level, to a maximum of 90%; this roll is made secretly.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Personal",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (incense worth at least 25 gp), F (a set of marked sticks or bones worth at least 25 gp)"
            },
            {
                "name": "Hideous Laughter",
                "description": "This spell afflicts the subject with uncontrollable laughter. It collapses into gales of manic laughter, falling prone. The subject can take no actions while laughing, but is not considered helpless. On the creature's next turn, it may attempt a new save to end the effect.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, M (tiny tarts that are thrown at the target and a feather that is waved in the air)"
            },
            {
                "name": "Pyrotechnics",
                "description": "This spell can turn a fire into either a burst of blinding fireworks or a thick cloud of choking smoke, depending on your choice. A fire source must be present for this spell to function.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1d4+1 rounds or 1d4+1 rounds after creatures leave the smoke cloud; see text",
                "components": "V, S, M (one fire source)"
            },
            {
                "name": "Scare",
                "description": "This spell causes creatures of 5 or fewer HD to become frightened. If the subject succeeds on a Will save, it is shaken for 1 round. Creatures with 6 or more Hit Dice are immune to this effect.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level or 1 round; see text",
                "components": "V, S, M (a bit of bone from an undead skeleton, zombie, ghoul, ghast, or mummy)"
            },
            {
                "name": "Sound Burst",
                "description": "You blast an area with a tremendous cacophony. Every creature in the area takes 1d8 points of sonic damage and must succeed on a Fortitude save to avoid being stunned for 1 round. Creatures that cannot hear are not stunned but are still damaged.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, F/DF (a musical instrument)"
            },
            {
                "name": "Spiritual Weapon",
                "description": "A weapon made of force appears and attacks foes at a distance, as you direct it, dealing 1d8 force damage per hit, + 1 per three caster levels (maximum +5 at 15th level). The weapon takes the shape of a weapon favored by your deity or a weapon with spiritual significance for you.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Acid Arrow",
                "description": "A magical arrow of acid springs from your hand and speeds to its target. You must succeed on a ranged touch attack to hit your target. The arrow deals 2d4 points of acid damage with no splash damage.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 round + 1 round per three levels",
                "components": "V, S, M (rhubarb leaf and an adder's stomach), F (a dart)"
            },
            {
                "name": "Alter Self",
                "description": "You assume the form of a creature of the same type as your normal form. The new form must be within one size category of your normal size.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S, M (a piece of the creature whose form you plan to assume)"
            },
            {
                "name": "Blur",
                "description": "The subject's outline appears blurred, shifting and wavering. This distortion grants the subject concealment (20% miss chance).",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V"
            },
            {
                "name": "Animal Aspect",
                "description": "You gain some of the beneficial qualities of an animal. Choose one of the following animals to gain its qualities: ape (+2 climb), bear (+2 CMD), bull (+2 CMB), falcon (+2 sight-based Perception), frog (+2 Acrobatics), monkey (+2 Acrobatics), owl (+2 stealth), or stag (+2 speed).",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Arcane Lock",
                "description": "An arcane lock spell cast upon a door, chest, or portal magically locks it. You can freely pass your own arcane lock without affecting it. While arcane lock is active, the DC to break open the door or lock increases by 10.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S, M (gold dust worth 25 gp)"
            },
            {
                "name": "Animal Messenger",
                "description": "You compel a Tiny animal to go to a spot you designate. The most common messengers are birds. The animal cannot be one you control through other means. It will wait there until someone takes the item it's carrying or returns with a reply.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S, M (a morsel of food)"
            },
            {
                "name": "Animal Trance",
                "description": "Your swaying motions and music (or singing, or chanting) compel animals to do nothing but watch you. Only normal animals (those with Intelligence scores of 1 or 2) can be fascinated by this spell. Roll 2d6 to determine the total number of HD worth of creatures that you fascinate.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Concentration",
                "components": "V, S"
            },
            {
                "name": "Consecrate",
                "description": "This spell blesses an area with positive energy. Each Charisma check made to turn undead within this area gains a +3 sacred bonus. Undead suffer minor disruption while in the area. Undead cannot be created within or summoned into a consecrated area.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level",
                "components": "V, S, M (a vial of holy water and 25 gp worth of silver dust), DF"
            },
            {
                "name": "Death Knell",
                "description": "You draw forth the ebbing life force of a creature and use it to fuel your own power. Upon casting this spell, you touch a living creature that has -1 or fewer hit points. If the subject fails its saving throw, it dies, and you gain 1d8 temporary hit points and a +2 enhancement bonus to Strength.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 minutes/level",
                "components": "V, S"
            },
            {
                "name": "Delay Poison",
                "description": "The subject becomes temporarily immune to poison. Any poison in its system or any poison to which it is exposed during the spell's duration does not affect the subject until the spell's duration has expired. Delay poison does not cure any damage that poison may have already done.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, DF"
            },
            {
                "name": "Desecrate",
                "description": "This spell imbues an area with negative energy. Each Charisma check made to turn undead within this area takes a -3 profane penalty, and undead within the area gain a +1 profane bonus to attack rolls, damage rolls, and saving throws. Undead created or summoned within a desecrate area gain +1 hit points per HD.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level",
                "components": "V, S, M (a vial of unholy water and 25 gp worth of black onyx), DF"
            },
            {
                "name": "Enthrall",
                "description": "If you succeed in a Perform check (DC 10 + 1 per creature), all creatures within range pay attention to you and ignore other distractions. Creatures with 4+ HD or Wisdom 16+ can attempt Will saves. Any obvious threat breaks the effect. If you fail the Perform check, subjects can attempt new saves to break free.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 round",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 hour or less",
                "components": "V, S"
            },
            {
                "name": "Find Traps",
                "description": "You gain intuitive insight into the presence of traps. You can use the Perception skill to notice traps as a free action and receive a +2 insight bonus on Perception checks made to find traps while the spell is in effect. The spell does not allow you to find traps you could not ordinarily find.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Grace",
                "description": "Until the end of your turn, your movement does not provoke attacks of opportunity. You can bring the benefits of this spell to bear the instant you cast it, and you can even cast it while taking a move action to gain its benefits during that movement.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 swift action",
                "range": "Personal",
                "duration": "See text",
                "components": "V"
            },
            {
                "name": "Make Whole",
                "description": "This spell functions like mending, except that it repairs 1d6 points of damage per level when cast on a constructed creature (maximum 5d6). Make whole can fix destroyed magic items, and restores the magic properties of the item if your caster level is at least twice that of the item.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "10 minutes",
                "range": "10 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Remove Paralysis",
                "description": "You can free one or more creatures from the effects of temporary paralysis or related magic, including a ghoul's touch or a slow spell. If the spell is cast on one creature, the paralysis is negated. If cast on two creatures, each receives another save with a +4 resistance bonus.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Shield Other",
                "description": "This spell wards the subject and creates a mystic connection between you and the subject so that some of its wounds are transferred to you. The subject gains a +1 deflection bonus to AC and a +1 resistance bonus on saves. Also, the subject takes only half damage from all wounds and attacks.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level (D)",
                "components": "V, S, F (a pair of platinum rings worth 50 gp worn by both you and the target)"
            },
            {
                "name": "Status",
                "description": "When you need to keep track of comrades who may get separated, status allows you to mentally monitor their relative positions and general condition. You are aware of direction and distance to the creatures and their status: unharmed, wounded, disabled, staggered, unconscious, dying, dead, etc.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S"
            },
            {
                "name": "Touch of Idiocy",
                "description": "With a touch, you reduce the target's mental faculties. Your successful melee touch attack applies a 1d6 penalty to the target's Intelligence, Wisdom, and Charisma scores. This penalty can't reduce any of these scores below 1.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S"
            },
            {
                "name": "Zone of Truth",
                "description": "Creatures within the emanation area (or those who enter it) can't speak any deliberate and intentional lies. Each potentially affected creature is allowed a save to avoid the effects when the spell is cast or when the creature first enters the emanation area. Affected creatures are aware of this enchantment.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Aspect of the Bear",
                "description": "You gain a +2 enhancement bonus to natural armor, a +2 enhancement bonus to Constitution, and you are treated as one size category larger when determining your CMB and CMD for grapple and overrun combat maneuvers.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Bear's Endurance",
                "description": "The affected creature gains greater vitality and stamina. The spell grants the subject a +4 enhancement bonus to Constitution, which adds the usual benefits to hit points, Fortitude saves, Constitution checks, and so forth.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, M/DF (a few hairs, or a pinch of dung, from a bear)"
            },
            {
                "name": "Chill Metal",
                "description": "Chill metal makes metal extremely cold. An unattended, nonmagical metal item gets no saving throw. A metal creature takes 2d4 points of cold damage and must make a Fortitude save or be slowed for 1 round.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "7 rounds",
                "components": "V, S, DF"
            },
            {
                "name": "Calm Emotions",
                "description": "This spell calms agitated creatures. You have no control over the affected creatures, but can prevent them from taking violent or hostile actions. Creatures so affected cannot take violent actions or do anything destructive. Any aggressive action against or damage dealt to a calmed creature immediately breaks the spell on all calmed creatures.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Concentration, up to 1 round/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Eagle's Splendor",
                "description": "The transmuted creature becomes more poised, articulate, and personally forceful. The spell grants a +4 enhancement bonus to Charisma, adding the usual benefits to Charisma-based skill checks and other uses of the Charisma modifier. Bards, paladins, and sorcerers gain bonus spells.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M/DF (feathers or droppings from an eagle)"
            },
            {
                "name": "Gentle Repose",
                "description": "You preserve the remains of a dead creature so that they do not decay. Doing so effectively extends the time limit on raising that creature from the dead. Days spent under the influence of this spell don't count against the time limit. Additionally, this spell makes transporting a fallen comrade more pleasant.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 day/level",
                "components": "V, S, M/DF (salt and a copper piece placed on each of the corpse's eyes)"
            },
            {
                "name": "Hold Person",
                "description": "This spell paralyzes a humanoid creature, freezing it in place. It is aware and breathes normally but cannot take any actions, even speech. Each round on its turn, the subject may attempt a new saving throw to end the effect. This is a full-round action that does not provoke attacks of opportunity.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, F/DF (a small, straight piece of iron)"
            },
            {
                "name": "Owl's Wisdom",
                "description": "The transmuted creature becomes wiser. The spell grants a +4 enhancement bonus to Wisdom, adding the usual benefits to Wisdom-based skill checks and other uses of the Wisdom modifier. Clerics, druids, and rangers gain bonus spells.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M/DF (feathers or droppings from an owl)"
            },
            {
                "name": "Resist Energy",
                "description": "This abjuration grants a creature limited protection from damage of whichever one of five energy types you select: acid, cold, electricity, fire, or sonic. The subject gains energy resistance 10 against the energy type chosen, meaning that each time the creature is subjected to such damage, that damage is reduced by 10 points before being applied to the creature's hit points.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Restoration, Lesser",
                "description": "Lesser restoration dispels any magical effects reducing one of the subject's ability scores or cures 1d4 points of temporary ability damage to one of the subject's ability scores. It also eliminates any fatigue suffered by the character, and improves an exhausted condition to fatigued.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "3 rounds",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Defensive Shock",
                "description": "You surround yourself with an electrical field. Any creature that makes a successful melee attack against you takes 1d6 points of electricity damage. This damage increases by 1d6 for every four caster levels you possess (maximum 5d6).",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Daze Monster",
                "description": "This spell functions like daze, but it can affect any one living creature of any type. Creatures of 7 or more HD are not affected.",
                "level": 2,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round",
                "components": "V, S, M (a pinch of wool or similar substance)"
            },
            {
                "name": "Elemental Touch",
                "description": "Your hands become charged with elemental energy (acid, cold, electricity, or fire, chosen when you cast the spell). A successful melee touch attack deals 1d6 points of damage of the chosen energy type per two caster levels (maximum 5d6).",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level (D)",
                "components": "V, S, M (element sample)"
            },
            {
                "name": "Fire Breath",
                "description": "Your breath becomes a cone of flame. The cone deals 1d8 points of fire damage per two caster levels (maximum 5d8). A successful Reflex save halves this damage.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "15 ft. cone",
                "duration": "1 round/level or until discharged; see text",
                "components": "V, S, M (a red dragon's scale)"
            },
            {
                "name": "Fox's Cunning",
                "description": "The target becomes smarter. The spell grants a +4 enhancement bonus to Intelligence, adding the usual benefits to Intelligence-based skill checks and other uses of the Intelligence modifier.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, M/DF (a few hairs, or a pinch of dung, from a fox)"
            },
            {
                "name": "Glide",
                "description": "You take no damage from falls (as if from feather fall) and can move up to 5 feet in any horizontal direction for every 1 foot you fall, at a speed of 60 feet per round.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level (D)",
                "components": "V, S, M (a leaf)"
            },
            {
                "name": "Iron Wind",
                "description": "You transform a collection of metal objects into a swirling mass of aerial projectiles. These projectiles automatically strike all targets within range, dealing 1d6 points of damage per two caster levels (maximum 5d6).",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, M (iron filings)"
            },
            {
                "name": "Locate Object",
                "description": "You sense the direction of a well-known or clearly visualized object. You can search for general items, in which case you locate the nearest of its kind if more than one is within range.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 min./level",
                "components": "V, S, F/DF (a forked twig)"
            },
            {
                "name": "Magic Mouth",
                "description": "This spell creates a mouth that appears on an object and speaks once when a specified event occurs. The message, which must be twenty-five or fewer words long, can be in any language known by you.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Permanent until discharged",
                "components": "V, S, M (a small bit of honeycomb and jade dust worth 10 gp)"
            },
            {
                "name": "Phantom Trap",
                "description": "This spell makes a lock or other small mechanism seem to be trapped to anyone who can detect traps. You place the spell upon any small mechanism or device, such as a lock, hinge, hasp, cork, cap, or ratchet.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent (D)",
                "components": "V, S, M (special dust worth 50 gp)"
            },
            {
                "name": "Pox Pustules",
                "description": "The target's skin breaks out in painful, itchy pustules that burst if the creature moves too much. The target takes a -2 penalty to Dexterity and a -2 penalty on attack rolls. Every time it moves, it takes 1 point of damage.",
                "level": 2,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 minute/level",
                "components": "V, S"
            },
            {
                "name": "Scarecrow",
                "description": "You create a supernatural scarecrow made of animated straw that radiates fear. Creatures must succeed at a Will save or become shaken while within 60 feet of the scarecrow.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level",
                "components": "V, S, M (a handful of straw)"
            },
            {
                "name": "Stone Call",
                "description": "A rain of dirt and stone falls in a cylindrical area, dealing 2d6 points of bludgeoning damage to creatures in the area and reducing speed by half. The ground in the area becomes difficult terrain.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Whispering Wind",
                "description": "You send a message or sound on the wind to a designated spot. The whispering wind travels to a specific location within range that is familiar to you, provided that it can find a way to the location.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "1 mile/level",
                "duration": "No more than 1 hour/level or until discharged (destination is reached)",
                "components": "V, S"
            },
            {
                "name": "Bull's Strength",
                "description": "The subject becomes stronger. The spell grants a +4 enhancement bonus to Strength, adding the usual benefits to melee attack rolls, melee damage rolls, and other uses of the Strength modifier.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M (a few hairs, or a pinch of dung, from a bull)"
            },
            {
                "name": "Darkness",
                "description": "This spell causes an object to radiate darkness out to a 20-foot radius. This darkness causes the illumination level in the area to drop one step, from bright light to normal light, from normal light to dim light, or from dim light to darkness.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, M/DF (bat fur and a piece of coal)"
            },
            {
                "name": "Darkvision",
                "description": "The subject gains the ability to see 60 feet even in total darkness. Darkvision is black and white only but otherwise like normal sight.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, M (either a pinch of dried carrot or an agate)"
            },
            {
                "name": "Detect Thoughts",
                "description": "You detect surface thoughts. The amount of information revealed depends on how long you study a particular area or subject.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Concentration, up to 1 min./level (D)",
                "components": "V, S, F/DF (a copper piece)"
            },
            {
                "name": "Flaming Sphere",
                "description": "A burning globe of fire rolls in whichever direction you point and burns those it strikes. It moves 30 feet per round. As part of this movement, it can ascend or jump up to 30 feet to strike a target.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M/DF (tallow, brimstone, and powdered iron)"
            },
            {
                "name": "Glitterdust",
                "description": "A cloud of golden particles covers everyone and everything in the area, causing creatures to become blinded and visibly outlining invisible things for the duration of the spell.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M (ground mica)"
            },
            {
                "name": "Invisibility",
                "description": "The creature or object touched becomes invisible. If the recipient is a creature carrying gear, that vanishes, too. If you cast the spell on someone else, neither you nor your allies can see the subject, unless you can normally see invisible things or you employ magic to do so.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, S, M/DF (an eyelash encased in gum arabic)"
            },
            {
                "name": "Knock",
                "description": "The knock spell opens stuck, barred, locked, held, or arcane locked doors. It opens secret doors, as well as locked or trick-opening boxes or chests. It also loosens welds, shackles, or chains.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Levitate",
                "description": "Levitate allows you to move yourself, another creature, or an object up and down as you wish. A creature must be willing to be levitated, and an object must be unattended or possessed by a willing creature.",
                "level": 2,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal or close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level (D)",
                "components": "V, S, F (either a small leather loop or a piece of golden wire bent into a cup shape)"
            },
            {
                "name": "Mirror Image",
                "description": "This spell creates a number of illusory doubles of you that inhabit your square. These duplicates make it difficult for enemies to precisely locate and attack you.",
                "level": 2,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Resist Energy",
                "description": "This abjuration grants a creature limited protection from damage of whichever one of five energy types you select: acid, cold, electricity, fire, or sonic.",
                "level": 2,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Scorching Ray",
                "description": "You blast your enemies with fiery rays. You may fire one ray, plus one additional ray for every four levels beyond 3rd (to a maximum of three rays at 11th level). Each ray requires a ranged touch attack to hit and deals 4d6 points of fire damage.",
                "level": 2,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "See Invisibility",
                "description": "You can see any objects or beings that are invisible within your range of vision, as well as any that are ethereal, as if they were normally visible.",
                "level": 2,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level (D)",
                "components": "V, S, M (talc and powdered silver)"
            },
            {
                "name": "Web",
                "description": "Web creates a many-layered mass of strong, sticky strands. These strands trap those caught in them. The strands are similar to spider webs but far larger and tougher.",
                "level": 2,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "10 min./level (D)",
                "components": "V, S, M (spider web)"
            },
            {
                "name": "Animate Dead",
                "description": "This spell turns corpses into undead skeletons or zombies that obey your spoken commands.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)"
            },
            {
                "name": "Blink",
                "description": "You \"blink\" quickly back and forth between the Material Plane and the Ethereal Plane and look as though you're winking in and out of reality at random.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Clairaudience/Clairvoyance",
                "description": "You can hear or see (your choice) some other place for a limited duration as if you were there.",
                "level": 3,
                "school": "Divination",
                "casting_time": "10 minutes",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 min./level (D)",
                "components": "V, S, F/DF (a small horn or a glass eye)"
            },
            {
                "name": "Arcane Sight",
                "description": "This spell makes your eyes glow blue and allows you to see magical auras within 120 feet of you. The effect is similar to that of a detect magic spell, but arcane sight does not require concentration and discerns aura location and power more quickly. You know the location and power of all magical auras within your sight.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Arc of Lightning",
                "description": "You create a bolt of lightning that arcs between two creatures you designate, dealing 1d6 points of electricity damage per caster level (maximum 10d6) to both targets and any creatures in a line between them. The lightning can originate from you or at any point you designate within range.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, M (a bit of fur and amber, crystal, or glass rod)"
            },
            {
                "name": "Beast Shape I",
                "description": "You transform into a Small or Medium animal and gain the following abilities: a +2 size bonus to one physical ability score and a +2 natural armor bonus. If the form you assume has any of the following abilities, you gain them: climb 30 feet, fly 30 feet (average maneuverability), swim 30 feet, darkvision 60 feet, low-light vision, and scent.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S, M (a piece of the animal)"
            },
            {
                "name": "Blood Biography",
                "description": "You learn the answers to questions about a creature whose blood you have contacted. You can learn the answers to one question per two caster levels about the creature's death or injuries, including the total damage taken, the precise type of weapon used, and the attacker's approximate height, weight, and handedness.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a scrap of parchment)"
            },
            {
                "name": "Burrow",
                "description": "The target gains a burrow speed of 15 feet. A creature with a burrow speed can tunnel through dirt, but not through rock unless the rock is worked stone, in which case it can burrow through the stone at half its normal burrow speed. The creature cannot charge or run while burrowing.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 minute/level",
                "components": "V, S, M (a piece of root from a tree)"
            },
            {
                "name": "Continual Flame",
                "description": "A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A continual flame can be covered and hidden but not smothered or quenched.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S, M (ruby dust worth 50 gp)"
            },
            {
                "name": "Deeper Darkness",
                "description": "This spell functions like darkness, but the object radiates darkness in a 60-foot radius and the darkness is deeper. Bright light in the area is reduced to dim light and normal light becomes darkness. Areas of dim light and darkness become supernaturally dark. This functions like darkness, but even creatures with darkvision cannot see within it.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level (D)",
                "components": "V, M (bat fur and a piece of coal)"
            },
            {
                "name": "Force Hook Charge",
                "description": "You create a hook of pure force that pulls you to a designated point within range. As part of casting this spell, you can move up to double your base speed in a straight line to a space adjacent to that point. This movement does not provoke attacks of opportunity. If you end this movement adjacent to an enemy, you can make a single melee attack against that creature with a +2 bonus on the attack roll.",
                "level": 3,
                "school": "Force",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Force Punch",
                "description": "You create a blast of focused force that strikes a single target, dealing 1d4 points of force damage per caster level (maximum 10d4). The force punch can also bull rush the target, using your caster level as the CMB for the bull rush attempt. This bull rush does not provoke attacks of opportunity.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Grove of Respite",
                "description": "You create a grove of trees that provides shelter and concealment. The grove is a 20-foot-radius spread that provides three-quarters cover. The grove has a comfortable temperature and can shelter up to eight Medium creatures. Creatures resting in the grove heal at twice the normal rate for natural healing.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 minute",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (a leaf and a drop of water)"
            },
            {
                "name": "Helping Hand",
                "description": "You create a ghostly hand that can be sent to find a creature within range. The hand then beckons to that creature and leads it back to you if the creature is willing to follow. The hand cannot engage in combat or cause damage. It has a speed of 50 feet.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "5 miles",
                "duration": "1 hour/level",
                "components": "V, S, DF"
            },
            {
                "name": "Nature's Exile",
                "description": "The target becomes an anathema to the natural world. Animals' starting attitude toward the target becomes hostile, and they gain a +2 bonus on attack and damage rolls against them. The target takes a –10 penalty on Survival checks, and natural hazards (such as thorns, difficult terrain, and extreme weather) affect the target as if they were one step more severe.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Pain Strike",
                "description": "You inflict wracking pains upon a creature, causing them to take a –4 penalty on attack rolls, skill checks, and ability checks. A successful Fortitude save reduces the duration to 1 round and negates the penalty. This spell causes no damage, but the target suffers excruciating pain for the duration.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Rage",
                "description": "Each affected creature gains a +2 morale bonus to Strength and Constitution, a +1 morale bonus on Will saves, and a –2 penalty to AC. The effect is otherwise identical with a barbarian's rage except that the subjects aren't fatigued at the end of the rage.",
                "level": 3,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Concentration + 1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Screech",
                "description": "You emit a piercing shriek that overwhelms creatures with sound. Each creature within the area must succeed on a Fortitude save or be stunned for 1 round and deafened for 1d4 rounds. Creatures that succeed on their save are instead deafened for 1 round. Creatures that are already deafened are not stunned but are still affected by the spell.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Seek Thoughts",
                "description": "You pick up the surface thoughts of creatures in the area. You can focus on one creature in range as a move action to learn the creature's surface thoughts. Creatures can resist with a Will save. The thoughts you detect must be in a language you speak, or else they are incomprehensible.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "1 min./level",
                "components": "V, S, M (a copper piece)"
            },
            {
                "name": "Shrink Item",
                "description": "You can shrink one nonmagical item (if it is within the size limit) to 1/16 of its normal size in each dimension (to about 1/4,096 of its normal volume). This change effectively reduces the object's size by four categories. Optionally, you can also change its now shrunken composition to a clothlike one.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 day/level; see text",
                "components": "V, S"
            },
            {
                "name": "Speak with Dead",
                "description": "You grant the semblance of life to a corpse, allowing it to answer questions. The corpse can answer only questions it could have answered in life. The corpse knows only what it knew in life, and cannot speculate about future events. If the dead creature's alignment was different from yours, the corpse gets a Will save to resist.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "10 minutes",
                "range": "10 ft.",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Speak with Plants",
                "description": "You can communicate with normal plants and plant creatures, and can ask questions of and receive answers from them. A normal plant's sense of its surroundings is limited, so it won't be able to give (or recognize) detailed descriptions of creatures or answer questions about events outside its immediate vicinity.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Tiny Hut",
                "description": "You create an unmoving, opaque sphere of force around you. Half the sphere projects above the ground, and the lower hemisphere passes through the ground. The sphere can be transparent on one side if you desire. Up to nine other Medium creatures can fit inside with you; they can freely pass into and out of the hut without harming it.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "20 ft.",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (a small crystal bead)"
            },
            {
                "name": "Water Walk",
                "description": "The transmuted creatures can tread on any liquid as if it were firm ground. Mud, oil, snow, quicksand, running water, ice, and even lava can be traversed easily, since the subjects' feet hover an inch or two above the surface. Creatures crossing molten lava still take damage from the heat.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Wind Wall",
                "description": "An invisible vertical curtain of wind appears. The wall is 2 feet thick and of considerable strength. It is a roaring blast sufficient to blow away any bird smaller than an eagle, or tear papers and similar materials from unsuspecting hands. Arrows and bolts are deflected upward and miss, while gases and most gaseous breath weapons cannot pass through.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M/DF (a tiny fan and an exotic feather)"
            },
            {
                "name": "Daylight",
                "description": "You touch an object and cause it to shed bright light in a 60-foot radius (and dim light for an additional 60 feet) like a lantern. The effect is immobile, but it can be cast on a movable object. Light taken into an area of magical darkness does not function.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Meld into Stone",
                "description": "You meld your body and possessions into a single block of stone. The stone must be large enough to accommodate your body in all three dimensions. When the casting is complete, you and not more than 100 pounds of nonliving gear merge with the stone. You remain aware of the passage of time and can cast spells on yourself while hiding in the stone.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Animate Dead, Lesser",
                "description": "This spell functions like animate dead, but you can only create one small or medium skeleton or zombie. The undead creature can't have more Hit Dice than your caster level. The created undead is not under your control, but it does not try to harm you.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (an onyx gem worth at least 50 gp)"
            },
            {
                "name": "Enter Image",
                "description": "You can enter any single image within range that you created using a spell of equal or lower level. While inside an image, you can see and hear through the image as if you were standing where it is. Each round, you can switch between any two images within range as a move action.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "50 ft./level",
                "duration": "Concentration",
                "components": "V, S, M (a drop of paint and a ball of clay)"
            },
            {
                "name": "Hydraulic Torrent",
                "description": "You create a powerful stream of water that you can direct at a target. Make a combat maneuver check with a bonus equal to your caster level plus your spellcasting ability modifier to attempt to knock your target prone. If successful, the target takes 2d6 points of nonlethal damage.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "60 ft. line",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Keen Edge",
                "description": "This spell makes a weapon magically keen, improving its ability to deal telling blows. This transmutation doubles the threat range of the weapon. A threat range of 20 becomes 19–20, a threat range of 19–20 becomes 17–20, and a threat range of 18–20 becomes 15–20.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "10 min./level",
                "components": "V, S"
            },
            {
                "name": "Magic Circle against Chaos",
                "description": "All creatures within the area gain the effects of a protection from chaos spell, and evil summoned creatures cannot enter the area either. You must overcome a creature's spell resistance to affect it at all, and the spell does not prevent the affected creature from taking actions against those within the circle.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M/DF (powdered silver worth 100 gp)"
            },
            {
                "name": "Magic Circle against Evil",
                "description": "All creatures within the area gain the effects of a protection from evil spell, and evil summoned creatures cannot enter the area either. You must overcome a creature's spell resistance to affect it at all, and the spell does not prevent the affected creature from taking actions against those within the circle.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M/DF (powdered silver worth 100 gp)"
            },
            {
                "name": "Magic Circle against Good",
                "description": "All creatures within the area gain the effects of a protection from good spell, and good summoned creatures cannot enter the area either. You must overcome a creature's spell resistance to affect it at all, and the spell does not prevent the affected creature from taking actions against those within the circle.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M/DF (powdered silver worth 100 gp)"
            },
            {
                "name": "Magic Circle against Law",
                "description": "All creatures within the area gain the effects of a protection from law spell, and lawful summoned creatures cannot enter the area either. You must overcome a creature's spell resistance to affect it at all, and the spell does not prevent the affected creature from taking actions against those within the circle.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M/DF (powdered silver worth 100 gp)"
            },
            {
                "name": "Nondetection",
                "description": "The warded creature or object becomes difficult to detect by divination spells such as clairaudience/clairvoyance, locate object, and detect spells. Nondetection also prevents location by such magic items as crystal balls. If a divination is attempted against the warded creature or item, the caster of the divination must succeed on a caster level check (1d20 + caster level) against a DC of 11 + the caster level of the spellcaster who cast nondetection.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, M (diamond dust worth 50 gp)"
            },
            {
                "name": "Secret Page",
                "description": "Secret page alters the contents of a page so that it appears to be something entirely different. The text of a spell can be changed to show recipes, maps, or any other written content. A comprehend languages spell alone cannot reveal the original contents. A true seeing spell reveals the presence of the hidden material but does not reveal the contents.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S, M (powdered herring scales and will-o'-wisp essence)"
            },
            {
                "name": "Sepia Snake Sigil",
                "description": "When triggered, the symbol turns into a brown serpent that strikes at the nearest creature, attempting a touch attack using your base attack bonus plus your Intelligence modifier. If successful, the target is encased in a shimmering amber field that holds them immobile and unconscious. Physical attacks cannot harm the victim, but dispel magic ends the effect.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent or until discharged; until released or 1d4 days + one day/level",
                "components": "V, S, M (powdered amber worth 500 gp and a snake scale)"
            },
            {
                "name": "Share Senses",
                "description": "You can share the senses of your familiar, allowing you to see, hear, smell, taste, and feel everything your familiar experiences. You can switch between using your own senses and those of your familiar as a standard action. You may maintain your own senses while accessing those of your familiar by making a DC 15 Concentration check.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 minute/level",
                "components": "V, S"
            },
            {
                "name": "Bestow Curse",
                "description": "You place a curse on the subject. Choose one of the following: -6 decrease to an ability score (minimum 1), -4 penalty on attack rolls, saves, ability checks, and skill checks, or 50% chance each round to act normally; otherwise, take no action. The curse cannot be dispelled, but it can be removed with break enchantment, limited wish, miracle, remove curse, or wish.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent",
                "components": "V, S"
            },
            {
                "name": "Channel Vigor",
                "description": "You channel vigor into one of your physical ability scores. Choose one of the following: +4 enhancement bonus to Strength for making melee attacks, +4 enhancement bonus to Dexterity for making ranged attacks and Reflex saves, or +4 enhancement bonus to Constitution for additional hit points and Fortitude saves.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Fly, Mass",
                "description": "This spell functions like fly, except it affects multiple creatures. Each target gains a fly speed of 60 feet with good maneuverability. The subjects can ascend at half speed and descend at double speed. When the spell ends, each target floats downward as per feather fall.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "10 min./level",
                "components": "V, S"
            },
            {
                "name": "Gentle Repose",
                "description": "This spell preserves the remains of a dead creature so that they do not decay, effectively extending the time limit on raising that creature from the dead. Days spent under the influence of this spell don't count against the time limit for spells like raise dead. The spell also works on severed body parts.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 day/level",
                "components": "V, S, M/DF (salt and a copper piece placed on each of the corpse's eyes)"
            },
            {
                "name": "Inflict Serious Wounds",
                "description": "When laying your hand upon a creature, you channel negative energy that deals 3d8 points of damage + 1 point per caster level (maximum +15). If used against an undead creature, it instead heals that amount of damage.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Magic Vestment",
                "description": "You imbue a suit of armor or a shield with an enhancement bonus of +1 per four caster levels (maximum +5 at 20th level). An outfit of regular clothing counts as armor that grants no AC bonus for the purpose of this spell.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, DF"
            },
            {
                "name": "Phantom Steed",
                "description": "You conjure a Large, quasi-real, horselike creature. The steed can be ridden only by you or by the one person for whom you specifically created the mount. A phantom steed has a black head and body, gray mane and tail, and smoke-colored, insubstantial hooves that make no sound. It has an AC of 18 and 7 hit points + 1 hit point per caster level.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "0 ft.",
                "duration": "1 hour/level (D)",
                "components": "V, S"
            },
            {
                "name": "Ray of Exhaustion",
                "description": "A black ray projects from your pointing finger. You must succeed on a ranged touch attack with the ray to strike a target. The subject is immediately exhausted for the spell's duration. A successful Fortitude save means the creature is only fatigued.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level",
                "components": "V, S, M (a drop of sweat)"
            },
            {
                "name": "Stone Shape",
                "description": "You can form an existing piece of stone into any shape that suits your purpose. While it's possible to make crude coffers, doors, and so forth with stone shape, fine detail isn't possible. There is a 30% chance that any shape including moving parts simply doesn't work.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (soft clay)"
            },
            {
                "name": "Tongues",
                "description": "The subject can speak and understand the language of any intelligent creature, whether it is a racial tongue or a regional dialect. The subject can speak only one language at a time, although they may be able to understand several languages. This spell doesn't enable the subject to speak with creatures who don't speak.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, M/DF (a small clay model of a ziggurat)"
            },
            {
                "name": "Vampiric Touch",
                "description": "You must succeed on a melee touch attack. Your touch deals 1d6 points of damage per two caster levels (maximum 10d6). You gain temporary hit points equal to the damage you deal. However, you can't gain more temporary hit points than the subject's current hit points +10.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous/1 hour; see text",
                "components": "V, S"
            },
            {
                "name": "Clairaudience/Clairvoyance",
                "description": "You create an invisible magical sensor at a specific location that enables you to hear or see (your choice) almost as if you were there. You can hear or see through the sensor as if you were using your own senses. The sensor can rotate allowing a 360-degree field of view. Lead sheeting or magical protection blocks the spell.",
                "level": 3,
                "school": "Divination",
                "casting_time": "10 minutes",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 min./level (D)",
                "components": "V, S, F/DF (a small horn or glass eye)"
            },
            {
                "name": "Contagion",
                "description": "The subject contracts a disease selected from the table below, which strikes immediately (no incubation period). The DC noted is for the subsequent saves to prevent further damage. Choose from: blinding sickness, bubonic plague, cackle fever, filth fever, leprosy, mindfire, red ache, shakes, or slimy doom.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Glyph of Warding",
                "description": "This powerful inscription harms those who enter, pass, or open the warded area or object. A glyph of warding can guard a bridge or passage, ward a portal, trap a chest or box, and so on. When triggered, the glyph deals damage according to the version chosen at casting.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent until discharged (D)",
                "components": "V, S, M (powdered diamond worth 200 gp)"
            },
            {
                "name": "Invisibility Purge",
                "description": "You surround yourself with a sphere of power with a radius of 5 feet per caster level that negates all forms of invisibility. Anything invisible becomes visible while in the area. This spell does not affect normal or magical darkness, or other forms of concealment.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Remove Curse",
                "description": "Remove curse instantaneously removes all curses on an object or a creature. Remove curse does not remove the curse from a cursed shield, weapon, or suit of armor, although a successful caster level check enables the creature afflicted with any such cursed item to remove and get rid of it.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Suggestion",
                "description": "You influence the actions of the target creature by suggesting a course of activity (limited to a sentence or two). The suggestion must be worded in such a manner as to make the activity sound reasonable. Tasks that would obviously result in the target's death are ineffective.",
                "level": 3,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level or until completed",
                "components": "V, M (a snake's tongue and either a bit of honeycomb or a drop of sweet oil)"
            },
            {
                "name": "Elemental Aura",
                "description": "You create an aura of energy around yourself that damages nearby opponents. Choose acid, cold, electricity, or fire. Creatures adjacent to you when this spell is cast and at the start of your turn take 2d6 points of energy damage of the chosen type. You are immune to the effects of your own elemental aura.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Explosive Runes",
                "description": "You trace mystic runes upon a book, scroll, map, or similar object. When read, the runes detonate in a 10-foot-radius burst, dealing 6d6 points of force damage. Anyone in the area can attempt a Reflex save for half damage. The object on which the runes were written is destroyed.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Permanent until discharged (D)",
                "components": "V, S"
            },
            {
                "name": "Flame Arrow",
                "description": "You touch up to fifty projectiles, which take on fiery energy. Each piece of ammunition deals an extra 1d6 points of fire damage to any target it hits. The flame on a particular piece of ammunition lasts until it is used or the duration ends, whichever comes first.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M (a drop of oil and a small piece of flint)"
            },
            {
                "name": "Greater Magic Weapon",
                "description": "This spell functions like magic weapon, except that it gives a weapon an enhancement bonus on attack and damage rolls of +1 per four caster levels (maximum +5). This bonus does not allow a weapon to bypass damage reduction aside from magic.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 hour/level",
                "components": "V, S, M (powdered lime and carbon)"
            },
            {
                "name": "Halt Undead",
                "description": "This spell renders as many as three undead creatures immobile. A nonintelligent undead creature gets no saving throw; an intelligent undead creature does. If the spell is successful, it renders the undead creature immobile for the duration of the spell.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M (a pinch of sulfur and powdered garlic)"
            },
            {
                "name": "Heal Mount",
                "description": "This spell functions like heal, but it affects only the paladin's special mount. This powerful spell channels positive energy into your mount to wipe away injury and afflictions. It cures all hit point damage, and removes blindness, disease, and negative levels.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Locate Object",
                "description": "You sense the direction of a well-known or clearly visualized object. You can search for general items, in which case you locate the nearest one of its kind if more than one is within range. Attempting to find a certain item requires a specific and accurate mental image.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 min./level",
                "components": "V, S, F/DF (a forked twig)"
            },
            {
                "name": "Protection from Energy",
                "description": "Protection from energy grants temporary immunity to the type of energy you specify when you cast it (acid, cold, electricity, fire, or sonic). When the spell absorbs 12 points per caster level of energy damage (to a maximum of 120 points at 10th level), it is discharged.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level or until discharged",
                "components": "V, S, DF"
            },
            {
                "name": "Sacred Bond",
                "description": "You create a sacred bond between yourself and another creature. When the bonded creature is at or below 0 hit points, you can cast cure spells on yourself to heal the bonded creature instead, using your effective caster level. You must be within 30 feet of the bonded creature for this effect to work.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, F (a pair of golden bracelets worth 100 gp each)"
            },
            {
                "name": "Speak with Animals",
                "description": "You can comprehend and communicate with animals. You are able to ask questions of and receive answers from animals, although the spell doesn't make them any more friendly or cooperative than normal. Furthermore, wary and cunning animals are likely to be terse and evasive.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Venomous Bolt",
                "description": "You fire a bolt of venom at your target. Make a ranged touch attack. If you hit, the target takes 1d3 points of Dexterity damage and must make a Fortitude save or take an additional 1d3 points of Dexterity damage one minute later. If either damage roll is a natural 1, that damage is instead 1 point.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous and 1 minute; see text",
                "components": "V, S, M (a fang from a venomous creature)"
            },
            {
                "name": "Water Breathing",
                "description": "The transmuted creatures can breathe water freely. Divide the duration evenly among all the creatures you touch. The spell does not make creatures unable to breathe air, and creatures under the effect of this spell can swim freely through water.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "2 hours/level; see text",
                "components": "V, S, M/DF (short reed or piece of straw)"
            },
            {
                "name": "Obscure Object",
                "description": "This spell hides an object from location by divination (scrying) effects, such as the locate object spell. It also renders the object difficult to detect by divination spells such as detect magic. If cast on a magic item, obscure object also prevents other spells from locating the item.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "8 hours (D)",
                "components": "V, S, M/DF (chameleon skin)"
            },
            {
                "name": "Prayer",
                "description": "You bring special favor upon yourself and your allies while bringing disfavor to your enemies. You and each of your allies gain a +1 luck bonus on attack rolls, weapon damage rolls, saves, and skill checks, while each of your foes takes a -1 penalty on such rolls.",
                "level": 3,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "40 ft.",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Remove Disease",
                "description": "Remove disease cures all diseases that the subject is suffering from. The spell also kills parasites, including green slime and others. Certain special diseases may not be countered by this spell or may be countered only by a caster of a certain level or higher.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Remove Blindness/Deafness",
                "description": "This spell cures blindness or deafness (your choice), whether the effect is normal or magical in nature. The spell does not restore ears or eyes that have been lost, but it repairs them if they are damaged.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Searing Light",
                "description": "Focusing divine power like a ray of the sun, you project a blast of light from your open palm. You must succeed on a ranged touch attack to strike your target. A creature struck by this ray of light takes 1d8 points of damage per two caster levels (maximum 5d8). Undead creatures take 1d6 points of damage per caster level (maximum 10d6).",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Sleet Storm",
                "description": "Driving sleet blocks all sight (even darkvision) within it and causes the ground in the area to be icy. A creature can walk within or through the area of sleet at half normal speed with a DC 10 Acrobatics check. Failure means it can't move in that round, while failure by 5 or more means it falls.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M/DF (dust and water)"
            },
            {
                "name": "Spike Growth",
                "description": "Any ground-covering vegetation in the spell's area becomes very hard and sharply pointed without changing its appearance. Creatures moving through the area take 1d4 points of piercing damage for each 5 feet traveled. The area must have some sort of undergrowth for this spell to take effect.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 hour/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Arc of Lightning",
                "description": "You create an arc of lightning that jumps between two creatures or objects. The arc deals 1d6 points of electricity damage per caster level (maximum 10d6) to all creatures in its path. Any creature struck can attempt a Reflex save for half damage.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "120 ft.",
                "duration": "Instantaneous",
                "components": "V, S, M (a small piece of fur and an amber, crystal, or glass rod)"
            },
            {
                "name": "Blood Biography",
                "description": "You learn the answers to questions about a creature whose blood you have contacted. You can cast this spell upon the blood of the dead or living. You learn the answers to the following four questions: Who are you? (name, race, and occupation/role), How was the blood shed? (cause of wound/death), When was the blood shed? (date and time), and Where was the blood shed?",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a scrap of parchment)"
            },
            {
                "name": "Force Hook Charge",
                "description": "You create a hook of force that pulls you to a designated point, allowing you to make a charge attack against a foe at the end of your movement. You can move up to double your speed in a straight line, and this movement does not provoke attacks of opportunity.",
                "level": 3,
                "school": "Force",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Force Punch",
                "description": "You create a blast of focused force that strikes a single target, dealing 1d4 points of force damage per caster level (maximum 10d4). The force punch can also bull rush the target, using your caster level as the CMB for the bull rush attempt.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Grove of Respite",
                "description": "You create a comfortable natural sanctuary in an area of natural terrain. The spell creates a 20-foot-radius grove of lush grass and mature trees, providing shade and basic shelter. The grove provides natural healing benefits, doubling natural healing rates for those who rest within it.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (a seed and a drop of water)"
            },
            {
                "name": "Helping Hand",
                "description": "You create a ghostly hand that can be sent to find a creature within range. The hand then beckons to that creature and leads it back to you if the creature is willing to follow. The hand cannot engage in combat or cause damage.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "5 miles",
                "duration": "1 hour/level",
                "components": "V, S, DF"
            },
            {
                "name": "Nature's Exile",
                "description": "The target becomes persona non grata in the eyes of nature. Animals' starting attitude toward the target is shifted two steps toward hostile, and they gain a +2 bonus on attack and damage rolls against the target. The target takes a -10 penalty on Survival checks.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Pain Strike",
                "description": "You inflict wracking pains on your target, dealing 1d6 points of nonlethal damage per round and imposing a -2 penalty on attack rolls, skill checks, and ability checks. A successful Fortitude save halves the damage and negates the penalty.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Screech",
                "description": "You emit a piercing shriek that deafens and stuns creatures in its area. Creatures within the area must make a Fortitude save or be stunned for 1 round and deafened for 1d4 rounds. On a successful save, they are instead deafened for 1 round.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Seek Thoughts",
                "description": "You detect the surface thoughts of creatures in the area. You can focus on one creature in range and read its surface thoughts, or you can read all surface thoughts that pass through the area. The amount of information revealed depends on how long you study a particular area or subject.",
                "level": 3,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "1 min./level",
                "components": "V, S, M (a copper piece)"
            },
            {
                "name": "Tiny Hut",
                "description": "You create an unmoving, opaque sphere of force around yourself that shields you and your companions from view and protects you from the elements. The sphere has a comfortable temperature and provides protection against wind, rain, snow, dust, and sandstorms.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "20 ft.",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (a small crystal bead)"
            },
            {
                "name": "Dispel Magic",
                "description": "You can use dispel magic to end one ongoing spell that has been cast on a creature or object, to temporarily suppress the magical abilities of a magic item, or to counter another spellcaster's spell.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Fireball",
                "description": "A fireball spell generates a searing explosion of flame that detonates with a low roar and deals 1d6 points of fire damage per caster level (maximum 10d6) to every creature within the area.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M (a tiny ball of bat guano and sulfur)"
            },
            {
                "name": "Fly",
                "description": "The subject can fly at a speed of 60 feet (or 40 feet if it wears medium or heavy armor, or if it carries a medium or heavy load). It can ascend at half speed and descend at double speed.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, F (a wing feather from any bird)"
            },
            {
                "name": "Gaseous Form",
                "description": "The subject and all its gear become insubstantial, misty, and translucent. Its material armor (including natural armor) becomes worthless, though its size, Dexterity, deflection bonuses, and armor bonuses from force effects still apply.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "2 min./level (D)",
                "components": "S, M/DF (a bit of gauze and a wisp of smoke)"
            },
            {
                "name": "Haste",
                "description": "The transmuted creatures move and act more quickly than normal. This extra speed has several effects.",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, M (a shaving of licorice root)"
            },
            {
                "name": "Lightning Bolt",
                "description": "You release a powerful stroke of electrical energy that deals 1d6 points of electricity damage per caster level (maximum 10d6) to each creature within its area.",
                "level": 3,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "120 ft.",
                "duration": "Instantaneous",
                "components": "V, S, M (fur and a glass rod)"
            },
            {
                "name": "Magic Circle against Evil",
                "description": "All creatures within the area gain the effects of a protection from evil spell, and evil summoned creatures cannot enter the area either.",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level",
                "components": "V, S, M/DF (a little powdered silver with which you trace a 3-foot-diameter circle on the floor around the creature to be warded)"
            },
            {
                "name": "Major Image",
                "description": "This spell functions like silent image, except that sound, smell, and thermal illusions are included in the spell effect. While concentrating, you can move the image within the range.",
                "level": 3,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Concentration + 3 rounds",
                "components": "V, S, F (a bit of fleece)"
            },
            {
                "name": "Phantom Steed",
                "description": "You conjure a Large, quasi-real, horselike creature. The steed can be ridden only by you or by the one person for whom you specifically created the mount.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "0 ft.",
                "duration": "1 hour/level (D)",
                "components": "V, S"
            },
            {
                "name": "Protection from Energy",
                "description": "Protection from energy grants temporary immunity to the type of energy you specify when you cast it (acid, cold, electricity, fire, or sonic).",
                "level": 3,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level or until discharged",
                "components": "V, S, DF"
            },
            {
                "name": "Slow",
                "description": "An affected creature moves and attacks at a drastically slowed rate. A slowed creature can take only a single move action or standard action each turn, but not both (nor may it take full-round actions).",
                "level": 3,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S, M (a drop of molasses)"
            },
            {
                "name": "Stinking Cloud",
                "description": "Stinking cloud creates a bank of fog like that created by fog cloud, except that the vapors are nauseating. Living creatures in the cloud become nauseated.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M (a rotten egg or several skunk cabbage leaves)"
            },
            {
                "name": "Summon Monster III",
                "description": "This spell functions like summon monster I, except that you can summon one creature from the 3rd-level list, 1d3 creatures of the same kind from the 2nd-level list, or 1d4+1 creatures of the same kind from the 1st-level list.",
                "level": 3,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S, F/DF (a tiny bag and a small candle)"
            },
            {
                "name": "Vampiric Touch",
                "description": "You must succeed on a melee touch attack. Your touch deals 1d6 points of damage per two caster levels (maximum 10d6). You gain temporary hit points equal to the damage you deal.",
                "level": 3,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous/1 hour; see text",
                "components": "V, S"
            },
            {
                "name": "Baleful Polymorph",
                "description": "You transform the subject into a Small or smaller animal of no more than 1 HD. If the new form would prove fatal to the creature, the subject gets a +4 bonus on the save.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Permanent",
                "components": "V, S"
            },
            {
                "name": "Black Tentacles",
                "description": "This spell causes a field of rubbery black tentacles to appear, grasping at creatures in the area. These tentacles grapple any creature in the area or that enters the area.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, M (piece of tentacle from a giant octopus or a giant squid)"
            },
            {
                "name": "Charm Monster",
                "description": "This spell functions like charm person, except that the effect is not restricted by creature type or size.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Arboreal Hammer",
                "description": "You create a Large wooden hammer that attacks creatures in the area. The hammer attacks with your base attack bonus and deals 2d6 + your Wisdom modifier in damage. It strikes as a magic weapon and can make one attack per round. The hammer gains a +1 enhancement bonus for every 4 caster levels.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Aspect of the Stag",
                "description": "You take on the aspects of a mighty stag, gaining a +2 enhancement bonus to Dexterity, a +2 dodge bonus to AC against attacks of opportunity, and an enhancement bonus to your base speed of +20 feet. You also gain low-light vision and woodland stride.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level",
                "components": "V, S, DF"
            },
            {
                "name": "Crushing Despair",
                "description": "An invisible cone of despair causes great sadness in the subjects. Each affected creature takes a –2 penalty on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls. A successful Will save reduces this duration to 1 round.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "1 min./level",
                "components": "V, S, M (a vial of tears)"
            },
            {
                "name": "Dragon's Breath",
                "description": "You breathe a powerful blast of energy of a type chosen when you cast this spell (acid, cold, electricity, or fire). The breath weapon deals 1d6 points of energy damage per caster level (maximum 12d6). A successful Reflex save halves the damage.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "30 ft. or 60 ft.",
                "duration": "Instantaneous",
                "components": "V, S, M (a dragon's scale of the appropriate color)"
            },
            {
                "name": "Fire Trap, Greater",
                "description": "This spell functions like fire trap, except that when triggered, the trap deals 1d8 points of fire damage + 1 point per caster level (maximum +20). A successful Reflex save halves the damage.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent until discharged (D)",
                "components": "V, S, M (gold dust worth 400 gp)"
            },
            {
                "name": "Firefall",
                "description": "You cause a shower of fire to rain down in the area. Any creature that starts its turn in the area takes 5d6 points of fire damage. The fire ignites flammable objects and deals 5d6 points of fire damage to objects in the area each round.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, M (a bit of phosphorus)"
            },
            {
                "name": "Fur Armor, Greater",
                "description": "This spell functions like fur armor, but provides better protection. The subject gains a +4 armor bonus to AC and a +4 circumstance bonus on Survival checks in cold weather. The armor has no armor check penalty, arcane spell failure chance, or maximum Dexterity bonus.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, M (a scrap of fur)"
            },
            {
                "name": "Ride the Waves",
                "description": "You can swim with great speed and skill. You gain a swim speed equal to your land speed, the ability to breathe water, and a +8 competence bonus on Swim checks. You can also walk on liquid surfaces as if using water walk.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 hour/level",
                "components": "V, S, M (a piece of cork)"
            },
            {
                "name": "Thorn Body",
                "description": "Your body sprouts thorns that harm those who strike you. Any creature striking you with a melee attack takes 1d6 + 1 point per caster level (maximum +15) points of piercing damage. Creatures using natural weapons or unarmed strikes take double damage.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Confusion",
                "description": "This spell causes confusion in the targets, making them unable to determine their actions. Roll on the following table at the start of each subject's turn each round to see what it does in that round.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M/DF (three nutshells)"
            },
            {
                "name": "Arboreal Hammer",
                "description": "You create a Large wooden hammer that can strike foes at a distance. The hammer strikes as a ranged attack using your base attack bonus + your Wisdom modifier. On a successful hit, it deals 2d6 + your Wisdom modifier in damage. The hammer gains a +1 enhancement bonus for every four caster levels (maximum +5).",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Aspect of the Stag",
                "description": "You take on the aspects of a mighty stag. You gain a +2 enhancement bonus to Dexterity, a +2 dodge bonus to AC against attacks of opportunity, and your base speed increases by 20 feet. You also gain low-light vision and the ability to move through any sort of undergrowth without penalty.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 minute/level",
                "components": "V, S, DF"
            },
            {
                "name": "Ball Lightning",
                "description": "You create one to four spheres of electricity that float near you. Once per round, you can move the spheres up to 30 feet and have them deal 3d6 electricity damage to all creatures within 5 feet. The spheres provide light as torches.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S, M (a few strands of fur rubbed with amber)"
            },
            {
                "name": "Control Water",
                "description": "This spell allows you to raise or lower water in a large area. You can lower water by up to 2 feet per caster level (to a minimum depth of 1 inch) in an area up to 10 square feet per caster level. You can also part water, creating a safe corridor for passage.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "10 min./level (D)",
                "components": "V, S, M/DF (a drop of water and a pinch of dust)"
            },
            {
                "name": "Crushing Despair",
                "description": "An invisible cone of despair causes great sadness in the subjects. Each affected creature takes a -2 penalty on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls. A successful Will save reduces the duration to 1 round.",
                "level": 4,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "1 min./level",
                "components": "V, S, M (a vial of tears)"
            },
            {
                "name": "Death Ward",
                "description": "The subject gains a +4 morale bonus on saves against all death spells and magical death effects. The subject is granted a save to negate such effects even if one is not normally allowed. The subject is immune to energy drain and any negative energy effects, including channeled negative energy.",
                "level": 4,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Detect Scrying",
                "description": "You immediately become aware of any attempt to observe you by means of a divination (scrying) spell or effect. The spell's area radiates from you and moves as you move. You know the location of every magical sensor within the spell's area.",
                "level": 4,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "40 ft.",
                "duration": "24 hours",
                "components": "V, S, M (a small piece of mirror and a miniature brass hearing trumpet)"
            },
            {
                "name": "Dimensional Anchor",
                "description": "A green ray springs from your hand and affects a creature or object you hit with a ranged touch attack. Any creature or object struck by the ray is covered with a shimmering emerald field that prevents extradimensional travel. Forms of movement barred include dimension door, plane shift, teleport, and similar abilities.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Divine Power",
                "description": "Calling upon the divine power of your patron, you imbue yourself with strength and skill in combat. Your base attack bonus equals your character level, you gain a +6 enhancement bonus to Strength, and you gain 1 temporary hit point per level.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level",
                "components": "V, S, DF"
            },
            {
                "name": "Dragon's Breath",
                "description": "You breathe a powerful blast of energy of a type matching that of one dragon variety (black - acid, blue - electricity, green - acid, red - fire, white - cold). The breath weapon deals 1d6 points of energy damage per caster level (maximum 12d6). A successful Reflex save halves the damage.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "30 ft. or 60 ft. cone",
                "duration": "Instantaneous",
                "components": "V, S, M (a dragon scale of the appropriate variety)"
            },
            {
                "name": "Fire Trap, Greater",
                "description": "This spell functions like fire trap, except it deals 1d8 points of fire damage + 1 point per caster level (maximum +20). A successful Reflex save halves the damage. This trap is harder to detect and disable than a regular fire trap, increasing the DCs of such attempts by 4.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent until discharged (D)",
                "components": "V, S, M (gold dust worth 400 gp)"
            },
            {
                "name": "Firefall",
                "description": "You cause a shower of fire to rain down in a cylindrical area. Creatures in the area take 5d6 points of fire damage when the spell is cast and again at the beginning of your next turn. This fire ignites flammable objects and deals 5d6 points of fire damage to objects in the area each round.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "2 rounds",
                "components": "V, S, M (a bit of phosphorus)"
            },
            {
                "name": "Freedom of Movement",
                "description": "This spell enables you or a creature you touch to move and attack normally for the duration of the spell, even under the influence of magic that usually impedes movement, such as paralysis, solid fog, slow, and web. The subject automatically succeeds on any grapple check made to resist a grapple attempt.",
                "level": 4,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Personal or touch",
                "duration": "10 min./level",
                "components": "V, S, M (a leather strip bound to the target), DF"
            },
            {
                "name": "Fur Armor, Greater",
                "description": "This spell functions like fur armor, but provides greater protection. The subject gains a +4 armor bonus to AC and a +4 circumstance bonus on Survival checks in cold weather. The armor has no armor check penalty, arcane spell failure chance, or maximum Dexterity bonus.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level",
                "components": "V, S, M (a scrap of fur)"
            },
            {
                "name": "Giant Vermin",
                "description": "You turn three normal-sized insects, arachnids, or other vermin into their giant counterparts. Only one type of vermin can be transmuted, and all must be the same kind. The HD of the giant vermin cannot exceed your caster level, to a maximum of 6 HD at 6th level.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level",
                "components": "V, S, DF"
            },
            {
                "name": "Dimension Door",
                "description": "You instantly transfer yourself from your current location to any other spot within range. You always arrive at exactly the spot desired – whether by simply visualizing the area or by stating direction.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Enervation",
                "description": "You point your finger and fire a black ray of negative energy that suppresses the life force of any living creature it strikes. You must make a ranged touch attack to hit. If you hit, the subject gains 1d4 negative levels.",
                "level": 4,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Fear",
                "description": "An invisible cone of terror causes each living creature in the area to become panicked unless it succeeds on a Will save.",
                "level": 4,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "30 ft.",
                "duration": "1 round/level or 1 round; see text",
                "components": "V, S, M (the heart of a hen or a white feather)"
            },
            {
                "name": "Greater Invisibility",
                "description": "This spell functions like invisibility, except that it doesn't end if the subject attacks.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Personal or touch",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Ice Storm",
                "description": "Great magical hailstones pound down for 1 full round, dealing 3d6 points of bludgeoning damage and 2d6 points of cold damage to every creature in the area.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "1 full round",
                "components": "V, S, M/DF (dust and water)"
            },
            {
                "name": "Phantasmal Killer",
                "description": "You create a phantasmal image of the most fearsome creature imaginable to the subject simply by forming the fears of the subject's subconscious mind into something that its conscious mind can visualize: this most horrible beast.",
                "level": 4,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Polymorph",
                "description": "This spell transforms a willing creature into an animal, humanoid or elemental of your choosing. The spell fails if the target's form is inappropriate for its new form or if the target is unwilling.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level (D)",
                "components": "V, S, M (a piece of the creature whose form you plan to assume)"
            },
            {
                "name": "Resilient Sphere",
                "description": "A globe of shimmering force encloses a creature, provided the creature is small enough to fit within the diameter of the sphere. The sphere contains its subject for the spell's duration.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 min./level (D)",
                "components": "V, S, F (a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic)"
            },
            {
                "name": "Scrying",
                "description": "You can observe a creature at any distance. If the subject succeeds on a Will save, the spell fails. The difficulty of the save depends on how well your knowledge of the subject and what sort of physical connection (if any) you have to that creature.",
                "level": 4,
                "school": "Divination",
                "casting_time": "1 hour",
                "range": "See text",
                "duration": "1 min./level",
                "components": "V, S, M/DF, F (a pool of water)"
            },
            {
                "name": "Solid Fog",
                "description": "This spell functions like fog cloud, but in addition to obscuring sight, the solid fog is so thick that it impedes movement.",
                "level": 4,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft. level)",
                "duration": "1 min./level",
                "components": "V, S, M (powdered peas and an animal hoof)"
            },
            {
                "name": "Stone Shape",
                "description": "You can form an existing piece of stone into any shape that suits your purpose. While it's possible to make crude coffers, doors, and so forth with stone shape, fine detail isn't possible.",
                "level": 4,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (soft clay)"
            },
            {
                "name": "Wall of Fire",
                "description": "An immobile, blazing curtain of shimmering violet fire springs into existence. One side of the wall, selected by you, sends forth waves of heat, dealing 2d4 points of fire damage to creatures within 10 feet and 1d4 points of fire damage to those past 10 feet but within 20 feet.",
                "level": 4,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Concentration + 1 round/level",
                "components": "V, S, M/DF (a piece of phosphorus)"
            },
            {
                "name": "Animate Objects",
                "description": "You imbue inanimate objects with mobility and a semblance of life. Each animated object then immediately attacks whomever or whatever you initially designate.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Baleful Polymorph",
                "description": "This spell functions like polymorph, except that you change the subject into a Small or smaller animal of no more than 1 HD. If the new form would prove fatal to the creature, the subject gets a +4 bonus on the save.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Permanent",
                "components": "V, S"
            },
            {
                "name": "Cloudkill",
                "description": "This spell generates a bank of fog, similar to a fog cloud, except that its vapors are yellowish green and poisonous. These vapors automatically kill any living creature with 3 or fewer HD (no save).",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Cone of Cold",
                "description": "Cone of cold creates an area of extreme cold, originating at your hand and extending outward in a cone. It causes 1d6 points of cold damage per caster level (maximum 15d6).",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Instantaneous",
                "components": "V, S, M (a small crystal or glass cone)"
            },
            {
                "name": "Dominate Person",
                "description": "You can control the actions of any humanoid creature through a telepathic link that you establish with the subject's mind.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Curse of Magic Negation",
                "description": "You curse a creature with anti-magical effects. The target gains spell resistance equal to 10 + your caster level, but this spell resistance cannot be lowered or disabled. Additionally, any spell the creature casts has a 20% chance of failure. A successful Will save negates the effect.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Life Bubble",
                "description": "You surround the target with a constant flow of clean air and protect them from environmental effects. Targets can breathe normally in any environment and are protected from poison gas, vapors, and similar atmospheric effects. They also gain protection from extreme temperatures (between -50° and 140° F).",
                "level": 5,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level",
                "components": "V, S, M/DF (a tiny glass bubble)"
            },
            {
                "name": "Plague Storm",
                "description": "You create a storm of disease, inflicting all creatures in the area with a chosen disease. The disease is contracted immediately with no onset time. A successful Fortitude save negates the effect. The DC to remove the disease is equal to this spell's save DC.",
                "level": 5,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Rampart",
                "description": "You create a 5-foot-thick earthen rampart up to 5 feet long per level. The rampart is 5 feet tall per two caster levels and provides cover to anyone behind it. The rampart must be created on solid ground, but can be dismissed as a standard action.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 round",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 hour/level (D)",
                "components": "V, S, M (a handful of earth)"
            },
            {
                "name": "Dream",
                "description": "You, or a messenger touched by you, sends a phantasmal message to others in the form of a dream. At the beginning of the spell, you must name the recipient or identify him or her by some title that leaves no doubt as to identity.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 minute",
                "range": "Unlimited",
                "duration": "See text",
                "components": "V, S"
            },
            {
                "name": "Feeblemind",
                "description": "If the target creature fails a Will saving throw, its Intelligence and Charisma scores each drop to 1. The affected creature is unable to use Intelligence- or Charisma-based skills, cast spells, understand language, or communicate coherently.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M (a handful of clay, crystal, glass, or mineral spheres)"
            },
            {
                "name": "Hold Monster",
                "description": "This spell functions like hold person, except that it affects any living creature that fails its Will save.",
                "level": 5,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)"
            },
            {
                "name": "Magic Jar",
                "description": "By casting magic jar, you place your soul in a gem or large crystal (known as the magic jar), leaving your body lifeless. Then you can attempt to take control of a nearby body, forcing its soul into the magic jar.",
                "level": 5,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 hour/level or until you return to your body",
                "components": "V, S, F (a gem or crystal worth at least 100 gp)"
            },
            {
                "name": "Passwall",
                "description": "You create a passage through wooden, plaster, or stone walls, but not through metal or other harder materials. The passage is 10 feet deep plus an additional 5 feet deep per three caster levels above 9th (15 feet at 12th, 20 feet at 15th, and a maximum of 25 feet deep at 18th level).",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, M (sesame seeds)"
            },
            {
                "name": "Persistent Image",
                "description": "This spell functions like silent image, except that the figment includes visual, auditory, olfactory, and thermal elements, and the spell is permanent.",
                "level": 5,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Permanent (D)",
                "components": "V, S, M (a bit of fleece and several grains of sand)"
            },
            {
                "name": "Telekinesis",
                "description": "You move objects or creatures by concentrating on them. Depending on the version selected, the spell can provide a gentle, sustained force, perform a variety of combat maneuvers, or exert a single short, violent thrust.",
                "level": 5,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Concentration (up to 1 round/level) or instantaneous",
                "components": "V, S"
            },
            {
                "name": "Teleport",
                "description": "This spell instantly transports you to a designated destination, which may be as distant as 100 miles per caster level. Interplanar travel is not possible.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Personal and touch",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Wall of Force",
                "description": "A wall of force creates an invisible wall of pure force. The wall cannot move and is not easily destroyed. A wall of force is immune to dispel magic, although a mage's disjunction can still dispel it.",
                "level": 5,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round /level (D)",
                "components": "V, S, M (powder made from a clear gem)"
            },
            {
                "name": "Wall of Stone",
                "description": "This spell creates a wall of rock that merges into adjoining rock surfaces. A wall of stone is 1 inch thick per four caster levels and composed of up to one 5-foot square per level.",
                "level": 5,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (a small block of granite)"
            },
            {
                "name": "Antimagic Field",
                "description": "An invisible barrier surrounds you and moves with you. The space within this barrier is impervious to most magical effects, including spells, spell-like abilities, and supernatural abilities.",
                "level": 6,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "10 min./level (D)",
                "components": "V, S, M/DF (a pinch of powdered iron or iron filings)"
            },
            {
                "name": "Fire Seeds",
                "description": "You turn acorns into explosive seeds or holly berries into bombs. Acorn grenades detonate in a 10-foot radius for 1d6 points of fire damage per caster level (maximum 15d6). Holly berry bombs can be thrown as splash weapons, dealing 1d8 points of fire damage plus additional splash damage in a 5-foot radius.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "10 min./level or until used",
                "components": "V, S, M (acorns or holly berries)"
            },
            {
                "name": "Sirocco",
                "description": "You create a blast of furnace-hot wind that deals 4d6 fire damage to all creatures in the area. Flying creatures are blown back 2d6 × 10 feet and take 2d6 nonlethal damage. A successful Fortitude save halves the fire damage and negates the nonlethal damage.",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Symphonic Nightmare",
                "description": "You create a cacophonous symphony that torments the target. The target takes 3d6 sonic damage per round and must make a Will save each round or be confused for that round. A successful save negates the confusion but not the damage.",
                "level": 6,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Chain Lightning",
                "description": "You create a stroke of lightning that arcs to a target of your choice. The bolt deals 1d6 points of electricity damage per caster level (maximum 20d6) to the primary target. After it strikes, lightning can arc to a number of secondary targets equal to your caster level (maximum 20).",
                "level": 6,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, F (a bit of fur; a piece of amber, glass, or a crystal rod; plus one silver pin for each of your caster levels)"
            },
            {
                "name": "Disintegrate",
                "description": "A thin, green ray springs from your pointing finger. You must make a successful ranged touch attack to hit. Any creature struck by the ray takes 2d6 points of damage per caster level (to a maximum of 40d6). Any creature reduced to 0 or fewer hit points by this spell is entirely disintegrated, leaving behind only a trace of fine dust.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (a lodestone and a pinch of dust)"
            },
            {
                "name": "Flesh to Stone",
                "description": "The subject, along with all its carried gear, turns into a mindless, inert statue. If the statue resulting from this spell is broken or damaged, the subject (if ever returned to its original state) has similar damage or deformities.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M (lime, water, and earth)"
            },
            {
                "name": "Globe of Invulnerability",
                "description": "An immobile, faintly shimmering magical sphere surrounds you and excludes all spell effects of 4th level or lower. The area or effect of any such spells does not include the area of the globe of invulnerability.",
                "level": 6,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "1 round/level (D)",
                "components": "V, S, M (a glass or crystal bead)"
            },
            {
                "name": "Greater Dispel Magic",
                "description": "This spell functions like dispel magic, except that it can end more than one spell on a target and it can be used to target multiple creatures.",
                "level": 6,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Heroism, Greater",
                "description": "This spell functions like heroism, but the creature gains a +4 morale bonus on attack rolls, saves, and skill checks, immunity to fear effects, and temporary hit points equal to your caster level (maximum 20).",
                "level": 6,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S"
            },
            {
                "name": "Mass Suggestion",
                "description": "This spell functions like suggestion, except that it can affect more creatures. You can suggest a course of action to multiple creatures (one suggestion per group of creatures).",
                "level": 6,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 hour/level or until completed",
                "components": "V, M (a snake's tongue and either a bit of honeycomb or a drop of sweet oil)"
            },
            {
                "name": "Move Earth",
                "description": "Move earth moves dirt (clay, loam, sand), possibly collapsing embankments, moving hillocks, shifting dunes, and so forth. However, in no event can rock formations be collapsed or moved.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "See text",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M (a mixture of soils in a small bag, and an iron blade)"
            },
            {
                "name": "Planar Binding",
                "description": "Casting this spell attempts a dangerous act: to lure a creature from another plane to a specifically prepared trap, which must lie within the spell's range. The called creature is held in the trap until it agrees to perform one service in return for its freedom.",
                "level": 6,
                "school": "Conjuration",
                "casting_time": "10 minutes",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Stone to Flesh",
                "description": "This spell restores a petrified creature to its normal state, restoring life and goods. The creature must make a DC 15 Fortitude save to survive the process.",
                "level": 6,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M (a pinch of earth and a drop of blood)"
            },
            {
                "name": "True Seeing",
                "description": "You confer on the subject the ability to see all things as they actually are. The subject sees through normal and magical darkness, notices secret doors hidden by magic, sees the exact locations of creatures or objects under blur or displacement effects, sees invisible creatures or objects normally, sees through illusions, and sees the true form of polymorphed, changed, or transmuted things.",
                "level": 6,
                "school": "Divination",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "1 min./level",
                "components": "V, S, M (an ointment for the eyes that costs 250 gp)"
            },
            {
                "name": "Veil",
                "description": "You instantly change the appearance of the subjects and then maintain that appearance for the spell's duration. You can make the subjects appear to be anything you wish.",
                "level": 6,
                "school": "Illusion",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Concentration + 1 hour/level (D)",
                "components": "V, S"
            },
            {
                "name": "Banishment",
                "description": "A banishment spell is a more powerful version of the dismissal spell. It enables you to force extraplanar creatures out of your home plane. As many as 2 Hit Dice of creatures per caster level can be banished.",
                "level": 7,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, F (see text)"
            },
            {
                "name": "Control Weather",
                "description": "You change the weather in the local area. It takes 10 minutes to cast the spell and an additional 10 minutes for the effects to manifest. You can call forth weather appropriate to the climate and season of the area you are in.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "10 minutes; see text",
                "range": "2 miles",
                "duration": "4d12 hours; see text",
                "components": "V, S"
            },
            {
                "name": "Resonating Word",
                "description": "You speak a word that resonates with destructive force through a single target. The target takes 10d6 sonic damage immediately, 1d6 Constitution damage, and is staggered for 1 round. One round later, it takes 5d6 sonic damage and is stunned for 1 round. In the final round, it takes 5d6 sonic damage and is confused for 1 round.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "3 rounds",
                "components": "V"
            },
            {
                "name": "Statue",
                "description": "You turn yourself or a willing creature to stone. The subject gains hardness 8 and can see, hear, and breathe normally, but cannot move or take any physical actions. The subject can dismiss the spell as a free action. While in statue form, the subject is immune to blindness, critical hits, ability score damage, deafness, disease, drowning, poison, stunning, and all spells that affect physiology or respiration.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 round",
                "range": "Touch",
                "duration": "1 hour/level (D)",
                "components": "V, S, M (lime, sand, and a drop of water stirred by an iron spike)"
            },
            {
                "name": "Sunbeam",
                "description": "You create dazzling beams of intense light each round. Each creature in the beam is blinded and takes 4d6 points of damage. Undead creatures take 1d6 points of damage per caster level (maximum 20d6), and instead of being blinded, they are staggered for 1d4 rounds. A successful Reflex save negates the blinding effect and reduces the damage by half.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "60 ft. line",
                "duration": "1 round/level or until all beams are exhausted",
                "components": "V, S, DF"
            },
            {
                "name": "Delayed Blast Fireball",
                "description": "This spell functions like fireball, except that it is more powerful and can detonate up to 5 rounds after the spell is cast. The burst of flame deals 1d6 points of fire damage per caster level (maximum 20d6).",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "5 rounds or less; see text",
                "components": "V, S, M (a tiny ball of bat guano and sulfur)"
            },
            {
                "name": "Ethereal Jaunt",
                "description": "You become ethereal, along with your equipment. For the duration of the spell, you are in the Ethereal Plane, which overlaps the Material Plane. When the spell expires, you return to material existence.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 round/level (D)",
                "components": "V, S"
            },
            {
                "name": "Finger of Death",
                "description": "You can slay any one living creature within range. The target is entitled to a Fortitude saving throw to survive the attack. If the save is successful, the creature instead takes 3d6 points of damage +1 point per caster level (maximum +25).",
                "level": 7,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Forcecage",
                "description": "This spell creates an immobile, invisible cubical prison composed of either bars of force or solid walls of force (your choice). Creatures within the area are caught and contained unless they are too big to fit inside, in which case the spell automatically fails.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, M (ruby dust worth 1,500 gp)"
            },
            {
                "name": "Greater Teleport",
                "description": "This spell functions like teleport, except that there is no range limit and there is no chance you arrive off target. You must have some clear idea of the location and layout of the destination.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Personal and touch",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Mage's Magnificent Mansion",
                "description": "You conjure up an extradimensional dwelling that has a single entrance on the plane from which the spell was cast. The entry point looks like a faint shimmering in the air that is 4 feet wide and 8 feet high.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, F (a miniature portal carved from ivory, a small piece of polished marble, and a tiny silver spoon, each item worth 5 gp)"
            },
            {
                "name": "Mass Hold Person",
                "description": "This spell functions like hold person, except that it affects multiple creatures and lasts longer.",
                "level": 7,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)"
            },
            {
                "name": "Phase Door",
                "description": "This spell creates an ethereal passage through wooden, plaster, or stone walls, but not other materials. The phase door is invisible and inaccessible to all creatures except you, and only you can use the passage.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "One usage per two levels",
                "components": "V"
            },
            {
                "name": "Plane Shift",
                "description": "You move yourself or some other creature to another plane of existence or alternate dimension. If several willing persons link hands in a circle, as many as eight can be affected by the plane shift at the same time.",
                "level": 7,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, F (a small, forked metal rod)"
            },
            {
                "name": "Prismatic Spray",
                "description": "This spell causes seven shimmering, intertwined, multicolored beams of light to spray from your hand. Each beam has a different power. Creatures in the area of the spell with 8 HD or less are automatically blinded for 2d4 rounds.",
                "level": 7,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "60 ft.",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Reverse Gravity",
                "description": "This spell reverses gravity in an area, causing unattached objects and creatures in the area to fall upward and reach the top of the area in 1 round. If a solid object (such as a ceiling) is encountered in this fall, falling objects and creatures strike it in the same manner as they would during a normal downward fall.",
                "level": 7,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level (D)",
                "components": "V, S, M/DF (a lodestone and iron filings)"
            },
            {
                "name": "Antipathy",
                "description": "You cause an object or location to emanate magical vibrations that repel either a specific kind of intelligent creature or creatures of a particular alignment, as defined by you.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 hour",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "2 hours/level (D)",
                "components": "V, S, M/DF (a lump of alum soaked in vinegar)"
            },
            {
                "name": "Clone",
                "description": "This spell makes an inert duplicate of a creature. If the original individual has been slain, its soul immediately transfers to the clone, creating a replacement (provided that the soul is free and willing to return).",
                "level": 8,
                "school": "Necromancy",
                "casting_time": "10 minutes",
                "range": "0 ft.",
                "duration": "Instantaneous",
                "components": "V, S, M (laboratory supplies worth 1,000 gp)"
            },
            {
                "name": "Create Greater Undead",
                "description": "This evil spell functions like create undead, except that you can create more powerful and intelligent sorts of undead: shadows, wraiths, spectres, and devourers.",
                "level": 8,
                "school": "Necromancy",
                "casting_time": "1 hour",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, M (a black sapphire worth 100 gp per HD of the undead to be created)"
            },
            {
                "name": "Dimensional Lock",
                "description": "You create a shimmering emerald barrier that completely blocks extradimensional travel. Forms of movement barred include astral projection, blink, dimension door, ethereal jaunt, etherealness, gate, maze, plane shift, shadow walk, teleport, and similar spell-like abilities.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Horrid Wilting",
                "description": "This spell evaporates moisture from the body of each subject living creature, causing flesh to wither and crack and crumble to dust. This deals 1d6 points of damage per caster level (maximum 20d6).",
                "level": 8,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S, M/DF (a bit of sponge)"
            },
            {
                "name": "Incendiary Cloud",
                "description": "An incendiary cloud spell creates a cloud of roiling smoke shot through with white-hot embers. The smoke obscures all sight as a fog cloud does. In addition, the white-hot embers within the cloud deal 6d6 points of fire damage to everything within the cloud on your turn each round.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "1 round/level",
                "components": "V, S"
            },
            {
                "name": "Iron Body",
                "description": "This spell transforms your body into living iron, which grants you several powerful resistances and abilities.",
                "level": 8,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1 min./level (D)",
                "components": "V, S, M/DF (a piece of iron from an iron golem, a hero's armor, or a war machine)"
            },
            {
                "name": "Maze",
                "description": "You banish the subject into an extradimensional labyrinth. Each round on its turn, it may attempt a DC 20 Intelligence check to escape the labyrinth as a full-round action.",
                "level": 8,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "See text",
                "components": "V, S"
            },
            {
                "name": "Mind Blank",
                "description": "The subject is protected from all devices and spells that gather information about the target through divination magic. This spell also grants a +8 resistance bonus on saving throws against all mind-affecting spells and effects.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "24 hours",
                "components": "V, S"
            },
            {
                "name": "Polar Ray",
                "description": "A blue-white ray of freezing air and ice springs from your hand. You must succeed on a ranged touch attack with the ray to deal damage to a target. The ray deals 1d6 points of cold damage per caster level (maximum 25d6).",
                "level": 8,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, F (a small, white ceramic cone or prism)"
            },
            {
                "name": "Polymorph Any Object",
                "description": "This spell functions like greater polymorph, except that it changes one object or creature into another. The duration of the spell depends on how radical a change is made from the original to the transmuted form.",
                "level": 8,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "See text",
                "components": "V, S, M/DF (mercury, gum arabic, and smoke)"
            },
            {
                "name": "Power Word Stun",
                "description": "You utter a single word of power that instantly causes one creature of your choice to become stunned, whether the creature can hear the word or not.",
                "level": 8,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "See text",
                "components": "V"
            },
            {
                "name": "Prismatic Wall",
                "description": "Prismatic wall creates a vertical, opaque wall—a shimmering, multicolored plane of light that protects you from all forms of attack. The wall flashes with seven colors, each of which has a distinct power and purpose.",
                "level": 8,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "10 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Astral Projection",
                "description": "By freeing your spirit from your physical body, this spell allows you to project an astral body onto another plane altogether.",
                "level": 9,
                "school": "Necromancy",
                "casting_time": "30 minutes",
                "range": "Touch",
                "duration": "See text",
                "components": "V, S, M (jacinth worth 1,000 gp)"
            },
            {
                "name": "Dominate Monster",
                "description": "This spell functions like dominate person, except that the spell is not restricted by creature type.",
                "level": 9,
                "school": "Enchantment",
                "casting_time": "1 round",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "1 day/level",
                "components": "V, S"
            },
            {
                "name": "Regenerate, Mass",
                "description": "This spell functions like regenerate, but affects multiple creatures. Each target regains 4d8 points of damage + 1 point per caster level (maximum +35), and all nonlethal damage. Also regenerates missing body parts and broken bones. Affects up to one creature per level, no two of which can be more than 30 feet apart.",
                "level": 9,
                "school": "Conjuration",
                "casting_time": "3 full rounds",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S, DF"
            },
            {
                "name": "World Wave",
                "description": "You create a massive wave of earth that you can ride and direct. The wave is 20 feet long per caster level and 20 feet high. Creatures caught in the wave's path take 10d6 points of damage (Reflex half) and may be knocked prone. You can ride the wave without harm and direct its movement as a move action. The wave moves at a speed of 100 feet per round.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "See text",
                "duration": "1 round/level (D)",
                "components": "V, S, DF"
            },
            {
                "name": "Energy Drain",
                "description": "This spell functions like enervation, except that the creature struck gains 2d4 negative levels, and the negative levels last longer.",
                "level": 9,
                "school": "Necromancy",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Etherealness",
                "description": "This spell functions like ethereal jaunt, except that you and other willing creatures joined by linked hands become ethereal. Besides yourself, you can bring one creature per three caster levels to the Ethereal Plane.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Touch; see text",
                "duration": "1 min./level (D)",
                "components": "V, S"
            },
            {
                "name": "Freedom",
                "description": "The subject is freed from spells and effects that restrict movement, including binding, entangle, grappling, imprisonment, maze, paralysis, petrification, pinning, sleep, slow, stunning, temporal stasis, and web.",
                "level": 9,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels) or touch",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Gate",
                "description": "Casting a gate spell has two effects. First, it creates an interdimensional connection between your plane of existence and a plane you specify, allowing travel between those two planes in either direction. Second, you may then call a particular individual or kind of being through the gate.",
                "level": 9,
                "school": "Conjuration",
                "casting_time": "1 standard action",
                "range": "Medium (100 ft. + 10 ft./level)",
                "duration": "Instantaneous or concentration (up to 1 round/level); see text",
                "components": "V, S, M (diamond worth 10,000 gp)"
            },
            {
                "name": "Imprisonment",
                "description": "When you cast imprisonment and touch a creature, it is entombed in a state of suspended animation in a small sphere far beneath the surface of the ground.",
                "level": 9,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "Touch",
                "duration": "Instantaneous",
                "components": "V, S, M (a miniature representation of the target)"
            },
            {
                "name": "Meteor Swarm",
                "description": "Meteor swarm is a very powerful and spectacular spell that is similar to fireball in many aspects. When you cast it, four 2-foot-diameter spheres spring from your outstretched hand and streak in straight lines to the spots you select.",
                "level": 9,
                "school": "Evocation",
                "casting_time": "1 standard action",
                "range": "Long (400 ft. + 40 ft./level)",
                "duration": "Instantaneous",
                "components": "V, S"
            },
            {
                "name": "Power Word Kill",
                "description": "You utter a single word of power that instantly kills one creature of your choice, whether the creature can hear the word or not.",
                "level": 9,
                "school": "Enchantment",
                "casting_time": "1 standard action",
                "range": "Close (25 ft. + 5 ft./2 levels)",
                "duration": "Instantaneous",
                "components": "V"
            },
            {
                "name": "Prismatic Sphere",
                "description": "This spell functions like prismatic wall, except you conjure up an immobile, opaque globe of shimmering, multicolored light that surrounds you and protects you from all forms of attack.",
                "level": 9,
                "school": "Abjuration",
                "casting_time": "1 standard action",
                "range": "10 ft.",
                "duration": "10 min./level (D)",
                "components": "V"
            },
            {
                "name": "Shapechange",
                "description": "This spell functions like polymorph, except that it enables you to assume the form of any single non-unique creature (of any type) from Fine to Colossal size. The assumed form cannot have more than twice your caster level in Hit Dice (to a maximum of 50 HD).",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "10 min./level (D)",
                "components": "V, S, F (jade circlet worth 1,500 gp)"
            },
            {
                "name": "Time Stop",
                "description": "This spell seems to make time cease to flow for everyone but you. In fact, you speed up so greatly that all other creatures seem frozen, though they are actually still moving at their normal speeds.",
                "level": 9,
                "school": "Transmutation",
                "casting_time": "1 standard action",
                "range": "Personal",
                "duration": "1d4+1 rounds (apparent time)",
                "components": "V"
            },
            {
                "name": "Wish",
                "description": "Wish is the mightiest spell a wizard or sorcerer can cast. By simply speaking aloud, you can alter reality to better suit you. Even wish, however, has its limits.",
                "level": 9,
                "school": "Universal",
                "casting_time": "1 standard action",
                "range": "See text",
                "duration": "See text",
                "components": "V, S, M (diamond worth 25,000 gp)"
            }
        ],
        "Call of Cthulhu": [
            {
                "name": "Acidic Spray",
                "description": "Creates a spray of corrosive acid that can damage targets.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "Variable Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Alter Weather",
                "description": "Allows the caster to influence local weather patterns.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "10+ Magic points",
                "duration": "1D6 hours"
            },
            {
                "name": "Apportion Ka",
                "description": "Transfers life force between individuals.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "Variable Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Augur",
                "description": "Grants visions of possible futures.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "5 Magic points, 1D6 Sanity points",
                "duration": "Visions last 1D6 rounds"
            },
            {
                "name": "Awareness",
                "description": "Heightens the caster's senses supernaturally.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "3 Magic points",
                "duration": "1 hour"
            },
            {
                "name": "Azure Blaze",
                "description": "Creates a bolt of blue fire that can ignite flammable objects.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "4 Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Bless Blade",
                "description": "Enhances a blade with magical properties.",
                "level": 0,
                "casting_time": "10 minutes",
                "cost": "5 Magic points",
                "duration": "24 hours"
            },
            {
                "name": "Call/Dismiss Azathoth",
                "description": "Attempts to summon or dismiss the Daemon Sultan. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Call/Dismiss Cthulhu",
                "description": "Attempts to summon or dismiss Great Cthulhu. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Call/Dismiss Hastur",
                "description": "Attempts to summon or dismiss Hastur. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Call/Dismiss Yog-Sothoth",
                "description": "Attempts to summon or dismiss Yog-Sothoth. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Cause/Cure Blindness",
                "description": "Inflicts or cures blindness on a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "8 Magic points",
                "duration": "Permanent until cured"
            },
            {
                "name": "Cloud Memory",
                "description": "Erases or alters recent memories of a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "5 Magic points, 3 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Conjure Glass of Mortlan",
                "description": "Creates a magical scrying device.",
                "level": 0,
                "casting_time": "1 day",
                "cost": "15 Magic points, 1D6 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Contact Deity",
                "description": "Establishes mental contact with a deity or Great Old One.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "1D10 Magic points, 1D10 Sanity points",
                "duration": "Brief"
            },
            {
                "name": "Contact Ghoul",
                "description": "Summons a ghoul to the caster's presence.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "7 Magic points",
                "duration": "Until dismissed"
            },
            {
                "name": "Create Barricade of Spirits",
                "description": "Forms a barrier of spectral energy.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "Variable Magic points",
                "duration": "1 hour"
            },
            {
                "name": "Create Mist of R'lyeh",
                "description": "Conjures a mist that disorients those who enter it.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "8 Magic points",
                "duration": "1D6 hours"
            },
            {
                "name": "Create Scorn of Ahriman",
                "description": "Crafts a powerful magical amulet.",
                "level": 0,
                "casting_time": "1 week",
                "cost": "20 Magic points, 1D10 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Curse of the Putrid Husk",
                "description": "Causes a target's body to rapidly decay.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "10 Magic points, 1D6 Sanity points",
                "duration": "Instantaneous"
            },
            {
                "name": "Deflect Harm",
                "description": "Creates a shield against physical and magical attacks.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "Variable Magic points",
                "duration": "1D6 rounds"
            },
            {
                "name": "Dominate",
                "description": "Allows control over a target's actions.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "1 Magic point per round, 1D6 Sanity points",
                "duration": "Concentration"
            },
            {
                "name": "Dread Curse of Azathoth",
                "description": "Inflicts a terrible curse on a target.",
                "level": 0,
                "casting_time": "1 day",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Elder Sign",
                "description": "Creates a protective symbol against cosmic entities.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "Variable Magic points (minimum 10)",
                "duration": "Permanent until destroyed"
            },
            {
                "name": "Elemental Conjuration",
                "description": "Summons an elemental being.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "15 Magic points",
                "duration": "Until dismissed"
            },
            {
                "name": "Enchant Knife",
                "description": "Imbues a blade with magical properties.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "5 Magic points, 1D4 Sanity points",
                "duration": "Until next sunrise"
            },
            {
                "name": "Enslave",
                "description": "Binds a summoned creature to the caster's will.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "Variable Magic points, 1D10 Sanity points",
                "duration": "1 year and 1 day"
            },
            {
                "name": "Evil Eye",
                "description": "Curses a target with bad luck.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "5 Magic points, 2 Sanity points",
                "duration": "1 week"
            },
            {
                "name": "Exhaust",
                "description": "Drains the energy from a target.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "6 Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Fist of Yog-Sothoth",
                "description": "Creates an invisible force to strike targets.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "Variable Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Flesh Ward",
                "description": "Toughens the caster's skin against damage.",
                "level": 0,
                "casting_time": "5 rounds",
                "cost": "3 Magic points",
                "duration": "24 hours"
            },
            {
                "name": "Gate",
                "description": "Opens a portal to another dimension or location.",
                "level": 0,
                "casting_time": "1D10 rounds",
                "cost": "40 Magic points, 1D100 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Gather Memories",
                "description": "Extracts memories from a corpse or location.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "12 Magic points, 1D6 Sanity points",
                "duration": "Instantaneous"
            },
            {
                "name": "Grasp of Cthulhu",
                "description": "Summons tentacles to grapple and crush targets.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "10 Magic points, 1D6 Sanity points",
                "duration": "1D6 rounds"
            },
            {
                "name": "Heal",
                "description": "Restores health to a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "Variable Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Implant Fear",
                "description": "Instills overwhelming fear in a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "8 Magic points, 1D4 Sanity points",
                "duration": "1D6 hours"
            },
            {
                "name": "Imprisonment",
                "description": "Traps a being in a magical prison.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "20 Magic points, 1D10 Sanity points",
                "duration": "Until released"
            },
            {
                "name": "Invoke Deity",
                "description": "Calls upon a deity for aid. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Brief"
            },
            {
                "name": "Invoke Yog-Sothoth",
                "description": "Attempts to gain knowledge from Yog-Sothoth. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Brief"
            },
            {
                "name": "Mindblast",
                "description": "Assaults a target's mind, causing confusion and pain.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "8 Magic points, 1D4 Sanity points",
                "duration": "Instantaneous"
            },
            {
                "name": "Possess",
                "description": "Allows the caster to take control of another's body.",
                "level": 0,
                "casting_time": "1D6 rounds",
                "cost": "15 Magic points, 1D10 Sanity points",
                "duration": "1 hour"
            },
            {
                "name": "Power Drain",
                "description": "Drains magical energy from a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "5 Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Primal Scream",
                "description": "Emits a psychically charged scream that can stun or harm.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "7 Magic points, 1D4 Sanity points",
                "duration": "Instantaneous"
            },
            {
                "name": "Resurrection",
                "description": "Brings a dead person back to life. Extremely dangerous.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "All Magic points, 1D100 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Return Greeting",
                "description": "Teleports the caster to a predetermined location.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "10 Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Revivify",
                "description": "Brings a recently dead person back to life.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "15 Magic points, 1D10 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Roi's Revolver",
                "description": "Expels a target from the immediate vicinity.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "20 Magic points",
                "duration": "Instantaneous"
            },
            {
                "name": "Sea Change",
                "description": "Transforms a human into a Deep One hybrid.",
                "level": 0,
                "casting_time": "1 day",
                "cost": "30 Magic points, 1D20 Sanity points",
                "duration": "Permanent"
            },
            {
                "name": "Send Dream",
                "description": "Implants a dream or message in a sleeping target's mind.",
                "level": 0,
                "casting_time": "10 minutes",
                "cost": "5 Magic points",
                "duration": "One night's sleep"
            },
            {
                "name": "Shrivelling",
                "description": "Causes a target's flesh to wither and die.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "Variable Magic points (minimum 8)",
                "duration": "Instantaneous"
            },
            {
                "name": "Summon/Bind Byakhee",
                "description": "Summons a Byakhee, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "10 Magic points, 1D6 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Summon/Bind Fire Vampire",
                "description": "Summons a Fire Vampire, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "10 Magic points, 1D6 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Summon/Bind Flying Polyp",
                "description": "Summons a Flying Polyp, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "15 Magic points, 1D10 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Summon/Bind Hunting Horror",
                "description": "Summons a Hunting Horror, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "12 Magic points, 1D8 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Summon/Bind Nightgaunt",
                "description": "Summons a Nightgaunt, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "11 Magic points, 1D6 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Summon/Bind Star Vampire",
                "description": "Summons a Star Vampire, which the caster can attempt to bind.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "14 Magic points, 1D8 Sanity points",
                "duration": "Until dismissed or slain"
            },
            {
                "name": "Time Gate",
                "description": "Opens a portal to the past or future.",
                "level": 0,
                "casting_time": "1D6 hours",
                "cost": "30 Magic points, 1D20 Sanity points",
                "duration": "Variable"
            },
            {
                "name": "Vanish",
                "description": "Makes the caster invisible.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "8 Magic points",
                "duration": "1D6 rounds"
            },
            {
                "name": "Voice of Ra",
                "description": "Allows the caster to speak with great authority and persuasiveness.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "6 Magic points",
                "duration": "1D6 rounds"
            },
            {
                "name": "Voorish Sign",
                "description": "A gesture that weakens dimensional barriers, aiding other spells.",
                "level": 0,
                "casting_time": "Instantaneous",
                "cost": "1 Magic point",
                "duration": "Instantaneous"
            },
            {
                "name": "Warding",
                "description": "Creates a barrier against supernatural entities.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "Variable Magic points",
                "duration": "1 day"
            },
            {
                "name": "Withering",
                "description": "Causes a target's limb to wither and become useless.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "8 Magic points, 1D4 Sanity points",
                "duration": "Permanent until cured"
            },
            {
                "name": "Wrack",
                "description": "Inflicts severe pain on a target.",
                "level": 0,
                "casting_time": "1 round",
                "cost": "6 Magic points, 1D4 Sanity points",
                "duration": "1D6 rounds"
            },
            {
                "name": "Zingaya",
                "description": "A voodoo-like curse that causes harm to a target through a simulacrum.",
                "level": 0,
                "casting_time": "1 hour",
                "cost": "10 Magic points, 1D6 Sanity points",
                "duration": "Until the simulacrum is destroyed"
            }
        ],
        "Shadowrun": [
            {
                "name": "Acid Stream",
                "description": "Creates a corrosive stream of acid that damages the target.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Analyze Device",
                "description": "Allows the caster to understand the purpose and operation of a device.",
                "level": 3,
                "school": "Detection",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Armor",
                "description": "Creates a field of magical protection around the target.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Clairaudience",
                "description": "Allows the caster to hear sounds from a distant location.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Clairvoyance",
                "description": "Allows the caster to see a distant location.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Combat Sense",
                "description": "Enhances the target's combat awareness and reflexes.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Confusion",
                "description": "Causes mental disorientation in the target.",
                "level": 2,
                "school": "Illusion",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Control Thoughts",
                "description": "Allows the caster to control the target's actions.",
                "level": 1,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Enemies",
                "description": "Alerts the caster to the presence of hostile individuals.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Individual",
                "description": "Allows the caster to locate a specific individual.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Life",
                "description": "Detects living beings in the spell's area of effect.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Magic",
                "description": "Reveals the presence of magic in the spell's area of effect.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Object",
                "description": "Allows the caster to locate a specific type of object.",
                "level": 3,
                "school": "Detection",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Flamethrower",
                "description": "Creates a stream of flame that damages the target.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Heal",
                "description": "Heals physical damage on the target.",
                "level": 4,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Improved Invisibility",
                "description": "Renders the target invisible to normal vision and technological sensors.",
                "level": 1,
                "school": "Illusion",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Influence",
                "description": "Allows the caster to implant a suggestion in the target's mind.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Levitate",
                "description": "Allows the caster to lift and move objects or persons without touching them.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Light",
                "description": "Creates a mobile point of light.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mana Barrier",
                "description": "Creates an invisible barrier that blocks magical effects.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Mask",
                "description": "Alters the perceived appearance of the target.",
                "level": 2,
                "school": "Illusion",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mind Probe",
                "description": "Allows the caster to read the thoughts and memories of the target.",
                "level": 1,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Phantasm",
                "description": "Creates a realistic illusion that affects all senses.",
                "level": 1,
                "school": "Illusion",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Physical Barrier",
                "description": "Creates a visible, physical wall of magical energy.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Power Bolt",
                "description": "Fires a bolt of magical energy at a target.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Silence",
                "description": "Creates an area where no sound can be produced or heard.",
                "level": 3,
                "school": "Illusion",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Stunball",
                "description": "Creates an area effect stunning attack.",
                "level": 3,
                "school": "Combat",
                "type": "Mana",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Stun Bolt",
                "description": "Fires a bolt of magical energy that stuns rather than damages.",
                "level": 3,
                "school": "Combat",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Trid Phantasm",
                "description": "Creates a realistic three-dimensional illusion.",
                "level": 1,
                "school": "Illusion",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Vehicle Mask",
                "description": "Alters the perceived appearance of a vehicle.",
                "level": 2,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Astral Armor",
                "description": "Creates a protective field around the target's aura in astral space.",
                "level": 2,
                "school": "Combat",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Ball Lightning",
                "description": "Creates a ball of electrical energy that can be directed at targets.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Control Actions",
                "description": "Allows the caster to puppeteer the target's physical movements.",
                "level": 1,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Demolish",
                "description": "Causes significant structural damage to buildings or vehicles.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Toxic Wave",
                "description": "Creates a wave of corrosive acid that damages everything in its path.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Mana Bind",
                "description": "Restrains a target with bands of magical energy, preventing movement.",
                "level": 3,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Mob Mind",
                "description": "Influences the emotions and actions of a group of people.",
                "level": 1,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Petrify",
                "description": "Turns the target into stone temporarily.",
                "level": 1,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Poltergeist",
                "description": "Allows the caster to telekinetically move multiple small objects.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Radiation Beam",
                "description": "Fires a beam of harmful radiation at the target.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Reshape",
                "description": "Allows the caster to mold and shape physical materials.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Slay",
                "description": "A powerful spell that can instantly kill a living target.",
                "level": 1,
                "school": "Combat",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Sterilize",
                "description": "Creates a sphere of purified, sterile space.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Turn to Goo",
                "description": "Transforms the target into a gelatinous state temporarily.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Wreck",
                "description": "Causes malfunctions and damage to a vehicle or mechanical device.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Alchemical Bomb",
                "description": "Creates a magical explosive that can be thrown or planted.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Special"
            },
            {
                "name": "Animate",
                "description": "Brings an inanimate object to life, allowing it to move and follow simple commands.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Astral Window",
                "description": "Creates a window into the astral plane that non-awakened individuals can see through.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Cataclysm",
                "description": "Causes widespread destruction in a large area, affecting structures and terrain.",
                "level": 1,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Clean",
                "description": "Instantly cleans an area or object, removing dirt, grime, and even some toxins.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch (Area)",
                "duration": "Permanent"
            },
            {
                "name": "Counterspelling",
                "description": "Allows the caster to disrupt or negate another spell as it's being cast.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Special",
                "duration": "Instant"
            },
            {
                "name": "Fashion",
                "description": "Allows the caster to create or alter clothing and accessories.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Foretell",
                "description": "Grants the caster a brief glimpse of potential future events.",
                "level": 1,
                "school": "Detection",
                "type": "Mana",
                "range": "Self",
                "duration": "Instant"
            },
            {
                "name": "Gecko Crawl",
                "description": "Allows the target to climb walls and ceilings like a gecko.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Gravity Manipulation",
                "description": "Alters the gravity in a targeted area, making it stronger, weaker, or redirected.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Hibernate",
                "description": "Puts the target into a state of suspended animation.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mana Sphere",
                "description": "Creates a mobile sphere of mana that can be used to cast spells at a distance.",
                "level": 1,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Nutrition",
                "description": "Provides the target with necessary nutrients, eliminating the need for food and water temporarily.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Shift",
                "description": "Allows the caster to teleport a short distance.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Self",
                "duration": "Instant"
            },
            {
                "name": "Spirit Barrier",
                "description": "Creates a barrier that blocks spirits and astral forms.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Agony",
                "description": "Causes intense pain in the target without causing physical damage.",
                "level": 2,
                "school": "Combat",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Antidote",
                "description": "Neutralizes toxins and poisons in the target's system.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Astral Cloak",
                "description": "Masks the target's astral signature, making them harder to detect in astral space.",
                "level": 3,
                "school": "Illusion",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Blast",
                "description": "Creates an explosion of pure magical energy at the target location.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Calm Animal",
                "description": "Soothes and calms an agitated animal.",
                "level": 3,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Chaotic World",
                "description": "Creates an illusion of a chaotic, ever-changing environment around the target.",
                "level": 2,
                "school": "Illusion",
                "type": "Mana",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Control Fire",
                "description": "Allows the caster to manipulate existing fire, controlling its size and direction.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Detect Enemies, Extended",
                "description": "An improved version of Detect Enemies with a larger area of effect.",
                "level": 1,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight (Extended Area)",
                "duration": "Sustained"
            },
            {
                "name": "Enhance Aim",
                "description": "Improves the target's accuracy with ranged weapons.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Fashion",
                "description": "Alters the appearance and style of clothing and accessories.",
                "level": 4,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Fling",
                "description": "Allows the caster to telekinetically throw objects or people.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Hardened Armor",
                "description": "Creates an extremely durable magical armor around the target.",
                "level": 1,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Ignite",
                "description": "Causes a target object to burst into flames.",
                "level": 4,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Laser",
                "description": "Creates a focused beam of light that can cut through objects.",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Lock",
                "description": "Magically seals a door, window, or container.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Alter Memory",
                "description": "Allows the caster to modify or erase specific memories of the target.",
                "level": 1,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Analyze Truth",
                "description": "Helps the caster determine if a target is telling the truth.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Astral Projection",
                "description": "Allows the caster to project their consciousness into astral space.",
                "level": 1,
                "school": "Health",
                "type": "Mana",
                "range": "Self",
                "duration": "Special"
            },
            {
                "name": "Catfall",
                "description": "Reduces falling damage for the target.",
                "level": 4,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Combat Sense",
                "description": "Enhances the target's awareness and reflexes in combat situations.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Control Water",
                "description": "Allows the caster to manipulate water, controlling its flow and shape.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Deflection",
                "description": "Creates a field that deflects incoming projectiles.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Detox",
                "description": "Removes toxins and alcohol from the target's system.",
                "level": 4,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Elemental Wall",
                "description": "Creates a wall of a chosen elemental force (fire, water, earth, or air).",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Enchant",
                "description": "Temporarily imbues an object with magical properties.",
                "level": 1,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Increase Reflexes",
                "description": "Magically enhances the target's reflexes and speed.",
                "level": 1,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mana Static",
                "description": "Creates an area of magical interference, making spellcasting more difficult.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Mob Mood",
                "description": "Influences the emotional state of a group of people.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Penetrating Spell",
                "description": "Enhances another spell to bypass magical defenses more easily.",
                "level": 1,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Self",
                "duration": "Instant"
            },
            {
                "name": "Reinforce",
                "description": "Temporarily increases the structural integrity of an object or building.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Aesthetic Enhancement",
                "description": "Temporarily improves the target's physical appearance.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Astral Beacon",
                "description": "Creates a bright beacon visible in astral space.",
                "level": 4,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Blur",
                "description": "Makes the target's outline blurry, making them harder to hit.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Cleanse",
                "description": "Removes contaminants and impurities from food and water.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Clean Air",
                "description": "Purifies air in an area, removing toxins and pollutants.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Convincing Lie",
                "description": "Enhances the caster's ability to lie convincingly.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Self",
                "duration": "Sustained"
            },
            {
                "name": "Crop Growth",
                "description": "Accelerates the growth of plants and crops.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch (Area)",
                "duration": "Permanent"
            },
            {
                "name": "Deathtouch",
                "description": "Delivers a potentially lethal shock to a living target.",
                "level": 1,
                "school": "Combat",
                "type": "Mana",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Deflect Attention",
                "description": "Makes the target less noticeable to others.",
                "level": 3,
                "school": "Illusion",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Enhance Strength",
                "description": "Temporarily increases the target's physical strength.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Extinguish Fire",
                "description": "Instantly puts out fires in the affected area.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Fallout",
                "description": "Creates a small area of radioactive contamination.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Freeze",
                "description": "Rapidly lowers the temperature of a target, potentially freezing it.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Glue",
                "description": "Creates a strong adhesive substance that can bind objects or creatures.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Hibernate",
                "description": "Puts the target into a state of suspended animation.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Aerodynamic",
                "description": "Reduces air resistance around a target, improving speed and maneuverability.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Alter Temperature",
                "description": "Allows the caster to raise or lower the temperature in a small area.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Astral Interference",
                "description": "Creates static in astral space, making astral perception and projection more difficult.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Borrow Sense",
                "description": "Allows the caster to temporarily use one of the target's senses.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Calm Pack",
                "description": "Soothes and calms a group of animals.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Camouflage",
                "description": "Makes the target blend in with their surroundings.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Canonize",
                "description": "Enhances the target's charisma and perceived importance.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Crank",
                "description": "Temporarily boosts the target's reaction time and physical capabilities.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Dehydrate",
                "description": "Rapidly removes moisture from the target.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Dig",
                "description": "Creates a tunnel or hole in earth or stone.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Energize",
                "description": "Temporarily eliminates the need for sleep for the target.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Enhance Speed",
                "description": "Increases the target's movement speed.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Firewall",
                "description": "Creates a barrier that blocks fire and heat.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Gravity Manipulation",
                "description": "Allows the caster to increase or decrease gravity in a small area.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Stealth",
                "description": "Makes the target more difficult to detect through technological means.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Armor-Piercing Spell",
                "description": "Enhances another combat spell to better penetrate magical and physical defenses.",
                "level": 1,
                "school": "Combat / Type: Special",
                "range": "Special",
                "duration": "Instant"
            },
            {
                "name": "Astral Message",
                "description": "Allows the caster to send a short message through astral space to a known recipient.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Special",
                "duration": "Instant"
            },
            {
                "name": "Awaken",
                "description": "Instantly wakes up a sleeping or unconscious target.",
                "level": 4,
                "school": "Health",
                "type": "Mana",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Balance",
                "description": "Improves the target's balance and coordination.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Bind",
                "description": "Creates magical restraints around a target.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Bullet Shield",
                "description": "Creates a field that slows down incoming projectiles.",
                "level": 2,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Categorize",
                "description": "Allows the caster to quickly sort and organize physical or digital information.",
                "level": 4,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Cellular Repair",
                "description": "Accelerates natural healing processes in the target.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Charged Barrier",
                "description": "Creates an electrified barrier that shocks those who touch it.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Clarity",
                "description": "Clears the target's mind, improving mental acuity and resistance to mental manipulation.",
                "level": 2,
                "school": "Health",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Dazzle",
                "description": "Creates a bright flash of light that can disorient or blind targets.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Instant"
            },
            {
                "name": "Decrypt",
                "description": "Assists in breaking codes or decrypting encrypted data.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Density Alteration",
                "description": "Temporarily changes the density of an object or being.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Disrupt Focus",
                "description": "Interferes with a target's ability to concentrate or maintain focus.",
                "level": 3,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Elasticity",
                "description": "Grants the target's body increased flexibility and elasticity.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Empathic Healing",
                "description": "Allows the caster to take on another's injuries, healing the target but harming the caster.",
                "level": 3,
                "school": "Health",
                "type": "Mana",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Enhance Cybernetics",
                "description": "Temporarily improves the functionality of cyberware or bioware.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Essence Drain",
                "description": "Drains a portion of the target's life force, weakening them and strengthening the caster.",
                "level": 1,
                "school": "Health",
                "type": "Mana",
                "range": "Touch",
                "duration": "Instant"
            },
            {
                "name": "Fabricate",
                "description": "Creates a small, simple object out of raw magical energy.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Faraday Cage",
                "description": "Creates a field that blocks electromagnetic signals.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Forced Defense",
                "description": "Compels the target to defend themselves, even against their will.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Sustained"
            },
            {
                "name": "Gravity Well",
                "description": "Creates a localized area of intense gravitational pull.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Line of Sight (Area)",
                "duration": "Sustained"
            },
            {
                "name": "Hibernate",
                "description": "Puts the target into a state of suspended animation.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Interference",
                "description": "Creates magical static that disrupts technological devices.",
                "level": 3,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Mana Bubble",
                "description": "Creates a small area where mana flows more freely, enhancing magical effects.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Metabolic Control",
                "description": "Allows the caster to control their own or another's metabolic processes.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mimic",
                "description": "Allows the caster to perfectly imitate the voice of another person.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Self",
                "duration": "Sustained"
            },
            {
                "name": "Nullify Toxin",
                "description": "Neutralizes toxins and poisons in the target's system.",
                "level": 3,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Permanent"
            },
            {
                "name": "Orb of Light",
                "description": "Creates a floating sphere of light that follows the caster.",
                "level": 4,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Self",
                "duration": "Sustained"
            },
            {
                "name": "Planar Step",
                "description": "Allows the caster to briefly step into the astral plane to avoid attacks.",
                "level": 2,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Self",
                "duration": "Instant"
            },
            {
                "name": "Alter Ballistics",
                "description": "Modifies the trajectory of projectiles in an area.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Astral Encryption",
                "description": "Encrypts the caster's astral signature, making it harder to track or identify.",
                "level": 3,
                "school": "Illusion",
                "type": "Mana",
                "range": "Self",
                "duration": "Sustained"
            },
            {
                "name": "Bioelectric Dampening",
                "description": "Reduces the target's bioelectric signature, making them harder to detect by certain sensors.",
                "level": 3,
                "school": "Illusion",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Codebreaker",
                "description": "Enhances the caster's ability to break codes and encryption.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Self",
                "duration": "Sustained"
            },
            {
                "name": "Electromagnetic Pulse",
                "description": "Creates a localized EMP effect, disabling electronic devices.",
                "level": 2,
                "school": "Manipulation",
                "type": "Physical",
                "range": "Area",
                "duration": "Instant"
            },
            {
                "name": "Elemental Strike",
                "description": "Imbues a melee attack with elemental energy (fire, ice, electricity, etc.).",
                "level": 3,
                "school": "Combat",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Enhance Reflexes",
                "description": "Drastically improves the target's reaction time and coordination.",
                "level": 1,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Foreboding",
                "description": "Gives the target a supernatural sense of impending danger.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Genetic Optimization",
                "description": "Temporarily enhances the target's natural genetic potential.",
                "level": 2,
                "school": "Health",
                "type": "Physical",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Hush",
                "description": "Creates an area of magical silence, dampening all sounds.",
                "level": 3,
                "school": "Illusion",
                "type": "Mana",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Intrusion Countermeasures",
                "description": "Creates magical defenses against technological and magical intrusion attempts.",
                "level": 3,
                "school": "Manipulation",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Mana Spike",
                "description": "Releases a concentrated burst of mana, damaging magical constructs and spirits.",
                "level": 3,
                "school": "Combat",
                "type": "Mana",
                "range": "Line of Sight",
                "duration": "Instant"
            },
            {
                "name": "Neural Dampening",
                "description": "Reduces the target's ability to feel pain.",
                "level": 3,
                "school": "Health",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            },
            {
                "name": "Rewind",
                "description": "Allows the caster to view recent events in an area in reverse.",
                "level": 2,
                "school": "Detection",
                "type": "Mana",
                "range": "Area",
                "duration": "Sustained"
            },
            {
                "name": "Spatial Comprehension",
                "description": "Enhances the target's understanding and perception of three-dimensional space.",
                "level": 3,
                "school": "Detection",
                "type": "Mana",
                "range": "Touch",
                "duration": "Sustained"
            }
        ],
        "Star Wars: Edge of the Empire": [
            {
                "name": "Sense",
                "description": "The Force user can feel the Force flowing through themselves and the world around them, gaining insight and information.",
                "level": 1,
                "school": "Universal",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "None",
                "force_power_tree": {
                    "base_power": "Sense the Force in immediate area",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase range of sense", "xp_cost": 10},
                        {"name": "Strength", "effect": "Sense Force potential in others", "xp_cost": 15},
                        {"name": "Duration", "effect": "Commit Force die to sense constantly", "xp_cost": 20},
                        {"name": "Power", "effect": "Sense emotions and hints of the future", "xp_cost": 25}
                    ]
                },
                "strain_cost": 1,
                "conflict_risk": 0
            },
            {
                "name": "Influence",
                "description": "The Force user can guide and direct the thoughts and actions of the weak-minded.",
                "level": 1,
                "school": "Control",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Verbal",
                "force_power_tree": {
                    "base_power": "Influence a target's emotional state",
                    "upgrades": [
                        {"name": "Control", "effect": "Influence a target's actions", "xp_cost": 15},
                        {"name": "Strength", "effect": "Influence multiple targets", "xp_cost": 20},
                        {"name": "Magnitude", "effect": "Increase range of influence", "xp_cost": 10},
                        {"name": "Mastery", "effect": "Dominate a target's mind", "xp_cost": 30}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 2
            },
            {
                "name": "Move",
                "description": "The Force user can manipulate physical objects through the power of the Force.",
                "level": 1,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Move small objects",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase range and size of objects", "xp_cost": 10},
                        {"name": "Strength", "effect": "Increase weight of movable objects", "xp_cost": 15},
                        {"name": "Control", "effect": "Perform fine manipulation", "xp_cost": 20},
                        {"name": "Mastery", "effect": "Hurl objects with great force", "xp_cost": 25}
                    ]
                },
                "strain_cost": 1,
                "conflict_risk": 1
            },
            {
                "name": "Enhance",
                "description": "The Force user can channel the Force to enhance their physical and mental attributes.",
                "level": 1,
                "school": "Control",
                "casting_time": "Action",
                "range": "Self",
                "duration": "Concentration",
                "components": "None",
                "force_power_tree": {
                    "base_power": "Enhance a single characteristic",
                    "upgrades": [
                        {"name": "Strength", "effect": "Enhance multiple characteristics", "xp_cost": 15},
                        {"name": "Duration", "effect": "Commit Force die for ongoing enhancement", "xp_cost": 20},
                        {"name": "Control", "effect": "Enhance specific skills", "xp_cost": 10},
                        {"name": "Mastery", "effect": "Superhuman feats", "xp_cost": 30}
                    ]
                },
                "strain_cost": 1,
                "conflict_risk": 0
            },
            {
                "name": "Heal/Harm",
                "description": "The Force user can manipulate the life energy of others, either to mend wounds or inflict damage.",
                "level": 2,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Touch",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Heal minor wounds or inflict minor damage",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase amount healed/harmed", "xp_cost": 15},
                        {"name": "Range", "effect": "Heal/harm at a distance", "xp_cost": 20},
                        {"name": "Control", "effect": "Cure critical injuries or diseases", "xp_cost": 25},
                        {"name": "Mastery", "effect": "Revive the recently deceased", "xp_cost": 30}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 3
            },
            {
                "name": "Foresee",
                "description": "The Force user can catch glimpses of the future or gain insight into present events.",
                "level": 2,
                "school": "Sense",
                "casting_time": "Action",
                "range": "Self",
                "duration": "Concentration",
                "components": "None",
                "force_power_tree": {
                    "base_power": "Catch brief glimpses of the future",
                    "upgrades": [
                        {"name": "Duration", "effect": "Extend the vision's reach into the future", "xp_cost": 15},
                        {"name": "Strength", "effect": "Gain more detailed visions", "xp_cost": 20},
                        {"name": "Range", "effect": "Foresee events at greater distances", "xp_cost": 10},
                        {"name": "Mastery", "effect": "Alter the foreseen future", "xp_cost": 30}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 1
            },
            {
                "name": "Protect/Unleash",
                "description": "The Force user can create barriers of Force energy or unleash it in destructive bursts.",
                "level": 2,
                "school": "Control",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create a personal force field or unleash a small burst of energy",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase size of barrier or blast", "xp_cost": 15},
                        {"name": "Strength", "effect": "Enhance protective/damaging capabilities", "xp_cost": 20},
                        {"name": "Range", "effect": "Protect/attack at greater distances", "xp_cost": 10},
                        {"name": "Control", "effect": "Selectively allow things through barrier", "xp_cost": 25}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 2
            },
            {
                "name": "Bind",
                "description": "The Force user can create bonds or restraints of Force energy.",
                "level": 3,
                "school": "Control",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create Force bonds to restrain a target",
                    "upgrades": [
                        {"name": "Strength", "effect": "Create stronger, harder to break bonds", "xp_cost": 20},
                        {"name": "Range", "effect": "Bind targets at greater distances", "xp_cost": 15},
                        {"name": "Control", "effect": "Bind specific body parts or objects", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Bind multiple targets simultaneously", "xp_cost": 30}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 2
            },
            {
                "name": "Seek",
                "description": "The Force user can search for specific people, objects, or information through the Force.",
                "level": 2,
                "school": "Sense",
                "casting_time": "Action",
                "range": "Long",
                "duration": "Concentration",
                "components": "None",
                "force_power_tree": {
                    "base_power": "Sense the general direction of a known person or object",
                    "upgrades": [
                        {"name": "Range", "effect": "Increase the distance at which targets can be sensed", "xp_cost": 15},
                        {"name": "Power", "effect": "Gain more detailed information about the target", "xp_cost": 20},
                        {"name": "Control", "effect": "Pierce through Force concealment", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Seek multiple targets simultaneously", "xp_cost": 30}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 1
            },
            {
                "name": "Misdirect",
                "description": "The Force user can create illusions or manipulate perceptions.",
                "level": 3,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create minor visual illusions",
                    "upgrades": [
                        {"name": "Strength", "effect": "Create more convincing, multi-sensory illusions", "xp_cost": 20},
                        {"name": "Range", "effect": "Create illusions at greater distances", "xp_cost": 15},
                        {"name": "Control", "effect": "Manipulate existing perceptions", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Affect multiple targets with illusions", "xp_cost": 30}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 2
            },
            {
                "name": "Ebb/Flow",
                "description": "The Force user can manipulate the Force to enhance or diminish the abilities of others.",
                "level": 3,
                "school": "Universal",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Temporarily boost or hinder a single characteristic of a target",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Affect multiple characteristics", "xp_cost": 20},
                        {"name": "Strength", "effect": "Increase the degree of enhancement or hindrance", "xp_cost": 25},
                        {"name": "Range", "effect": "Affect targets at greater distances", "xp_cost": 15},
                        {"name": "Control", "effect": "Affect specific skills instead of characteristics", "xp_cost": 30}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 2
            },
            {
                "name": "Alter Environment",
                "description": "The Force user can manipulate the physical environment around them.",
                "level": 2,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Make minor alterations to the immediate environment",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Affect a larger area", "xp_cost": 15},
                        {"name": "Control", "effect": "Make more significant environmental changes", "xp_cost": 25},
                        {"name": "Range", "effect": "Alter environment at greater distances", "xp_cost": 20},
                        {"name": "Duration", "effect": "Sustain environmental changes for longer periods", "xp_cost": 30}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 1
            },
            {
                "name": "Battle Meditation",
                "description": "The Force user can influence the morale and coordination of allies in battle.",
                "level": 3,
                "school": "Sense",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Boost the morale of a small group of allies",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Affect a larger number of allies", "xp_cost": 25},
                        {"name": "Strength", "effect": "Provide greater combat bonuses", "xp_cost": 30},
                        {"name": "Control", "effect": "Coordinate complex battle strategies", "xp_cost": 35},
                        {"name": "Range", "effect": "Influence battles over greater distances", "xp_cost": 20}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 1
            },
            {
                "name": "Force Cloak",
                "description": "The Force user can conceal their presence in the Force.",
                "level": 3,
                "school": "Control",
                "casting_time": "Action",
                "range": "Self",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Mask Force presence from basic detection",
                    "upgrades": [
                        {"name": "Strength", "effect": "Improve concealment against stronger Force users", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Extend cloaking effect to nearby allies", "xp_cost": 30},
                        {"name": "Duration", "effect": "Maintain cloak for extended periods", "xp_cost": 20},
                        {"name": "Control", "effect": "Selectively reveal presence to specific individuals", "xp_cost": 35}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 1
            },
            {
                "name": "Force Empathy",
                "description": "The Force user can sense and influence the emotions of others.",
                "level": 2,
                "school": "Sense",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Sense the surface emotions of a single target",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Sense emotions of multiple targets", "xp_cost": 20},
                        {"name": "Strength", "effect": "Delve into deeper emotions and memories", "xp_cost": 25},
                        {"name": "Range", "effect": "Sense emotions at greater distances", "xp_cost": 15},
                        {"name": "Control", "effect": "Subtly influence emotional states", "xp_cost": 30}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 2
            },
            {
                "name": "Force Ghost",
                "description": "The Force user can project their consciousness beyond their physical body, appearing as a spectral form.",
                "level": 5,
                "school": "Universal",
                "casting_time": "1 hour",
                "range": "Planetary",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Project a visible but intangible form of oneself",
                    "upgrades": [
                        {"name": "Duration", "effect": "Extend the time one can remain as a Force ghost", "xp_cost": 30},
                        {"name": "Strength", "effect": "Gain ability to interact with physical world", "xp_cost": 35},
                        {"name": "Range", "effect": "Project across greater distances, even to other planets", "xp_cost": 40},
                        {"name": "Control", "effect": "Maintain consciousness after physical death", "xp_cost": 50}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 0
            },
            {
                "name": "Fold Space",
                "description": "The Force user can create a temporary wormhole, instantly transporting themselves or objects across space.",
                "level": 4,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Touch",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create a small wormhole to transport an object",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase size of wormhole to transport larger objects or beings", "xp_cost": 30},
                        {"name": "Range", "effect": "Create wormholes over greater distances", "xp_cost": 35},
                        {"name": "Control", "effect": "Precisely control the exit point of the wormhole", "xp_cost": 40},
                        {"name": "Mastery", "effect": "Create stable, longer-lasting wormholes", "xp_cost": 45}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 3
            },
            {
                "name": "Force Storm",
                "description": "The Force user can create a massive storm of Force energy, causing widespread destruction.",
                "level": 5,
                "school": "Alter",
                "casting_time": "1 minute",
                "range": "Long",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Create a small localized Force storm",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase the size and power of the storm", "xp_cost": 35},
                        {"name": "Control", "effect": "Direct the storm's movement and effects", "xp_cost": 40},
                        {"name": "Duration", "effect": "Sustain the storm for longer periods", "xp_cost": 30},
                        {"name": "Mastery", "effect": "Create storms capable of destroying capital ships", "xp_cost": 50}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 5
            },
            {
                "name": "Transfer Essence",
                "description": "The Force user can transfer their consciousness into another body or object.",
                "level": 5,
                "school": "Universal",
                "casting_time": "1 hour",
                "range": "Touch",
                "duration": "Permanent",
                "components": "Verbal, Somatic, Material (rare artifacts)",
                "force_power_tree": {
                    "base_power": "Transfer consciousness to a prepared vessel",
                    "upgrades": [
                        {"name": "Range", "effect": "Perform transfer from a distance", "xp_cost": 40},
                        {"name": "Control", "effect": "Transfer into unwilling hosts", "xp_cost": 45},
                        {"name": "Magnitude", "effect": "Transfer multiple consciousnesses simultaneously", "xp_cost": 50},
                        {"name": "Mastery", "effect": "Create multiple active copies of one's consciousness", "xp_cost": 55}
                    ]
                },
                "strain_cost": 10,
                "conflict_risk": 5
            },
            {
                "name": "Force Harmony",
                "description": "The Force user can create a powerful synergy between Force users, amplifying their collective abilities.",
                "level": 4,
                "school": "Universal",
                "casting_time": "1 minute",
                "range": "Short",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Link the Force abilities of a small group",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Include more individuals in the harmony", "xp_cost": 30},
                        {"name": "Strength", "effect": "Increase the power amplification of the harmony", "xp_cost": 35},
                        {"name": "Range", "effect": "Maintain harmony over greater distances", "xp_cost": 25},
                        {"name": "Control", "effect": "Selectively amplify specific Force abilities", "xp_cost": 40}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 1
            },
            {
                "name": "Force Light",
                "description": "The Force user channels the light side to create purifying energy that is particularly effective against dark side entities.",
                "level": 4,
                "school": "Universal",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Instant",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Create a burst of light side energy",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase the area affected by Force Light", "xp_cost": 30},
                        {"name": "Strength", "effect": "Enhance the purifying effect against dark side corruption", "xp_cost": 35},
                        {"name": "Control", "effect": "Shape the light to create barriers or weapons", "xp_cost": 40},
                        {"name": "Mastery", "effect": "Permanently purify locations tainted by the dark side", "xp_cost": 45}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 0
            },
            {
                "name": "Force Suppression",
                "description": "The Force user can temporarily suppress the Force abilities of others.",
                "level": 3,
                "school": "Control",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Suppress minor Force abilities of a single target",
                    "upgrades": [
                        {"name": "Strength", "effect": "Suppress more powerful Force abilities", "xp_cost": 30},
                        {"name": "Range", "effect": "Suppress Force abilities at greater distances", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Suppress abilities of multiple targets", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain suppression for longer periods", "xp_cost": 30}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 2
            },
            {
                "name": "Force Breach",
                "description": "The Force user can break through Force-based defenses and illusions.",
                "level": 3,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Instant",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Break through basic Force barriers or illusions",
                    "upgrades": [
                        {"name": "Strength", "effect": "Pierce stronger Force defenses", "xp_cost": 30},
                        {"name": "Range", "effect": "Breach Force effects at greater distances", "xp_cost": 25},
                        {"name": "Control", "effect": "Selectively breach specific Force effects", "xp_cost": 35},
                        {"name": "Magnitude", "effect": "Breach multiple Force effects simultaneously", "xp_cost": 40}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 1
            },
            {
                "name": "Force Repulse",
                "description": "The Force user releases a powerful omnidirectional blast of Force energy.",
                "level": 3,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create a short-range Force blast",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase the range and area of effect", "xp_cost": 25},
                        {"name": "Strength", "effect": "Increase the power of the blast", "xp_cost": 30},
                        {"name": "Control", "effect": "Shape the blast to avoid allies", "xp_cost": 35},
                        {"name": "Mastery", "effect": "Create sustained Force Repulse field", "xp_cost": 40}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 2
            },
            {
                "name": "Force Comprehension",
                "description": "The Force user can rapidly understand and learn new information or skills.",
                "level": 2,
                "school": "Sense",
                "casting_time": "10 minutes",
                "range": "Self",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Gain basic understanding of a new concept or skill",
                    "upgrades": [
                        {"name": "Strength", "effect": "Comprehend more complex information", "xp_cost": 25},
                        {"name": "Duration", "effect": "Retain comprehended information for longer", "xp_cost": 30},
                        {"name": "Magnitude", "effect": "Comprehend multiple subjects simultaneously", "xp_cost": 35},
                        {"name": "Mastery", "effect": "Instantly master complex skills temporarily", "xp_cost": 40}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 1
            },
            {
                "name": "Force Stealth",
                "description": "The Force user can mask their presence in both the physical and Force realms.",
                "level": 3,
                "school": "Control",
                "casting_time": "Action",
                "range": "Self",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Conceal Force presence and dampen physical signs",
                    "upgrades": [
                        {"name": "Strength", "effect": "Improve concealment against stronger Force users", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Extend stealth effect to nearby allies", "xp_cost": 30},
                        {"name": "Duration", "effect": "Maintain stealth for extended periods", "xp_cost": 20},
                        {"name": "Mastery", "effect": "Completely vanish from Force perception", "xp_cost": 35}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 1
            },
            {
                "name": "Psychometry",
                "description": "The Force user can sense impressions and traces of information about the past by touching objects.",
                "level": 2,
                "school": "Sense",
                "casting_time": "Action",
                "range": "Touch",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Sense recent, strong impressions from an object",
                    "upgrades": [
                        {"name": "Strength", "effect": "Perceive older or fainter impressions", "xp_cost": 20},
                        {"name": "Control", "effect": "Focus on specific types of information", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Read impressions from larger areas", "xp_cost": 30},
                        {"name": "Mastery", "effect": "Experience vivid visions of past events", "xp_cost": 35}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 1
            },
            {
                "name": "Force Absorb",
                "description": "The Force user can absorb and neutralize energy, including blaster bolts and Force lightning.",
                "level": 4,
                "school": "Alter",
                "casting_time": "Reaction",
                "range": "Self",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Absorb minor energy attacks",
                    "upgrades": [
                        {"name": "Strength", "effect": "Absorb more powerful energy attacks", "xp_cost": 30},
                        {"name": "Magnitude", "effect": "Absorb attacks aimed at nearby allies", "xp_cost": 35},
                        {"name": "Control", "effect": "Redirect absorbed energy as an attack", "xp_cost": 40},
                        {"name": "Mastery", "effect": "Absorb and neutralize Force powers", "xp_cost": 45}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 1
            },
            {
                "name": "Beast Control",
                "description": "The Force user can influence and control the minds of animals and creatures.",
                "level": 2,
                "school": "Control",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Influence the behavior of a single, simple-minded creature",
                    "upgrades": [
                        {"name": "Strength", "effect": "Control more intelligent or resistant creatures", "xp_cost": 25},
                        {"name": "Magnitude", "effect": "Control multiple creatures simultaneously", "xp_cost": 30},
                        {"name": "Range", "effect": "Influence creatures at greater distances", "xp_cost": 20},
                        {"name": "Mastery", "effect": "Permanently bond with and control a creature", "xp_cost": 35}
                    ]
                },
                "strain_cost": 2,
                "conflict_risk": 2
            },
            {
                "name": "Force Body",
                "description": "The Force user can push their body beyond normal physical limits, enhancing strength, speed, and endurance.",
                "level": 3,
                "school": "Control",
                "casting_time": "Action",
                "range": "Self",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Enhance physical attributes slightly beyond normal limits",
                    "upgrades": [
                        {"name": "Strength", "effect": "Push physical abilities to superhuman levels", "xp_cost": 30},
                        {"name": "Duration", "effect": "Maintain enhancements for extended periods", "xp_cost": 25},
                        {"name": "Control", "effect": "Selectively enhance specific attributes or abilities", "xp_cost": 35},
                        {"name": "Mastery", "effect": "Achieve temporary physical invulnerability", "xp_cost": 40}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 2
            },
            {
                "name": "Force Ionize",
                "description": "The Force user can disrupt electronic systems and droids using the Force.",
                "level": 3,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Short",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Temporarily disable a single electronic device or droid",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Affect multiple devices or a larger area", "xp_cost": 25},
                        {"name": "Strength", "effect": "Cause permanent damage to electronics", "xp_cost": 30},
                        {"name": "Range", "effect": "Ionize targets at greater distances", "xp_cost": 20},
                        {"name": "Control", "effect": "Selectively disable specific systems", "xp_cost": 35}
                    ]
                },
                "strain_cost": 3,
                "conflict_risk": 1
            },
            {
                "name": "Force Immerse",
                "description": "The Force user can submerge themselves deeply in the Force, gaining heightened awareness and abilities.",
                "level": 4,
                "school": "Universal",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Gain enhanced sensory awareness and Force sensitivity",
                    "upgrades": [
                        {"name": "Strength", "effect": "Dramatically increase Force power while immersed", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain immersion for extended periods", "xp_cost": 30},
                        {"name": "Control", "effect": "Perform complex Force techniques while immersed", "xp_cost": 40},
                        {"name": "Mastery", "effect": "Achieve a state of oneness with the Force", "xp_cost": 50}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 3
            },
            {
                "name": "Force Flash",
                "description": "The Force user can travel instantaneously between two points by briefly entering the Force realm.",
                "level": 5,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Instant",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Instantly teleport to a visible location",
                    "upgrades": [
                        {"name": "Range", "effect": "Increase the distance of the teleportation", "xp_cost": 35},
                        {"name": "Control", "effect": "Teleport with pinpoint accuracy", "xp_cost": 40},
                        {"name": "Magnitude", "effect": "Bring additional beings or objects along", "xp_cost": 45},
                        {"name": "Mastery", "effect": "Teleport to unseen, known locations", "xp_cost": 50}
                    ]
                },
                "strain_cost": 6,
                "conflict_risk": 2
            },
            {
                "name": "Force Cipher",
                "description": "The Force user can encode or decode information within the fabric of the Force itself.",
                "level": 3,
                "school": "Alter",
                "casting_time": "10 minutes",
                "range": "Touch",
                "duration": "Permanent",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Encode or decode a small amount of information in the Force",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase the amount of information that can be stored", "xp_cost": 25},
                        {"name": "Strength", "effect": "Create more complex and secure Force ciphers", "xp_cost": 30},
                        {"name": "Control", "effect": "Embed Force ciphers in physical objects", "xp_cost": 35},
                        {"name": "Mastery", "effect": "Create self-updating Force records", "xp_cost": 40}
                    ]
                },
                "strain_cost": 4,
                "conflict_risk": 1
            },
            {
                "name": "Force Nullify",
                "description": "The Force user can create areas where the Force cannot be used or sensed.",
                "level": 4,
                "school": "Control",
                "casting_time": "1 minute",
                "range": "Short",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Create a small area where minor Force abilities fail",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Increase the size of the nullified area", "xp_cost": 30},
                        {"name": "Strength", "effect": "Nullify more powerful Force abilities", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain the nullification for extended periods", "xp_cost": 25},
                        {"name": "Mastery", "effect": "Create permanent Force-null zones", "xp_cost": 45}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 3
            },
            {
                "name": "Force Nexus Attunement",
                "description": "The Force user can attune themselves to Force nexuses, drawing upon their power.",
                "level": 5,
                "school": "Universal",
                "casting_time": "1 hour",
                "range": "Self",
                "duration": "1 day",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Attune to a Force nexus, gaining enhanced Force abilities while near it",
                    "upgrades": [
                        {"name": "Range", "effect": "Maintain connection to nexus from greater distances", "xp_cost": 40},
                        {"name": "Strength", "effect": "Draw more power from the nexus", "xp_cost": 45},
                        {"name": "Duration", "effect": "Extend the attunement period", "xp_cost": 35},
                        {"name": "Mastery", "effect": "Carry a portion of the nexus's power with you", "xp_cost": 50}
                    ]
                },
                "strain_cost": 6,
                "conflict_risk": 3
            },
            {
                "name": "Force Conduit",
                "description": "The Force user becomes a living conduit for the Force, channeling its raw power.",
                "level": 4,
                "school": "Universal",
                "casting_time": "1 minute",
                "range": "Self",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Channel the Force to enhance all Force abilities",
                    "upgrades": [
                        {"name": "Strength", "effect": "Increase the power of channeled abilities", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain the conduit state longer", "xp_cost": 30},
                        {"name": "Control", "effect": "Selectively enhance specific Force powers", "xp_cost": 40},
                        {"name": "Mastery", "effect": "Share channeled power with other Force users", "xp_cost": 45}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 4
            },
            {
                "name": "Force Weave",
                "description": "The Force user can manipulate the very fabric of the Force, creating complex patterns and effects.",
                "level": 5,
                "school": "Alter",
                "casting_time": "1 minute",
                "range": "Medium",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Create simple Force constructs or patterns",
                    "upgrades": [
                        {"name": "Complexity", "effect": "Create more intricate and powerful Force weaves", "xp_cost": 40},
                        {"name": "Magnitude", "effect": "Increase the size and scope of the weave", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain weaves for extended periods", "xp_cost": 30},
                        {"name": "Mastery", "effect": "Create semi-permanent Force structures", "xp_cost": 50}
                    ]
                },
                "strain_cost": 6,
                "conflict_risk": 3
            },
            {
                "name": "Force Echo",
                "description": "The Force user can project echoes of themselves through the Force, creating multiple instances of their presence.",
                "level": 4,
                "school": "Alter",
                "casting_time": "Action",
                "range": "Medium",
                "duration": "Concentration",
                "components": "Somatic",
                "force_power_tree": {
                    "base_power": "Create a single Force echo of yourself",
                    "upgrades": [
                        {"name": "Magnitude", "effect": "Create multiple Force echoes", "xp_cost": 35},
                        {"name": "Fidelity", "effect": "Increase the realism and capability of echoes", "xp_cost": 40},
                        {"name": "Range", "effect": "Project echoes at greater distances", "xp_cost": 30},
                        {"name": "Mastery", "effect": "Grant echoes limited independent action", "xp_cost": 45}
                    ]
                },
                "strain_cost": 5,
                "conflict_risk": 2
            },
            {
                "name": "Force Synthesis",
                "description": "The Force user can temporarily merge the properties of physical objects or even living beings.",
                "level": 5,
                "school": "Alter",
                "casting_time": "1 minute",
                "range": "Touch",
                "duration": "Concentration",
                "components": "Verbal, Somatic",
                "force_power_tree": {
                    "base_power": "Merge two small, simple objects",
                    "upgrades": [
                        {"name": "Complexity", "effect": "Synthesize more complex or disparate objects", "xp_cost": 40},
                        {"name": "Magnitude", "effect": "Merge larger or multiple objects", "xp_cost": 35},
                        {"name": "Duration", "effect": "Maintain synthesis for longer periods", "xp_cost": 30},
                        {"name": "Mastery", "effect": "Temporarily synthesize living beings", "xp_cost": 50}
                    ]
                },
                "strain_cost": 6,
                "conflict_risk": 4
            }
        ],
        "Mothership RPG": [
            {"name": "EMP Pulse", "description": "A pulse that disables nearby electronic devices.", "level": 1, "school": "Tech", "casting_time": "1 action", "range": "10 feet", "duration": "Instantaneous", "components": "S"}
        ]
    }

    class_spells = {
        "Dungeons & Dragons 5th Edition": {
            "Druid": [
                # Level 0 (Cantrips)
                "Create Bonfire",
                "Druidcraft",
                "Frostbite",
                "Guidance",
                "Magic Stone",
                "Mending",
                "Poison Spray",
                "Produce Flame",
                "Resistance",
                "Shillelagh",
                "Thorn Whip",

                # Level 1
                "Absorb Elements",
                "Cure Wounds",
                "Detect Magic",
                "Detect Poison and Disease",
                "Earth Tremor",
                "Entangle",
                "Faerie Fire",
                "Fog Cloud",
                "Goodberry",
                "Healing Word",
                "Ice Knife",
                "Jump",
                "Longstrider",
                "Purify Food and Drink",
                "Speak with Animals",
                "Thunderwave",

                # Level 2
                "Animal Messenger",
                "Barkskin",
                "Beast Sense",
                "Darkvision",
                "Dust Devil",
                "Enhance Ability",
                "Find Traps",
                "Flame Blade",
                "Flaming Sphere",
                "Gust of Wind",
                "Heat Metal",
                "Hold Person",
                "Lesser Restoration",
                "Locate Animals or Plants",
                "Locate Object",
                "Moonbeam",
                "Pass without Trace",
                "Protection from Poison",
                "Skywrite",
                "Spike Growth",

                # Level 3
                "Call Lightning",
                "Conjure Animals",
                "Daylight",
                "Dispel Magic",
                "Erupting Earth",
                "Feign Death",
                "Meld into Stone",
                "Plant Growth",
                "Protection from Energy",
                "Sleet Storm",
                "Speak with Plants",
                "Tidal Wave",
                "Wall of Water",
                "Water Breathing",
                "Water Walk",
                "Wind Wall",

                # Level 4
                "Blight",
                "Charm Monster",
                "Confusion",
                "Conjure Minor Elementals",
                "Conjure Woodland Beings",
                "Control Water",
                "Dominate Beast",
                "Freedom of Movement",
                "Giant Insect",
                "Grasping Vine",
                "Hallucinatory Terrain",
                "Ice Storm",
                "Locate Creature",
                "Polymorph",
                "Stone Shape",
                "Stoneskin",
                
                # Level 5
                "Antilife Shell",
                "Awaken",
                "Commune with Nature",
                "Conjure Elemental",
                "Contagion",
                "Geas",
                "Greater Restoration",
                "Insect Plague",
                "Maelstrom",
                "Mass Cure Wounds",
                "Planar Binding",
                "Reincarnate",
                "Scrying",
                "Transmute Rock",
                "Tree Stride",
                "Wall of Stone",

                # Level 6
                "Conjure Fey",
                "Find the Path",
                "Heal",
                "Heroes' Feast",
                "Move Earth",
                "Sunbeam",
                "Transport via Plants",
                "Wall of Thorns",
                "Wind Walk",

                # Level 7
                "Fire Storm",
                "Mirage Arcane",
                "Plane Shift",
                "Regenerate",
                "Reverse Gravity",

                # Level 8
                "Animal Shapes",
                "Control Weather",
                "Earthquake",
                "Feeblemind",
                "Sunburst",
                "Tsunami",

                # Level 9
                "Foresight",
                "Shapechange",
                "Storm of Vengeance"
            ],
            "Wizard": [
                # Level 0 (Cantrips)
                "Acid Splash",
                "Blade Ward",
                "Booming Blade",
                "Chill Touch",
                "Control Flames",
                "Create Bonfire",
                "Dancing Lights",
                "Encode Thoughts",
                "Fire Bolt",
                "Friends",
                "Frostbite",
                "Green-Flame Blade",
                "Gust",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Minor Illusion",
                "Mold Earth",
                "Poison Spray",
                "Prestidigitation",
                "Ray of Frost",
                "Shape Water",
                "Shocking Grasp",
                "Sword Burst",
                "Thunderclap",
                "Toll the Dead",
                "True Strike",

                # Level 1
                "Alarm",
                "Burning Hands",
                "Charm Person",
                "Chromatic Orb",
                "Color Spray",
                "Comprehend Languages",
                "Detect Magic",
                "Disguise Self",
                "Expeditious Retreat",
                "False Life",
                "Feather Fall",
                "Find Familiar",
                "Fog Cloud",
                "Grease",
                "Identify",
                "Illusory Script",
                "Jump",
                "Longstrider",
                "Mage Armor",
                "Magic Missile",
                "Ray of Sickness",
                "Shield",
                "Silent Image",
                "Sleep",
                "Tasha's Hideous Laughter",
                "Tenser's Floating Disk",
                "Thunderwave",
                "Unseen Servant",
                "Witch Bolt",

                # Level 2
                "Alter Self",
                "Arcane Lock",
                "Blindness/Deafness",
                "Blur",
                "Cloud of Daggers",
                "Continual Flame",
                "Crown of Madness",
                "Darkvision",
                "Detect Thoughts",
                "Dust Devil",
                "Enlarge/Reduce",
                "Flaming Sphere",
                "Gust of Wind",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Levitate",
                "Locate Object",
                "Magic Mouth",
                "Magic Weapon",
                "Melf's Acid Arrow",
                "Mirror Image",
                "Misty Step",
                "Nystul's Magic Aura",
                "Phantasmal Force",
                "Ray of Enfeeblement",
                "Rope Trick",
                "Scorching Ray",
                "See Invisibility",
                "Shadow Blade",
                "Shatter",
                "Spider Climb",
                "Suggestion",
                "Warding Wind",
                "Web",

                # Level 3
                "Animate Dead",
                "Bestow Curse",
                "Blink",
                "Counterspell",
                "Dispel Magic",
                "Enemies Abound",
                "Erupting Earth",
                "Fear",
                "Fireball",
                "Flame Arrows",
                "Fly",
                "Gaseous Form",
                "Glyph of Warding",
                "Haste",
                "Hypnotic Pattern",
                "Leomund's Tiny Hut",
                "Lightning Bolt",
                "Major Image",
                "Nondetection",
                "Phantom Steed",
                "Protection from Energy",
                "Remove Curse",
                "Sending",
                "Sleet Storm",
                "Slow",
                "Stinking Cloud",
                "Tidal Wave",
                "Tongues",
                "Vampiric Touch",
                "Wall of Water",
                "Water Breathing",
                "Water Walk",

                # Level 4
                "Arcane Eye",
                "Banishment",
                "Blight",
                "Charm Monster",
                "Confusion",
                "Conjure Minor Elementals",
                "Control Water",
                "Dimension Door",
                "Divination",
                "Dominate Beast",
                "Evard's Black Tentacles",
                "Fabricate",
                "Faithful Hound",
                "Fire Shield",
                "Greater Invisibility",
                "Hallucinatory Terrain",
                "Ice Storm",
                "Leomund's Secret Chest",
                "Locate Creature",
                "Mordenkainen's Private Sanctum",
                "Phantasmal Killer",
                "Polymorph",
                "Resilient Sphere",
                "Sickening Radiance",
                "Stone Shape",
                "Stoneskin",
                "Wall of Fire",

                # Level 5
                "Animate Objects",
                "Bigby's Hand",
                "Cloudkill",
                "Cone of Cold",
                "Conjure Elemental",
                "Contact Other Plane",
                "Control Winds",
                "Creation",
                "Danse Macabre",
                "Dominate Person",
                "Dream",
                "Enervation",
                "Far Step",
                "Geas",
                "Hold Monster",
                "Immolation",
                "Legend Lore",
                "Mislead",
                "Modify Memory",
                "Negative Energy Flood",
                "Passwall",
                "Rary's Telepathic Bond",
                "Scrying",
                "Seeming",
                "Steel Wind Strike",
                "Synaptic Static",
                "Telekinesis",
                "Teleportation Circle",
                "Wall of Force",
                "Wall of Stone",

                # Level 6
                "Arcane Gate",
                "Chain Lightning",
                "Circle of Death",
                "Contingency",
                "Create Undead",
                "Disintegrate",
                "Eyebite",
                "Flesh to Stone",
                "Globe of Invulnerability",
                "Guards and Wards",
                "Magic Jar",
                "Mass Suggestion",
                "Move Earth",
                "Otiluke's Freezing Sphere",
                "Programmed Illusion",
                "Scatter",
                "Sunbeam",
                "True Seeing",
                "Wall of Ice",

                # Level 7
                "Delayed Blast Fireball",
                "Etherealness",
                "Finger of Death",
                "Forcecage",
                "Mirage Arcane",
                "Mordenkainen's Magnificent Mansion",
                "Plane Shift",
                "Power Word Pain",
                "Prismatic Spray",
                "Project Image",
                "Reverse Gravity",
                "Sequester",
                "Simulacrum",
                "Symbol",
                "Teleport",

                # Level 8
                "Antimagic Field",
                "Clone",
                "Control Weather",
                "Demiplane",
                "Dominate Monster",
                "Feeblemind",
                "Incendiary Cloud",
                "Maze",
                "Mind Blank",
                "Power Word Stun",
                "Sunburst",
                "Telepathy",

                # Level 9
                "Astral Projection",
                "Foresight",
                "Gate",
                "Imprisonment",
                "Mass Polymorph",
                "Meteor Swarm",
                "Power Word Kill",
                "Prismatic Wall",
                "Shapechange",
                "Time Stop",
                "True Polymorph",
                "Weird",
                "Wish"
            ],
            "Sorcerer": [
                # Level 0 (Cantrips)
                "Acid Splash",
                "Blade Ward",
                "Booming Blade",
                "Chill Touch",
                "Control Flames",
                "Create Bonfire",
                "Dancing Lights",
                "Fire Bolt",
                "Friends",
                "Frostbite",
                "Green-Flame Blade",
                "Gust",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Minor Illusion",
                "Mold Earth",
                "Poison Spray",
                "Prestidigitation",
                "Ray of Frost",
                "Shape Water",
                "Shocking Grasp",
                "Sword Burst",
                "Thunderclap",
                "Toll the Dead",
                "True Strike",

                # Level 1
                "Burning Hands",
                "Charm Person",
                "Chromatic Orb",
                "Color Spray",
                "Comprehend Languages",
                "Detect Magic",
                "Disguise Self",
                "Expeditious Retreat",
                "False Life",
                "Feather Fall",
                "Fog Cloud",
                "Jump",
                "Mage Armor",
                "Magic Missile",
                "Ray of Sickness",
                "Shield",
                "Silent Image",
                "Sleep",
                "Thunderwave",
                "Witch Bolt",

                # Level 2
                "Alter Self",
                "Blindness/Deafness",
                "Blur",
                "Crown of Madness",
                "Darkness",
                "Detect Thoughts",
                "Enhance Ability",
                "Enlarge/Reduce",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Levitate",
                "Mirror Image",
                "Misty Step",
                "Phantasmal Force",
                "Scorching Ray",
                "See Invisibility",
                "Shatter",
                "Spider Climb",
                "Suggestion",
                "Warding Wind",
                "Web",

                # Level 3
                "Animate Dead",
                "Bestow Curse",
                "Blink",
                "Counterspell",
                "Daylight",
                "Dispel Magic",
                "Fear",
                "Fireball",
                "Fly",
                "Gaseous Form",
                "Haste",
                "Hypnotic Pattern",
                "Lightning Bolt",
                "Major Image",
                "Protection from Energy",
                "Sleet Storm",
                "Slow",
                "Stinking Cloud",
                "Tongues",
                "Vampiric Touch",
                "Water Breathing",

                # Level 4
                "Banishment",
                "Blight",
                "Confusion",
                "Dimension Door",
                "Dominate Beast",
                "Greater Invisibility",
                "Ice Storm",
                "Polymorph",
                "Stoneskin",
                "Wall of Fire",

                # Level 5
                "Cloudkill",
                "Cone of Cold",
                "Creation",
                "Dominate Person",
                "Hold Monster",
                "Seeming",
                "Teleportation Circle",
                "Wall of Stone",

                # Level 6
                "Arcane Gate",
                "Chain Lightning",
                "Circle of Death",
                "Disintegrate",
                "Eyebite",
                "Globe of Invulnerability",
                "Mass Suggestion",
                "Move Earth",
                "Sunbeam",
                "True Seeing",

                # Level 7
                "Delayed Blast Fireball",
                "Etherealness",
                "Finger of Death",
                "Plane Shift",
                "Reverse Gravity",
                "Teleport",

                # Level 8
                "Dominate Monster",
                "Earthquake",
                "Incendiary Cloud",
                "Power Word Stun",
                "Sunburst",

                # Level 9
                "Gate",
                "Meteor Swarm",
                "Power Word Kill",
                "Time Stop",
                "Wish"
            ],
                "Cleric": [
                # Level 0 (Cantrips)
                "Guidance",
                "Light",
                "Mending",
                "Resistance",
                "Sacred Flame",
                "Spare the Dying",
                "Thaumaturgy",
                "Toll the Dead",
                "Word of Radiance",

                # Level 1
                "Bane",
                "Bless",
                "Command",
                "Create or Destroy Water",
                "Cure Wounds",
                "Detect Evil and Good",
                "Detect Magic",
                "Detect Poison and Disease",
                "Guiding Bolt",
                "Healing Word",
                "Inflict Wounds",
                "Protection from Evil and Good",
                "Purify Food and Drink",
                "Sanctuary",
                "Shield of Faith",

                # Level 2
                "Aid",
                "Augury",
                "Blindness/Deafness",
                "Calm Emotions",
                "Continual Flame",
                "Enhance Ability",
                "Find Traps",
                "Gentle Repose",
                "Hold Person",
                "Lesser Restoration",
                "Locate Object",
                "Prayer of Healing",
                "Protection from Poison",
                "Silence",
                "Spiritual Weapon",
                "Warding Bond",
                "Zone of Truth",

                # Level 3
                "Animate Dead",
                "Beacon of Hope",
                "Bestow Curse",
                "Create Food and Water",
                "Daylight",
                "Dispel Magic",
                "Feign Death",
                "Glyph of Warding",
                "Magic Circle",
                "Mass Healing Word",
                "Meld into Stone",
                "Protection from Energy",
                "Remove Curse",
                "Revivify",
                "Sending",
                "Speak with Dead",
                "Spirit Guardians",
                "Tongues",
                "Water Walk",

                # Level 4
                "Banishment",
                "Control Water",
                "Death Ward",
                "Divination",
                "Freedom of Movement",
                "Guardian of Faith",
                "Locate Creature",
                "Stone Shape",

                # Level 5
                "Commune",
                "Contagion",
                "Dispel Evil and Good",
                "Flame Strike",
                "Geas",
                "Greater Restoration",
                "Hallow",
                "Insect Plague",
                "Legend Lore",
                "Mass Cure Wounds",
                "Planar Binding",
                "Raise Dead",
                "Scrying",

                # Level 6
                "Blade Barrier",
                "Find the Path",
                "Forbiddance",
                "Harm",
                "Heal",
                "Heroes' Feast",
                "Word of Recall",

                # Level 7
                "Divine Word",
                "Etherealness",
                "Fire Storm",
                "Plane Shift",
                "Regenerate",
                "Resurrection",
                "Symbol",

                # Level 8
                "Antimagic Field",
                "Control Weather",
                "Earthquake",
                "Holy Aura",

                # Level 9
                "Astral Projection",
                "Gate",
                "Mass Heal",
                "True Resurrection"
            ],
                "Bard": [
                # Level 0 (Cantrips)
                "Blade Ward",
                "Dancing Lights",
                "Friends",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Minor Illusion",
                "Prestidigitation",
                "Thunderclap",
                "True Strike",
                "Vicious Mockery",

                # Level 1
                "Animal Friendship",
                "Bane",
                "Charm Person",
                "Comprehend Languages",
                "Cure Wounds",
                "Detect Magic",
                "Disguise Self",
                "Dissonant Whispers",
                "Faerie Fire",
                "Feather Fall",
                "Healing Word",
                "Heroism",
                "Identify",
                "Illusory Script",
                "Longstrider",
                "Silent Image",
                "Sleep",
                "Speak with Animals",
                "Tasha's Hideous Laughter",
                "Thunderwave",
                "Unseen Servant",

                # Level 2
                "Animal Messenger",
                "Blindness/Deafness",
                "Calm Emotions",
                "Cloud of Daggers",
                "Crown of Madness",
                "Detect Thoughts",
                "Enhance Ability",
                "Enthrall",
                "Heat Metal",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Lesser Restoration",
                "Locate Animals or Plants",
                "Locate Object",
                "Magic Mouth",
                "Mirror Image",
                "Misty Step",
                "Phantasmal Force",
                "See Invisibility",
                "Shatter",
                "Silence",
                "Suggestion",
                "Warding Wind",
                "Zone of Truth",

                # Level 3
                "Bestow Curse",
                "Clairvoyance",
                "Dispel Magic",
                "Fear",
                "Feign Death",
                "Glyph of Warding",
                "Hypnotic Pattern",
                "Leomund's Tiny Hut",
                "Major Image",
                "Nondetection",
                "Plant Growth",
                "Sending",
                "Speak with Dead",
                "Speak with Plants",
                "Stinking Cloud",
                "Tongues",

                # Level 4
                "Compulsion",
                "Confusion",
                "Dimension Door",
                "Freedom of Movement",
                "Greater Invisibility",
                "Hallucinatory Terrain",
                "Locate Creature",
                "Phantasmal Killer",
                "Polymorph",

                # Level 5
                "Animate Objects",
                "Awaken",
                "Dominate Person",
                "Dream",
                "Geas",
                "Greater Restoration",
                "Hold Monster",
                "Legend Lore",
                "Mass Cure Wounds",
                "Mislead",
                "Modify Memory",
                "Planar Binding",
                "Raise Dead",
                "Seeming",
                "Scrying",
                "Teleportation Circle",

                # Level 6
                "Eyebite",
                "Find the Path",
                "Guards and Wards",
                "Mass Suggestion",
                "Otto's Irresistible Dance",
                "Programmed Illusion",
                "True Seeing",

                # Level 7
                "Etherealness",
                "Forcecage",
                "Mirage Arcane",
                "Mordenkainen's Magnificent Mansion",
                "Plane Shift",
                "Project Image",
                "Regenerate",
                "Resurrection",
                "Symbol",
                "Teleport",

                # Level 8
                "Dominate Monster",
                "Feeblemind",
                "Glibness",
                "Mind Blank",
                "Power Word Stun",

                # Level 9
                "Foresight",
                "Power Word Heal",
                "Power Word Kill",
                "True Polymorph"
            ],
            "Paladin": [
                # Level 1
                "Bless",
                "Command",
                "Compelled Duel",
                "Cure Wounds",
                "Detect Evil and Good",
                "Detect Magic",
                "Detect Poison and Disease",
                "Divine Favor",
                "Heroism",
                "Protection from Evil and Good",
                "Purify Food and Drink",
                "Searing Smite",
                "Shield of Faith",
                "Thunderous Smite",
                "Wrathful Smite",

                # Level 2
                "Aid",
                "Branding Smite",
                "Find Steed",
                "Lesser Restoration",
                "Locate Object",
                "Magic Weapon",
                "Protection from Poison",
                "Zone of Truth",

                # Level 3
                "Aura of Vitality",
                "Blinding Smite",
                "Create Food and Water",
                "Crusader's Mantle",
                "Daylight",
                "Dispel Magic",
                "Elemental Weapon",
                "Magic Circle",
                "Remove Curse",
                "Revivify",

                # Level 4
                "Aura of Life",
                "Aura of Purity",
                "Banishment",
                "Death Ward",
                "Locate Creature",
                "Staggering Smite",

                # Level 5
                "Banishing Smite",
                "Circle of Power",
                "Destructive Wave",
                "Dispel Evil and Good",
                "Geas",
                "Raise Dead"
            ],
            "Ranger": [
                # Level 1
                "Alarm",
                "Animal Friendship",
                "Cure Wounds",
                "Detect Magic",
                "Detect Poison and Disease",
                "Ensnaring Strike",
                "Fog Cloud",
                "Goodberry",
                "Hail of Thorns",
                "Hunter's Mark",
                "Jump",
                "Longstrider",
                "Speak with Animals",

                # Level 2
                "Animal Messenger",
                "Barkskin",
                "Beast Sense",
                "Cordon of Arrows",
                "Darkvision",
                "Find Traps",
                "Lesser Restoration",
                "Locate Animals or Plants",
                "Locate Object",
                "Pass without Trace",
                "Protection from Poison",
                "Silence",
                "Spike Growth",

                # Level 3
                "Conjure Animals",
                "Conjure Barrage",
                "Daylight",
                "Lightning Arrow",
                "Meld into Stone",
                "Nondetection",
                "Plant Growth",
                "Protection from Energy",
                "Speak with Plants",
                "Water Breathing",
                "Water Walk",
                "Wind Wall",

                # Level 4
                "Conjure Woodland Beings",
                "Divination",
                "Freedom of Movement",
                "Grasping Vine",
                "Locate Creature",
                "Stoneskin",

                # Level 5
                "Commune with Nature",
                "Conjure Volley",
                "Swift Quiver",
                "Tree Stride"
            ],
            # (Eldritch Knight)
            "Fighter": [
                # Level 0 (Cantrips)
                "Blade Ward",
                "Booming Blade",
                "Chill Touch",
                "Fire Bolt",
                "Green-Flame Blade",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Minor Illusion",
                "Prestidigitation",
                "Ray of Frost",
                "Shocking Grasp",
                "Sword Burst",
                "True Strike",

                # Level 1
                "Absorb Elements",
                "Burning Hands",
                "Charm Person",
                "Chromatic Orb",
                "Color Spray",
                "Comprehend Languages",
                "Detect Magic",
                "Expeditious Retreat",
                "False Life",
                "Feather Fall",
                "Mage Armor",
                "Magic Missile",
                "Ray of Sickness",
                "Shield",
                "Silent Image",
                "Sleep",
                "Thunderwave",
                "Witch Bolt",

                # Level 2
                "Alter Self",
                "Blur",
                "Darkness",
                "Detect Thoughts",
                "Enhance Ability",
                "Enlarge/Reduce",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Levitate",
                "Magic Weapon",
                "Misty Step",
                "Mirror Image",
                "Scorching Ray",
                "See Invisibility",
                "Shadow Blade",
                "Shatter",
                "Spider Climb",
                "Suggestion",
                "Web",

                # Level 3
                "Blink",
                "Counterspell",
                "Dispel Magic",
                "Fear",
                "Fireball",
                "Fly",
                "Gaseous Form",
                "Haste",
                "Hypnotic Pattern",
                "Lightning Bolt",
                "Major Image",
                "Protection from Energy",
                "Sleet Storm",
                "Slow",
                "Stinking Cloud",
                "Tongues",
                "Vampiric Touch",
                "Water Breathing",

                # Level 4
                "Banishment",
                "Blight",
                "Confusion",
                "Dimension Door",
                "Greater Invisibility",
                "Ice Storm",
                "Polymorph",
                "Stoneskin",
                "Wall of Fire"
            ],
             "Warlock": [
                # Level 0 (Cantrips)
                "Blade Ward",
                "Booming Blade",
                "Chill Touch",
                "Create Bonfire",
                "Eldritch Blast",
                "Frostbite",
                "Green-Flame Blade",
                "Mage Hand",
                "Magic Stone",
                "Minor Illusion",
                "Poison Spray",
                "Prestidigitation",
                "Sword Burst",
                "Thunderclap",
                "Toll the Dead",
                "True Strike",

                # Level 1
                "Armor of Agathys",
                "Arms of Hadar",
                "Burning Hands",
                "Charm Person",
                "Comprehend Languages",
                "Expeditious Retreat",
                "Hellish Rebuke",
                "Hex",
                "Mage Armor",
                "Protection from Evil and Good",
                "Unseen Servant",
                "Witch Bolt",

                # Level 2
                "Cloud of Daggers",
                "Crown of Madness",
                "Darkness",
                "Enthrall",
                "Hold Person",
                "Invisibility",
                "Misty Step",
                "Mirror Image",
                "Phantasmal Force",
                "Ray of Enfeeblement",
                "Scorching Ray",
                "Shatter",
                "Spider Climb",
                "Suggestion",

                # Level 3
                "Bestow Curse",
                "Blink",
                "Counterspell",
                "Dispel Magic",
                "Enemies Abound",
                "Fear",
                "Fireball",
                "Fly",
                "Gaseous Form",
                "Hunger of Hadar",
                "Hypnotic Pattern",
                "Magic Circle",
                "Major Image",
                "Remove Curse",
                "Sending",
                "Stinking Cloud",
                "Vampiric Touch",

                # Level 4
                "Banishment",
                "Blight",
                "Dimension Door",
                "Elemental Bane",
                "Greater Invisibility",
                "Phantasmal Killer",
                "Sickening Radiance",

                # Level 5
                "Cloudkill",
                "Contact Other Plane",
                "Enervation",
                "Far Step",
                "Hold Monster",
                "Negative Energy Flood",
                "Scrying",
                "Synaptic Static",
                "Wall of Light",

                # Level 6
                "Arcane Gate",
                "Circle of Death",
                "Conjure Fey",
                "Create Undead",
                "Eyebite",
                "Flesh to Stone",
                "Mass Suggestion",
                "Scatter",
                "True Seeing",

                # Level 7
                "Etherealness",
                "Finger of Death",
                "Forcecage",
                "Plane Shift",

                # Level 8
                "Demiplane",
                "Dominate Monster",
                "Feeblemind",
                "Glibness",
                "Power Word Stun",

                # Level 9
                "Astral Projection",
                "Foresight",
                "Imprisonment",
                "Power Word Kill",
                "True Polymorph"
            ],
            #  (Arcane Trickster)
            "Rogue": [
                # Level 0 (Cantrips)
                "Blade Ward",
                "Booming Blade",
                "Chill Touch",
                "Green-Flame Blade",
                "Mage Hand",
                "Message",
                "Minor Illusion",
                "Prestidigitation",
                "Ray of Frost",
                "Shocking Grasp",
                "True Strike",

                # Level 1
                "Charm Person",
                "Color Spray",
                "Disguise Self",
                "Feather Fall",
                "Mage Armor",
                "Magic Missile",
                "Shield",
                "Silent Image",
                "Sleep",
                "Tasha's Hideous Laughter",
                "Thunderwave",

                # Level 2
                "Blur",
                "Darkness",
                "Detect Thoughts",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Levitate",
                "Mirror Image",
                "Misty Step",
                "Phantasmal Force",
                "Shadow Blade",
                "Spider Climb",
                "Suggestion",
                "Web",

                # Level 3
                "Blink",
                "Counterspell",
                "Dispel Magic",
                "Fear",
                "Fly",
                "Gaseous Form",
                "Haste",
                "Hypnotic Pattern",
                "Lightning Bolt",
                "Major Image",
                "Slow",
                "Vampiric Touch",

                # Level 4
                "Arcane Eye",
                "Greater Invisibility",
                "Phantasmal Killer",
                "Stoneskin"
            ]
        },
        "Pathfinder": {
            "Wizard": [
                # Level 0 (Cantrips)
                "Acid Splash",
                "Arcane Mark",
                "Bleed",
                "Dancing Lights",
                "Daze",
                "Detect Magic",
                "Detect Poison",
                "Disrupt Undead",
                "Flare",
                "Ghost Sound",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Open/Close",
                "Prestidigitation",
                "Ray of Frost",
                "Read Magic",
                "Resistance",
                "Touch of Fatigue",

                # Level 1
                "Alarm",
                "Animate Rope",
                "Burning Hands",
                "Cause Fear",
                "Charm Person",
                "Chill Touch",
                "Color Spray",
                "Comprehend Languages",
                "Detect Secret Doors",
                "Detect Undead",
                "Disguise Self",
                "Endure Elements",
                "Enlarge Person",
                "Erase",
                "Expeditious Retreat",
                "Feather Fall",
                "Floating Disk",
                "Grease",
                "Hold Portal",
                "Hypnotism",
                "Identify",
                "Jump",
                "Mage Armor",
                "Magic Aura",
                "Magic Missile",
                "Magic Weapon",
                "Mount",
                "Obscuring Mist",
                "Protection from Chaos",
                "Protection from Evil",
                "Protection from Good",
                "Protection from Law",
                "Ray of Enfeeblement",
                "Reduce Person",
                "Shield",
                "Shocking Grasp",
                "Silent Image",
                "Sleep",
                "Summon Monster I",
                "True Strike",
                "Unseen Servant",
                "Ventriloquism",

                # Level 2
                "Acid Arrow",
                "Alter Self",
                "Arcane Lock",
                "Bear's Endurance",
                "Blindness/Deafness",
                "Blur",
                "Bull's Strength",
                "Cat's Grace",
                "Continual Flame",
                "Darkness",
                "Darkvision",
                "Daze Monster",
                "Detect Thoughts",
                "Disguise Self",
                "Eagle's Splendor",
                "False Life",
                "Flaming Sphere",
                "Fog Cloud",
                "Fox's Cunning",
                "Gentle Repose",
                "Ghoul Touch",
                "Glitterdust",
                "Gust of Wind",
                "Hideous Laughter",
                "Hypnotic Pattern",
                "Invisibility",
                "Knock",
                "Levitate",
                "Location Object",
                "Magic Mouth",
                "Mirror Image",
                "Misdirection",
                "Owl's Wisdom",
                "Phantom Trap",
                "Protection from Arrows",
                "Pyrotechnics",
                "Resist Energy",
                "Rope Trick",
                "Scorching Ray",
                "See Invisibility",
                "Shatter",
                "Spider Climb",
                "Summon Monster II",
                "Summon Swarm",
                "Touch of Idiocy",
                "Web",
                "Whispering Wind",

                "Animate Dead",
                "Arcane Sight",
                "Beast Shape I",
                "Blink",
                "Clairaudience/Clairvoyance",
                "Daylight",
                "Deep Slumber",
                "Dispel Magic",
                "Displacement",
                "Explosive Runes",
                "Fireball",
                "Flame Arrow",
                "Fly",
                "Gaseous Form",
                "Gentle Repose",
                "Halt Undead",
                "Haste",
                "Heroism",
                "Hold Person",
                "Illusory Script",
                "Invisibility Sphere",
                "Lightning Bolt",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Magic Circle against Good",
                "Magic Circle against Law",
                "Magic Weapon, Greater",
                "Major Image",
                "Nondetection",
                "Phantom Steed",
                "Protection from Energy",
                "Rage",
                "Ray of Exhaustion",
                "Secret Page",
                "Sepia Snake Sigil",
                "Shrink Item",
                "Sleet Storm",
                "Slow",
                "Stinking Cloud",
                "Suggestion",
                "Summon Monster III",
                "Tiny Hut",
                "Tongues",
                "Vampiric Touch",
                "Water Breathing",
                "Wind Wall",

                # Level 4
                "Animate Dead",
                "Arcane Eye",
                "Beast Shape II",
                "Bestow Curse",
                "Black Tentacles",
                "Charm Monster",
                "Confusion",
                "Contagion",
                "Crushing Despair",
                "Dimension Door",
                "Dimensional Anchor",
                "Elemental Body I",
                "Enervation",
                "Enlarge Person, Mass",
                "Fear",
                "Fire Shield",
                "Fire Trap",
                "Fur Armor, Greater",
                "Geas, Lesser",
                "Globe of Invulnerability, Lesser",
                "Hallucinatory Terrain",
                "Ice Storm",
                "Illusory Wall",
                "Invisibility, Greater",
                "Locate Creature",
                "Minor Creation",
                "Modify Memory",
                "Neutralize Poison",
                "Phantasmal Killer",
                "Polymorph",
                "Rainbow Pattern",
                "Reduce Person, Mass",
                "Remove Curse",
                "Resilient Sphere",
                "Scrying",
                "Secure Shelter",
                "Shadow Conjuration",
                "Solid Fog",
                "Stone Shape",
                "Stoneskin",
                "Summon Monster IV",
                "Wall of Fire",
                "Wall of Ice",

                # Level 5
                "Acid Arrow, Greater",
                "Animal Growth",
                "Baleful Polymorph",
                "Beast Shape III",
                "Break Enchantment",
                "Cloudkill",
                "Cone of Cold",
                "Contact Other Plane",
                "Dismissal",
                "Dominate Person",
                "Dream",
                "Elemental Body II",
                "Fabricate",
                "False Vision",
                "Feeblemind",
                "Hold Monster",
                "Interposing Hand",
                "Magic Jar",
                "Major Creation",
                "Mind Fog",
                "Mirage Arcana",
                "Mage's Faithful Hound",
                "Mage's Private Sanctum",
                "Nightmare",
                "Overland Flight",
                "Passwall",
                "Permanency",
                "Persistent Image",
                "Planar Binding, Lesser",
                "Plant Shape I",
                "Polymorph, Greater",
                "Secret Chest",
                "Shadow Evocation",
                "Summon Monster V",
                "Telekinesis",
                "Teleport",
                "Transmute Mud to Rock",
                "Transmute Rock to Mud",
                "Wall of Force",
                "Wall of Stone",
                "Waves of Fatigue",

                # Level 6
                "Acid Fog",
                "Analyze Dweomer",
                "Antimagic Field",
                "Beast Shape IV",
                "Bear's Endurance, Mass",
                "Bull's Strength, Mass",
                "Cat's Grace, Mass",
                "Chain Lightning",
                "Circle of Death",
                "Contingency",
                "Control Water",
                "Create Undead",
                "Disintegrate",
                "Dispel Magic, Greater",
                "Eagle's Splendor, Mass",
                "Elemental Body III",
                "Eyebite",
                "Flesh to Stone",
                "Fox's Cunning, Mass",
                "Freezing Sphere",
                "Geas/Quest",
                "Globe of Invulnerability",
                "Guards and Wards",
                "Heroism, Greater",
                "Legend Lore",
                "Mislead",
                "Move Earth",
                "Owl's Wisdom, Mass",
                "Permanent Image",
                "Planar Binding",
                "Plant Shape II",
                "Programmed Image",
                "Repulsion",
                "Shadow Walk",
                "Stone to Flesh",
                "Suggestion, Mass",
                "Summon Monster VI",
                "Symbol of Fear",
                "Symbol of Persuasion",
                "Transformation",
                "True Seeing",
                "Veil",
                "Wall of Iron",

                # Level 7
                "Arcane Sight, Greater",
                "Banishment",
                "Control Undead",
                "Control Weather",
                "Delayed Blast Fireball",
                "Elemental Body IV",
                "Ethereal Jaunt",
                "Finger of Death",
                "Fire Storm",
                "Forcecage",
                "Form of the Dragon I",
                "Hold Person, Mass",
                "Insanity",
                "Instant Summons",
                "Invisible Companion, Greater",
                "Limited Wish",
                "Mage's Magnificent Mansion",
                "Mage's Sword",
                "Phase Door",
                "Plant Shape III",
                "Plane Shift",
                "Power Word Blind",
                "Prismatic Spray",
                "Project Image",
                "Reverse Gravity",
                "Scrying, Greater",
                "Sequester",
                "Shadow Conjuration, Greater",
                "Simulacrum",
                "Spell Turning",
                "Summon Monster VII",
                "Symbol of Stunning",
                "Symbol of Weakness",
                "Teleport, Greater",
                "Vision",
                "Waves of Exhaustion",

                # Level 8
                "Antipathy",
                "Binding",
                "Charm Monster, Mass",
                "Clone",
                "Create Greater Undead",
                "Demand",
                "Dimensional Lock",
                "Discern Location",
                "Form of the Dragon II",
                "Horrid Wilting",
                "Incendiary Cloud",
                "Iron Body",
                "Maze",
                "Mind Blank",
                "Planar Binding, Greater",
                "Polar Ray",
                "Polymorph Any Object",
                "Power Word Stun",
                "Prismatic Wall",
                "Protection from Spells",
                "Scintillating Pattern",
                "Screen",
                "Shadow Evocation, Greater",
                "Summon Monster VIII",
                "Symbol of Death",
                "Symbol of Insanity",
                "Sympathy",
                "Telekinetic Sphere",
                "Temporal Stasis",
                "Trap the Soul",

                # Level 9
                "Astral Projection",
                "Crushing Hand",
                "Dominate Monster",
                "Energy Drain",
                "Etherealness",
                "Foresight",
                "Form of the Dragon III",
                "Freedom",
                "Gate",
                "Hold Monster, Mass",
                "Imprisonment",
                "Meteor Swarm",
                "Mage's Disjunction",
                "Power Word Kill",
                "Prismatic Sphere",
                "Refuge",
                "Shades",
                "Shapechange",
                "Soul Bind",
                "Summon Monster IX",
                "Teleportation Circle",
                "Time Stop",
                "Wail of the Banshee",
                "Weird",
                "Wish"
            ],
            
            "Cleric": [
                # Level 0 (cantrips)
                "Bleed",
                "Create Water",
                "Detect Magic",
                "Detect Poison",
                "Guidance",
                "Light",
                "Mending",
                "Purify Food and Drink",
                "Read Magic",
                "Resistance",
                "Spark",
                "Stabilize",
                "Virtue",

                # Level 1
                "Abundant Ammunition",
                "Air Bubble",
                "Bane",
                "Bless",
                "Bless Water",
                "Cause Fear",
                "Command",
                "Comprehend Languages",
                "Cure Light Wounds",
                "Curse Water",
                "Deathwatch",
                "Detect Chaos",
                "Detect Evil",
                "Detect Good",
                "Detect Law",
                "Detect Undead",
                "Divine Favor",
                "Doom",
                "Endure Elements",
                "Entropic Shield",
                "Hide from Undead",
                "Inflict Light Wounds",
                "Magic Stone",
                "Magic Weapon",
                "Obscuring Mist",
                "Protection from Chaos",
                "Protection from Evil",
                "Protection from Good",
                "Protection from Law",
                "Remove Fear",
                "Sanctuary",
                "Shield of Faith",
                "Summon Monster I",

                # Level 2
                "Aid",
                "Align Weapon",
                "Animal Messenger",
                "Augury",
                "Bear's Endurance",
                "Bull's Strength",
                "Calm Emotions",
                "Consecrate",
                "Cure Moderate Wounds",
                "Darkness",
                "Death Knell",
                "Delay Poison",
                "Desecrate",
                "Eagle's Splendor",
                "Enthrall",
                "Find Traps",
                "Gentle Repose",
                "Hold Person",
                "Inflict Moderate Wounds",
                "Make Whole",
                "Owl's Wisdom",
                "Remove Paralysis",
                "Resist Energy",
                "Restoration, Lesser",
                "Shatter",
                "Shield Other",
                "Silence",
                "Sound Burst",
                "Spiritual Weapon",
                "Status",
                "Summon Monster II",
                "Undetectable Alignment",
                "Zone of Truth",

                # Level 3
                "Animate Dead",
                "Bestow Curse",
                "Blindness/Deafness",
                "Contagion",
                "Continual Flame",
                "Create Food and Water",
                "Cure Serious Wounds",
                "Daylight",
                "Deeper Darkness",
                "Dispel Magic",
                "Glyph of Warding",
                "Helping Hand",
                "Inflict Serious Wounds",
                "Invisibility Purge",
                "Locate Object",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Magic Circle against Good",
                "Magic Circle against Law",
                "Magic Vestment",
                "Meld into Stone",
                "Obscure Object",
                "Prayer",
                "Protection from Energy",
                "Remove Blindness/Deafness",
                "Remove Curse",
                "Remove Disease",
                "Searing Light",
                "Speak with Dead",
                "Stone Shape",
                "Summon Monster III",
                "Water Breathing",
                "Water Walk",
                "Wind Wall",

                # Level 4
                "Air Walk",
                "Blessing of Fervor",
                "Chaos Hammer",
                "Control Water",
                "Cure Critical Wounds",
                "Death Ward",
                "Dimensional Anchor",
                "Discern Lies",
                "Dismissal",
                "Divination",
                "Divine Power",
                "Freedom of Movement",
                "Giant Vermin",
                "Holy Smite",
                "Imbue with Spell Ability",
                "Inflict Critical Wounds",
                "Magic Weapon, Greater",
                "Neutralize Poison",
                "Order's Wrath",
                "Planar Ally, Lesser",
                "Poison",
                "Repel Vermin",
                "Restoration",
                "Sending",
                "Spell Immunity",
                "Summon Monster IV",
                "Tongues",
                "Unholy Blight",

                # Level 5
                "Atonement",
                "Break Enchantment",
                "Breath of Life",
                "Command, Greater",
                "Commune",
                "Cure Light Wounds, Mass",
                "Dispel Chaos",
                "Dispel Evil",
                "Dispel Good",
                "Dispel Law",
                "Disrupting Weapon",
                "Flame Strike",
                "Hallow",
                "Inflict Light Wounds, Mass",
                "Insect Plague",
                "Mark of Justice",
                "Plane Shift",
                "Raise Dead",
                "Righteous Might",
                "Scrying",
                "Slay Living",
                "Spell Resistance",
                "Summon Monster V",
                "Symbol of Pain",
                "Symbol of Sleep",
                "True Seeing",
                "Unhallow",
                "Wall of Stone",

                # Level 6
                "Animate Objects",
                "Antilife Shell",
                "Banishment",
                "Bear's Endurance, Mass",
                "Blade Barrier",
                "Bull's Strength, Mass",
                "Create Undead",
                "Cure Moderate Wounds, Mass",
                "Dispel Magic, Greater",
                "Eagle's Splendor, Mass",
                "Find the Path",
                "Forbiddance",
                "Geas/Quest",
                "Glyph of Warding, Greater",
                "Harm",
                "Heal",
                "Heroes' Feast",
                "Inflict Moderate Wounds, Mass",
                "Owl's Wisdom, Mass",
                "Planar Ally",
                "Sound Burst, Greater",
                "Spell Immunity, Greater",
                "Summon Monster VI",
                "Symbol of Fear",
                "Symbol of Persuasion",
                "Undeath to Death",
                "Wind Walk",
                "Word of Recall",

                # Level 7
                "Blasphemy",
                "Control Weather",
                "Cure Serious Wounds, Mass",
                "Destruction",
                "Dictum",
                "Ethereal Jaunt",
                "Holy Word",
                "Inflict Serious Wounds, Mass",
                "Refuge",
                "Regenerate",
                "Repulsion",
                "Restoration, Greater",
                "Resurrection",
                "Scrying, Greater",
                "Summon Monster VII",
                "Symbol of Stunning",
                "Symbol of Weakness",
                "Word of Chaos",

                # Level 8
                "Antimagic Field",
                "Cloak of Chaos",
                "Create Greater Undead",
                "Cure Critical Wounds, Mass",
                "Dimensional Lock",
                "Discern Location",
                "Earthquake",
                "Fire Storm",
                "Holy Aura",
                "Inflict Critical Wounds, Mass",
                "Planar Ally, Greater",
                "Shield of Law",
                "Spell Immunity, Greater",
                "Summon Monster VIII",
                "Symbol of Death",
                "Symbol of Insanity",
                "Unholy Aura",

                # Level 9
                "Astral Projection",
                "Energy Drain",
                "Etherealness",
                "Gate",
                "Heal, Mass",
                "Implosion",
                "Miracle",
                "Soul Bind",
                "Storm of Vengeance",
                "Summon Monster IX",
                "True Resurrection"
            ],

            "Druid": [
                # Level 0 (cantrips)
                "Create Water",
                "Detect Magic",
                "Detect Poison",
                "Flare",
                "Guidance",
                "Know Direction",
                "Light",
                "Mending",
                "Purify Food and Drink",
                "Read Magic",
                "Resistance",
                "Stabilize",
                "Virtue",

                # Level 1
                "Alter Winds",
                "Ant Haul",
                "Aspect of the Falcon",
                "Calm Animals",
                "Charm Animal",
                "Cure Light Wounds",
                "Detect Animals or Plants",
                "Detect Snares and Pits",
                "Endure Elements",
                "Entangle",
                "Faerie Fire",
                "Goodberry",
                "Hide from Animals",
                "Jump",
                "Longstrider",
                "Magic Fang",
                "Magic Stone",
                "Obscuring Mist",
                "Pass without Trace",
                "Produce Flame",
                "Shillelagh",
                "Speak with Animals",
                "Summon Minor Ally",
                "Summon Nature's Ally I",

                # Level 2
                "Animal Aspect",
                "Animal Messenger",
                "Animal Trance",
                "Aspect of the Bear",
                "Barkskin",
                "Bear's Endurance",
                "Bull's Strength",
                "Cat's Grace",
                "Chill Metal",
                "Delay Poison",
                "Fire Trap",
                "Flame Blade",
                "Flaming Sphere",
                "Fog Cloud",
                "Gust of Wind",
                "Heat Metal",
                "Hold Animal",
                "Owl's Wisdom",
                "Reduce Animal",
                "Resist Energy",
                "Restoration, Lesser",
                "Soften Earth and Stone",
                "Spider Climb",
                "Summon Nature's Ally II",
                "Tree Shape",
                "Warp Wood",
                "Wood Shape",

                # Level 3
                "Air Walk",
                "Animal Aspect, Greater",
                "Call Lightning",
                "Contagion",
                "Cure Moderate Wounds",
                "Daylight",
                "Diminish Plants",
                "Dominate Animal",
                "Magic Fang, Greater",
                "Meld into Stone",
                "Neutralize Poison",
                "Plant Growth",
                "Poison",
                "Protection from Energy",
                "Quench",
                "Remove Disease",
                "Sleet Storm",
                "Snare",
                "Speak with Plants",
                "Spike Growth",
                "Stone Shape",
                "Summon Nature's Ally III",
                "Water Breathing",
                "Wind Wall",

                # Level 4
                "Air Walk",
                "Antiplant Shell",
                "Arboreal Hammer",
                "Aspect of the Stag",
                "Blight",
                "Command Plants",
                "Control Water",
                "Cure Serious Wounds",
                "Dispel Magic",
                "Flame Strike",
                "Freedom of Movement",
                "Giant Vermin",
                "Grove of Respite",
                "Ice Storm",
                "Reincarnate",
                "Repel Vermin",
                "Rusting Grasp",
                "Scrying",
                "Spike Stones",
                "Summon Nature's Ally IV",
                "Thorn Body",
                "Tree Stride",
                "Vermin Shape I",

                # Level 5
                "Animal Growth",
                "Aspect of the Wolf",
                "Awaken",
                "Baleful Polymorph",
                "Call Lightning Storm",
                "Commune with Nature",
                "Control Winds",
                "Cure Critical Wounds",
                "Death Ward",
                "Hallow",
                "Insect Plague",
                "Life Bubble",
                "Stoneskin",
                "Summon Nature's Ally V",
                "Transmute Mud to Rock",
                "Transmute Rock to Mud",
                "Tree Stride",
                "Unhallow",
                "Wall of Fire",
                "Wall of Thorns",

                # Level 6
                "Antilife Shell",
                "Bear's Endurance, Mass",
                "Bull's Strength, Mass",
                "Cat's Grace, Mass",
                "Cure Light Wounds, Mass",
                "Dispel Magic, Greater",
                "Find the Path",
                "Fire Seeds",
                "Ironwood",
                "Liveoak",
                "Move Earth",
                "Owl's Wisdom, Mass",
                "Plague Storm",
                "Repel Wood",
                "Stone Tell",
                "Summon Nature's Ally VI",
                "Transport via Plants",
                "Wall of Stone",

                # Level 7
                "Animate Plants",
                "Changestaff",
                "Control Weather",
                "Creeping Doom",
                "Cure Moderate Wounds, Mass",
                "Fire Storm",
                "Heal",
                "Rampart",
                "Regenerate",
                "Scrying, Greater",
                "Summon Nature's Ally VII",
                "Sunbeam",
                "Transmute Metal to Wood",
                "True Seeing",
                "Wind Walk",

                # Level 8
                "Animal Shapes",
                "Control Plants",
                "Cure Serious Wounds, Mass",
                "Earthquake",
                "Finger of Death",
                "Repel Metal or Stone",
                "Reverse Gravity",
                "Storm of Vengeance",
                "Summon Nature's Ally VIII",
                "Sunburst",
                "Whirlwind",
                "Word of Recall",

                # Level 9
                "Antipathy",
                "Cure Critical Wounds, Mass",
                "Elemental Swarm",
                "Foresight",
                "Regenerate, Mass",
                "Shambler",
                "Shapechange",
                "Storm of Vengeance",
                "Summon Nature's Ally IX",
                "Sympathy",
                "World Wave"
            ],

            "Sorcerer": [
                # Level 0 (Cantrips)
                "Acid Splash",
                "Arcane Mark",
                "Bleed",
                "Dancing Lights",
                "Daze",
                "Detect Magic",
                "Detect Poison",
                "Disrupt Undead",
                "Flare",
                "Ghost Sound",
                "Light",
                "Mage Hand",
                "Mending",
                "Message",
                "Open/Close",
                "Prestidigitation",
                "Ray of Frost",
                "Read Magic",
                "Resistance",
                "Touch of Fatigue",

                # Level 1
                "Alarm",
                "Animate Rope",
                "Burning Hands",
                "Cause Fear",
                "Charm Person",
                "Chill Touch",
                "Color Spray",
                "Comprehend Languages",
                "Detect Secret Doors",
                "Detect Undead",
                "Disguise Self",
                "Endure Elements",
                "Enlarge Person",
                "Erase",
                "Expeditious Retreat",
                "Feather Fall",
                "Floating Disk",
                "Grease",
                "Hold Portal",
                "Hypnotism",
                "Identify",
                "Jump",
                "Mage Armor",
                "Magic Missile",
                "Magic Weapon",
                "Mount",
                "Obscuring Mist",
                "Protection from Chaos",
                "Protection from Evil",
                "Protection from Good",
                "Protection from Law",
                "Ray of Enfeeblement",
                "Reduce Person",
                "Shield",
                "Shocking Grasp",
                "Silent Image",
                "Sleep",
                "Summon Monster I",
                "True Strike",
                "Unseen Servant",
                "Ventriloquism",

                # Level 2
                "Acid Arrow",
                "Alter Self",
                "Bear's Endurance",
                "Blur",
                "Bull's Strength",
                "Cat's Grace",
                "Continual Flame",
                "Darkness",
                "Darkvision",
                "Daze Monster",
                "Detect Thoughts",
                "Eagle's Splendor",
                "False Life",
                "Fire Breath",
                "Flaming Sphere",
                "Fox's Cunning",
                "Ghoul Touch",
                "Glide",
                "Glitterdust",
                "Gust of Wind",
                "Hideous Laughter",
                "Hypnotic Pattern",
                "Invisibility",
                "Knock",
                "Levitate",
                "Minor Image",
                "Mirror Image",
                "Misdirection",
                "Owl's Wisdom",
                "Protection from Arrows",
                "Pyrotechnics",
                "Resist Energy",
                "Rope Trick",
                "Scorching Ray",
                "See Invisibility",
                "Shatter",
                "Spider Climb",
                "Summon Monster II",
                "Summon Swarm",
                "Touch of Idiocy",
                "Web",
                "Whispering Wind",

                # Level 3
                "Arcane Sight",
                "Beast Shape I",
                "Blink",
                "Clairaudience/Clairvoyance",
                "Deep Slumber",
                "Dispel Magic",
                "Displacement",
                "Fireball",
                "Flame Arrow",
                "Fly",
                "Gaseous Form",
                "Haste",
                "Heroism",
                "Hold Person",
                "Invisibility Sphere",
                "Lightning Bolt",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Magic Circle against Good",
                "Magic Circle against Law",
                "Magic Weapon, Greater",
                "Major Image",
                "Phantom Steed",
                "Protection from Energy",
                "Rage",
                "Ray of Exhaustion",
                "Secret Page",
                "Shrink Item",
                "Slow",
                "Stinking Cloud",
                "Suggestion",
                "Summon Monster III",
                "Tongues",
                "Vampiric Touch",
                "Water Breathing",

                # Level 4
                "Animate Dead",
                "Arcane Eye",
                "Beast Shape II",
                "Bestow Curse",
                "Black Tentacles",
                "Charm Monster",
                "Confusion",
                "Contagion",
                "Crushing Despair",
                "Dimension Door",
                "Dimensional Anchor",
                "Elemental Body I",
                "Enervation",
                "Enlarge Person, Mass",
                "Fear",
                "Fire Shield",
                "Fire Trap",
                "Firefall",
                "Form of the Dragon I",
                "Geas, Lesser",
                "Globe of Invulnerability, Lesser",
                "Hallucinatory Terrain",
                "Ice Storm",
                "Illusory Wall",
                "Invisibility, Greater",
                "Locate Creature",
                "Minor Creation",
                "Modify Memory",
                "Phantasmal Killer",
                "Polymorph",
                "Rainbow Pattern",
                "Reduce Person, Mass",
                "Remove Curse",
                "Resilient Sphere",
                "Scrying",
                "Shadow Conjuration",
                "Shout",
                "Solid Fog",
                "Stone Shape",
                "Stoneskin",
                "Summon Monster IV",
                "Wall of Fire",
                "Wall of Ice",

                # Level 5
                "Animal Growth",
                "Baleful Polymorph",
                "Beast Shape III",
                "Break Enchantment",
                "Cloudkill",
                "Cone of Cold",
                "Contact Other Plane",
                "Dismissal",
                "Dominate Person",
                "Dream",
                "Elemental Body II",
                "Fabricate",
                "Feeblemind",
                "Form of the Dragon II",
                "Hold Monster",
                "Interposing Hand",
                "Magic Jar",
                "Major Creation",
                "Mind Fog",
                "Mirage Arcana",
                "Nightmare",
                "Overland Flight",
                "Passwall",
                "Persistent Image",
                "Planar Binding, Lesser",
                "Plant Shape I",
                "Polymorph, Greater",
                "Secret Chest",
                "Shadow Evocation",
                "Summon Monster V",
                "Telekinesis",
                "Teleport",
                "Transmute Mud to Rock",
                "Transmute Rock to Mud",
                "Wall of Force",
                "Wall of Stone",
                "Waves of Fatigue",

                # Level 6
                "Acid Fog",
                "Analyze Dweomer",
                "Beast Shape IV",
                "Bear's Endurance, Mass",
                "Bull's Strength, Mass",
                "Cat's Grace, Mass",
                "Chain Lightning",
                "Circle of Death",
                "Contingency",
                "Control Water",
                "Create Undead",
                "Disintegrate",
                "Dispel Magic, Greater",
                "Eagle's Splendor, Mass",
                "Elemental Body III",
                "Eyebite",
                "Flesh to Stone",
                "Form of the Dragon III",
                "Fox's Cunning, Mass",
                "Geas/Quest",
                "Globe of Invulnerability",
                "Guards and Wards",
                "Heroism, Greater",
                "Mislead",
                "Move Earth",
                "Owl's Wisdom, Mass",
                "Permanent Image",
                "Planar Binding",
                "Plant Shape II",
                "Programmed Image",
                "Shadow Walk",
                "Stone to Flesh",
                "Suggestion, Mass",
                "Summon Monster VI",
                "Symbol of Fear",
                "Symbol of Persuasion",
                "Transformation",
                "True Seeing",
                "Veil",
                "Wall of Iron",

                # Level 7
                "Arcane Sight, Greater",
                "Banishment",
                "Control Undead",
                "Control Weather",
                "Delayed Blast Fireball",
                "Elemental Body IV",
                "Ethereal Jaunt",
                "Finger of Death",
                "Fire Storm",
                "Fly, Mass",
                "Forcecage",
                "Form of the Dragon III",
                "Hold Person, Mass",
                "Insanity",
                "Instant Summons",
                "Invisibility, Mass",
                "Limited Wish",
                "Mage's Magnificent Mansion",
                "Mage's Sword",
                "Phase Door",
                "Plant Shape III",
                "Plane Shift",
                "Power Word Blind",
                "Prismatic Spray",
                "Project Image",
                "Reverse Gravity",
                "Scrying, Greater",
                "Shadow Conjuration, Greater",
                "Spell Turning",
                "Statue",
                "Summon Monster VII",
                "Symbol of Stunning",
                "Symbol of Weakness",
                "Teleport, Greater",
                "Vision",
                "Waves of Exhaustion",

                # Level 8
                "Antipathy",
                "Binding",
                "Charm Monster, Mass",
                "Clone",
                "Create Greater Undead",
                "Demand",
                "Dimensional Lock",
                "Discern Location",
                "Horrid Wilting",
                "Incendiary Cloud",
                "Iron Body",
                "Maze",
                "Mind Blank",
                "Planar Binding, Greater",
                "Polar Ray",
                "Polymorph Any Object",
                "Power Word Stun",
                "Prismatic Wall",
                "Protection from Spells",
                "Scintillating Pattern",
                "Screen",
                "Shadow Evocation, Greater",
                "Summon Monster VIII",
                "Symbol of Death",
                "Symbol of Insanity",
                "Sympathy",
                "Telekinetic Sphere",
                "Temporal Stasis",
                "Trap the Soul",

                # Level 9
                "Astral Projection",
                "Crushing Hand",
                "Dominate Monster",
                "Energy Drain",
                "Etherealness",
                "Foresight",
                "Freedom",
                "Gate",
                "Hold Monster, Mass",
                "Imprisonment",
                "Meteor Swarm",
                "Mage's Disjunction",
                "Power Word Kill",
                "Prismatic Sphere",
                "Refuge",
                "Shades",
                "Shapechange",
                "Soul Bind",
                "Summon Monster IX",
                "Teleportation Circle",
                "Time Stop",
                "Wail of the Banshee",
                "Weird",
                "Wish"
            ],

            "Bard": [
                # Level 0 (Cantrips)
                "Dancing Lights",
                "Daze",
                "Detect Magic",
                "Flare",
                "Ghost Sound",
                "Know Direction",
                "Light",
                "Lullaby",
                "Mage Hand",
                "Mending",
                "Message",
                "Open/Close",
                "Prestidigitation",
                "Read Magic",
                "Resistance",
                "Summon Instrument",

                # Level 1
                "Alarm",
                "Animate Rope",
                "Cause Fear",
                "Charm Person",
                "Comprehend Languages",
                "Cure Light Wounds",
                "Detect Secret Doors",
                "Disguise Self",
                "Expeditious Retreat",
                "Feather Fall",
                "Grease",
                "Hideous Laughter",
                "Hypnotism",
                "Identify",
                "Magic Mouth",
                "Magic Aura",
                "Obscure Object",
                "Remove Fear",
                "Silent Image",
                "Sleep",
                "Summon Monster I",
                "Undetectable Alignment",
                "Unseen Servant",
                "Ventriloquism",

                # Level 2
                "Alter Self",
                "Animal Messenger",
                "Animal Trance",
                "Blindness/Deafness",
                "Blur",
                "Calm Emotions",
                "Cat's Grace",
                "Cure Moderate Wounds",
                "Darkness",
                "Daze Monster",
                "Delay Poison",
                "Detect Thoughts",
                "Eagle's Splendor",
                "Enthrall",
                "Fox's Cunning",
                "Glitterdust",
                "Heroism",
                "Hold Person",
                "Hypnotic Pattern",
                "Invisibility",
                "Locate Object",
                "Minor Image",
                "Mirror Image",
                "Misdirection",
                "Pyrotechnics",
                "Rage",
                "Scare",
                "Shatter",
                "Silence",
                "Sound Burst",
                "Suggestion",
                "Summon Monster II",
                "Tongues",
                "Whispering Wind",

                # Level 3
                "Blink",
                "Charm Monster",
                "Clairaudience/Clairvoyance",
                "Confusion",
                "Crushing Despair",
                "Cure Serious Wounds",
                "Daylight",
                "Deep Slumber",
                "Dispel Magic",
                "Displacement",
                "Fear",
                "Gaseous Form",
                "Geas, Lesser",
                "Glibness",
                "Good Hope",
                "Haste",
                "Illusory Script",
                "Invisibility Sphere",
                "Major Image",
                "Phantom Steed",
                "Remove Curse",
                "Scrying",
                "Sculpt Sound",
                "Secret Page",
                "See Invisibility",
                "Sepia Snake Sigil",
                "Slow",
                "Speak with Animals",
                "Summon Monster III",
                "Tiny Hut",

                # Level 4
                "Break Enchantment",
                "Cure Critical Wounds",
                "Detect Scrying",
                "Dimension Door",
                "Dominate Person",
                "Freedom of Movement",
                "Hallucinatory Terrain",
                "Hold Monster",
                "Invisibility, Greater",
                "Legend Lore",
                "Locate Creature",
                "Modify Memory",
                "Neutralize Poison",
                "Rainbow Pattern",
                "Repel Vermin",
                "Secure Shelter",
                "Shadow Conjuration",
                "Shout",
                "Speak with Plants",
                "Summon Monster IV",
                "Zone of Silence",

                # Level 5
                "Animate Objects",
                "Cloak of Chaos",
                "Cure Light Wounds, Mass",
                "Dispel Magic, Greater",
                "Dream",
                "False Vision",
                "Heroism, Greater",
                "Mind Fog",
                "Mirage Arcana",
                "Mislead",
                "Nightmare",
                "Persistent Image",
                "Seeming",
                "Shadow Evocation",
                "Shadow Walk",
                "Song of Discord",
                "Suggestion, Mass",
                "Summon Monster V",
                "Symbol of Sleep",
                "Telepathic Bond",

                # Level 6
                "Analyze Dweomer",
                "Animate Objects",
                "Cat's Grace, Mass",
                "Charm Monster, Mass",
                "Cure Moderate Wounds, Mass",
                "Eagle's Splendor, Mass",
                "Eyebite",
                "Find the Path",
                "Fox's Cunning, Mass",
                "Geas/Quest",
                "Heroes' Feast",
                "Irresistible Dance",
                "Permanent Image",
                "Programmed Image",
                "Project Image",
                "Scrying, Greater",
                "Shout, Greater",
                "Summon Monster VI",
                "Sympathetic Vibration",
                "Symphonic Nightmare",
                "Veil",
                "Waves of Exhaustion",
            ],

            "Oracle": [
                # Level 0 (cantrips)
                "Bleed",
                "Create Water",
                "Detect Magic",
                "Detect Poison",
                "Guidance",
                "Light",
                "Mending",
                "Purify Food and Drink",
                "Read Magic",
                "Resistance",
                "Stabilize",
                "Virtue",

                # Level 1
                "Alarm",
                "Bane",
                "Bless",
                "Bless Water",
                "Burning Hands",
                "Cause Fear",
                "Command",
                "Comprehend Languages",
                "Cure Light Wounds",
                "Curse Water",
                "Deathwatch",
                "Detect Chaos",
                "Detect Evil",
                "Detect Good",
                "Detect Law",
                "Detect Undead",
                "Divine Favor",
                "Doom",
                "Endure Elements",
                "Entropic Shield",
                "Hide from Undead",
                "Inflict Light Wounds",
                "Magic Stone",
                "Magic Weapon",
                "Obscuring Mist",
                "Protection from Chaos",
                "Protection from Evil",
                "Protection from Good",
                "Protection from Law",
                "Remove Fear",
                "Sanctuary",
                "Shield of Faith",
                "Summon Monster I",

                # Level 2
                "Aid",
                "Align Weapon",
                "Alter Self",
                "Augury",
                "Bear's Endurance",
                "Bull's Strength",
                "Calm Emotions",
                "Consecrate",
                "Cure Moderate Wounds",
                "Darkness",
                "Death Knell",
                "Delay Poison",
                "Desecrate",
                "Eagle's Splendor",
                "Enthrall",
                "Find Traps",
                "Flame Blade",
                "Fog Cloud",
                "Gentle Repose",
                "Hold Person",
                "Identitfy",
                "Inflict Moderate Wounds",
                "Make Whole",
                "Owl's Wisdom",
                "Remove Paralysis",
                "Resist Energy",
                "Restoration, Lesser",
                "Shatter",
                "Shield Other",
                "Silence",
                "Sound Burst",
                "Spiritual Weapon",
                "Status",
                "Summon Monster II",
                "Undetectable Alignment",
                "Zone of Truth",

                # Level 3
                "Animate Dead",
                "Bestow Curse",
                "Blindness/Deafness",
                "Contagion",
                "Continual Flame",
                "Create Food and Water",
                "Cure Serious Wounds",
                "Daylight",
                "Deeper Darkness",
                "Dispel Magic",
                "Glyph of Warding",
                "Helping Hand",
                "Inflict Serious Wounds",
                "Invisibility Purge",
                "Locate Object",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Magic Circle against Good",
                "Magic Circle against Law",
                "Magic Vestment",
                "Meld into Stone",
                "Obscure Object",
                "Prayer",
                "Protection from Energy",
                "Remove Blindness/Deafness",
                "Remove Curse",
                "Remove Disease",
                "Searing Light",
                "Speak with Dead",
                "Stone Shape",
                "Summon Monster III",
                "Water Breathing",
                "Water Walk",
                "Wind Wall",

                # Level 4
                "Air Walk",
                "Blessing of Fervor",
                "Chaos Hammer",
                "Control Water",
                "Cure Critical Wounds",
                "Death Ward",
                "Dimensional Anchor",
                "Discern Lies",
                "Dismissal",
                "Divination",
                "Divine Power",
                "Freedom of Movement",
                "Giant Vermin",
                "Holy Smite",
                "Imbue with Spell Ability",
                "Inflict Critical Wounds",
                "Magic Weapon, Greater",
                "Neutralize Poison",
                "Order's Wrath",
                "Planar Ally, Lesser",
                "Poison",
                "Repel Vermin",
                "Restoration",
                "Sending",
                "Spell Immunity",
                "Summon Monster IV",
                "Tongues",
                "Unholy Blight",

                # Level 5
                "Atonement",
                "Break Enchantment",
                "Breath of Life",
                "Command, Greater",
                "Commune",
                "Cure Light Wounds, Mass",
                "Dispel Chaos",
                "Dispel Evil",
                "Dispel Good",
                "Dispel Law",
                "Disrupting Weapon",
                "Flame Strike",
                "Hallow",
                "Inflict Light Wounds, Mass",
                "Insect Plague",
                "Mark of Justice",
                "Plane Shift",
                "Raise Dead",
                "Righteous Might",
                "Scrying",
                "Slay Living",
                "Spell Resistance",
                "Summon Monster V",
                "Symbol of Pain",
                "Symbol of Sleep",
                "True Seeing",
                "Unhallow",
                "Wall of Stone",

                # Level 6
                "Animate Objects",
                "Antilife Shell",
                "Banishment",
                "Bear's Endurance, Mass",
                "Blade Barrier",
                "Bull's Strength, Mass",
                "Create Undead",
                "Cure Moderate Wounds, Mass",
                "Dispel Magic, Greater",
                "Eagle's Splendor, Mass",
                "Find the Path",
                "Forbiddance",
                "Geas/Quest",
                "Glyph of Warding, Greater",
                "Harm",
                "Heal",
                "Heroes' Feast",
                "Inflict Moderate Wounds, Mass",
                "Owl's Wisdom, Mass",
                "Planar Ally",
                "Summon Monster VI",
                "Symbol of Fear",
                "Symbol of Persuasion",
                "Undeath to Death",
                "Wind Walk",
                "Word of Recall",

                # Level 7
                "Blasphemy",
                "Control Weather",
                "Cure Serious Wounds, Mass",
                "Destruction",
                "Dictum",
                "Ethereal Jaunt",
                "Holy Word",
                "Inflict Serious Wounds, Mass",
                "Refuge",
                "Regenerate",
                "Repulsion",
                "Restoration, Greater",
                "Resurrection",
                "Scrying, Greater",
                "Summon Monster VII",
                "Symbol of Stunning",
                "Symbol of Weakness",
                "Word of Chaos",

                # Level 8
                "Antimagic Field",
                "Cloak of Chaos",
                "Create Greater Undead",
                "Cure Critical Wounds, Mass",
                "Dimensional Lock",
                "Discern Location",
                "Earthquake",
                "Fire Storm",
                "Holy Aura",
                "Inflict Critical Wounds, Mass",
                "Planar Ally, Greater",
                "Shield of Law",
                "Spell Immunity, Greater",
                "Summon Monster VIII",
                "Symbol of Death",
                "Symbol of Insanity",
                "Unholy Aura",

                # Level 9
                "Astral Projection",
                "Energy Drain",
                "Etherealness",
                "Gate",
                "Heal, Mass",
                "Implosion",
                "Miracle",
                "Soul Bind",
                "Storm of Vengeance",
                "Summon Monster IX",
                "True Resurrection"
            ],

            "Witch": [
                # Level 0 (Cantrips)
                "Arcane Mark",
                "Bleed",
                "Dancing Lights",
                "Daze",
                "Detect Magic",
                "Detect Poison",
                "Guidance",
                "Light",
                "Mending",
                "Message",
                "Putrefy Food and Drink",
                "Read Magic",
                "Resistance",
                "Spark",
                "Stabilize",
                "Touch of Fatigue",

                # Level 1
                "Adhesive Spittle",
                "Animate Rope",
                "Beguiling Gift",
                "Burning Hands",
                "Cause Fear",
                "Charm Person",
                "Chill Touch",
                "Command",
                "Comprehend Languages",
                "Cure Light Wounds",
                "Dancing Lantern",
                "Darkness",
                "Detect Secret Doors",
                "Disguise Self",
                "Doom",
                "Ear-Piercing Scream",
                "Enlarge Person",
                "Expeditious Retreat",
                "Identify",
                "Ill Omen",
                "Inflict Light Wounds",
                "Mage Armor",
                "Magic Missile",
                "Mount",
                "Obscuring Mist",
                "Ray of Enfeeblement",
                "Reduce Person",
                "Sleep",
                "Summon Monster I",
                "Unseen Servant",

                # Level 2
                "Alter Self",
                "Beast Shape I",
                "Blindness/Deafness",
                "Blur",
                "Bull's Strength",
                "Cat's Grace",
                "Cure Moderate Wounds",
                "Darkness",
                "Death Knell",
                "Detect Thoughts",
                "Eagle's Splendor",
                "False Life",
                "Fox's Cunning",
                "Gentle Repose",
                "Ghoul Touch",
                "Glide",
                "Hideous Laughter",
                "Hold Person",
                "Invisibility",
                "Levitate",
                "Mirror Image",
                "Misfortune",
                "Owl's Wisdom",
                "Pox Pustules",
                "Scare",
                "See Invisibility",
                "Spectral Hand",
                "Spider Climb",
                "Summon Monster II",
                "Summon Swarm",
                "Touch of Idiocy",
                "Vomit Swarm",
                "Web",

                # Level 3
                "Arcane Sight",
                "Beast Shape II",
                "Bestow Curse",
                "Clairaudience/Clairvoyance",
                "Deep Slumber",
                "Dispel Magic",
                "Fly",
                "Gaseous Form",
                "Glyph of Warding",
                "Heroism",
                "Lightning Bolt",
                "Major Image",
                "Nature's Exile",
                "Pain Strike",
                "Poison",
                "Remove Curse",
                "Screech",
                "Seek Thoughts",
                "Sepia Snake Sigil",
                "Sleet Storm",
                "Stinking Cloud",
                "Suggestion",
                "Summon Monster III",
                "Tongues",
                "Vampiric Touch",
                "Water Breathing",

                # Level 4
                "Arcane Eye",
                "Beast Shape III",
                "Black Tentacles",
                "Charm Monster",
                "Confusion",
                "Crush of the Depth",
                "Cure Critical Wounds",
                "Dimension Door",
                "Discern Lies",
                "Enervation",
                "Fear",
                "Ice Storm",
                "Inflict Critical Wounds",
                "Lesser Globe of Invulnerability",
                "Lesser Planar Ally",
                "Locate Creature",
                "Minor Creation",
                "Modify Memory",
                "Neutralize Poison",
                "Phantasmal Killer",
                "Poison",
                "Scrying",
                "Secure Shelter",
                "Solid Fog",
                "Summon Monster IV",
                "Wall of Ice",

                # Level 5
                "Animal Growth",
                "Baleful Polymorph",
                "Beast Shape IV",
                "Break Enchantment",
                "Cloudkill",
                "Contact Other Plane",
                "Curse of Magic Negation",
                "Dominate Person",
                "Feeblemind",
                "Hold Monster",
                "Magic Jar",
                "Major Creation",
                "Mind Fog",
                "Nightmare",
                "Overland Flight",
                "Passwall",
                "Persistent Image",
                "Polymorph",
                "Secret Chest",
                "Sending",
                "Summon Monster V",
                "Telepathic Bond",
                "Teleport",
                "Waves of Fatigue",

                # Level 6
                "Analyze Dweomer",
                "Bear's Endurance, Mass",
                "Bull's Strength, Mass",
                "Cat's Grace, Mass",
                "Circle of Death",
                "Create Undead",
                "Disintegrate",
                "Eagle's Splendor, Mass",
                "Eyebite",
                "Flesh to Stone",
                "Fox's Cunning, Mass",
                "Geas/Quest",
                "Guards and Wards",
                "Legend Lore",
                "Owl's Wisdom, Mass",
                "Permanent Image",
                "Programmed Image",
                "Repulsion",
                "Stone to Flesh",
                "Suggestion, Mass",
                "Summon Monster VI",
                "Symbol of Fear",
                "True Seeing",
                "Veil",

                # Level 7
                "Arcane Sight, Greater",
                "Control Undead",
                "Control Weather",
                "Finger of Death",
                "Hold Person, Mass",
                "Insanity",
                "Instant Summons",
                "Limited Wish",
                "Phase Door",
                "Plane Shift",
                "Power Word Blind",
                "Prismatic Spray",
                "Scrying, Greater",
                "Spell Turning",
                "Summon Monster VII",
                "Symbol of Stunning",
                "Teleport, Greater",
                "Vision",
                "Waves of Exhaustion",

                # Level 8
                "Antipathy",
                "Charm Monster, Mass",
                "Clone",
                "Create Greater Undead",
                "Dimensional Lock",
                "Discern Location",
                "Horrid Wilting",
                "Iron Body",
                "Maze",
                "Mind Blank",
                "Moment of Prescience",
                "Power Word Stun",
                "Prismatic Wall",
                "Protection from Spells",
                "Scintillating Pattern",
                "Screen",
                "Shadow Evocation, Greater",
                "Summon Monster VIII",
                "Symbol of Death",
                "Symbol of Insanity",
                "Sympathy",
                "Temporal Stasis",
                "Trap the Soul",

                # Level 9
                "Astral Projection",
                "Dominate Monster",
                "Energy Drain",
                "Etherealness",
                "Foresight",
                "Hold Monster, Mass",
                "Power Word Kill",
                "Prismatic Sphere",
                "Shades",
                "Soul Bind",
                "Summon Monster IX",
                "Teleportation Circle",
                "Time Stop",
                "Wail of the Banshee",
                "Weird"
            ],

            "Magus": [
                # Level 0 (Cantrips)
                "Acid Splash",
                "Arcane Mark",
                "Dancing Lights",
                "Daze",
                "Detect Magic",
                "Disrupt Undead",
                "Flare",
                "Ghost Sound",
                "Light",
                "Mage Hand",
                "Open/Close",
                "Prestidigitation",
                "Ray of Frost",
                "Read Magic",
                "Spark",

                # Level 1
                "Burning Hands",
                "Chill Touch",
                "Color Spray",
                "Corrosive Touch",
                "Enlarge Person",
                "Expeditious Retreat",
                "Feather Fall",
                "Flare Burst",
                "Floating Disk",
                "Force Hook Charge",
                "Frostbite",
                "Grease",
                "Jump",
                "Magic Missile",
                "Magic Weapon",
                "Mount",
                "Obscuring Mist",
                "Ray of Enfeeblement",
                "Reduce Person",
                "Shield",
                "Shocking Grasp",
                "True Strike",
                "Vanish",

                # Level 2
                "Alter Self",
                "Blur",
                "Bull's Strength",
                "Cat's Grace",
                "Darkness",
                "Defensive Shock",
                "Eagle's Splendor",
                "Elemental Touch",
                "Fire Breath",
                "Flaming Sphere",
                "Fox's Cunning",
                "Glide",
                "Invisibility",
                "Iron Wind",
                "Levitate",
                "Mirror Image",
                "Owl's Wisdom",
                "Resist Energy",
                "Scorching Ray",
                "See Invisibility",
                "Spider Climb",
                "Stone Call",
                "Web",

                # Level 3
                "Arcane Sight",
                "Beast Shape I",
                "Blink",
                "Daylight",
                "Dispel Magic",
                "Displacement",
                "Fireball",
                "Flame Arrow",
                "Fly",
                "Force Hook Charge",
                "Force Punch",
                "Gaseous Form",
                "Haste",
                "Hold Person",
                "Keen Edge",
                "Lightning Bolt",
                "Magic Weapon, Greater",
                "Phantom Steed",
                "Protection from Energy",
                "Slow",
                "Vampiric Touch",
                "Wind Wall",

                # Level 4
                "Arc of Lightning",
                "Beast Shape II",
                "Black Tentacles",
                "Dimension Door",
                "Dragon's Breath",
                "Elemental Body I",
                "Enervation",
                "Fear",
                "Fire Shield",
                "Globe of Invulnerability, Lesser",
                "Ice Storm",
                "Phantasmal Killer",
                "Ride the Waves",
                "Shout",
                "Solid Fog",
                "Stoneskin",
                "Wall of Fire",
                "Wall of Ice",

                # Level 5
                "Baleful Polymorph",
                "Beast Shape III",
                "Break Enchantment",
                "Cloudkill",
                "Cone of Cold",
                "Dismissal",
                "Elemental Body II",
                "Hold Monster",
                "Overland Flight",
                "Passwall",
                "Polymorph",
                "Telekinesis",
                "Teleport",
                "Transmute Mud to Rock",
                "Transmute Rock to Mud",
                "Wall of Force",
                "Wall of Stone"
                # Level 6
                "Beast Shape IV",
                "Blade Barrier",
                "Chain Lightning",
                "Disintegrate",
                "Dispel Magic, Greater",
                "Elemental Body III",
                "Flesh to Stone",
                "Form of the Dragon I",
                "Freezing Sphere",
                "Lightning Bolt, Intensified",
                "Sirocco",
                "Stone to Flesh",
                "Transformation",
                "True Seeing",
                "Wall of Iron"
            ],

            "Inquisitor": [
                # Level 0 (cantrips)
                "Acid Splash",
                "Brand",
                "Create Water",
                "Detect Magic",
                "Detect Poison",
                "Disrupt Undead",
                "Guidance",
                "Light",
                "Read Magic",
                "Resistance",
                "Sift",
                "Stabilize",
                "Virtue",

                # Level 1
                "Alarm",
                "Bane",
                "Bless",
                "Burst Bonds",
                "Cause Fear",
                "Command",
                "Comprehend Languages",
                "Cure Light Wounds",
                "Detect Chaos",
                "Detect Evil",
                "Detect Good",
                "Detect Law",
                "Detect Undead",
                "Divine Favor",
                "Doom",
                "Expeditious Retreat",
                "Hide from Undead",
                "Inflict Light Wounds",
                "Magic Weapon",
                "Protection from Chaos",
                "Protection from Evil",
                "Protection from Good",
                "Protection from Law",
                "Remove Fear",
                "Sanctuary",
                "Shield of Faith",
                "True Strike",
                "Wrath",

                # Level 2
                "Aid",
                "Align Weapon",
                "Bear's Endurance",
                "Bull's Strength",
                "Cure Moderate Wounds",
                "Darkness",
                "Death Knell",
                "Delay Poison",
                "Detect Thoughts",
                "Eagle's Splendor",
                "Find Traps",
                "Fox's Cunning",
                "Hold Person",
                "Invisibility",
                "Knock",
                "Lesser Restoration",
                "Lock Gaze",
                "Owl's Wisdom",
                "Remove Paralysis",
                "Resist Energy",
                "Silence",
                "See Invisibility",
                "Spiritual Weapon",
                "Undetectable Alignment",
                "Zone of Truth",

                # Level 3
                "Arcane Sight",
                "Bestow Curse",
                "Blindness/Deafness",
                "Blood Biography",
                "Cure Serious Wounds",
                "Daylight",
                "Deeper Darkness",
                "Dimensional Anchor",
                "Dispel Magic",
                "Forced Repentance",
                "Glyph of Warding",
                "Heal Mount",
                "Heroism",
                "Invisibility Purge",
                "Locate Object",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Magic Circle against Good",
                "Magic Circle against Law",
                "NonDetection",
                "Prayer",
                "Remove Curse",
                "Remove Disease",
                "Seek Thoughts",
                "Speak with Dead",

                # Level 4
                "Break Enchantment",
                "Cure Critical Wounds",
                "Death Ward",
                "Detect Scrying",
                "Dimensional Anchor",
                "Discern Lies",
                "Dismissal",
                "Divine Power",
                "Fear",
                "Freedom of Movement",
                "Giant Vermin",
                "Holy Smite",
                "Lesser Globe of Invulnerability",
                "Neutralize Poison",
                "Order's Wrath",
                "Sending",
                "Spell Immunity",
                "Chaos Hammer",
                "Unholy Blight",

                # Level 5
                "Atonement",
                "Banishment",
                "Breath of Life",
                "Command, Greater",
                "Commune",
                "Cure Light Wounds, Mass",
                "Dispel Chaos",
                "Dispel Evil",
                "Dispel Good",
                "Dispel Law",
                "Disrupting Weapon",
                "False Vision",
                "Flame Strike",
                "Hallow",
                "Mark of Justice",
                "Righteous Might",
                "Spell Resistance",
                "True Seeing",
                "Unhallow",

                # Level 6
                "Blade Barrier",
                "Circle of Death",
                "Cure Moderate Wounds, Mass",
                "Dispel Magic, Greater",
                "Forbiddance",
                "Geas/Quest",
                "Greater Globe of Invulnerability",
                "Harm",
                "Heal",
                "Heroes' Feast",
                "Legend Lore",
                "Planar Ally",
                "Repulsion",
                "Symbol of Fear",
                "Symbol of Persuasion",
                "Undeath to Death",
                "Word of Recall"
            ],

            "Ranger": [
                # Level 1
                "Alarm",
                "Animal Messenger",
                "Calm Animals",
                "Charm Animal",
                "Delay Poison",
                "Detect Animals or Plants",
                "Detect Poison",
                "Detect Snares and Pits",
                "Endure Elements",
                "Entangle",
                "Hide from Animals",
                "Jump",
                "Longstrider",
                "Magic Fang",
                "Pass without Trace",
                "Read Magic",
                "Resist Energy",
                "Speak with Animals",
                "Summon Nature's Ally I",

                # Level 2
                "Barkskin",
                "Bear's Endurance",
                "Cat's Grace",
                "Cure Light Wounds",
                "Hold Animal",
                "Owl's Wisdom",
                "Protection from Energy",
                "Locate Object",
                "Scarecrow",
                "Snare",
                "Speak with Plants",
                "Spike Growth",
                "Summon Nature's Ally II",
                "Web",
                "Wind Wall",
                "Whispering Wind",

                # Level 3
                "Cure Moderate Wounds",
                "Darkvision",
                "Daylight",
                "Diminish Plants",
                "Magic Fang, Greater",
                "Neutralize Poison",
                "Plant Growth",
                "Remove Disease",
                "Repel Vermin",
                "Spider Climb",
                "Summon Nature's Ally III",
                "Tree Shape",
                "Water Walk",

                # Level 4
                "Animal Growth",
                "Commune with Nature",
                "Cure Serious Wounds",
                "Freedom of Movement",
                "Grove of Respite",
                "Tree Stride",
                "Nondetection",
                "Summon Nature's Ally IV"
            ],

            "Paladin": [
                # Level 1
                "Bless",
                "Bless Water",
                "Bless Weapon",
                "Create Water",
                "Cure Light Wounds",
                "Detect Poison",
                "Detect Undead",
                "Divine Favor",
                "Endure Elements",
                "Hero's Defiance",
                "Lesser Restoration",
                "Magic Weapon",
                "Protection from Chaos",
                "Protection from Evil",
                "Read Magic",
                "Resistance",
                "Restore Virtue",
                "Sacrifice",
                "Shield of Faith",
                "Virtue",

                # Level 2
                "Bull's Strength",
                "Delay Poison",
                "Eagle's Splendor",
                "Grace",
                "Hold Person",
                "Instant Armor",
                "Owl's Wisdom",
                "Remove Paralysis",
                "Resist Energy",
                "Shield Other",
                "Undetectable Alignment",
                "Zone of Truth",

                # Level 3
                "Cure Moderate Wounds",
                "Daylight",
                "Discern Lies",
                "Dispel Magic",
                "Greater Magic Weapon",
                "Heal Mount",
                "Magic Circle against Chaos",
                "Magic Circle against Evil",
                "Prayer",
                "Remove Blindness/Deafness",
                "Remove Curse",
                "Remove Disease",

                # Level 4
                "Break Enchantment",
                "Cure Serious Wounds",
                "Death Ward",
                "Dispel Evil",
                "Holy Sword",
                "Mark of Justice",
                "Neutralize Poison",
                "Restoration",
                "Holy Sword"
            ],

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
                1: {"cantrips": 2, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 2, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 2, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 3, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 3, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 3, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 3, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 3, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 3, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 11, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 12, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 12, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 13, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 13, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 14, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 14, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 15, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 15, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 15, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 16, "available_spell_level": 9}
            },
            "Wizard": {
                1: {"cantrips": 3, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 3, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 3, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 5, "spells": 11, "available_spell_level": 5},
                11: {"cantrips": 5, "spells": 12, "available_spell_level": 6},
                12: {"cantrips": 5, "spells": 12, "available_spell_level": 6},
                13: {"cantrips": 5, "spells": 13, "available_spell_level": 7},
                14: {"cantrips": 5, "spells": 13, "available_spell_level": 7},
                15: {"cantrips": 5, "spells": 14, "available_spell_level": 8},
                16: {"cantrips": 5, "spells": 14, "available_spell_level": 8},
                17: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                18: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                19: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                20: {"cantrips": 5, "spells": 16, "available_spell_level": 9}
            },
            "Cleric": {
                1: {"cantrips": 3, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 3, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 3, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 5, "spells": 11, "available_spell_level": 5},
                11: {"cantrips": 5, "spells": 12, "available_spell_level": 6},
                12: {"cantrips": 5, "spells": 12, "available_spell_level": 6},
                13: {"cantrips": 5, "spells": 13, "available_spell_level": 7},
                14: {"cantrips": 5, "spells": 13, "available_spell_level": 7},
                15: {"cantrips": 5, "spells": 14, "available_spell_level": 8},
                16: {"cantrips": 5, "spells": 14, "available_spell_level": 8},
                17: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                18: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                19: {"cantrips": 5, "spells": 15, "available_spell_level": 9},
                20: {"cantrips": 5, "spells": 16, "available_spell_level": 9}
            },
            "Sorcerer": {
                1: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 5, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 5, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 5, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 5, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 5, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 5, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 6, "spells": 11, "available_spell_level": 5},
                11: {"cantrips": 6, "spells": 12, "available_spell_level": 6},
                12: {"cantrips": 6, "spells": 12, "available_spell_level": 6},
                13: {"cantrips": 6, "spells": 13, "available_spell_level": 7},
                14: {"cantrips": 6, "spells": 13, "available_spell_level": 7},
                15: {"cantrips": 6, "spells": 14, "available_spell_level": 8},
                16: {"cantrips": 6, "spells": 14, "available_spell_level": 8},
                17: {"cantrips": 6, "spells": 15, "available_spell_level": 9},
                18: {"cantrips": 6, "spells": 15, "available_spell_level": 9},
                19: {"cantrips": 6, "spells": 15, "available_spell_level": 9},
                20: {"cantrips": 6, "spells": 15, "available_spell_level": 9}
            },
            "Bard": {
                1: {"cantrips": 2, "spells": 4, "available_spell_level": 1},
                2: {"cantrips": 2, "spells": 5, "available_spell_level": 1},
                3: {"cantrips": 2, "spells": 6, "available_spell_level": 2},
                4: {"cantrips": 3, "spells": 7, "available_spell_level": 2},
                5: {"cantrips": 3, "spells": 8, "available_spell_level": 3},
                6: {"cantrips": 3, "spells": 9, "available_spell_level": 3},
                7: {"cantrips": 3, "spells": 10, "available_spell_level": 4},
                8: {"cantrips": 3, "spells": 11, "available_spell_level": 4},
                9: {"cantrips": 3, "spells": 12, "available_spell_level": 5},
                10: {"cantrips": 3, "spells": 14, "available_spell_level": 5},
                11: {"cantrips": 3, "spells": 15, "available_spell_level": 6},
                12: {"cantrips": 3, "spells": 15, "available_spell_level": 6},
                13: {"cantrips": 3, "spells": 16, "available_spell_level": 7},
                14: {"cantrips": 3, "spells": 18, "available_spell_level": 7},
                15: {"cantrips": 3, "spells": 19, "available_spell_level": 8},
                16: {"cantrips": 3, "spells": 19, "available_spell_level": 8},
                17: {"cantrips": 3, "spells": 20, "available_spell_level": 9},
                18: {"cantrips": 3, "spells": 22, "available_spell_level": 9},
                19: {"cantrips": 3, "spells": 22, "available_spell_level": 9},
                20: {"cantrips": 3, "spells": 22, "available_spell_level": 9}
            },
            "Paladin": {
                1: {"cantrips": 0, "spells": 0, "available_spell_level": 0},
                2: {"cantrips": 0, "spells": 0, "available_spell_level": 0},
                3: {"cantrips": 0, "spells": 2, "available_spell_level": 1},
                4: {"cantrips": 0, "spells": 3, "available_spell_level": 1},
                5: {"cantrips": 0, "spells": 4, "available_spell_level": 1},
                6: {"cantrips": 0, "spells": 4, "available_spell_level": 1},
                7: {"cantrips": 0, "spells": 5, "available_spell_level": 2},
                8: {"cantrips": 0, "spells": 5, "available_spell_level": 2},
                9: {"cantrips": 0, "spells": 6, "available_spell_level": 2},
                10: {"cantrips": 0, "spells": 7, "available_spell_level": 2},
                11: {"cantrips": 0, "spells": 8, "available_spell_level": 3},
                12: {"cantrips": 0, "spells": 8, "available_spell_level": 3},
                13: {"cantrips": 0, "spells": 9, "available_spell_level": 3},
                14: {"cantrips": 0, "spells": 10, "available_spell_level": 3},
                15: {"cantrips": 0, "spells": 10, "available_spell_level": 4},
                16: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                17: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                18: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                19: {"cantrips": 0, "spells": 12, "available_spell_level": 5},
                20: {"cantrips": 0, "spells": 13, "available_spell_level": 5}
            },
            "Ranger": {
                1: {"cantrips": 0, "spells": 0, "available_spell_level": 0},
                2: {"cantrips": 0, "spells": 0, "available_spell_level": 0},
                3: {"cantrips": 0, "spells": 2, "available_spell_level": 1},
                4: {"cantrips": 0, "spells": 3, "available_spell_level": 1},
                5: {"cantrips": 0, "spells": 4, "available_spell_level": 1},
                6: {"cantrips": 0, "spells": 4, "available_spell_level": 1},
                7: {"cantrips": 0, "spells": 5, "available_spell_level": 2},
                8: {"cantrips": 0, "spells": 5, "available_spell_level": 2},
                9: {"cantrips": 0, "spells": 6, "available_spell_level": 2},
                10: {"cantrips": 0, "spells": 7, "available_spell_level": 2},
                11: {"cantrips": 0, "spells": 8, "available_spell_level": 3},
                12: {"cantrips": 0, "spells": 8, "available_spell_level": 3},
                13: {"cantrips": 0, "spells": 9, "available_spell_level": 3},
                14: {"cantrips": 0, "spells": 10, "available_spell_level": 3},
                15: {"cantrips": 0, "spells": 10, "available_spell_level": 4},
                16: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                17: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                18: {"cantrips": 0, "spells": 11, "available_spell_level": 4},
                19: {"cantrips": 0, "spells": 12, "available_spell_level": 5},
                20: {"cantrips": 0, "spells": 13, "available_spell_level": 5}
            },
            "Warlock": {
                1: {"cantrips": 2, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 2, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 2, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 3, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 3, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 3, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 3, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 3, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 3, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 3, "spells": 10, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 11, "available_spell_level": 5},
                12: {"cantrips": 4, "spells": 11, "available_spell_level": 5},
                13: {"cantrips": 4, "spells": 12, "available_spell_level": 5},
                14: {"cantrips": 4, "spells": 12, "available_spell_level": 5},
                15: {"cantrips": 4, "spells": 13, "available_spell_level": 5},
                16: {"cantrips": 4, "spells": 13, "available_spell_level": 5},
                17: {"cantrips": 4, "spells": 14, "available_spell_level": 5},
                18: {"cantrips": 4, "spells": 14, "available_spell_level": 5},
                19: {"cantrips": 4, "spells": 15, "available_spell_level": 5},
                20: {"cantrips": 4, "spells": 15, "available_spell_level": 5}
            },
        },
        "Pathfinder": {
            "Oracle": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 2, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 3, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 6, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 6, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 7, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 7, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 8, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 8, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 9, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 9, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 11, "available_spell_level": 9}
            },
            
            "Witch": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 2, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 3, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 6, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 6, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 7, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 7, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 8, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 8, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 9, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 9, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 11, "available_spell_level": 9}
            },

            "Magus": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 3, "available_spell_level": 1},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                8: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 3},
                10: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                11: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                12: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                13: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                14: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                15: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                16: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                17: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                18: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                19: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                20: {"cantrips": 4, "spells": 5, "available_spell_level": 6}
            },

            "Inquisitor": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 3, "available_spell_level": 1},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                8: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 3},
                10: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                11: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                12: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                13: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                14: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                15: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                16: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                17: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                18: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                19: {"cantrips": 4, "spells": 5, "available_spell_level": 6},
                20: {"cantrips": 4, "spells": 5, "available_spell_level": 6}
            },

            "Ranger": {
                1: {"spells": 0, "available_spell_level": 0},
                2: {"spells": 0, "available_spell_level": 0},
                3: {"spells": 0, "available_spell_level": 0},
                4: {"spells": 1, "available_spell_level": 1},
                5: {"spells": 1, "available_spell_level": 1},
                6: {"spells": 1, "available_spell_level": 1},
                7: {"spells": 1, "available_spell_level": 2},
                8: {"spells": 1, "available_spell_level": 2},
                9: {"spells": 2, "available_spell_level": 2},
                10: {"spells": 2, "available_spell_level": 3},
                11: {"spells": 2, "available_spell_level": 3},
                12: {"spells": 2, "available_spell_level": 3},
                13: {"spells": 3, "available_spell_level": 4},
                14: {"spells": 3, "available_spell_level": 4},
                15: {"spells": 3, "available_spell_level": 4},
                16: {"spells": 3, "available_spell_level": 4},
                17: {"spells": 4, "available_spell_level": 4},
                18: {"spells": 4, "available_spell_level": 4},
                19: {"spells": 4, "available_spell_level": 4},
                20: {"spells": 4, "available_spell_level": 4}
            },

            "Paladin": {
                1: {"spells": 0, "available_spell_level": 0},
                2: {"spells": 0, "available_spell_level": 0},
                3: {"spells": 0, "available_spell_level": 0},
                4: {"spells": 1, "available_spell_level": 1},
                5: {"spells": 1, "available_spell_level": 1},
                6: {"spells": 1, "available_spell_level": 1},
                7: {"spells": 1, "available_spell_level": 2},
                8: {"spells": 1, "available_spell_level": 2},
                9: {"spells": 2, "available_spell_level": 2},
                10: {"spells": 2, "available_spell_level": 3},
                11: {"spells": 2, "available_spell_level": 3},
                12: {"spells": 2, "available_spell_level": 3},
                13: {"spells": 3, "available_spell_level": 4},
                14: {"spells": 3, "available_spell_level": 4},
                15: {"spells": 3, "available_spell_level": 4},
                16: {"spells": 3, "available_spell_level": 4},
                17: {"spells": 4, "available_spell_level": 4},
                18: {"spells": 4, "available_spell_level": 4},
                19: {"spells": 4, "available_spell_level": 4},
                20: {"spells": 4, "available_spell_level": 4}
            },

            "Wizard": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 2, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 3, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 6, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 6, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 7, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 7, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 8, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 8, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 9, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 9, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 11, "available_spell_level": 9}
            },

            "Cleric": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 2, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 3, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 6, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 6, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 7, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 7, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 8, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 8, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 9, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 9, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 11, "available_spell_level": 9}
            },

            "Druid": {
                1: {"cantrips": 3, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 2, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 3, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 4, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 4, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 5, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 5, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 6, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 6, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 7, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 7, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 8, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 8, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 9, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 9, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 10, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 11, "available_spell_level": 9}
            },
            "Sorcerer": {
                1: {"cantrips": 4, "spells": 2, "available_spell_level": 1},
                2: {"cantrips": 4, "spells": 3, "available_spell_level": 1},
                3: {"cantrips": 4, "spells": 4, "available_spell_level": 2},
                4: {"cantrips": 4, "spells": 5, "available_spell_level": 2},
                5: {"cantrips": 4, "spells": 6, "available_spell_level": 3},
                6: {"cantrips": 4, "spells": 7, "available_spell_level": 3},
                7: {"cantrips": 4, "spells": 8, "available_spell_level": 4},
                8: {"cantrips": 4, "spells": 9, "available_spell_level": 4},
                9: {"cantrips": 4, "spells": 10, "available_spell_level": 5},
                10: {"cantrips": 4, "spells": 11, "available_spell_level": 5},
                11: {"cantrips": 4, "spells": 12, "available_spell_level": 6},
                12: {"cantrips": 4, "spells": 13, "available_spell_level": 6},
                13: {"cantrips": 4, "spells": 14, "available_spell_level": 7},
                14: {"cantrips": 4, "spells": 15, "available_spell_level": 7},
                15: {"cantrips": 4, "spells": 16, "available_spell_level": 8},
                16: {"cantrips": 4, "spells": 17, "available_spell_level": 8},
                17: {"cantrips": 4, "spells": 18, "available_spell_level": 9},
                18: {"cantrips": 4, "spells": 19, "available_spell_level": 9},
                19: {"cantrips": 4, "spells": 20, "available_spell_level": 9},
                20: {"cantrips": 4, "spells": 22, "available_spell_level": 9},
            },
            "Bard": {
                1: {"cantrips": 4, "spells": 1, "available_spell_level": 1},
                2: {"cantrips": 5, "spells": 2, "available_spell_level": 1},
                3: {"cantrips": 5, "spells": 3, "available_spell_level": 1},
                4: {"cantrips": 5, "spells": 3, "available_spell_level": 2},
                5: {"cantrips": 5, "spells": 4, "available_spell_level": 2},
                6: {"cantrips": 5, "spells": 4, "available_spell_level": 2},
                7: {"cantrips": 5, "spells": 4, "available_spell_level": 3},
                8: {"cantrips": 5, "spells": 4, "available_spell_level": 3},
                9: {"cantrips": 5, "spells": 5, "available_spell_level": 3},
                10: {"cantrips": 5, "spells": 5, "available_spell_level": 4},
                11: {"cantrips": 6, "spells": 5, "available_spell_level": 4},
                12: {"cantrips": 6, "spells": 5, "available_spell_level": 4},
                13: {"cantrips": 6, "spells": 5, "available_spell_level": 5},
                14: {"cantrips": 6, "spells": 5, "available_spell_level": 5},
                15: {"cantrips": 6, "spells": 5, "available_spell_level": 5},
                16: {"cantrips": 6, "spells": 5, "available_spell_level": 6},
                17: {"cantrips": 6, "spells": 5, "available_spell_level": 6},
                18: {"cantrips": 6, "spells": 5, "available_spell_level": 6},
                19: {"cantrips": 6, "spells": 5, "available_spell_level": 6},
                20: {"cantrips": 6, "spells": 5, "available_spell_level": 6}
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

    backgrounds = {
        "Dungeons & Dragons 5th Edition": [
            {
                "name": "Acolyte",
                "description": "You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices to conduct worshipers into the presence of the divine.",
                "proficiencies": {
                    "skills": ["Insight", "Religion"],
                    "languages": ["Two languages of your choice"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Holy symbol",
                    "Prayer book or prayer wheel",
                    "5 sticks of incense",
                    "Vestments",
                    "Set of common clothes",
                    "15 gold pieces"
                ],
                "languages": ["Two of your choice"],
                "background_features": {
                    "name": "Shelter of the Faithful",
                    "description": "You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle."
                },
                "system_specific_data": None
            },
            {
                "name": "Criminal",
                "description": "You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the underworld. You're far closer than others to the world of murder, theft, and violence that pervades the underbelly of civilization.",
                "proficiencies": {
                    "skills": ["Deception", "Stealth"],
                    "tools": ["One type of gaming set", "Thieves' tools"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Crowbar",
                    "Set of dark common clothes including a hood",
                    "Belt pouch containing 15 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "Criminal Contact",
                    "description": "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
                },
                "system_specific_data": None
            },
            {
                "name": "Folk Hero",
                "description": "You come from a humble social rank, but you are destined for so much more. Already the people of your home village regard you as their champion, and your destiny calls you to stand against the tyrants and monsters that threaten the common folk everywhere.",
                "proficiencies": {
                    "skills": ["Animal Handling", "Survival"],
                    "tools": ["One type of artisan's tools", "Vehicles (land)"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Set of artisan's tools (your choice)",
                    "Shovel",
                    "Iron pot",
                    "Set of common clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "Rustic Hospitality",
                    "description": "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."
                },
                "system_specific_data": None
            },
            {
                "name": "Noble",
                "description": "You understand wealth, power, and privilege. You carry a noble title, and your family owns land, collects taxes, and wields significant political influence. You might be a pampered aristocrat unfamiliar with work or discomfort, or a former merchant just elevated to the nobility, or a disinherited scoundrel with a disproportionate sense of entitlement.",
                "proficiencies": {
                    "skills": ["History", "Persuasion"],
                    "tools": ["One type of gaming set"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Set of fine clothes",
                    "Signet ring",
                    "Scroll of pedigree",
                    "Purse containing 25 gold pieces"
                ],
                "languages": ["One of your choice"],
                "background_features": {
                    "name": "Position of Privilege",
                    "description": "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."
                },
                "system_specific_data": None
            },
            {
                "name": "Charlatan",
                "description": "You have always had a way with people. You know what makes them tick, you can tease out their hearts’ desires after a few minutes of conversation, and with a few leading questions you can read them like they were children’s books.",
                "proficiencies": {
                    "skills": ["Deception", "Sleight of Hand"],
                    "tools": ["Disguise kit", "Forgery kit"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Fine clothes",
                    "Disguise kit",
                    "Tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)",
                    "Belt pouch containing 15 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "False Identity",
                    "description": "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."
                },
                "system_specific_data": None
            },
            {
                "name": "Entertainer",
                "description": "You thrive in front of an audience. You know how to entrance them, entertain them, and even inspire them. Your poise and wit are the products of years of practice, study, and hard work.",
                "proficiencies": {
                    "skills": ["Acrobatics", "Performance"],
                    "tools": ["Disguise kit", "One musical instrument"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "One musical instrument",
                    "The favor of an admirer (love letter, lock of hair, or trinket)",
                    "Costume",
                    "Belt pouch containing 15 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "By Popular Demand",
                    "description": "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble’s court. You receive free lodging and food of a modest or comfortable standard as long as you perform each night."
                },
                "system_specific_data": None
            },
            {
                "name": "Guild Artisan",
                "description": "You are a member of an artisan’s guild, skilled in a particular field and closely associated with other artisans. You are well established in the world of trade and commerce, and you take pride in your guild membership.",
                "proficiencies": {
                    "skills": ["Insight", "Persuasion"],
                    "tools": ["One type of artisan's tools"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Set of artisan's tools (one of your choice)",
                    "Letter of introduction from your guild",
                    "Set of traveler’s clothes",
                    "Belt pouch containing 15 gold pieces"
                ],
                "languages": ["One of your choice"],
                "background_features": {
                    "name": "Guild Membership",
                    "description": "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession."
                },
                "system_specific_data": None
            },
            {
                "name": "Hermit",
                "description": "You lived in seclusion—either in a sheltered community such as a monastery, or entirely alone—for a formative part of your life. In your time apart from the clamor of society, you found quiet, solitude, and perhaps some of the answers you were looking for.",
                "proficiencies": {
                    "skills": ["Medicine", "Religion"],
                    "tools": ["Herbalism kit"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Scroll case stuffed full of notes from your studies or prayers",
                    "Winter blanket",
                    "Set of common clothes",
                    "Herbalism kit",
                    "5 gold pieces"
                ],
                "languages": ["One of your choice"],
                "background_features": {
                    "name": "Discovery",
                    "description": "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion."
                },
                "system_specific_data": None
            },
            {
                "name": "Outlander",
                "description": "You grew up in the wilds, far from the comforts of town and technology. You’ve witnessed the migration of herds larger than forests, survived weather more extreme than any city-dweller could comprehend, and enjoyed the solitude of being the only thinking creature for miles in any direction.",
                "proficiencies": {
                    "skills": ["Athletics", "Survival"],
                    "tools": ["One type of musical instrument"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Staff",
                    "Hunting trap",
                    "Trophy from an animal you killed",
                    "Set of traveler’s clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": ["One of your choice"],
                "background_features": {
                    "name": "Wanderer",
                    "description": "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers such resources."
                },
                "system_specific_data": None
            },
            {
                "name": "Sage",
                "description": "You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you.",
                "proficiencies": {
                    "skills": ["Arcana", "History"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Bottle of black ink",
                    "Quill",
                    "Small knife",
                    "Letter from a dead colleague posing a question you have not yet been able to answer",
                    "Set of common clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": ["Two of your choice"],
                "background_features": {
                    "name": "Researcher",
                    "description": "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person."
                },
                "system_specific_data": None
            },
            {
                "name": "Sailor",
                "description": "You sailed on a seagoing vessel for years. In that time, you faced down mighty storms, monsters of the deep, and those who wanted to sink your craft to the bottomless depths. Your first love is the distant line of the horizon, but the sea is in your blood.",
                "proficiencies": {
                    "skills": ["Athletics", "Perception"],
                    "tools": ["Navigator's tools", "Vehicles (water)"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Belaying pin (club)",
                    "50 feet of silk rope",
                    "Lucky charm such as a rabbit foot or small stone",
                    "Set of common clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "Ship’s Passage",
                    "description": "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship with which you have good relations."
                },
                "system_specific_data": None
            },
            {
                "name": "Soldier",
                "description": "War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, learned basic survival techniques, including how to stay alive on the battlefield.",
                "proficiencies": {
                    "skills": ["Athletics", "Intimidation"],
                    "tools": ["One type of gaming set", "Vehicles (land)"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Insignia of rank",
                    "Trophy taken from a fallen enemy (dagger, broken blade, or piece of a banner)",
                    "Set of bone dice or deck of cards",
                    "Set of common clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "Military Rank",
                    "description": "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank."
                },
                "system_specific_data": None
            },
            {
                "name": "Urchin",
                "description": "You grew up on the streets alone, orphaned, and poor, enduring the hardships of life in the slums. You had no one to watch over you or to provide for you, so you learned to provide for yourself.",
                "proficiencies": {
                    "skills": ["Sleight of Hand", "Stealth"],
                    "tools": ["Disguise kit", "Thieves' tools"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Small knife",
                    "Map of the city you grew up in",
                    "Pet mouse",
                    "Token to remember your parents by",
                    "Set of common clothes",
                    "Belt pouch containing 10 gold pieces"
                ],
                "languages": [],
                "background_features": {
                    "name": "City Secrets",
                    "description": "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."
                },
                "system_specific_data": None
            }
        ],
        "Pathfinder": [
            {
                "name": "Acolyte",
                "description": "You spent your formative years serving a deity, learning sacred rites and the mysteries of the divine.",
                "proficiencies": {
                    "skills": ["Religion"],
                    "lore": ["Temple Lore"]
                },
                "ability_score_increases": {
                    "Wisdom": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Student of the Canon"],
                "choosable_feats": None,
                "equipment": [
                    "Holy symbol",
                    "Religious text",
                    "Vestments",
                    "10 silver pieces"
                ],
                "languages": ["Celestial", "One other language of your choice"],
                "background_features": {
                    "name": "Divine Initiate",
                    "description": "You are trained in the Religion skill and Temple Lore. You gain the Student of the Canon skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Craftsman",
                "description": "You have honed your skills in a particular craft, creating goods that are both practical and beautiful.",
                "proficiencies": {
                    "skills": ["Crafting"],
                    "lore": ["Guild Lore"]
                },
                "ability_score_increases": {
                    "Intelligence": 1,
                    "Dexterity": 1
                },
                "granted_feats": ["Specialty Crafting"],
                "choosable_feats": None,
                "equipment": [
                    "Artisan’s tools",
                    "50 silver pieces worth of raw materials",
                    "10 silver pieces"
                ],
                "languages": ["Dwarven", "One other language of your choice"],
                "background_features": {
                    "name": "Guild Artisan",
                    "description": "You are trained in the Crafting skill and Guild Lore. You gain the Specialty Crafting skill feat for a specific type of craft."
                },
                "system_specific_data": None
            },
            {
                "name": "Merchant",
                "description": "You spent years working in commerce, learning the ins and outs of trade and negotiation.",
                "proficiencies": {
                    "skills": ["Diplomacy"],
                    "lore": ["Mercantile Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Bargain Hunter"],
                "choosable_feats": None,
                "equipment": [
                    "Ledgers",
                    "Set of scales",
                    "20 silver pieces",
                    "10 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Trade Savvy",
                    "description": "You are trained in the Diplomacy skill and Mercantile Lore. You gain the Bargain Hunter skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Outlander",
                "description": "You hail from the wilderness, learning how to survive and thrive in untamed lands.",
                "proficiencies": {
                    "skills": ["Survival"],
                    "lore": ["Wilderness Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Forager"],
                "choosable_feats": None,
                "equipment": [
                    "Hunting trap",
                    "Traveler’s clothing",
                    "Rations for a week",
                    "10 silver pieces"
                ],
                "languages": ["Common", "Sylvan"],
                "background_features": {
                    "name": "Wilderness Training",
                    "description": "You are trained in the Survival skill and Wilderness Lore. You gain the Forager skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Scholar",
                "description": "Your curiosity and intellect drove you to spend years poring over books, learning the secrets of the world.",
                "proficiencies": {
                    "skills": ["Arcana"],
                    "lore": ["Academia Lore"]
                },
                "ability_score_increases": {
                    "Intelligence": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Assured Identification"],
                "choosable_feats": None,
                "equipment": [
                    "Scholarly text",
                    "Quill and ink",
                    "Case of parchment",
                    "10 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Academic Training",
                    "description": "You are trained in the Arcana skill and Academia Lore. You gain the Assured Identification skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Entertainer",
                "description": "You have performed in front of crowds, thrilling them with your skill and charisma. Whether a musician, dancer, or stage actor, you know how to captivate an audience.",
                "proficiencies": {
                    "skills": ["Performance"],
                    "lore": ["Theater Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Dexterity": 1
                },
                "granted_feats": ["Fascinating Performance"],
                "choosable_feats": None,
                "equipment": [
                    "Musical instrument or performance prop",
                    "Fine clothes",
                    "10 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Star Performer",
                    "description": "You are trained in the Performance skill and Theater Lore. You gain the Fascinating Performance skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Gladiator",
                "description": "You are a skilled combatant who has entertained crowds by fighting in arenas. Your experience in public duels has made you adept at combat and winning over onlookers.",
                "proficiencies": {
                    "skills": ["Intimidation"],
                    "lore": ["Gladiatorial Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Charisma": 1
                },
                "granted_feats": ["Impressive Display"],
                "choosable_feats": None,
                "equipment": [
                    "Arena weapon (club, spear, or shortsword)",
                    "Light armor",
                    "10 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Arena Combatant",
                    "description": "You are trained in the Intimidation skill and Gladiatorial Lore. You gain the Impressive Display skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Sailor",
                "description": "You have spent years working on ships, learning how to handle the rigors of the open seas. Whether a merchant or a privateer, you are no stranger to hard work and danger.",
                "proficiencies": {
                    "skills": ["Athletics"],
                    "lore": ["Sailing Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Underwater Marauder"],
                "choosable_feats": None,
                "equipment": [
                    "Sailor's uniform",
                    "Navigational tools",
                    "10 silver pieces"
                ],
                "languages": ["Common", "Aquan"],
                "background_features": {
                    "name": "Seafarer",
                    "description": "You are trained in the Athletics skill and Sailing Lore. You gain the Underwater Marauder skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Street Urchin",
                "description": "You grew up in the alleys and on the rooftops of a bustling city, surviving by wit and quick reflexes. You know how to navigate the chaos of urban life.",
                "proficiencies": {
                    "skills": ["Thievery"],
                    "lore": ["City Lore"]
                },
                "ability_score_increases": {
                    "Dexterity": 1,
                    "Charisma": 1
                },
                "granted_feats": ["Pickpocket"],
                "choosable_feats": None,
                "equipment": [
                    "Small knife",
                    "Worn-out clothes",
                    "5 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Urban Survivalist",
                    "description": "You are trained in the Thievery skill and City Lore. You gain the Pickpocket skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Soldier",
                "description": "You were trained in the art of warfare, learning how to fight as part of an organized unit. You are accustomed to discipline and hardship.",
                "proficiencies": {
                    "skills": ["Warfare Lore"],
                    "lore": ["Military Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Shield Block"],
                "choosable_feats": None,
                "equipment": [
                    "Shield",
                    "Military uniform",
                    "10 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Combat Trained",
                    "description": "You are trained in Warfare Lore and Military Lore. You gain the Shield Block skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Animal Whisperer",
                "description": "You have a knack for understanding animals and calming them, whether as a trainer, rancher, or naturalist.",
                "proficiencies": {
                    "skills": ["Nature"],
                    "lore": ["Animal Lore"]
                },
                "ability_score_increases": {
                    "Wisdom": 1,
                    "Charisma": 1
                },
                "granted_feats": ["Train Animal"],
                "choosable_feats": None,
                "equipment": [
                    "Whistle",
                    "Simple feed",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Animal Affinity",
                    "description": "You are trained in the Nature skill and Animal Lore. You gain the Train Animal skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Artisan",
                "description": "You have studied a craft and take pride in creating objects of utility or beauty.",
                "proficiencies": {
                    "skills": ["Crafting"],
                    "lore": ["Artisan Lore"]
                },
                "ability_score_increases": {
                    "Intelligence": 1,
                    "Strength": 1
                },
                "granted_feats": ["Specialty Crafting"],
                "choosable_feats": None,
                "equipment": [
                    "Crafting tools",
                    "50 silver pieces worth of raw materials",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Craftsmanship",
                    "description": "You are trained in the Crafting skill and Artisan Lore. You gain the Specialty Crafting skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Artist",
                "description": "Your passion for creativity drives you to produce visual or auditory masterpieces, whether paintings, sculptures, or music.",
                "proficiencies": {
                    "skills": ["Performance"],
                    "lore": ["Art Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Dexterity": 1
                },
                "granted_feats": ["Fascinating Performance"],
                "choosable_feats": None,
                "equipment": [
                    "Art supplies or musical instrument",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Creative Flair",
                    "description": "You are trained in the Performance skill and Art Lore. You gain the Fascinating Performance skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Barkeep",
                "description": "As the keeper of an inn or tavern, you’ve heard countless tales and know how to deal with rowdy patrons.",
                "proficiencies": {
                    "skills": ["Diplomacy"],
                    "lore": ["Alcohol Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Hobnobber"],
                "choosable_feats": None,
                "equipment": [
                    "Tankard",
                    "Towel",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Hospitality Expert",
                    "description": "You are trained in the Diplomacy skill and Alcohol Lore. You gain the Hobnobber skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Bounty Hunter",
                "description": "You excel at tracking down individuals, whether for justice, vengeance, or profit.",
                "proficiencies": {
                    "skills": ["Survival"],
                    "lore": ["Bounty Hunter Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Experienced Tracker"],
                "choosable_feats": None,
                "equipment": [
                    "Rope",
                    "Manacles",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Tracker",
                    "description": "You are trained in the Survival skill and Bounty Hunter Lore. You gain the Experienced Tracker skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Charlatan",
                "description": "You make a living by convincing others of falsehoods, selling fake remedies, or impersonating others.",
                "proficiencies": {
                    "skills": ["Deception"],
                    "lore": ["Underworld Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Dexterity": 1
                },
                "granted_feats": ["Lie to Me"],
                "choosable_feats": None,
                "equipment": [
                    "Disguise kit",
                    "False credentials",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Con Artist",
                    "description": "You are trained in the Deception skill and Underworld Lore. You gain the Lie to Me skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Criminal",
                "description": "You are no stranger to the underworld, having made your living through theft, smuggling, or other illicit activities.",
                "proficiencies": {
                    "skills": ["Stealth"],
                    "lore": ["Underworld Lore"]
                },
                "ability_score_increases": {
                    "Dexterity": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Pickpocket"],
                "choosable_feats": None,
                "equipment": [
                    "Lockpicks",
                    "Dark clothing",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Underworld Connections",
                    "description": "You are trained in the Stealth skill and Underworld Lore. You gain the Pickpocket skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Farmhand",
                "description": "You grew up performing manual labor on a farm, developing a strong physique and a deep connection to the land.",
                "proficiencies": {
                    "skills": ["Athletics"],
                    "lore": ["Farming Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Hefty Hauler"],
                "choosable_feats": None,
                "equipment": [
                    "Pitchfork or shovel",
                    "Work clothes",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Hard Labor",
                    "description": "You are trained in the Athletics skill and Farming Lore. You gain the Hefty Hauler skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Field Medic",
                "description": "You’ve spent time treating the sick and wounded, gaining knowledge of how to save lives in critical moments.",
                "proficiencies": {
                    "skills": ["Medicine"],
                    "lore": ["Anatomy Lore"]
                },
                "ability_score_increases": {
                    "Wisdom": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Battle Medicine"],
                "choosable_feats": None,
                "equipment": [
                    "Healer’s tools",
                    "Bandages",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Medical Expertise",
                    "description": "You are trained in the Medicine skill and Anatomy Lore. You gain the Battle Medicine skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Fortune Teller",
                "description": "You’ve honed your ability to interpret signs and predict events, captivating audiences with your foresight.",
                "proficiencies": {
                    "skills": ["Occultism"],
                    "lore": ["Fortune-Telling Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Oddity Identification"],
                "choosable_feats": None,
                "equipment": [
                    "Tarot cards or crystal ball",
                    "Flowing robes",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Divinatory Insight",
                    "description": "You are trained in the Occultism skill and Fortune-Telling Lore. You gain the Oddity Identification skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Guard",
                "description": "You’ve trained in maintaining order and protecting those under your care, often serving in a city watch or as a personal protector.",
                "proficiencies": {
                    "skills": ["Intimidation"],
                    "lore": ["Legal Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Charisma": 1
                },
                "granted_feats": ["Quick Coercion"],
                "choosable_feats": None,
                "equipment": [
                    "Spear",
                    "Shield",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Protector's Discipline",
                    "description": "You are trained in the Intimidation skill and Legal Lore. You gain the Quick Coercion skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Herbalist",
                "description": "You’ve studied the properties of plants and their uses in healing or harmful remedies.",
                "proficiencies": {
                    "skills": ["Nature"],
                    "lore": ["Herbalism Lore"]
                },
                "ability_score_increases": {
                    "Wisdom": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Natural Medicine"],
                "choosable_feats": None,
                "equipment": [
                    "Herbalist’s kit",
                    "Dried herbs",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Herbal Expertise",
                    "description": "You are trained in the Nature skill and Herbalism Lore. You gain the Natural Medicine skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Hunter",
                "description": "You’ve spent time stalking prey in the wilderness, honing your skills with ranged weapons and tracking.",
                "proficiencies": {
                    "skills": ["Survival"],
                    "lore": ["Hunting Lore"]
                },
                "ability_score_increases": {
                    "Dexterity": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Survey Wildlife"],
                "choosable_feats": None,
                "equipment": [
                    "Bow and 20 arrows",
                    "Hunting trap",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Wilderness Tracker",
                    "description": "You are trained in the Survival skill and Hunting Lore. You gain the Survey Wildlife skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Laborer",
                "description": "Your years of manual labor have given you great physical strength and endurance.",
                "proficiencies": {
                    "skills": ["Athletics"],
                    "lore": ["Labor Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Hefty Hauler"],
                "choosable_feats": None,
                "equipment": [
                    "Work gloves",
                    "Toolkit",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Strengthened Body",
                    "description": "You are trained in the Athletics skill and Labor Lore. You gain the Hefty Hauler skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Miner",
                "description": "You’ve toiled in the depths of the earth, unearthing precious metals and gems.",
                "proficiencies": {
                    "skills": ["Survival"],
                    "lore": ["Mining Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Hardy Traveler"],
                "choosable_feats": None,
                "equipment": [
                    "Mining pick",
                    "Lantern",
                    "10 silver pieces"
                ],
                "languages": ["Common", "Dwarven"],
                "background_features": {
                    "name": "Underground Expertise",
                    "description": "You are trained in the Survival skill and Mining Lore. You gain the Hardy Traveler skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Noble",
                "description": "Born to wealth and privilege, you have been groomed to navigate high society and command respect.",
                "proficiencies": {
                    "skills": ["Diplomacy"],
                    "lore": ["Nobility Lore"]
                },
                "ability_score_increases": {
                    "Charisma": 1,
                    "Intelligence": 1
                },
                "granted_feats": ["Courtly Graces"],
                "choosable_feats": None,
                "equipment": [
                    "Fine clothing",
                    "Signet ring",
                    "15 silver pieces"
                ],
                "languages": ["Common", "One other language of your choice"],
                "background_features": {
                    "name": "Social Grace",
                    "description": "You are trained in the Diplomacy skill and Nobility Lore. You gain the Courtly Graces skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Scout",
                "description": "You are adept at reconnaissance and navigating difficult terrain, excelling in gathering information on the move.",
                "proficiencies": {
                    "skills": ["Survival"],
                    "lore": ["Scouting Lore"]
                },
                "ability_score_increases": {
                    "Dexterity": 1,
                    "Wisdom": 1
                },
                "granted_feats": ["Terrain Stalker"],
                "choosable_feats": None,
                "equipment": [
                    "Map and compass",
                    "Cloak",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Reconnaissance Expert",
                    "description": "You are trained in the Survival skill and Scouting Lore. You gain the Terrain Stalker skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Tinker",
                "description": "You’ve spent years repairing and creating useful tools and gadgets, using both ingenuity and dexterity.",
                "proficiencies": {
                    "skills": ["Crafting"],
                    "lore": ["Engineering Lore"]
                },
                "ability_score_increases": {
                    "Intelligence": 1,
                    "Dexterity": 1
                },
                "granted_feats": ["Specialty Crafting"],
                "choosable_feats": None,
                "equipment": [
                    "Tinker’s tools",
                    "Scrap materials",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Innovator",
                    "description": "You are trained in the Crafting skill and Engineering Lore. You gain the Specialty Crafting skill feat."
                },
                "system_specific_data": None
            },
            {
                "name": "Warrior",
                "description": "You have dedicated your life to the mastery of martial combat, training to become a formidable fighter.",
                "proficiencies": {
                    "skills": ["Athletics"],
                    "lore": ["Warfare Lore"]
                },
                "ability_score_increases": {
                    "Strength": 1,
                    "Constitution": 1
                },
                "granted_feats": ["Shield Block"],
                "choosable_feats": None,
                "equipment": [
                    "Weapon of choice",
                    "Shield",
                    "10 silver pieces"
                ],
                "languages": ["Common"],
                "background_features": {
                    "name": "Martial Prowess",
                    "description": "You are trained in the Athletics skill and Warfare Lore. You gain the Shield Block skill feat."
                },
                "system_specific_data": None
            }
        ],
        "Star Wars: Edge of the Empire": [
            {
                "name": "Bounty Hunter",
                "description": "You are a skilled tracker and fighter, known for pursuing individuals across the galaxy for a reward. Whether you work for the Hutts, a bounty hunter guild, or operate independently, you thrive in high-stakes pursuits.",
                "proficiencies": {
                    "skills": ["Perception", "Survival"],
                    "tools": ["Blaster proficiency", "Tracking devices"]
                },
                "ability_score_increases": {
                    "Agility": 1,
                    "Cunning": 1
                },
                "granted_feats": ["Quick Draw"],
                "choosable_feats": ["Deadly Accuracy"],
                "equipment": [
                    "Blaster pistol",
                    "Tracking fob",
                    "Utility belt",
                    "Comlink",
                    "500 credits"
                ],
                "languages": ["Basic", "One other language of your choice"],
                "background_features": {
                    "name": "Relentless Pursuit",
                    "description": "You have an extensive network of contacts in the underworld and law enforcement who can provide information about your quarry. This grants you advantage on checks related to locating individuals."
                },
                "system_specific_data": None
            },
            {
                "name": "Smuggler",
                "description": "You make your living moving illegal or restricted goods across the galaxy. Whether working with the Rebel Alliance, criminal syndicates, or simply for profit, you are adept at avoiding trouble with the authorities.",
                "proficiencies": {
                    "skills": ["Deception", "Piloting (Space)"],
                    "tools": ["Astrogation charts", "Modified freighter tools"]
                },
                "ability_score_increases": {
                    "Cunning": 1,
                    "Presence": 1
                },
                "granted_feats": ["Sleight of Hand"],
                "choosable_feats": ["Astrogation Expert"],
                "equipment": [
                    "Blaster pistol",
                    "Fake identification card",
                    "Data pad",
                    "500 credits",
                    "Cargo container with hidden compartment"
                ],
                "languages": ["Basic", "Huttese"],
                "background_features": {
                    "name": "Under the Radar",
                    "description": "You have an uncanny ability to evade patrols and scanners. Gain advantage on checks to avoid detection during space travel."
                },
                "system_specific_data": None
            },
            {
                "name": "Rebel Operative",
                "description": "You are a member of the Rebel Alliance, working to undermine the Galactic Empire. Whether as a soldier, spy, or engineer, you risk everything for freedom and justice.",
                "proficiencies": {
                    "skills": ["Athletics", "Mechanics"],
                    "tools": ["Explosives", "Communications equipment"]
                },
                "ability_score_increases": {
                    "Brawn": 1,
                    "Intellect": 1
                },
                "granted_feats": ["Leadership"],
                "choosable_feats": ["Demolition Expert"],
                "equipment": [
                    "Blaster carbine",
                    "Explosives kit",
                    "Rebel insignia",
                    "Comlink",
                    "200 credits"
                ],
                "languages": ["Basic", "Binary (Droidspeak)"],
                "background_features": {
                    "name": "Alliance Support",
                    "description": "You can call upon Rebel Alliance resources for limited aid. This includes transport, intelligence, or basic supplies when operating in friendly territory."
                },
                "system_specific_data": None
            },
            {
                "name": "Colonist",
                "description": "You are a civilian from one of the many colonized worlds in the galaxy. Whether as a doctor, scientist, or entrepreneur, you possess specialized knowledge that sets you apart.",
                "proficiencies": {
                    "skills": ["Medicine", "Knowledge (Outer Rim)"],
                    "tools": ["Medical kit", "Diagnostic scanner"]
                },
                "ability_score_increases": {
                    "Intellect": 2
                },
                "granted_feats": ["Improvised Healer"],
                "choosable_feats": ["Field Medic"],
                "equipment": [
                    "Datapad",
                    "Portable laboratory",
                    "Medical supplies",
                    "300 credits"
                ],
                "languages": ["Basic", "One other language of your choice"],
                "background_features": {
                    "name": "Specialized Knowledge",
                    "description": "Your expertise in a particular field grants you advantage on skill checks related to that subject."
                },
                "system_specific_data": None
            },
            {
                "name": "Explorer",
                "description": "You are driven to discover the galaxy's uncharted regions. Whether searching for lost civilizations or resource-rich worlds, you thrive in the unknown.",
                "proficiencies": {
                    "skills": ["Survival", "Piloting (Planetary)"],
                    "tools": ["Mapping equipment", "Survey drones"]
                },
                "ability_score_increases": {
                    "Cunning": 1,
                    "Brawn": 1
                },
                "granted_feats": ["Pathfinder"],
                "choosable_feats": ["Cartographer"],
                "equipment": [
                    "Survey equipment",
                    "Blaster pistol",
                    "Explorer's pack",
                    "Comlink",
                    "400 credits"
                ],
                "languages": ["Basic", "One rare language of your choice"],
                "background_features": {
                    "name": "Trailblazer",
                    "description": "You can guide your allies through difficult terrain with ease. Allies gain advantage on survival checks when following your lead."
                },
                "system_specific_data": None
            },
            {
                "name": "Technician",
                "description": "Technicians are highly skilled individuals who specialize in crafting, maintaining, and improving technology, from starships and droids to slicing computer systems. Often underestimated, their knowledge and ingenuity can turn the tide in any situation.",
                "proficiencies": {
                    "skills": ["Mechanics", "Computers"],
                    "tools": ["Toolkit", "Slicing tools"]
                },
                "ability_score_increases": {
                    "Intellect": 2
                },
                "granted_feats": ["Tinkerer"],
                "choosable_feats": ["Slicer"],
                "equipment": [
                    "Tool kit",
                    "Portable computer terminal",
                    "Comlink",
                    "Datapad with schematics",
                    "300 credits"
                ],
                "languages": ["Basic", "Binary (Droidspeak)"],
                "background_features": {
                    "name": "Technical Expertise",
                    "description": "You have an intuitive understanding of technology. You gain advantage on skill checks related to repairing or modifying mechanical devices."
                },
                "system_specific_data": None
            },
            {
                "name": "Hired Gun",
                "description": "A professional soldier or enforcer who specializes in combat for hire. Whether working for a criminal syndicate, a corporate interest, or as an independent mercenary, your skillset ensures you are a force to be reckoned with.",
                "proficiencies": {
                    "skills": ["Athletics", "Ranged (Heavy)"],
                    "tools": ["Combat training", "Explosives handling"]
                },
                "ability_score_increases": {
                    "Brawn": 2
                },
                "granted_feats": ["Toughness"],
                "choosable_feats": ["Deadly Accuracy"],
                "equipment": [
                    "Blaster rifle",
                    "Fragmentation grenade",
                    "Combat knife",
                    "Armor (light)",
                    "400 credits"
                ],
                "languages": ["Basic"],
                "background_features": {
                    "name": "Combat Veteran",
                    "description": "Your extensive experience in battle gives you advantage on initiative rolls and checks related to combat tactics."
                },
                "system_specific_data": None
            },
            {
                "name": "Ace",
                "description": "Aces are the best pilots and vehicle operators in the galaxy, excelling in both high-speed maneuvers and combat. Whether piloting a starfighter or a speeder bike, you are unmatched in your ability to navigate treacherous situations.",
                "proficiencies": {
                    "skills": ["Piloting (Space)", "Piloting (Planetary)"],
                    "tools": ["Navigation charts", "Starship systems"]
                },
                "ability_score_increases": {
                    "Agility": 2
                },
                "granted_feats": ["Quick Reflexes"],
                "choosable_feats": ["Starship Ace"],
                "equipment": [
                    "Flight suit",
                    "Helmet with targeting visor",
                    "Blaster pistol",
                    "Comlink",
                    "Astromech droid (optional, subject to GM approval)",
                    "500 credits"
                ],
                "languages": ["Basic", "One other language of your choice"],
                "background_features": {
                    "name": "Ace Pilot",
                    "description": "You are an expert in piloting vehicles. Gain advantage on checks related to maneuvering starships or vehicles, especially in high-pressure situations."
                },
                "system_specific_data": None
            },
            {
                "name": "Diplomat",
                "description": "Diplomats are masters of negotiation, political maneuvering, and fostering alliances. Whether working for the Rebel Alliance or an independent faction, you are skilled at resolving conflicts and influencing decisions.",
                "proficiencies": {
                    "skills": ["Negotiation", "Knowledge (Core Worlds)"],
                    "tools": ["Etiquette training", "Formal attire"]
                },
                "ability_score_increases": {
                    "Presence": 2
                },
                "granted_feats": ["Silver Tongue"],
                "choosable_feats": ["Inspirational Leader"],
                "equipment": [
                    "Formal attire",
                    "Comlink",
                    "Data pad with diplomatic credentials",
                    "Recording device",
                    "500 credits"
                ],
                "languages": ["Basic", "One other language of your choice"],
                "background_features": {
                    "name": "Diplomatic Immunity",
                    "description": "Your diplomatic status allows you to gain safe passage in neutral or hostile territories. You gain advantage on checks to avoid trouble when displaying credentials."
                },
                "system_specific_data": None
            },
            {
                "name": "Force-Sensitive Exile",
                "description": "As a Force-sensitive individual, you have discovered or rediscovered your connection to the Force. Hunted by the Empire, you hide your abilities while trying to understand and control them.",
                "proficiencies": {
                    "skills": ["Discipline", "Perception"],
                    "tools": ["None"]
                },
                "ability_score_increases": {
                    "Willpower": 1,
                    "Cunning": 1
                },
                "granted_feats": ["Force Awareness"],
                "choosable_feats": ["Force Control"],
                "equipment": [
                    "Concealed lightsaber or training blade (optional, subject to GM approval)",
                    "Simple robes",
                    "Holocron (optional, subject to GM approval)",
                    "300 credits"
                ],
                "languages": ["Basic"],
                "background_features": {
                    "name": "Connection to the Force",
                    "description": "Your connection to the Force grants you insight into the world around you. You gain advantage on checks related to sensing danger or detecting others' emotions."
                },
                "system_specific_data": None
            },
        ],
        "Call of Cthulhu": [
            {
                "name": "Antiquarian",
                "description": "You specialize in the collection and study of antiques, artifacts, and rare books. You have a deep knowledge of history and a network of contacts in academic and collector circles.",
                "proficiencies": {
                    "skills": ["Appraise", "History", "Library Use", "Spot Hidden", "Other Language (Choose one)", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Magnifying glass",
                    "Notebook",
                    "Collection of antiques or rare books"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Historical Expertise",
                    "description": "You gain an edge in identifying the origins and significance of historical artifacts and documents."
                },
                "system_specific_data": {
                    "income_range": "10–40% Credit Rating"
                }
            },
            {
                "name": "Detective",
                "description": "You are skilled in solving crimes and uncovering hidden truths. Whether a private investigator or a law enforcement officer, you know how to find clues and piece together evidence.",
                "proficiencies": {
                    "skills": ["Law", "Spot Hidden", "Psychology", "Persuade", "Library Use", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Notebook",
                    "Badge or credentials (if law enforcement)",
                    "Revolver or standard firearm"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Investigative Skills",
                    "description": "You gain advantage when following leads or interrogating suspects."
                },
                "system_specific_data": {
                    "income_range": "20–60% Credit Rating"
                }
            },
            {
                "name": "Doctor of Medicine",
                "description": "You are a trained medical professional, skilled in diagnosing and treating physical ailments. Your knowledge of anatomy and health is invaluable.",
                "proficiencies": {
                    "skills": ["First Aid", "Medicine", "Biology", "Psychology", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Medical bag",
                    "Set of surgical tools",
                    "Reference book on medicine"
                ],
                "languages": ["English", "Latin (optional for medical terms)"],
                "background_features": {
                    "name": "Medical Expertise",
                    "description": "You gain proficiency in diagnosing and treating injuries or illnesses."
                },
                "system_specific_data": {
                    "income_range": "30–80% Credit Rating"
                }
            },
            {
                "name": "Professor",
                "description": "You are an academic, teaching and researching in your field of expertise. Your knowledge is broad, and your ability to inspire others makes you a valuable ally.",
                "proficiencies": {
                    "skills": ["Library Use", "Own Language", "History", "Anthropology", "Archaeology", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Textbooks",
                    "Notes on lectures",
                    "Academic robes"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Academic Network",
                    "description": "You can access university libraries and call upon academic colleagues for assistance."
                },
                "system_specific_data": {
                    "income_range": "20–70% Credit Rating"
                }
            },
            {
                "name": "Journalist",
                "description": "You are adept at gathering information and reporting it to the public. Whether working for a newspaper or as a freelancer, you know how to find and tell a compelling story.",
                "proficiencies": {
                    "skills": ["Library Use", "Fast Talk", "Spot Hidden", "Photography", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Notebook",
                    "Camera",
                    "Press credentials"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Scoop Finder",
                    "description": "You excel at uncovering leads and gaining the trust of informants."
                },
                "system_specific_data": {
                    "income_range": "10–40% Credit Rating"
                }
            },
            {
                "name": "Dilettante",
                "description": "As a person of wealth and privilege, you have the freedom to pursue hobbies and adventures. You are well-connected and enjoy the finer things in life.",
                "proficiencies": {
                    "skills": ["Credit Rating", "Art/Craft (Choose one)", "History", "Other Language (Choose one)", "Library Use"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Elegant wardrobe",
                    "Personal collection of antiques or art",
                    "Social contacts in high society"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Socialite's Charm",
                    "description": "You gain proficiency in social interactions with the wealthy or influential."
                },
                "system_specific_data": {
                    "income_range": "50–99% Credit Rating"
                }
            },
            {
                "name": "Explorer",
                "description": "You are a daring adventurer, traveling to distant and often dangerous locations. You thrive in the wilderness and in the unknown.",
                "proficiencies": {
                    "skills": ["Survival", "Climb", "Swim", "Navigate", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Compass",
                    "Rope",
                    "Adventurer's gear"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Explorer’s Instinct",
                    "description": "You gain an edge in navigating unfamiliar terrain and identifying hazards."
                },
                "system_specific_data": {
                    "income_range": "10–50% Credit Rating"
                }
            },
            {
                "name": "Author",
                "description": "You are a writer, expressing ideas through novels, short stories, or investigative journalism. Your ability to craft compelling narratives is unmatched.",
                "proficiencies": {
                    "skills": ["Library Use", "Own Language", "History", "Psychology", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Notebook",
                    "Writing tools",
                    "Published works"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Wordsmith",
                    "description": "You gain proficiency in written communication and can influence others through your works."
                },
                "system_specific_data": {
                    "income_range": "10–30% Credit Rating"
                }
            },
            {
                "name": "Archaeologist",
                "description": "You study ancient cultures through excavation and analysis of artifacts, often working in remote and challenging environments.",
                "proficiencies": {
                    "skills": ["Appraise", "Archaeology", "History", "Library Use", "Other Language (Choose one)", "Spot Hidden", "Navigate", "Science (Choose one)"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Notebook",
                    "Excavation tools",
                    "Reference books"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Field Expertise",
                    "description": "You excel at identifying and preserving artifacts and navigating difficult terrains."
                },
                "system_specific_data": {
                    "income_range": "10–50% Credit Rating"
                }
            },
            {
                "name": "Artist",
                "description": "You create visual, auditory, or performance-based works to express ideas or emotions. Your creativity makes you adaptable and resourceful.",
                "proficiencies": {
                    "skills": ["Art (Choose one)", "History", "Psychology", "Spot Hidden", "Own Language", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Art supplies or performance equipment",
                    "Portfolio of past works"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Creative Intuition",
                    "description": "You gain insight into cultural or artistic patterns and meanings."
                },
                "system_specific_data": {
                    "income_range": "10–40% Credit Rating"
                }
            },
            {
                "name": "Soldier",
                "description": "You are trained military personnel with experience in combat, survival, and tactical operations.",
                "proficiencies": {
                    "skills": ["Firearms", "Survival", "Dodge", "Fighting (Choose one)", "Climb", "Mechanical Repair", "First Aid"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Military uniform",
                    "Standard firearm",
                    "Combat knife"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Combat Training",
                    "description": "You are skilled in combat and survival techniques."
                },
                "system_specific_data": {
                    "income_range": "10–50% Credit Rating"
                }
            },
            {
                "name": "Engineer",
                "description": "You design, build, and maintain structures or mechanical systems, often applying your expertise to solve technical challenges.",
                "proficiencies": {
                    "skills": ["Mechanical Repair", "Science (Physics or Engineering)", "Navigate", "Spot Hidden", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Toolbox",
                    "Blueprints or technical plans"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Technical Expertise",
                    "description": "You gain proficiency in diagnosing and solving mechanical problems."
                },
                "system_specific_data": {
                    "income_range": "20–60% Credit Rating"
                }
            },
            {
                "name": "Lawyer",
                "description": "You are trained in legal knowledge and negotiation, often representing others in court or providing legal advice.",
                "proficiencies": {
                    "skills": ["Law", "Library Use", "Persuade", "Psychology", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Legal texts",
                    "Writing tools"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Legal Expertise",
                    "description": "You gain proficiency in interpreting laws and using them to your advantage."
                },
                "system_specific_data": {
                    "income_range": "20–80% Credit Rating"
                }
            },
            {
                "name": "Clergy",
                "description": "You serve as a spiritual guide and leader, offering counsel and performing sacred rites.",
                "proficiencies": {
                    "skills": ["Psychology", "History", "Other Language (Latin or Greek)", "Persuade", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Holy book",
                    "Ceremonial robes"
                ],
                "languages": ["English", "Latin (or other sacred language)"],
                "background_features": {
                    "name": "Spiritual Guidance",
                    "description": "You provide counsel and gain the trust of those in need of support."
                },
                "system_specific_data": {
                    "income_range": "10–40% Credit Rating"
                }
            },
            {
                "name": "Nurse",
                "description": "You assist in medical care, providing support to doctors and tending to patients in need.",
                "proficiencies": {
                    "skills": ["First Aid", "Medicine", "Psychology", "Listen", "Spot Hidden"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Medical supplies",
                    "Nursing uniform"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Caregiver",
                    "description": "You excel in assisting and calming patients during medical emergencies."
                },
                "system_specific_data": {
                    "income_range": "10–30% Credit Rating"
                }
            },
            {
                "name": "Pilot",
                "description": "You are skilled in operating aircraft, whether commercial or military, with a talent for navigation and quick reflexes.",
                "proficiencies": {
                    "skills": ["Pilot", "Navigate", "Mechanical Repair", "Spot Hidden", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Flight jacket",
                    "Navigation tools"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Aviation Expertise",
                    "description": "You gain proficiency in flying aircraft and reading flight paths."
                },
                "system_specific_data": {
                    "income_range": "20–60% Credit Rating"
                }
            },
            {
                "name": "Scientist",
                "description": "You are an academic or professional dedicated to the pursuit of knowledge in a particular field of science.",
                "proficiencies": {
                    "skills": ["Science (Choose one)", "Library Use", "Other Language (Choose one)", "Psychology", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Laboratory tools",
                    "Research notes"
                ],
                "languages": ["English", "One other language of your choice"],
                "background_features": {
                    "name": "Scientific Expertise",
                    "description": "You excel at conducting research and solving scientific problems."
                },
                "system_specific_data": {
                    "income_range": "20–70% Credit Rating"
                }
            },
            {
                "name": "Tradesperson",
                "description": "You are skilled in a particular craft or trade, such as carpentry, blacksmithing, or mechanics.",
                "proficiencies": {
                    "skills": ["Mechanical Repair", "Appraise", "Craft (Choose one)", "Spot Hidden", "Credit Rating"]
                },
                "ability_score_increases": None,
                "granted_feats": None,
                "choosable_feats": None,
                "equipment": [
                    "Toolset for trade",
                    "Work gloves"
                ],
                "languages": ["English"],
                "background_features": {
                    "name": "Skilled Artisan",
                    "description": "You excel at creating and maintaining functional tools and objects."
                },
                "system_specific_data": {
                    "income_range": "10–40% Credit Rating"
                }
            }
        ]
    }

    alignments = {
        "Dungeons & Dragons 5th Edition": [
            {
                "name": "Lawful Good",
                "description": "Lawful good characters believe that a strong, well-ordered society with a well-established code of conduct can make life better for the majority of people. Lawful good characters will support just laws and honor agreements.",
                "moral_axis": "Good",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "Neutral Good",
                "description": "Neutral good characters do the best they can to help others according to their needs. They do not feel beholden to any particular moral code or order, but instead strive to do the most good in a situation.",
                "moral_axis": "Good",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Good",
                "description": "Chaotic good characters act as their conscience directs, with little regard for what others expect. They believe in doing what is right, but their methods may be unconventional or even disruptive.",
                "moral_axis": "Good",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            },
            {
                "name": "Lawful Neutral",
                "description": "Lawful neutral characters follow the law or a code of conduct strictly, whether it is good or bad. They believe in order, but not necessarily in promoting good or evil—stability is paramount.",
                "moral_axis": "Neutral",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "True Neutral",
                "description": "True neutral characters do not feel compelled to choose between good and evil or law and chaos. They act according to their own needs and the needs of the situation, without attachment to a particular philosophy or code.",
                "moral_axis": "Neutral",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Neutral",
                "description": "Chaotic neutral characters follow their own whims and are individualistic above all. They prioritize personal freedom, often disregarding laws and traditions, and believe that chaos is the natural state of the universe.",
                "moral_axis": "Neutral",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            },
            {
                "name": "Lawful Evil",
                "description": "Lawful evil characters follow a code or a set of rules, but their purpose is primarily to dominate or gain power. They believe that society functions best when it is structured and ordered, but they may exploit the system to serve their own interests.",
                "moral_axis": "Evil",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "Neutral Evil",
                "description": "Neutral evil characters do whatever they can get away with, without regard for law or chaos. They care only for themselves and do not care who they hurt or what they destroy in their pursuit of personal gain.",
                "moral_axis": "Evil",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Evil",
                "description": "Chaotic evil characters thrive on chaos and destruction. They act with complete disregard for laws, customs, or human life, seeking to sow discord wherever they go.",
                "moral_axis": "Evil",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            }
        ],
        "Pathfinder": [
            {
                "name": "Lawful Good",
                "description": "Lawful good characters act with compassion and honor, combining a commitment to helping others with a respect for law and tradition.",
                "moral_axis": "Good",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "Neutral Good",
                "description": "Neutral good characters act altruistically, striving to do the best they can to help others without any particular regard for law or chaos.",
                "moral_axis": "Good",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Good",
                "description": "Chaotic good characters follow their conscience, striving to make the world better while valuing freedom over order.",
                "moral_axis": "Good",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            },
            {
                "name": "Lawful Neutral",
                "description": "Lawful neutral characters value structure and order, adhering strictly to laws, traditions, or a personal code.",
                "moral_axis": "Neutral",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "True Neutral",
                "description": "True neutral characters prefer to maintain balance and avoid extreme actions, neither wholly good nor wholly evil, lawful nor chaotic.",
                "moral_axis": "Neutral",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Neutral",
                "description": "Chaotic neutral characters follow their whims, valuing freedom and individuality, often acting unpredictably without moral or ethical considerations.",
                "moral_axis": "Neutral",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            },
            {
                "name": "Lawful Evil",
                "description": "Lawful evil characters use law, tradition, or a personal code to further their own goals, often at the expense of others.",
                "moral_axis": "Evil",
                "ethical_axis": "Lawful",
                "system_specific_data": None
            },
            {
                "name": "Neutral Evil",
                "description": "Neutral evil characters are selfish and ruthless, doing whatever they can to advance their own interests regardless of laws or chaos.",
                "moral_axis": "Evil",
                "ethical_axis": "Neutral",
                "system_specific_data": None
            },
            {
                "name": "Chaotic Evil",
                "description": "Chaotic evil characters act purely out of self-interest and cruelty, thriving in the destruction and suffering of others.",
                "moral_axis": "Evil",
                "ethical_axis": "Chaotic",
                "system_specific_data": None
            }
        ],
        "Star Wars: Edge of the Empire": [
            {
                "name": "Light Side",
                "description": "Characters aligned with the Light Side value compassion, selflessness, and the pursuit of justice and peace. They act in ways that promote harmony and protect life.",
                "moral_axis": "Good",
                "ethical_axis": "Lawful",
                "system_specific_data": {
                    "associated_mechanics": "Morality (high Light Side score)"
                }
            },
            {
                "name": "Gray",
                "description": "Gray characters tread the line between the Light and Dark sides, balancing their actions and motivations. They make choices situationally, without fully committing to either side.",
                "moral_axis": "Neutral",
                "ethical_axis": "Neutral",
                "system_specific_data": {
                    "associated_mechanics": "Balanced Morality"
                }
            },
            {
                "name": "Dark Side",
                "description": "Characters aligned with the Dark Side are driven by selfishness, hatred, and the pursuit of power, often at the expense of others and the greater good.",
                "moral_axis": "Evil",
                "ethical_axis": "Chaotic",
                "system_specific_data": {
                    "associated_mechanics": "Morality (high Dark Side score)"
                }
            },
            {
                "name": "Lawful Scoundrel",
                "description": "Lawful scoundrels adhere to personal codes or the rules of an organization, such as a bounty hunter guild or crime syndicate. They are pragmatic yet reliable in their methods.",
                "moral_axis": "Neutral",
                "ethical_axis": "Lawful",
                "system_specific_data": {
                    "associated_mechanics": "Obligation-based actions"
                }
            },
            {
                "name": "Chaotic Opportunist",
                "description": "Chaotic opportunists act on impulse and prioritize their own gain above all else. They thrive on unpredictability and exploit opportunities wherever they arise.",
                "moral_axis": "Neutral",
                "ethical_axis": "Chaotic",
                "system_specific_data": {
                    "associated_mechanics": "Obligation and Duty impact actions"
                }
            },
            {
                "name": "Rebel Patriot",
                "description": "Rebel patriots fight for freedom and justice, believing in the overthrow of oppressive systems like the Galactic Empire. They value the collective good over personal ambition.",
                "moral_axis": "Good",
                "ethical_axis": "Chaotic",
                "system_specific_data": {
                    "associated_mechanics": "Duty alignment"
                }
            },
            {
                "name": "Imperial Loyalist",
                "description": "Imperial loyalists believe in the structure and order imposed by the Empire, prioritizing stability over freedom. They value loyalty and discipline.",
                "moral_axis": "Neutral",
                "ethical_axis": "Lawful",
                "system_specific_data": {
                    "associated_mechanics": "Duty alignment"
                }
            }
        ]

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
                    rpg_system_id=system.id
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
                    rpg_system_id=system.id
                )
                db.session.add(new_feat)

        # Seed spells
        if system_data["name"] in spells:
            for spell_data in spells[system_data["name"]]:
                new_spell = Spell(
                    name=spell_data["name"],
                    description=spell_data["description"],
                    level=spell_data["level"],
                    school=spell_data.get("school"),
                    casting_time=spell_data.get("casting_time"),
                    range=spell_data.get("range"),
                    duration=spell_data.get("duration"),
                    components=spell_data.get("components"),
                    type=spell_data.get("type"),
                    strain_cost=spell_data.get("strain_cost"),
                    conflict_risk=spell_data.get('conflict_risk'),
                    
                    rpg_system_id=system.id
                )

                if "force_power_tree" in spell_data:
                    new_spell.force_power_tree = spell_data["force_power_tree"]

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
                    rpg_system_id=system.id
                )
                db.session.add(new_race)

        # Seed skills
        if system_data["name"] in skills:
            for skill_data in skills[system_data["name"]]:
                new_skill = Skill(
                    name=skill_data["name"],
                    description=skill_data["description"],
                    associated_ability=skill_data["associated_ability"],
                    rpg_system_id=system.id
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
                    material=item_data.get("material"),
                    slot_type=item_data.get("slot_type"),
                    rpg_system_id=system.id
                )
                db.session.add(new_item)
            db.session.commit()

        # Seed monsters
        if system_data["name"] in monsters:
            for monster_data in monsters[system_data["name"]]:
                new_monster = Monster(
                    name=monster_data["name"],
                    description=monster_data["description"],
                    size=monster_data["size"],
                    hit_points=monster_data["hit_points"],
                    armor_class=monster_data["armor_class"],
                    rpg_system_id=system.id
                )
                db.session.add(new_monster)


        if system_data["name"] in backgrounds:
            for background_data in backgrounds[system_data["name"]]:
                new_background = Background(
                    name=background_data["name"],
                    description=background_data["description"],
                    proficiencies=background_data["proficiencies"],
                    ability_score_increases=background_data["ability_score_increases"],
                    granted_feats=background_data["granted_feats"],
                    choosable_feats=background_data["choosable_feats"],
                    equipment=background_data["equipment"],
                    languages=background_data["languages"],
                    background_features=background_data["background_features"],
                    system_specific_data=background_data["system_specific_data"],
                    rpg_system_id=system.id
                )
                db.session.add(new_background)
            db.session.commit()

        if system_data["name"] in alignments:
            for alignment_data in alignments[system_data["name"]]:
                new_alignment = Alignment(
                    name=alignment_data["name"],
                    description=alignment_data["description"],
                    moral_axis=alignment_data["moral_axis"],
                    ethical_axis=alignment_data["ethical_axis"],
                    system_specific_data=alignment_data["system_specific_data"],
                    rpg_system_id=system.id
                )
                db.session.add(new_alignment)
            db.session.commit()
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
        db.session.query(Background).delete()
        db.session.query(Alignment).delete()
        db.session.commit()
        seed_rpg_systems()


if __name__ == '__main__':
    run_seed()
