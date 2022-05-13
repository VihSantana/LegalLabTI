import pathlib
from os import path


appDir = str(pathlib.Path().resolve())
dirDownloads = str(path.join(path.expanduser("~"), "Downloads"))
filtroUrls = "jurisprudencia/pes"
showBrowser = True