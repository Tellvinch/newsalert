import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_newss(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newss_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_newss_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(newss_list):
    '''
    Function that processes the source result and transforms them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''

    newss_results = []
    for news_item in newss_list:
        id = news_item.get("id")
        name = news_item.get("name")
        description = news_item.get("description")
        url = news_item.get("url")
        category = news_item.get("category")
        language = news_item.get("language")
        country = news_item.get("country")

        if description:

            newss_object =News(id, name, description, url,category, language, country)
            newss_results.append(newss_object)

    return newss_results

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')


            news_object = News(id,name,description,url,category,language,country)

    return news_object