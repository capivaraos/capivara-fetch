"""Application-wide constants for Capivara Fetch.

Change APP_NAME / APP_ID here if the branding name is ever revisited
(e.g. "Snap" collides with Canonical Snap packages, hence "Fetch").
"""

import os

APP_ID = "org.capivaraos.Fetch"
APP_NAME = "Capivara Fetch"
VERSION = "0.1.0"

# Where the "Try CapivaraOS" funnel points.
WEBSITE_URL = "https://capivaraos.org"
DOWNLOAD_URL = "https://sourceforge.net/projects/capivaraos/files/"
ISSUE_URL = "https://github.com/capivaraos"

# CapivaraOS brand palette (used to render the shareable card).
BRAND_NAVY = (0.086, 0.137, 0.239)      # #16233d — deep navy background
BRAND_NAVY_2 = (0.055, 0.090, 0.169)    # #0e172b — gradient bottom
BRAND_BROWN = (0.541, 0.353, 0.231)     # #8a5a3b — capybara brown accent
BRAND_CREAM = (0.960, 0.925, 0.870)     # #f5ecde — warm off-white text
BRAND_MUTED = (0.65, 0.70, 0.80)        # muted label grey-blue


def _first_existing(*paths):
    for p in paths:
        if p and os.path.exists(p):
            return p
    return None


def brand_head_png():
    """Best-effort path to the capybara head PNG used on the card/icon.

    Falls back across: installed data dir, in-repo data/, and the sibling
    brand-assets/ repo when running from the CapivaraOS workspace.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, "..", ".."))
    workspace = os.path.abspath(os.path.join(repo_root, ".."))
    return _first_existing(
        os.path.join(os.sep, "app", "share", APP_ID, "capybara-head.png"),
        os.path.join(repo_root, "data", "icons", "256x256", "apps", APP_ID + ".png"),
        os.path.join(workspace, "brand-assets", "capivaraos-cabeca-marrom.png"),
        os.path.join(workspace, "brand-assets", "capivaraos-cabeca.png"),
    )
