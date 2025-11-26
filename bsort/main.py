import argparse
import yaml
import os
import sys
from bsort.infer import BottleDetector

def load_config(config_path: str) -> dict:
    """Loads configuration from a YAML file."""
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    """Main entry point for the bsort CLI tool."""
    parser = argparse.ArgumentParser(description="BSORT: Bottle Cap Sorter System")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Command: infer
    infer_parser = subparsers.add_parser('infer', help='Run detection on an image')
    infer_parser.add_argument('--config', type=str, default='config/settings.yaml', help='Path to config file')
    infer_parser.add_argument('--image', type=str, required=True, help='Path to image file')

    # Command: train (Placeholder agar sesuai syarat tugas)
    train_parser = subparsers.add_parser('train', help='Train model (Cloud/GPU recommended)')
    train_parser.add_argument('--config', type=str, default='config/settings.yaml')

    args = parser.parse_args()
    config = load_config(args.config)

    if args.command == 'infer':
        detector = BottleDetector(config)
        detector.predict_image(args.image)

    elif args.command == 'train':
        print("    Training is best performed on Google Colab/Cloud GPU.")
        print("    Please refer to the provided Jupyter Notebook for training steps.")

if __name__ == "__main__":
    main()