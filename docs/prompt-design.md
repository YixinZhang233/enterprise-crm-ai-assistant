# Prompt Engineering

This project treats prompt design as an engineering interface between messy CRM screenshots and structured output.

## Scenario-Based Prompt Routing

The user selects a CRM scenario before extraction. That scenario determines which schema is loaded and which fields the agent must return.

Supported scenarios include membership tier benefits, member-day campaigns, existing customer communication, prospect communication, mixed audience benefits, and new customer communication.

## Schema-Driven Extraction

Each scenario has an explicit field schema in `src/crm_ci_agent/schemas.py`. The prompt builder uses that schema to tell the extraction agent exactly what to look for.

This avoids broad summaries and keeps outputs consistent across screenshots.

## Strict Evidence-Based Extraction

The extractor should only return information that is directly supported by the input text. It should not infer from industry knowledge, historical campaigns, or assumptions about CRM programs.

This rule is especially important for competitive intelligence workflows because unsupported guesses can pollute benchmark data.

## Not Mentioned Handling

When a field cannot be confirmed, the agent returns `Not Mentioned`.

This makes missing information explicit and keeps downstream review cleaner. A reviewer can quickly see which fields were observed and which fields were absent from the available source.

## Markdown Table + JSON Dual Output

The project exports both:

- Markdown tables for human-readable reports and spreadsheet-style review.
- JSON records for automation, storage, dashboarding, or downstream analysis.

Both output formats preserve the same core structure:

```json
{
  "field": "Birthday Benefit",
  "exists": "Yes",
  "extracted_content": "All tiers receive birthday benefits."
}
```
