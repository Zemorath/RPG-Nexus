from backend import create_app, db
from backend.models import RPGSystem, Class, Race, Skill, Item, Monster
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
        db.session.commit()
        seed_rpg_systems()


if __name__ == '__main__':
    run_seed()
