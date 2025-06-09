import os
from core.version_check import fetch_json, run_check

URL = "https://api.github.com/repos/ImageMagick/ImageMagick/releases/latest"


def fetch_imagemagick():
    data = fetch_json(URL)
    return {"version": data["tag_name"], "url": data["html_url"]}


if __name__ == "__main__":
    run_check(
        "ImageMagick",
        fetch_imagemagick,
        os.path.join("updates", "LATEST_IMGMGCK"),
        "\U0001F5BC\uFE0F ImageMagick: new version available! {version} \nDownload from {url} (or, as alternative, https://imagemagick.org/script/download.php)",
    )
