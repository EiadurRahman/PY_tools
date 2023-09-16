while True:
    from googlesearch import search
    keyword = input(' keyword (press [ q ]) to exit > ')
    if keyword == 'q':
        break

    query = f"image_url:{keyword}"
    search_results = search(query, num=10, stop=30, pause=2)

    # Print search results
    for result in search_results:
        print("Search Result:", result)
