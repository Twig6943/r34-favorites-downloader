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
- Works (at least on my machine :D ) (It used to not work without the useragent stuff. That might not be the case for everybody tho) 
  ### Work-in-progress features of this fork // Not implemented 
- Uses Cloudflare to accsess the site (work-in-progress) (use a VPN or your OS's DNS for now.)
- Ublock origin (work-in-progress) (Still trying to figure out how firefox profiles work without relying on a OS specific directory) (Might just make it so that it asks the user where their firefox profile is located at) 

I literally just tweaked some stuff using ChatGPT. (Da Useragent stuff and what not) Please don't credit me for this in any way. I've used ChatGPT like a bitch just like I usually do. I was going to contact the original developer but his socials seem dead. Most of the code in this repo is written by @owosus . This repo will be taken down if I manage to contact @owosus somehow.

Resources I've used:

https://stackoverflow.com/questions/54271599/how-to-change-user-agent-for-firefox-webdriver-in-python
