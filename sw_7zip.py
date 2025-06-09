import os
from core.version_check import fetch_json, run_check


def clean_version(filename):
    first_slash_index = filename.index("/", 1)
    second_slash_index = filename.index("/", first_slash_index + 1)
    return filename[first_slash_index + 1:second_slash_index]


def fetch_sevenzip():
    data = fetch_json("https://sourceforge.net/projects/sevenzip/best_release.json")
    version = clean_version(data["release"]["filename"])
    return {"version": version, "url": data["release"]["url"]}


if __name__ == "__main__":
    run_check(
        "7-Zip",
        fetch_sevenzip,
        os.path.join("updates", "LATEST_7ZIP"),
        "\U0001F910 7-Zip: new version {version} available! \nDownload from {url}",
    )
