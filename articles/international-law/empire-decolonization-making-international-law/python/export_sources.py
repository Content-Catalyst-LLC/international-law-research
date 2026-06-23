#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'outputs' / 'source_export.md'
out.write_text('# Empire, Decolonization, and the Making of International Law — Source Export\n\nGenerated source export placeholder.\n')
print(out)
