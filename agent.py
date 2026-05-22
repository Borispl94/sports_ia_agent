from tools import SportsAPIConnector

class SportsAgent:
    def __init__(self):
        self.connector = SportsAPIConnector()

    def run(self, team_name):
        data = self.connector.get_team_info(team_name)
        
        if "error" in data:
            return f"System Error: {data['error']}"

        name = data.get("strTeam", "Unknown Team")
        league = data.get("strLeague", "Unknown League")
        stadium = data.get("strStadium", "Unknown Stadium")
        desc = data.get("strDescriptionEN") or "No description available."

        if len(desc) > 197:
            desc = desc[:194] + "..."

        report = (
            f"========================================\n"
            f"TEAM: {name}\n"
            f"LEAGUE: {league}\n"
            f"STADIUM: {stadium}\n"
            f"----------------------------------------\n"
            f"HISTORY:\n{desc}\n"
            f"========================================"
        )
        return report