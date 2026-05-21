import urllib.request
import urllib.parse
import urllib.error
import json

class SportsAPIConnector:
    def __init__(self):
        self.base_url = "https://www.thesportsdb.com/api/v1/json/3"

    def get_team_info(self, team_name="Paris SG"):
        safe_team_name = urllib.parse.quote(team_name)
        endpoint = f"{self.base_url}/searchteams.php?t={safe_team_name}"
        
        try:
            req = urllib.request.Request(endpoint, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode('utf-8'))
                
            if not data.get("teams"):
                return {"error": f"No data found for team: '{team_name}'."}
            return data["teams"][0]
            
        except urllib.error.URLError as e:
            return {"error": f"API connection failed: {str(e)}"}