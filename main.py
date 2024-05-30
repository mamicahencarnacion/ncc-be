from fastapi import Depends, FastAPI, Query

import deps
from deps import load_assets, load_scans, load_users, load_vulnerabilities

app = FastAPI()


@app.get("/")
async def root(
    users: list = Depends(load_users),
    scans: list = Depends(load_scans),
    vulnerabilities: list = Depends(load_vulnerabilities),
    assets: list = Depends(load_assets),
):
    """
    Returns all vulnerability scan data provided.
    """
    return {
        "users": users,
        "scans": scans,
        "vulnerabilities": vulnerabilities,
        "assets": assets,
    }


@app.get("/users")
async def users(
    users: list = Depends(load_users),
):
    """
    Returns all users data.
    """
    return users


@app.get("/users/{id}")
async def users(users: list = Depends(load_users), id: int = None):
    """
    Returns user data by user id.
    """
    if id in users:
        return users[id]
    return "User does not exist"


@app.get("/scans")
async def scans(
    scans: list = Depends(load_scans),
):
    """
    Returns all scans data.
    """
    return scans


@app.get("/scans/{id}")
async def scans(
    scans: list = Depends(load_scans),
    users: list = Depends(load_users),
    assets: list = Depends(load_assets),
    id: int = None,
):
    """
    Returns scan data by scan id.
    """
    if id in scans:
        scan_data = scans[id]
        scan_data["requested_by"] = users[scan_data["requested_by"]]
        assets_scanned = []
        for asset in scan_data["assets_scanned"]:
            assets_scanned.append(assets[asset])
        scan_data["assets_scanned"] = assets_scanned
        return scan_data
    return "Scan does not exist"


@app.get("/vulnerabilities")
async def vulnerabilities(
    vulnerabilities: list = Depends(load_vulnerabilities),
    from_scan: int = Query(None),
):
    """
    Returns all vulnerabilities data.
    Can be filtered by scan id.
    """
    if from_scan:
        from_scan_vulnerabilities = {}
        for vulnerability_id, vulnerability in vulnerabilities.items():
            if vulnerability["from_scan"] == from_scan:
                from_scan_vulnerabilities[vulnerability_id] = vulnerability
        return from_scan_vulnerabilities
    return vulnerabilities


@app.get("/vulnerabilities/{id}")
async def vulnerabilities(
    vulnerabilities: list = Depends(load_vulnerabilities),
    scans: list = Depends(load_scans),
    assets: list = Depends(load_assets),
    id: int = None,
):
    """
    Returns vulnerability data by vulnerability id.
    """
    if id in vulnerabilities:
        v_data = vulnerabilities[id]
        v_data["from_scan"] = scans[v_data["from_scan"]]
        affected_assets = []
        for asset in v_data["affected_assets"]:
            affected_assets.append(assets[asset])
        v_data["affected_assets"] = affected_assets
        return v_data
    return "Vulnerability does not exist"


@app.get("/assets")
async def assets(
    assets: list = Depends(load_assets),
):
    """
    Returns all assets data.
    """
    return assets


@app.get("/assets/{id}")
async def assets(
    assets: list = Depends(load_assets),
    id: int = None,
):
    """
    Returns asset data by asset id.
    """
    if id in assets:
        return assets[id]
    return "Asset does not exist"
