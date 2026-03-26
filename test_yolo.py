from pathlib import Path
from ultralytics import YOLO

PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "best.pt"
SOURCE_PATH = Path("/Volumes/T7/Paliwowo/processed/frames_for_inference")

def main() -> None:
    model = YOLO(str(MODEL_PATH))
    model.predict(
        source=str(SOURCE_PATH),
        save=True,
        save_crop=True,
        conf=0.6,
        project=str(PROJECT_DIR / "runs" / "detect"),
    )
    print("Done.")

if __name__ == "__main__":
    main()