# r34-favorites-downloader

![placeholder](https://github.com/Twig6943/r34-favorites-downloader/blob/main/r34favdl.png?raw=true) 

Extremely simple python script, that can download any users favorites from rule34.xxx
Also very easy to modify to fit your own needs.

1. Enter profile ID
2. Enter page to download
3. Don't touch the browser (It will operate itself)

### Requirements
- selenium (Python module)
- webdriver_manager (Python module)
- wget (Python module)
- Firefox Browser

### Extra features of this fork
- Can download multiple pages at once
- Works (at least on my machine :D ) (It used to not work without the useragent stuff. At least on my machine) 
  ### Work-in-progress features // Not implemented 
- Uses Cloudflare to accsess the site (work-in-progress) (use a VPN or your OS's DNS for now.)
- Ublock origin (work-in-progress) (Still trying to figure out how firefox profiles work without relying on a OS specific directory) (Might just make it so that it asks the user where their firefox profile is located at) 

I literally tweaked some stuff to get with ChatGPT (Useragent stuff) to get it working again and added some features. Please don't credit me for this in any way. I just used ChatGPT like a bitch to get it working. I was going to contact the original developer but his socials seem dead. Most of the code in this repo is written by @owosu . This repo will be taken down if I manage to contact @owosu somehow.

Resources I've used:
https://stackoverflow.com/questions/54271599/how-to-change-user-agent-for-firefox-webdriver-in-python
https://www.reddit.com/r/selenium/comments/p44sie/dns_settings_with_geckodriver/
https://stackoverflow.com/questions/54754945/how-to-install-extension-permanently-in-geckodriver
