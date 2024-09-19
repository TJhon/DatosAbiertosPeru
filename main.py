from DatosPeru.scrapper.search import get_list_content_link_name, SearchGroup, get_soup
import pandas as pd

a = SearchGroup()

# a = get_list_content_link_name(
#     "https://expresateperu.datosabiertos.gob.pe/search/type/group?query=&sort_by=changed&sort_order=DESC&page=0%2C1",
#     "s",
# )
base_url = "https://expresateperu.datosabiertos.gob.pe"
url = a.data_group.head()["url"].values[0]
b = get_soup(url)
print(url)
# view_content = b.find("div", {"id": "main-wrapper"})
data_divs = b.find_all("h2", {"class": "node-title"})
n_data = len(data_divs)

# Data links in in
hrefs = [base_url + data_div.find("a").get("href") for data_div in data_divs]

href_id = hrefs[0]
c = get_soup(href_id)
id_datasets = c.find("div", {"class": "field-name-field-identifier"}).text

# api, datasets: https://expresateperu.datosabiertos.gob.pe/api/3/action/package_show?id=ba35e951-c2ef-4b0b-9faf-3e539d1bea92


url_api = base_url + f"/api/3/action/package_show?id={id_datasets}"
import requests as r

data_set = r.get(url_api).json()

result = data_set["result"][0]
resources = result["resources"]  # []
group = result["groups"][0]  # []

result_info = ["title", "notes"]
# print(result)
info_metadata = [result[info] for info in result_info]


resource_info = ["id", "url", "name", "description", "format", "size"]
# resouces_metadata = []
# for
group_info = ["id", "title"]
group_metadata = [group[info] for info in group_info]

print(group_metadata, info_metadata)

metadata = []
for resource in resources:
    metadata_i = []
    for info in resource_info:
        metadata_i.append(resource[info])
    metadata.append(metadata_i)
print(metadata)

metadata = [[resource[info] for info in resource_info] for resource in resources]
print(metadata)
