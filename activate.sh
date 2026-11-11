# Run from any directory: source /path/to/automation-testing-lab/activate.sh
LAB5_PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$LAB5_PROJECT_DIR/.venv/bin/activate"
export PLAYWRIGHT_BROWSERS_PATH="$LAB5_PROJECT_DIR/../.local/ms-playwright"
export XDG_CACHE_HOME="$LAB5_PROJECT_DIR/../.local/cache"
export TMPDIR="$LAB5_PROJECT_DIR/../.local/tmp"
export PIP_CACHE_DIR="$XDG_CACHE_HOME/pip"
