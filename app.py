"""Command-line interface for plant disease detection and control suggestions."""

from pathlib import Path
from src.predict import predict

def main():
    print("=" * 64)
    print(" DETECTION OF PLANT DISEASES AND CONTROL IN AGRICULTURE")
    print("=" * 64)
    print("Enter the path to a plant image.")
    print("Type 'exit' to quit.\n")

    while True:
        raw = input("Image path: ").strip().strip('"')
        if raw.lower() == "exit":
            break
        if not raw:
            continue

        try:
            result = predict(Path(raw))
            print("\nPlant species       :", result["plant_species"])
            print("Detected disease    :", result["disease"])
            print("Confidence          :", f'{result["detection_confidence"]:.2%}')
            print("Spread risk         :", result["spread_risk"])
            print("Control suggestion  :", result["control_suggestion"])
        except Exception as exc:
            print("\nError:", exc)
        print()

if __name__ == "__main__":
    main()
