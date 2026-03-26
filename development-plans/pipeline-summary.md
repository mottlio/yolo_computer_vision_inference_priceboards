# Pipeline Summary

## Full Target Pipeline

video clip → sample frames → YOLO board crop → crop cleanup/normalization → OCR → structured price parsing → multi-frame voting

## Current State

YOLO detection and cropping are working. OCR pipeline is the next major milestone.

## Development Phases

### Phase A — Quick Baseline
- Export clean YOLO crops (not annotated images)
- Run PaddleOCR out-of-the-box on crops
- Inspect 100–200 examples to learn what fails

### Phase B — Preprocessing Sweep
- Try variants: grayscale, resize, threshold, contrast boost, deskew
- Compare which variant gives best OCR quality most often
- Preprocessing typically matters more than switching OCR engines

### Phase C — Structured Parser
- Extract numbers matching Polish price format
- Associate prices to rows (diesel, pb95, pb98)
- Reject impossible values
- Target output: `{"diesel": "6.59", "pb95": "6.79", "pb98": "7.09", "confidence": 0.91}`

### Phase D — Temporal Fusion
- Combine OCR across multiple frames (already extracting 10 per clip)
- Majority vote / confidence-weighted vote / best-frame fallback

## Key Design Decisions

- Start with PaddleOCR, not custom OCR training or multimodal models
- Save per-crop artifacts: `crop.jpg`, `meta.json`, `ocr_raw.json`, `ocr_parsed.json`
- Vote across multiple frames rather than picking "best frame"
- Do NOT yet: train custom OCR, build multimodal model, optimize Azure deployment, or solve every edge case

## Per-Crop Artifact Structure

```
crop.jpg
meta.json       # clip ID, frame number, confidence, station ID
ocr_raw.json
ocr_parsed.json
```

## Near-Term Milestone

For 50–100 station clips, output:
- Best crop
- OCR text
- Parsed prices
- Confidence
- Link to source frame

Then diagnose whether the bottleneck is: bad YOLO crops, poor board rectification, OCR engine weakness, or parsing logic.
