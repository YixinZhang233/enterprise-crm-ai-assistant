# Prompt Engineering

The prompt layer is designed for controlled extraction, not open-ended summarization. It gives the model a scenario, a field schema, and strict rules for missing information.

## Scenario Routing

The user selects a scenario before extraction. The scenario determines which fields are expected and prevents one prompt from trying to handle every CRM use case at once.

Examples:

- `membership_tier_benefits`
- `member_day_campaign`
- `existing_customer_communication_benefits`
- `prospect_communication_benefits`

## Schema Design

Schemas are defined in `src/crm_ci_agent/schemas.py`. Each schema is a list of field names and descriptions. This makes the output predictable and easy to compare across different screenshots.

The output record shape is intentionally simple:

```json
{
  "field": "Birthday Benefit",
  "exists": "Yes",
  "extracted_content": "Birthday month double points, once per year"
}
```

## Evidence-Based Extraction

The extraction instruction requires the model to use only information present in the OCR text. This is important for competitive intelligence because unsupported assumptions can turn into bad benchmark data.

## Hallucination Prevention

When a value is missing, the system returns `Not Mentioned`. The model should not infer benefits, channels, dates, or eligibility rules from CRM norms.

This rule makes uncertainty visible and keeps human review efficient.

## JSON Validation

The project uses scenario schemas as the validation contract. A production implementation could add formal JSON Schema validation before writing results to a database or dashboard.

The key checks are:

- The scenario is supported.
- Every expected field is returned.
- Each record has `field`, `exists`, and extracted content.
- Missing values use `Not Mentioned`.
