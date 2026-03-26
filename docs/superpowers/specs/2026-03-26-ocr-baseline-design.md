# OCR Baseline Design

## Goal

Run two OCR engines (PaddleOCR and GPT-4o vision) on all 64 existing YOLO priceboard crops side by side, to learn what each engine reads and where they fail. This is Phase A — no preprocessing, no parsing, just raw extraction and comparison.

## Input

- 64 crop images in `runs/detect/predict/crops/priceboard/`
- 8 unique clips, ~10 frames each
- Filename pattern: `{clip_id}_frame_{NNN}.jpg`

## Script

**`ocr_baseline.py`** in the project root.

### Flow

1. Scan `runs/detect/predict/crops/priceboard/` for all `.jpg` files
2. Group by clip ID (everything before `_frame_`)
3. For each crop image:
   - Run PaddleOCR: extract detected text lines with bounding box y-coordinates
   - Call GPT-4o vision API: send the image, prompt it to return detected numbers/text with their vertical position (rank from top to bottom)
4. Save per-crop result as JSON to `runs/ocr_baseline/{crop_filename}.json`
5. After all crops are processed, write `runs/ocr_baseline/summary.json` with per-clip aggregated results

### PaddleOCR Details

- Use `paddleocr` Python package with default English + number detection
- Extract: text string, confidence, bounding box coordinates (use top-left y as vertical position)
- No preprocessing — pass raw crop image directly

### GPT-4o Vision Details

- Use `openai` Python SDK
- API key from `OPENAI_API_KEY` environment variable
- Prompt strategy: send the crop image and ask the model to return all visible text/numbers on the priceboard, ordered from top to bottom, with a rank indicating vertical position
- Request structured JSON response
- Model: `gpt-4o`

### Per-Crop Output Format

```json
{
  "image": "0d1e44e..._frame_005.jpg",
  "clip_id": "0d1e44e09af1621329253b28c2b25811_20260326_044605_1of1_a8ef252b",
  "frame": 5,
  "paddleocr": {
    "lines": [
      {"text": "6.59", "confidence": 0.92, "y_position": 120},
      {"text": "6.79", "confidence": 0.87, "y_position": 250}
    ]
  },
  "gpt4o": {
    "lines": [
      {"text": "6.59", "y_rank": 1},
      {"text": "6.79", "y_rank": 2}
    ]
  }
}
```

### Summary Output Format

```json
{
  "total_crops": 64,
  "clips": [
    {
      "clip_id": "0d1e44e...",
      "frames_processed": 10,
      "paddleocr_detected_any_text": 8,
      "gpt4o_detected_any_text": 10
    }
  ]
}
```

## Dependencies

- `paddleocr` — PaddleOCR Python package
- `openai` — OpenAI Python SDK
- `OPENAI_API_KEY` environment variable must be set

## What This Is NOT

- No image preprocessing (grayscale, threshold, deskew) — that is Phase B
- No structured price parsing (fuel type mapping) — that is Phase C
- No multi-frame voting — that is Phase D
- No production pipeline — this is a diagnostic experiment

## Success Criteria

- Script runs end-to-end on all 64 crops without crashing
- Per-crop JSON files are saved with results from both engines
- Summary JSON shows detection rates per clip
- Human can visually inspect results and identify: which engine performs better, what types of failures occur (missed text, garbled text, wrong numbers), and which crops/conditions are hardest
