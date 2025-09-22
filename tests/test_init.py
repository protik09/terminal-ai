from protai.__init__ import read_version

def test_read_version_exists(tmp_path):
    version_file = tmp_path / "VERSION"
    version_file.write_text("1.2.3")
    result = read_version(str(version_file))
    assert result == "1.2.3"

def test_read_version_missing():
    result = read_version("nonexistent_file")
    assert result == "0.0.0"
