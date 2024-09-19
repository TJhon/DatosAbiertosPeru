from .utils import get_soup
import pandas as pd, re


def get_list_content_link_name(url: str, base_url: str):
    soup = get_soup(url)
    view_content = soup.find("div", {"class", "view-content"})
    if view_content is None:
        return pd.DataFrame([[None, None]])
    anchors = view_content.find_all("a")
    links_names = [[base_url + anchor.get("href"), anchor.text] for anchor in anchors]
    return pd.DataFrame(links_names)


class SearchGroup:
    def __init__(
        self,
        base_url_type="https://expresateperu.datosabiertos.gob.pe/search/type",
        after: str = '/group?query=&sort_by=changed&sort_order=DESC&page=0%2C{}"',
        pages=10,
    ) -> None:
        # note: 0 is page 1 -> n is page n-1
        self.urls = [base_url_type + after.format(page) for page in range(pages)]
        self.base_url_main = base_url_type
        self.gen_group_urls()

    def gen_group_urls(self):
        base_url_group = self.base_url_main
        base_url = re.sub(r"(\.gob\.pe).*", r"\1", base_url_group)
        self.base_url = base_url

        info_df = [get_list_content_link_name(url, base_url) for url in self.urls]

        data_url_name = pd.concat(info_df).dropna()
        data_url_name.columns = ["url", "group"]
        self.data_group = data_url_name
