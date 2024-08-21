"""_summary_"""


class Pagination:
    """ Pagination """

    def __init__(self, page_no: int, page_size: int, total_count: int):

        self.total_count = total_count
        self.total_pages = (total_count // page_size) + 1

        self.previous_page = page_no - 1 if page_no - 1 > 0 else 0
        self.next_page = page_no + 1 if page_no + \
            1 <= self.total_pages else self.total_pages
