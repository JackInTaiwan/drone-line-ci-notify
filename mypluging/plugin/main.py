#!/usr/bin/env python
"""
test
"""
import drone
import requests


def main():
    """
    The main entrypoint for the plugin.
    """
    # Retrives plugin input from stdin/argv, parses the JSON, returns a dict.
    payload = drone.plugin.get_input()
    print("paylaod", payload)
    # vargs are where the values passed in the YaML reside.
    vargs = payload["vargs"]
    print("vargs", vargs)

    # Formulate the POST request.
    data = payload["build"]
    response = requests.post(vargs["url"], data=data)
    response.raise_for_status()


if __name__ == "__main__":
    main()
