import pytest
from bsort.main import load_config
import os

# Tes 1: Pastikan bisa import package
def test_import():
    try:
        import bsort
        assert True
    except ImportError:
        assert False, "Gagal mengimport paket bsort"

# Tes 2: Cek apakah file config default ada
def test_config_exists():
    config_path = "config/settings.yaml"
    assert os.path.exists(config_path), "File config/settings.yaml tidak ditemukan"

# Tes 3: Cek fungsi load_config (jika file ada)
def test_load_config():
    config_path = "config/settings.yaml"
    if os.path.exists(config_path):
        cfg = load_config(config_path)
        assert isinstance(cfg, dict), "Config harus berupa dictionary"
        assert "model" in cfg, "Key 'model' harus ada di config"