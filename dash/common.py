import sys
from pathlib import Path

# Get the aboslute path of the repo
project_path = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(project_path))

from Common import *