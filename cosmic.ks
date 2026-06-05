WORKFLOW daily_ai_news

TRIGGER schedule "0 8 * * *"

AGENT researcher

SEARCH "latest artificial intelligence news"

SAVE results AS news

AGENT analyst

READ news

SUMMARIZE

SAVE summary

AGENT narrator

SPEAK summary

END
