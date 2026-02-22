README — Selenium Comic Image Downloader
Overview

This script is a Selenium-based downloader that automates the process of navigating a comic-hosting website and saving page images locally.

It uses SeleniumBase with an undetected Chromium driver to:

Navigate through comic pages

Locate image elements

Extract image URLs

Download images directly to the local machine (Desktop)

The script is currently tailored to a specific comic and page structure and is not yet generalized.

Requirements

Python 3.x

seleniumbase

selenium

requests

Example install:

pip install seleniumbase selenium requests

Current Behavior

Launches a Chromium browser (non-headless for debugging)

Iterates through pages using a fragment identifier (#k)

Waits for specific image elements using XPath

Extracts the src attribute of the image

Downloads the image to the macOS Desktop

Refreshes the page between iterations

File Output

Images are currently saved to:

/Desktop/


⚠️ Known Issue:
Known Limitations / Issues

Hard-coded XPaths
The script relies on absolute XPaths (/html/body/...) which are fragile and likely to break if the site layout changes.

Page-specific logic
The script is hard-coded for:

A specific comic

A specific page structure

Optional: run fully headless once stable

Disclaimer

This script is provided as-is for educational and experimental purposes.
It may break without warning due to site changes or protections.
