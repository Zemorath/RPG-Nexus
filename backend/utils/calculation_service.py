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
        for ability, score in character['ability_scores'].items():
            # Check if override_score exists and use it if available
            if score.get('override_score') is not None:
                score['total_score'] = score['override_score']
            else:
                # Otherwise, calculate total_score from base_score and other bonuses
                base_score = score.get('base_score', 0)
                species_bonus = score.get('species_bonus', 0)
                ability_improvements = score.get('ability_improvements', 0)
                misc_bonus = score.get('misc_bonus', 0)
                score['total_score'] = (
                    base_score + species_bonus + ability_improvements + misc_bonus
                )

            # Calculate modifier based on the total_score
            score['modifier'] = (score['total_score'] - 10) // 2
        return character

    def calculate_initiative(self, character):
        """Calculate initiative for D&D 5e."""
        character['initiative'] = character['ability_scores']['Dexterity']['modifier']
        return character

    def calculate_armor_class(self, character):
        """Calculate armor class for D&D 5e (basic)."""
        dex_mod = character['ability_scores']['Dexterity']['modifier']
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
        
        # Ensure saving_throws is present
        if 'saving_throws' not in character:
            character['saving_throws'] = {}  # Initialize it if missing

        for saving_throw, details in character['saving_throws'].items():
            modifier = character['ability_scores'][saving_throw]['modifier']
            if details.get('proficient', False):
                details['total'] = modifier + proficiency_bonus
            else:
                details['total'] = modifier
        return character

    def calculate_skills(self, character):
        """Calculate skill checks for D&D 5e."""
        proficiency_bonus = character['proficiency_bonus']
        
        # Ensure skills is present
        if 'skills' not in character:
            character['skills'] = {}  # Initialize as empty if missing

        for skill, details in character['skills'].items():
            ability = details['ability']  # Example: 'Dexterity' for Acrobatics
            modifier = character['ability_scores'][ability]['modifier']
            if details.get('proficient', False):
                details['total'] = modifier + proficiency_bonus + details.get('bonus', 0)
            else:
                details['total'] = modifier + details.get('bonus', 0)
        return character


