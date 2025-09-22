# Modern PyPI upload script for protai
# Usage: Run this script from the project root after updating your code and version.

# Update README model references to match protai/protai.py
python update_readme_models.py

# Clean old build artifacts
Remove-Item -Recurse -Force dist, build, protai.egg-info -ErrorAction SilentlyContinue

# Ensure build and twine are installed
uv pip install --upgrade build twine

# Build the package (PEP 517)
python -m build

# Upload to PyPI
$twineExe = "twine"
if (-not (Get-Command $twineExe -ErrorAction SilentlyContinue)) {
	$twineExe = "python -m twine"
}
Invoke-Expression "$twineExe upload dist/*"