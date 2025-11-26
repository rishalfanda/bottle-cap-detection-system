import time
from ultralytics import YOLO
from typing import Dict, Any

class BottleDetector:
    """
    Handles object detection inference using YOLO models.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the detector with configuration.

        Args:
            config (Dict[str, Any]): Configuration dictionary loaded from yaml.
        """
        self.model_path = config['model']['path']
        self.conf = config['model']['conf_threshold']
        self.img_size = config['model']['img_size']

        print(f"Loading model from: {self.model_path}")
        # Task='detect' memastikan mode deteksi objek
        self.model = YOLO(self.model_path, task='detect')

    def predict_image(self, image_path: str) -> None:
        """
        Runs inference on a single image and displays the result.

        Args:
            image_path (str): Path to the input image file.
        """
        print(f"Running inference on: {image_path}")
        start_time = time.time()

        # Run inference
        results = self.model.predict(
            source=image_path,
            conf=self.conf,
            imgsz=self.img_size,
            save=True,   # Simpan hasil gambar dengan kotak
            show=True    # Tampilkan jendela pop-up (jika di local)
        )

        end_time = time.time()
        process_time = (end_time - start_time) * 1000

        print(f"Done in {process_time:.2f} ms")
        print(f"Result saved to: {results[0].save_dir}")