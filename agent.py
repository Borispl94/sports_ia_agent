from tools import SportsAPIConnector

class SportsAgent:
    def __init__(self) -> None:
        self.api_tool = SportsAPIConnector()

    def analyze_team(self, team_name: str) -> str:
        print(f"[*] Agent is analyzing data for '{team_name}'...")
        raw_data = self.api_tool.get_team_info(team_name)

        if "error" in raw_data:
            return f"[!] Error: {raw_data['error']}\n"

        name = raw_data.get("strTeam", "Unknown")
        stadium = raw_data.get("strStadium", "Unknown")
        league = raw_data.get("strLeague", "Unknown")
        description = raw_data.get("strDescriptionEN", "No description available.")
        
        if description and len(description) > 200:
            description = description[:197] + "..."

        report = (
            f"\n"
            f"===================================\n"
            f"       SPORTS REPORT : {name.upper()}\n"
            f"===================================\n"
            f" > League  : {league}\n"
            f" > Stadium : {stadium}\n"
            f" > Summary : {description}\n"
            f"===================================\n"
        )
        return report