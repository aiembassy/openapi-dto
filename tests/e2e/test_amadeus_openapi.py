from pathlib import Path

import pytest

from openapi_dto.cli import main
from openapi_dto.config import NamingConvention, OutputEngine

CURRENT_DIR = Path(__file__).parent / "fixtures"


@pytest.mark.parametrize("input_file", CURRENT_DIR.glob("*.json"))
def test_load_openapi_defs(input_file: Path):
    main(
        str(input_file),
        naming_convention=NamingConvention.CAMEL_CASE,
        output_engine=OutputEngine.DATACLASS,
    )
