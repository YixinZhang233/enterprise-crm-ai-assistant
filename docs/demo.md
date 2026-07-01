# Demo

## Demo Preview

This repository does not include a real GIF because the project uses anonymized mock input instead of real screenshots. The flow below shows the intended demo experience.

```text
Input
  Mock OCR text reconstructed from public-style loyalty program screenshots

Scenario Selection
  membership_tier_benefits

Extraction
  Scenario router loads the Membership Tier Benefits schema
  Prompt builder applies strict evidence-based extraction rules
  Structured extraction agent fills each field
  Missing fields are returned as Not Mentioned

Output
  Markdown table
  JSON records
```

## Demo Case

The included demo case uses:

- Brand: `Brand A`
- Loyalty program: `Brand A Loyalty Program`
- Channel: `Official Mini Program`

Files:

| File | Purpose |
| --- | --- |
| `examples/input/membership_tier_benefits.md` | Demo input description |
| `examples/sample_ocr_text/membership_tier_benefits.txt` | Mock OCR text |
| `examples/output/membership_tier_benefits_table.md` | Markdown table output |
| `examples/output/membership_tier_benefits.json` | JSON output |

Run the CLI demo:

```bash
python src/run_demo.py \
  --scenario member_day_campaign \
  --input examples/sample_inputs/member_day_campaign.txt \
  --format both
```
