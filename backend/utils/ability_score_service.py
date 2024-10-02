class AbilityScoreService:
    # Dungeons and Dragons 5e settings
    DND_STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]
    DND_POINT_BUY_COST = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}

    @staticmethod
    def generate_dd_5e_standard_array():
        """Standard array for D&D 5e."""
        return {"standard_array": AbilityScoreService.DND_STANDARD_ARRAY}

    @staticmethod
    def generate_dd_5e_point_buy(assigned_scores=None):
        """Point Buy system for D&D 5e (27 points)."""
        points = 27
        if not assigned_scores:
            return {"error": "No scores provided"}

        total_points_spent = 0
        for ability_score in assigned_scores.values():
            base_score = ability_score.get('base_score')
            if base_score and base_score != '--':
                try:
                    score = int(base_score)
                    total_points_spent += AbilityScoreService.DND_POINT_BUY_COST.get(score, 0)
                except ValueError:
                    # If conversion fails, skip this score
                    continue

        if total_points_spent > points:
            return {"error": "Exceeded maximum points"}

        return {
            "assigned_scores": {k: v['base_score'] for k, v in assigned_scores.items()},
            "remaining_points": points - total_points_spent
        }