from tools import SportsAPIConnector

class SportsAgent:
    def __init__(self):
        self.connector = SportsAPIConnector()

    def run(self, team_name):
        perceived_data = self.connector.get_team_info(team_name)
        
        if "error" in perceived_data:
            return f"System Error: {perceived_data['error']}"

        name = perceived_data.get("strTeam", "Unknown Team")
        league = perceived_data.get("strLeague", "Unknown League")
        stadium = perceived_data.get("strStadium", "Unknown Stadium")
        desc = perceived_data.get("strDescriptionEN") or "No description available."

        if len(desc) > 197:
            desc = desc[:197] + "..."

        action_output = (
            f"========================================\n"
            f"TEAM: {name}\n"
            f"LEAGUE: {league}\n"
            f"STADIUM: {stadium}\n"
            f"----------------------------------------\n"
            f"HISTORY:\n{desc}\n"
            f"========================================"
        )
        return action_output