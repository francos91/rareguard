"""Smoke test — verifies the package imports."""
import rareguard


def test_package_imports():
    assert rareguard.__version__ == "0.1.0"
