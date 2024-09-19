AFTER = "group?query=&sort_by=changed&sort_order=DESC&page=0%2C{0}"


def get_page_entity(base_url, page) -> str:
    url = base_url + AFTER.format(page)
    return url
