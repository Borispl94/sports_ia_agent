import unittest
from tools import SportsAPIConnector
from agent import SportsAgent

class TestSportsSystem(unittest.TestCase):
    def setUp(self):
        self.api_tool = SportsAPIConnector()
        self.agent = SportsAgent()

    def test_api_valid_team(self):
        result = self.api_tool.get_team_info("Arsenal")
        self.assertNotIn("error", result)
        self.assertEqual(result["strTeam"], "Arsenal")

    def test_api_invalid_team(self):
        result = self.api_tool.get_team_info("Paris SG")
        self.assertIn("error", result)

    def test_agent_formatting(self):
        report = self.agent.analyze_team("Arsenal")
        self.assertIn("SPORTS REPORT : Arsenal", report)

if __name__ == "__main__":
    unittest.main()