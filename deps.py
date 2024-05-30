import json


def load_users():
    """
    Returns users data as dict with user id as key.
    """
    with open("data/users.json") as users:
        users_data = json.load(users)
        users_dict = {}
        for user in users_data:
            id = user.pop("id")
            users_dict[id] = user
        return users_dict


def load_scans():
    """
    Returns scans data as dict with scan id as key.
    """
    with open("data/scans.json") as scans:
        scans_data = json.load(scans)
        scans_dict = {}
        for scan in scans_data:
            id = scan.pop("id")
            scans_dict[id] = scan
        return scans_dict


def load_vulnerabilities():
    """
    Returns vulnerabilities data as dict with vulnerability id as key.
    """
    with open("data/vulnerabilities.json") as vulnerabilities:
        vulnerabilities_data = json.load(vulnerabilities)
        vulnerabilities_dict = {}
        for vulnerability in vulnerabilities_data:
            id = vulnerability.pop("id")
            vulnerabilities_dict[id] = vulnerability
        return vulnerabilities_dict


def load_assets():
    """
    Returns assets data as dict with assets id as key.
    """
    with open("data/assets.json") as assets:
        assets_data = json.load(assets)
        assets_dict = {}
        for asset in assets_data:
            id = asset.pop("id")
            assets_dict[id] = asset
        return assets_dict
