from pathlib import Path

folder = Path("./test_folder")
folder.mkdir(exist_ok=True)
file = folder/"process.json"
file.mkdir(exist_ok=True)




