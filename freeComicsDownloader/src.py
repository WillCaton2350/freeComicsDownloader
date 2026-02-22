
from dataclasses import dataclass


@dataclass
class data:
    img_id: str = 'divImage'
    page_id: str = 'selectPage.value'



class nums:
    num_pg: int = 26
    y = 0

class xpaths:
    xpath_1: str = '//*[@id="containerRoot"]/div[4]/div[1]/label[2]'
    nxt_pg: str = '//*[@id="selectPage"]'
    next_page_btn_xpath: str = '//*[@id="btnNext"]'

class urls:
    url: str = 'https://readcomiconline.li/Comic/Extremity/Issue-1?id=105627#1'
