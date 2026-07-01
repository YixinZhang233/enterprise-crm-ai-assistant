# Demo

## Demo Preview

This repository uses Markdown-only demo assets so it can be safely shared without real screenshots or proprietary data.

```text
Input
  examples/input/sample_ocr.txt

Scenario Selection
  membership_tier_benefits

Extraction
  Load Membership Tier Benefits schema
  Build evidence-grounded prompt
  Extract structured records
  Normalize missing values as Not Mentioned

Output
  examples/output/structured_table.md
  examples/output/structured_output.json
```

## Demo Case

The primary demo uses fictional CRM data:

- Brand: `Brand A`
- Loyalty program: `Brand A Loyalty Program`
- Channel: `Official Mini Program`

Files:

| File | Purpose |
| --- | --- |
| `examples/input/membership_benefits.md` | Demo input description |
| `examples/input/sample_ocr.txt` | Mock OCR text |
| `examples/output/structured_table.md` | Markdown table output |
| `examples/output/structured_output.json` | JSON output |

Run the CLI demo:

```bash
python src/run_demo.py \
  --scenario membership_tier_benefits \
  --input examples/input/sample_ocr.txt \
  --format both
```
