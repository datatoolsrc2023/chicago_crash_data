from pathlib import Path

root = Path(__file__).absolute().parent.parent
data = root / 'data'
sql = root / 'sql'
tasks = root / 'tasks'
db = data / 'db'
import_files = data / 'import_files'
