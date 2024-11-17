from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(
    default_headers={"Authorization": f"Bearer {OPENAI_API_KEY}"}
)

def analyze_article(text):
    """
    Analyze a financial article using OpenAI's GPT-4 model to extract stock recommendations 
    or market insights.

    Args:
        text (str): The article text to analyze.

    Returns:
        str: A concise summary of the analysis with stock recommendations or insights.
    """
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a financial analyst. You need to analyze news articles and make stock "
                    "recommendations for the user. \nHere are some basic information that may help you "
                    "with your analysis: \nStock prices tick up and down constantly due to fluctuations "
                    "in supply and demand. If more people want to buy a stock, its market price will increase. "
                    "If more people are trying to sell a stock, its price will fall. The relationship between "
                    "supply and demand is highly sensitive to the news of the moment. Nonetheless, chasing the "
                    "news is not a good stock-picking strategy for the individual investor. In most cases, "
                    "professional traders react in anticipation of an event, not when the event is reported. "
                    "How News Affects Wall Street: Say Microsoft reports a hefty year-over-year increase in "
                    "its quarterly earnings. That's good news. Except that Wall Street may have been expecting "
                    "an even heftier increase. The stock price may fall.\n\n"
                    "Key Takeaways:\n"
                    "- Government economic reports are always news, as they suggest the strength or weakness of the "
                    "economy, the consumer, and key industry sectors.\n"
                    "- Quarterly financial reports indicate how a company did in recent months and may contain clues "
                    "for the near future.\n"
                    "- Global events can wreak unexpected havoc.\n"
                    "A day later, traders may decide that Microsoft's price has fallen lower than its fair price. They "
                    "will buy it, driving the share price up, in anticipation of even better sales to come in the "
                    "current quarter. Hours later, a new report may predict slowing sales in the overall tech sector. "
                    "Microsoft stock may fall, along with every other tech company out there.\n\n"
                    "This is one reason why so-called conservative stock pickers prefer a buy-and-hold strategy. They can "
                    "ignore the hour-to-hour noise, confident that a good company's stock will, over the long run, go up.\n\n"
                    "Good News/Bad News:\n"
                    "Negative news will normally cause people to sell stocks. A bad earnings report, a lapse in corporate "
                    "governance, big-picture economic and political uncertainty, and unfortunate occurrences all translate "
                    "to selling pressure and a decrease in the prices of many if not most stocks.\n\n"
                    "Wall Street traders don't try to follow the news. They try to anticipate it. Positive news will normally "
                    "cause individuals to buy stocks. Good earnings reports, an announcement of a new product, a corporate "
                    "acquisition, and positive economic indicators all translate into buying pressure and an increase in stock prices.\n\n"
                    "When Bad News Is Good News:\n"
                    "Bad news for some stocks is good news for others. For example, news that a hurricane has made landfall may "
                    "cause a decline in utility stocks, in anticipation of costly emergency responses and repairs. Depending on "
                    "the severity of the storm, insurance stocks will take a hit on the news.\n\n"
                    "Meanwhile, the stocks of home improvement retailers will rise in anticipation of higher sales over the months to come.\n\n"
                    "Anticipating the News:\n"
                    "As noted, professional traders spend much of their time trying to anticipate the next news cycle, so that they can "
                    "buy or sell stocks before the real numbers are released. Professionals use a number of sources of information in their efforts.\n\n"
                    "Government Economic Reports:\n"
                    "- The employment report from the Bureau of Labor Statistics is an indicator of the strength of the economy and the consumer.\n"
                    "- The U.S. Census Bureau report on durable goods orders suggests how confident retailers are of the strength of spending "
                    "in the months ahead. These are among many government reports that are used as lagging indicators and leading indicators. "
                    "Leading indicators, like those durable goods orders, are more highly prized.\n\n"
                    "Company and Industry News:\n"
                    "Quarterly reports are, literally, old news. Traders want to know how orders are shaping up right now, what products are "
                    "getting hot, and which trends are dying.\n\n"
                    "Gossip:\n"
                    "Business news reports often note that a company's revenues or sales met or failed to meet a 'whisper number.' This is exactly "
                    "what it sounds like. In the absence of hard facts, Wall Street professionals swap gossip, some of it based on solid information "
                    "and some not.\n\n"
                    "Unexpected News:\n"
                    "There are events that simply cannot be anticipated, like a massive auto safety recall, a Mideast crisis that drives up oil prices, "
                    "or a prolonged drought that devastates crops. Traders may think they're pricing in risks, but the possibilities for things going "
                    "wrong are limitless. Thus, it's unexpected news – not just any old news – that drives prices in one direction or the other."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Analyze the following finance article and identify any stock recommendations or market insights. "
                    f"Provide a concise summary and list any mentioned stocks (including their tickers) with your analysis.\n\nArticle:\n{text}"
                )
            }
        ]
    )
    return completion.choices[0].message.content
