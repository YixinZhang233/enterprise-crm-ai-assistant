# Workflow

This workflow shows how screenshots or OCR text become a structured CRM competitive intelligence report.

```mermaid
flowchart TD
    A["CRM Screenshots"] --> B["OCR or Manual Text Transcript"]
    A2["Mock OCR Text"] --> B
    B --> C["Select CRM Scenario"]
    C --> D{"Scenario Type"}
    D --> D1["Membership Tier Benefits"]
    D --> D2["Member Day Campaign"]
    D --> D3["Existing Customer Communication"]
    D --> D4["Prospect Communication"]
    D --> D5["Prospect / New / Existing Member Benefits"]
    D --> D6["New Customer Communication"]
    D1 --> E["Load Matching Extraction Schema"]
    D2 --> E
    D3 --> E
    D4 --> E
    D5 --> E
    D6 --> E
    E --> F["Build Evidence-Grounded Prompt"]
    F --> G["Run Structured Extraction Agent"]
    G --> H["Normalize Missing Fields as Not Mentioned"]
    H --> I["Export Markdown Table"]
    H --> J["Export JSON"]
    I --> K["Structured CRM Intelligence Report"]
    J --> K
    K --> L["Human Review"]
```

## End-to-End Steps

1. Collect screenshots or receive OCR text from CRM touchpoints.
2. Select the CRM scenario type.
3. Load the scenario-specific schema.
4. Build an extraction prompt that requires evidence-based answers.
5. Extract structured records with `field`, `exists`, and `extracted_content`.
6. Export both Markdown and JSON.
7. Review missing or uncertain fields before downstream use.

The demo uses mock OCR text and fictional brand data so it can be safely shared in a public portfolio repository.
