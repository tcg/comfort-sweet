# ARCHIVE PURPOSES ONLY

This code *very likely* doesn't work anymore. It's left here for archival and research purposes only. Thanks! 👋🏻 



comfort-sweet
==============

Automatically preserve internet connectivity at Comfort Suites, via their captive portal.

## Usage

 * `pip install requests` to get the `requests` library.
 * Run `python comfort_sweet.py` in a background terminal somewhere.
 * Enjoy.

## Wuuuut?

This script simply checks a given URL at a regular interval, to see if your internet service is being redirected
to the captive portal. If it appears to be, it will send the same exact form data to the proper URL that would be
sent if you were to check the "accept terms" checkbox and submit the form. 

Please don't use this script if you don't agree with their terms of internet/network usage. That's not nice.
