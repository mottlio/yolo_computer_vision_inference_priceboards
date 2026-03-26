from pathlib import Path
from ultralytics import YOLO

MODEL_PATH = Path("/Users/michal/Desktop/Developer/yolo_computer_vision_inference_priceboards/best.pt")
SOURCE_PATH = Path("/Volumes/T7/Paliwowo/processed/frames_for_cvat/2026-03-26")

def main() -> None:
    model = YOLO(str(MODEL_PATH))
    model.predict(
        source=str(SOURCE_PATH),
        save=True,
        conf=0.25,
    )
    print("Done.")

if __name__ == "__main__":
    main()