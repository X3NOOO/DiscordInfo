#!/bin/python3
#DiscordInfo (https://github.com/X3NOOO/DiscordInfo)
#Copyright (C) X3NO [X3NO@disroot.org] 
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from urllib.request import Request, urlopen
from rich.console import Console
from rich.table import Table
from datetime import datetime
from json import loads
import pprint
import requests
#from base64 import b64decode

DEBUG = bool(True)

class debug:
    RichConsole = Console()

    @staticmethod
    def Info(text):
        if DEBUG:
            debug.RichConsole.print("[cyan bold][*] [/cyan bold]" + text)

    @staticmethod
    def Warning(text):
        if DEBUG:
            debug.RichConsole.print("[bright_red bold][-] [/bright_red bold]" + text)

    @staticmethod
    def Error(text):
        if DEBUG:
            debug.RichConsole.print("[red bold][!] [/red bold]" + text)

def welcomeScreen():
    ascii_art = """
▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▓ ███▄    █   █████▒▒█████  
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒     ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
   ░     ░        ░  ░ ░          ░ ░     ░        ░        ░           ░            ░ ░  
 ░                   ░                           ░                                        
"""
    print(ascii_art  + "By X3NO (https://github.com/X3NOOO)")

def makeRequest(token):
    debug.Info("makeRequest")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Authorization": token
    }
    try:
        info_general = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    except Exception as e:
        debug.Error(str(e))
    
    lg_codes = {
        'da'    : 'Denmark',
        'de'    : 'Germany',
        'en-GB' : 'UK',
        'en-US' : 'US',
        'es-ES' : 'Spain',
        'fr'    : 'France',
        'hr'    : 'Croatia',
        'lt'    : 'Lithuania',
        'hu'    : 'Hungary',
        'nl'    : 'Netherlands',
        'no'    : 'Norway',
        'pl'    : 'Poland',
        'pt-BR' : 'Brazil',
        'ro'    : 'Romania',
        'fi'    : 'Finland',
        'sv-SE' : 'Sweden',
        'vi'    : 'Vietnam',
        'tr'    : 'Turkey',
        'cs'    : 'Czech Republic',
        'el'    : 'Greece',
        'bg'    : 'Bulgaria',
        'ru'    : 'Russia',
        'uk'    : 'Ukraine',
        'th'    : 'Thailand',
        'zh-CN' : 'China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Taiwan',
        'ko'    : 'Korea'
    }
    friends = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    debug.Info(f"{friends=}")
    channels = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=headers)).read().decode())
    debug.Info(f"{channels=}")
    ## format info
    user_name = info_general["username"]
    debug.Info(f"{user_name=}")
    uid = str(info_general["id"])
    debug.Info(f"{uid=}")
    avid = info_general["avatar"]
    av_url = f"https://cdn.discordapp.com/avatars/{uid}/{avid}"
    phone = str(info_general["phone"])
    debug.Info(f"{phone=}")
    email = info_general["email"]
    debug.Info(f"{email=}")
    mfa_enabled = str(info_general['mfa_enabled'])
    debug.Info(f"{mfa_enabled=}")
    flags = str(info_general['flags'])
    debug.Info(f"{flags=}")
    locale = info_general['locale']
    debug.Info(f"{locale=}")
    verified = str(info_general['verified'])
    debug.Info(f"{verified=}")
    nsfw_allowed = str(info_general['nsfw_allowed'])
    debug.Info(f"{nsfw_allowed=}")
    discriminator = str(info_general['discriminator'])
    debug.Info(f"{discriminator=}")
    # visuals
    bio = str(info_general['bio'])
    debug.Info(f"{bio=}")
    banner = info_general['banner']
    debug.Info(f"{banner=}")
    banner_color = str(info_general['banner_color'])
    debug.Info(f"{banner_color=}")
    accent_color = str(info_general['accent_color'])
    debug.Info(f"{accent_color=}")
    lang = lg_codes.get(locale)
    debug.Info(f"{lang=}")
    creation_date = datetime.utcfromtimestamp(((int(uid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S')
    nitro_data = (requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)).json()
    has_nitro = bool(len(nitro_data) > 0)
    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        nitro_days_left = abs((d2 - d1).days)

    # billing info - by wodxgod https://github.com/wodxgod/DTI/blob/master/DTI.py
    billing_info = []
    for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']

        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
                        
            data = {
                'Payment Type': 'Credit Card',
                'Valid': not x['invalid'],
                'CC Holder Name': name,
                'CC Brand': cc_brand.title(),
                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment Method': x['default']
            }

        elif x['type'] == 2:
            data = {
                'Payment Type': 'PayPal',
                'Valid': not x['invalid'],
                'PayPal Name': name,
                'PayPal Email': x['email'],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment Method': x['default']
            }

        billing_info.append(data)
        
    ## display info
    RichConsole=Console()
    basicTable=Table(title="\nBasic information", show_header=True, show_edge=False, show_lines=True, width=120)
    basicTable.add_column("Name", justify="left")
    basicTable.add_column("Value", justify="left")
    basicTable.add_row("User Name", user_name)
    basicTable.add_row("User ID", uid)
    basicTable.add_row("Email", email)
    basicTable.add_row("Phone", phone)
    basicTable.add_row("Token", token)
    basicTable.add_row("Creation date", creation_date)
    basicTable.add_row("Locale", locale)
    basicTable.add_row("Language", lang)
    basicTable.add_row("Avatar id", avid)
    basicTable.add_row("Avatar url", av_url)
    basicTable.add_row("Discriminator", discriminator)
    RichConsole.print(basicTable)
        
    visualsTable=Table(title="\nVisuals information", show_header=True, show_edge=False, show_lines=True, width=120)
    visualsTable.add_column("Name", justify="left")
    visualsTable.add_column("Value", justify="left")
    visualsTable.add_row("Bio", bio)
    visualsTable.add_row("Banner", banner)
    visualsTable.add_row("Banner color", banner_color)
    visualsTable.add_row("Accent color", accent_color)
    RichConsole.print(visualsTable)
    
    nitroTable=Table(title="\nNitro information", show_header=True, show_edge=False, show_lines=True, width=120)
    nitroTable.add_column("Name", justify="left")
    nitroTable.add_column("Value", justify="left")
    nitroTable.add_row("Has nitro", str(has_nitro))
    if has_nitro:
        nitroTable.add_row("Expires in", nitro_days_left)
    RichConsole.print(nitroTable)
    
    securityTable=Table(title="\nSecurity information", show_header=True, show_edge=False, show_lines=True, width=120)
    securityTable.add_column("Name", justify="left")
    securityTable.add_column("Value", justify="left")
    securityTable.add_row("MFA enabled", mfa_enabled)
    securityTable.add_row("Flags", flags)
    securityTable.add_row("Email verified", verified)
    securityTable.add_row("NSFW allowed", nsfw_allowed)
    RichConsole.print(securityTable)

    if len(billing_info) > 0:
        billingTable=Table(title="\nBilling info", show_header=True, show_edge=False, show_lines=True, width=120)
        billingTable.add_column("Name", justify="left")
        billingTable.add_column("Value", justify="left")
        if len(billing_info) == 1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    billingTable.add_row(key, val)
        else:
            for i, x in enumerate(billing_info):
                #title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                billingTable.add_row(f"Payment Method #{i + 1}", f'{x["Payment Type"]}')
                #print('    ' + title)
                #print('    ' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    #print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))
                    billingTable.add_row(key, val)
                if i < len(billing_info) - 1:
                    print(f'{Fore.RESET}\n')
        print(f'{Fore.RESET}\n')
        RichConsole.print(billingTable)
    
    #TODO Format friends and channels output
    print("\nSaved friends to ./friends.log")
    with open("friends.log", 'w') as f:
        f.write(str(pprint.pprint(friends)))
        f.close
    print("\nSaved channels to ./channels.log")
    with open("channels.log", 'w') as f:
        f.write(str(pprint.pprint(channels)))
        f.close

    
def main():
    debug.Info("main")
    welcomeScreen()

    if str(input("This software was created for educational purposes only, by using it you automatically agree not to use it for any other purpose. Do you understand? (yes/no): ")) == "yes":
        token = str(input("Enter token: "))
        debug.Info(f"{token=}")
        makeRequest(token)
    return 0

    
if __name__ == "__main__":
    main()
