from pathlib import Path
from typing import Union

import orjson
from typeguard import typechecked


@typechecked
def write_json(data, filename: Union[str, Path]):
    with open(filename, "wb") as f:
        f.write(orjson.dumps(data))
