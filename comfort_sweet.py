import requests  # `pip install requests`; DO IT!
import sys
import time


class ComfortSweet:

    def main(self):
        # This sets up the form data that gets passed when you click to 
        # "accept" the terms/connection... 
        expected_form_data = {
            'username': 'hotelguest',  # Checkbox
            'password': 'wireless',  # Hidden
            'original_url': 'http://www.gstatic.com/generate_204',  # Hidden
            'login': 'Accept',  # Named Submit button
        }
        # This can request any public URL. Even a HEAD request would work, 
        # if you were concerned about preserving bandwidth, etc. 
        result = requests.get(
            "http://www.icanhaztimestamp.com/", allow_redirects=False)
        # When we receive anything other than a 200, we can safely assume
        # we're being redirected to the captive portal. Once this happens, 
        # we will send the "accept" form data to the captive portal, 
        # which will immediately re-enable normal internet service. 
        if result.status_code != 200:
            requests.post(
                'http://wireless.colubris.com:1080/goform/HtmlLoginRequest',
                data=expected_form_data)
            print "\nPosted the goods. Welcome back to the internet."
        sys.stdout.write(".")
        # Be nice. Sleep for a few seconds.
        time.sleep(5)
        sys.stdout.flush()


if __name__ == '__main__':
    CS = ComfortSweet()
    while True:
        try:
            CS.main()
        except KeyboardInterrupt:
            sys.exit()
        except requests.exceptions.RequestException as e:
            print e.__class__.__name__
