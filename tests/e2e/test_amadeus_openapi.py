from pathlib import Path

from openapi_dto.cli import main
from openapi_dto.config import NamingConvention, OutputEngine

CURRENT_DIR = Path(__file__).parent / "fixtures"


def test_load_flight_offers_search_amadeus_openapi_v2():
    input_file = CURRENT_DIR / "amadeus_fos_openapi_v2.json"

    main(
        str(input_file),
        naming_convention=NamingConvention.CAMEL_CASE,
        output_engine=OutputEngine.DATACLASS,
    )
