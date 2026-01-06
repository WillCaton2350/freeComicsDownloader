README — Selenium Comic Image Downloader (WIP)
Overview

This script is a work in progress Selenium-based downloader intended to automate the process of navigating a comic-hosting website and saving page images locally.

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

~/Desktop/image_<j>.jpg


⚠️ Known Issue:
The script currently risks overwriting images because the filename logic is not finalized.

Known Limitations / Issues

Hard-coded XPaths
The script relies on absolute XPaths (/html/body/...) which are fragile and likely to break if the site layout changes.

Page-specific logic
The script is hard-coded for:

A specific comic

A specific issue

A specific page structure

Minimal error handling
Only NoSuchElementException is explicitly handled.

Timing-sensitive
Uses short wait times (WDW(..., 1)), which may cause failures on slower connections.

TODO / Next Steps

Ensure unique filenames to prevent overwriting

Replace absolute XPaths with relative or attribute-based XPaths

Generalize script to support:

Different comics

Different issues

Different page counts

Improve exception handling and logging

Add configurable output directory

Optional: run fully headless once stable

Disclaimer

This script is provided as-is for educational and experimental purposes.
It may break without warning due to site changes or protections.
