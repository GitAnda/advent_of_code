import time
import os
from pathlib import Path

path = Path(__file__).parent
print()
for file in os.listdir(path):
    if file.startswith('day') and file.endswith('.py'):
        print(f"[Running] {file}")
         
        txtfile = path / (Path(file).stem + ".txt")
        if txtfile.exists():
            t_start = time.time()
            code = os.system(f'python {path / file}')
            t_end = time.time()
            print(f"[Done] Finished with {code=} in {round(t_end - t_start, 3)} seconds\n")
        else:
            print(f"[Aborted] No accompanying .txt file for {file}\n")
