class CalculationService:
    def calculate_dnd5e_stats(self, character):
        """Calculate D&D 5e stats for a character."""
        character = self.calculate_ability_modifiers(character)
        character = self.calculate_initiative(character)
        character = self.calculate_armor_class(character)
        character = self.calculate_proficiency_bonus(character)
        character = self.calculate_saving_throws(character)
        character = self.calculate_skills(character)
        return character

    def calculate_ability_modifiers(self, character):
        """Calculate ability modifiers for D&D 5e."""
        ability_scores = character.get('ability_scores', {})
        character['ability_modifiers'] = {}
        
        for ability, score in ability_scores.items():
            modifier = (score - 10) // 2
            character['ability_modifiers'][ability] = modifier
        
        return character

    def calculate_initiative(self, character):
        """Calculate initiative for D&D 5e."""
        character['initiative'] = character['ability_modifiers'].get('Dexterity', 0)
        return character

    def calculate_armor_class(self, character):
        """Calculate armor class for D&D 5e (basic)."""
        dex_mod = character['ability_modifiers'].get('Dexterity', 0)
        armor_bonus = character.get('armor_bonus', 0)
        character['armor_class'] = 10 + dex_mod + armor_bonus
        return character

    def calculate_proficiency_bonus(self, character):
        """Calculate proficiency bonus based on character level."""
        level = character['level']
        if 1 <= level <= 4:
            character['proficiency_bonus'] = 2
        elif 5 <= level <= 8:
            character['proficiency_bonus'] = 3
        elif 9 <= level <= 12:
            character['proficiency_bonus'] = 4
        elif 13 <= level <= 16:
            character['proficiency_bonus'] = 5
        elif 17 <= level <= 20:
            character['proficiency_bonus'] = 6
        return character

    def calculate_saving_throws(self, character):
        """Calculate saving throws for D&D 5e."""
        proficiency_bonus = character['proficiency_bonus']
        
        if 'saving_throws' not in character:
            character['saving_throws'] = {}

        for saving_throw, details in character['saving_throws'].items():
            modifier = character['ability_modifiers'].get(saving_throw, 0)
            if details.get('proficient', False):
                details['total'] = modifier + proficiency_bonus
            else:
                details['total'] = modifier
        return character

    def calculate_skills(self, character):
        """Calculate skill checks for D&D 5e."""
        proficiency_bonus = character['proficiency_bonus']
        
        if 'skills' not in character:
            character['skills'] = {}

        for skill, details in character['skills'].items():
            ability = details['ability']
            modifier = character['ability_modifiers'].get(ability, 0)
            if details.get('proficient', False):
                details['total'] = modifier + proficiency_bonus + details.get('bonus', 0)
            else:
                details['total'] = modifier + details.get('bonus', 0)
        return character