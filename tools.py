import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

class SportsAPIConnector:
    def __init__(self):
        self.base_url = "https://www.thesportsdb.com/api/v1/json/3"

    def get_team_info(self, team_name="Arsenal"):
        if team_name.lower() != "arsenal":
            return {"error": f"API Limit: The free tier only provides data for 'Arsenal'. Cannot fetch '{team_name}'."}
            
        safe_team_name = urllib.parse.quote(team_name)
        endpoint = f"{self.base_url}/searchteams.php?t={safe_team_name}"
        
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        try:
            req = urllib.request.Request(endpoint, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
                data = json.loads(response.read().decode('utf-8'))
                
            if not data.get("teams"):
                return {"error": f"No data found for team: '{team_name}'."}
            return data["teams"][0]
            
        except urllib.error.URLError as e:
            return {"error": f"API connection failed: {str(e)}"}