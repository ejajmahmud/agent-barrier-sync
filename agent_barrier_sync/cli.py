"""Command-line interface for Agent Barrier Sync."""
import argparse
from .barrier import BarrierSync

def main():
    parser = argparse.ArgumentParser(description="Agent Barrier Sync CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate barrier synchronization")
    args = parser.parse_args()

    barrier = BarrierSync("CODE_REVIEW_MILESTONE", {"security_agent", "qa_agent"})
    print("Agent 1 arriving...")
    rel1 = barrier.arrive("security_agent", {"audit": "PASS"})
    print(f"Barrier released? {rel1}")

    print("Agent 2 arriving...")
    rel2 = barrier.arrive("qa_agent", {"tests": "100% PASS"})
    print(f"Barrier released? {rel2}")
    print("Consolidated manifest:", barrier.get_manifest())

if __name__ == "__main__":
    main()
