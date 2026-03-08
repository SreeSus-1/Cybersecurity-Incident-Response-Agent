from agents.base_agent import BaseAgent

class LogParserAgent(BaseAgent):
    def run(self, log_text: str) -> str:
        prompt = f"""
        You are a cybersecurity Log Parser Agent.

        Analyze the following system logs or security alerts.
        Extract:
        - key suspicious events
        - failed login attempts
        - unusual IP addresses
        - repeated patterns
        - timestamps
        - affected systems or users

        Return the result in structured bullet points.

        Logs:
        {log_text}
        """
        return self.call_ollama(prompt)