"""_summary_"""


class Pagination:
    """ Pagination """

    def __init__(self, page_no: int, page_size: int, total_count: int):

        self.total_count = total_count
        self.total_pages = (total_count // page_size)
        extra = (total_count % page_size)
        if extra > 0:
            self.total_pages += 1
        self.next_page = page_no + 1 if page_no + \
            1 <= self.total_pages else 0
        self.previous_page = page_no - 1 if page_no - 1 > 0 else 0
