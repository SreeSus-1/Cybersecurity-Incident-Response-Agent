from agents.base_agent import BaseAgent

class ContainmentAdvisorAgent(BaseAgent):
    def run(self, threat_analysis: str) -> str:
        prompt = f"""
        You are a cybersecurity Containment Advisor Agent.

        Based on the threat analysis below, recommend:
        - immediate containment steps
        - short-term investigation actions
        - remediation steps
        - monitoring recommendations
        - escalation guidance

        Keep the response practical and incident-response focused.

        Threat Analysis:
        {threat_analysis}
        """
        return self.call_ollama(prompt)