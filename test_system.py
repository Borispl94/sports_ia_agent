import unittest
from unittest.mock import patch
import urllib.error
from tools import SportsAPIConnector
from agent import SportsAgent

class TestSportsAIAgent(unittest.TestCase):

    def setUp(self):
        self.agent = SportsAgent()
        self.connector = SportsAPIConnector()

    @patch('urllib.request.urlopen')
    def test_successful_data_retrieval(self, mock_urlopen):
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"teams": [{"strTeam": "Arsenal", "strLeague": "Premier League", "strStadium": "Emirates", "strDescriptionEN": "Short description."}]}'
        
        result = self.agent.run("Arsenal")
        
        self.assertIn("TEAM: Arsenal", result)
        self.assertIn("LEAGUE: Premier League", result)
        self.assertIn("STADIUM: Emirates", result)
        self.assertIn("HISTORY:\nShort description.", result)

    @patch('urllib.request.urlopen')
    def test_description_truncation(self, mock_urlopen):
        long_desc = "A" * 300
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = f'{{"teams": [{{"strTeam": "Test", "strLeague": "Test", "strStadium": "Test", "strDescriptionEN": "{long_desc}"}}]}}'.encode('utf-8')
        
        result = self.agent.run("TestTeam")
        
        self.assertIn("A" * 194 + "...", result)
        self.assertNotIn("A" * 200, result)

    @patch('urllib.request.urlopen')
    def test_team_not_found(self, mock_urlopen):
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"teams": null}'
        
        result = self.agent.run("UnknownTeam")
        
        self.assertIn("System Error: No data found for team: 'UnknownTeam'", result)

    @patch('urllib.request.urlopen')
    def test_network_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection timed out")
        
        result = self.agent.run("Arsenal")
        
        self.assertIn("System Error: API connection failed", result)
        self.assertIn("Connection timed out", result)

if __name__ == '__main__':
    unittest.main()