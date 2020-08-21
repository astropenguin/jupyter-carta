# standard library
from functools import partial
from pathlib import Path
from socket import gethostbyname, gethostname
from subprocess import Popen, PIPE, STDOUT
from typing import Optional


# dependencies
from IPython.display import HTML
from requests import get, ConnectionError


# constants
CARTA_PATH = (Path() / "carta" / "carta").resolve()
NGROK_PATH = (Path() / "carta" / "ngrok").resolve()


def get_ngrok_url(port: int) -> str:
    """Get an ngrok URL."""
    while True:
        try:
            ret = get(f"http://localhost:{port}/api/tunnels")
        except ConnectionError:
            continue

        try:
            tunnel = ret.json()["tunnels"][0]
        except (IndexError, KeyError):
            continue

        return tunnel["public_url"].split("//")[1]


def run_carta(
    port: int = 41578,
    fport: int = 39138,
    carta_path: Path = CARTA_PATH,
    ngrok_path: Path = NGROK_PATH,
) -> None:
    """Run CARTA server and create an open URL."""
    host = gethostbyname(gethostname())
    popen = partial(Popen, stdin=PIPE, stdout=PIPE, stderr=STDOUT)

    popen([str(carta_path), "--remote", f"--port={port}", f"--fport={fport}"])
    popen([str(ngrok_path), "http", f"{host}:{fport}"])
    popen([str(ngrok_path), "http", f"{host}:{port}"])

    href = f"https://{get_ngrok_url(4040)}/?socketUrl=wss://{get_ngrok_url(4041)}"
    print(f"CARTA has started. Open here: {href}")


if __name__ == "__main__":
    run_carta()
