import urllib.request, json
from .models import News_Update
from .models import Article


api_key = None
base_url = None
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_updates(category):
    '''
    function to get json response of out request
    :param category
    :return:
    '''

    get_updates_url = base_url.format(category, api_key)
    print(get_updates_url)
    with urllib.request.urlopen(get_updates_url) as url:
        get_updates_data = url.read()
        get_updates_response = json.loads(get_updates_data)

        update_results = []

        if get_updates_response['sources']:
            update_results = get_updates_response['sources']
            update_results = process_results(update_results)

    return update_results


def process_results(update_results_list):
    '''
    process update result and transform to list of object
    '''
    update_results = []
    for update_content in update_results_list:
        id = update_content.get('id')
        name = update_content.get('name')
        category = update_content.get('category')
        url = update_content.get('url')

        update_object = News_Update(id, name, category, url)
        update_results.append(update_object)
    return update_results


def get_articles(id):
    get_articles_url = articles_url.format(id, api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results = get_articles_response['articles']
            articles_results = process_articles(articles_results)

    return articles_results

    #     articles_results = json.loads(url.read())
    #     articles_object = None
    #     if articles_results['articles']:
    #         articles_object = process_articles(articles_results['articles'])
    #
    # return articles_object


def process_articles(articles_list):
    articles_results = []

    for article_cont in articles_list:
        id = article_cont.get('id')
        author = article_cont.get('author')
        title = article_cont.get('title')
        description = article_cont.get('description')
        url = article_cont.get('url')
        image = article_cont.get('urlToImage')
        date = article_cont.get('publishedAt')
        articles_object = Article(id,author,title,description,url,image,date)
        articles_results.append(articles_object)

    return articles_results
