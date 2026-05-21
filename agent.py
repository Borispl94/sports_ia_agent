from tools import SportsAPIConnector

class SportsAgent:
    def __init__(self):
        self.api_tool = SportsAPIConnector()

    def analyze_team(self, team_name):
        print(f"[*] Analyzing data for '{team_name}'...")
        raw_data = self.api_tool.get_team_info(team_name)

        if "error" in raw_data:
            return raw_data["error"]

        name = raw_data.get("strTeam", "Unknown")
        stadium = raw_data.get("strStadium", "Unknown")
        league = raw_data.get("strLeague", "Unknown")
        description = raw_data.get("strDescriptionEN", "No description available.")
        
        if len(description) > 200:
            description = description[:200] + "..."

        report = (
            f"\n--- SPORTS REPORT : {name} ---\n"
            f"League : {league}\n"
            f"Stadium : {stadium}\n"
            f"Summary : {description}\n"
            f"-----------------------------------\n"
        )
        return report