# twitch-scraper
Simple scraper and clip assembler.

Basic usage\
REQUIRED: TWITCH API CREDENTIALS.

I used a config.py file with global variables for ease of sharing however you could easily implement a .env or settings.json etc...\


Required args in this order:\ 
GameName ex "League of Legends"\
TimeGap ex "Daily" or "Weekly"\ 
Iteration ex 1 or 2\

Full Example:\
python main.py "League of Legends" "Daily" 5\

Program is currently using a NVIDIA based encoder so AMD users may have issues.\
# YTGenerator
