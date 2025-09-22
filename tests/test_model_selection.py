import os
import tempfile
import pytest
from protai.protai import get_valid_models, fetch_groq_models, save_model_cache, load_cached_models, MODEL_CACHE_PATH

class DummyAPI:
    def __init__(self, models):
        self.models = models
    def fetch(self, api_key):
        return self.models

def test_model_cache_refresh(monkeypatch):
    # Simulate model list and cache
    models = ['model-a', 'model-b']
    monkeypatch.setattr('protai.protai.fetch_groq_models', lambda api_key: models)
    # Remove cache if exists
    if os.path.exists(MODEL_CACHE_PATH):
        os.remove(MODEL_CACHE_PATH)
    # Should fetch and cache
    result = get_valid_models('dummy-key')
    assert result == models
    # Should load from cache now
    result2 = get_valid_models('dummy-key')
    assert result2 == models

def test_model_cache_expiry(monkeypatch):
    models = ['model-x']
    monkeypatch.setattr('protai.protai.fetch_groq_models', lambda api_key: models)
    # Save old cache
    save_model_cache(['old-model'])
    # Expire cache
    import time
    old = int(time.time()) - 90000
    with open(MODEL_CACHE_PATH, 'r+') as f:
        import json
        cache = json.load(f)
        cache['timestamp'] = old
        f.seek(0)
        json.dump(cache, f)
        f.truncate()
    # Should refresh
    result = get_valid_models('dummy-key')
    assert result == models

def test_load_cached_models_empty(monkeypatch):
    # Remove cache if exists
    if os.path.exists(MODEL_CACHE_PATH):
        os.remove(MODEL_CACHE_PATH)
    models, timestamp = load_cached_models()
    assert models is None or models == []
    assert timestamp == 0
