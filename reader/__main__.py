import sys

import reader
from reader import feed, viewer


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]

    url = reader.URL

    if args:
        for article_id in args:
            article = feed.get_article(article_id, url=url)
            viewer.show(article)
    else:
        site = feed.get_site(url=url)
        titles = feed.get_titles(url=url)
        viewer.show_list(site, titles)


if __name__ == "__main__":
    main()
