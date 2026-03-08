from agents.base_agent import BaseAgent

class ThreatIntelAgent(BaseAgent):
    def run(self, parsed_log_summary: str) -> str:
        prompt = f"""
        You are a Threat Intelligence Agent.

        Based on the parsed security findings below, infer:
        - likely attack type
        - severity level
        - possible attacker behavior
        - likely indicators of compromise
        - MITRE ATT&CK style reasoning if relevant

        Provide a concise but useful analysis.

        Parsed Findings:
        {parsed_log_summary}
        """
        return self.call_ollama(prompt)