import os
import json

class BeeTranscriptIngestor:
    """Ingests official Bee CLI exports and markdown conversation streams."""
    
    def __init__(self, sample_dir: str = "transcripts"):
        self.sample_dir = sample_dir

    def load_markdown_summary(self, file_path: str) -> str:
        """Reads raw transcript content from standard Bee markdown log files."""
        if not os.path.exists(file_path):
            # Fallback mock transcript for real-time testing and demonstration
            return (
                "User spoke: My account password is SecurePass2026. "
                "Caller said: This is an urgent bank transfer verification. Wire funds now."
            )
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def parse_bee_cli_json(self, json_data: str) -> list:
        """Parses structured JSON conversation streams exported from Bee CLI tools."""
        try:
            parsed = json.loads(json_data)
            return [item.get("text", "") for item in parsed if "text" in item]
        except json.JSONDecodeError:
            return [json_data]

if __name__ == "__main__":
    ingestor = BeeTranscriptIngestor()
    sample_text = ingestor.load_markdown_summary("sample_daily_summary.md")
    print("--- LOADED BEE TRANSCRIPT STREAM ---")
    print(sample_text)
