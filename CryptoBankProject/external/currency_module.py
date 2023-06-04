import sys
from pathlib import Path

root = Path(__file__).resolve()
root = root.parent.parent.parent
sys.path.append(str(root))

try:
    from ...CurrencyProject import src as CurrencyProject
except ImportError:
    from CurrencyProject import src as CurrencyProject # type: ignore