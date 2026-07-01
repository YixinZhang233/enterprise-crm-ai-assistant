from __future__ import annotations

import argparse
from pathlib import Path

from .agent import CrmCompetitiveIntelligenceAgent
from .exporters import to_json, to_markdown_table
from .ocr import ocr_placeholder
from .schemas import Scenario


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CRM competitive intelligence extraction demo.")
    parser.add_argument(
        "--scenario",
        required=True,
        choices=[scenario.value for scenario in Scenario],
        help="CRM scenario schema to apply.",
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Text transcript or screenshot description file.",
    )
    parser.add_argument(
        "--format",
        default="both",
        choices=["markdown", "json", "both"],
        help="Output format.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_text = ocr_placeholder(args.input)
    agent = CrmCompetitiveIntelligenceAgent()
    result = agent.run(Scenario(args.scenario), source_text)

    if args.format in {"markdown", "both"}:
        print(to_markdown_table(result))
    if args.format == "both":
        print()
    if args.format in {"json", "both"}:
        print(to_json(result))


if __name__ == "__main__":
    main()
