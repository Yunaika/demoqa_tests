from selene.support.shared import browser


class Table:
    @staticmethod
    def path_to_cell(tr: int, td: int):
        return browser.element(f'//*[@class="table-responsive"]//tr[{tr}]//td[{td}]')
