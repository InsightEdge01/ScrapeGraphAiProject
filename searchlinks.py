from scrapegraphai.graphs import SearchLinkGraph
from scrapegraphai.utils import prettify_exec_info

# Define the configuration for the graph
# This dictionary sets up the parameters for the SearchLinkGraph instance.
graph_config = {
    # Configuration for the language model (LLM)
    "llm": {
        "model": "ollama/llama3.2",  # Specify the LLM model to use
        "temperature": 0,  # Set the temperature for deterministic outputs
        "format": "json",  # Output format explicitly required by Ollama
        "base_url": "http://localhost:11434",  # Base URL for the LLM API
    },
    "verbose": True,  # Enable verbose logging for debugging or detailed execution
    "headless": False,  # Run the scraper in a non-headless mode (browser visible)
    "filter_config": {  # Configuration for filtering URLs during scraping
        "diff_domain_filter": True,  # Filter out links from different domains
        "img_exts": [  # List of image file extensions to exclude
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'
        ],
        "lang_indicators": [  # Indicators to filter based on language in URLs
            #'lang=', '/fr', '/pt', '/es', '/de', '/jp', '/it'
            'lang=' '/es'
        ],
        "irrelevant_keywords": [  # Keywords or patterns to exclude irrelevant URLs
            '/login', '/signup', '/register', '/contact', 'facebook.com', 
            'twitter.com', 'linkedin.com', 'instagram.com', '.js', '.css', 
            '/wp-content/', '/wp-admin/', '/wp-includes/', '/wp-json/', 
            '/wp-comments-post.php', ';amp', '/about', '/careers', '/jobs', 
            '/privacy', '/terms', '/legal', '/faq', '/help', '.pdf', '.zip', 
            '/news', '/files', '/downloads'
        ]
    },
}

# Create the SearchLinkGraph instance and configure it for scraping
smart_scraper_graph = SearchLinkGraph(
    source="https://www.dataedgehub.com",  # URL to scrape
    config=graph_config  # Pass the defined configuration
)

# Run the scraper and print the result
result = smart_scraper_graph.run()
print(result)

# Retrieve and prettify graph execution information for debugging
graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
