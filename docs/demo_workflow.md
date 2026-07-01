# Demo Workflow

This workflow uses a text transcript as a stand-in for OCR output.

## Step 1: Select Scenario

Choose one supported scenario:

```text
member_day_campaign
```

## Step 2: Prepare Screenshot Transcript

Use a public mock transcript:

```text
examples/sample_inputs/member_day_campaign.txt
```

In production, this file would be replaced by OCR output or a multimodal model response from a screenshot.

## Step 3: Run Extraction

```bash
python src/run_demo.py \
  --scenario member_day_campaign \
  --input examples/sample_inputs/member_day_campaign.txt \
  --format both
```

## Step 4: Review Markdown Table

The Markdown table can be copied into spreadsheets, CRM research docs, or competitive intelligence reports.

## Step 5: Store JSON

The JSON output can be saved to a data warehouse, reviewed by an analyst, or used by downstream dashboard code.

## Step 6: Human Review

Any field marked `Not Mentioned` should be reviewed only if the original screenshot may contain hidden, cropped, or low-confidence text. The agent should not fill missing fields through inference.
