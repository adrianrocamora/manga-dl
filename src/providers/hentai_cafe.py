from src.providers.jaiminisbox_com import JaiminIsBoxCom


class HentaiCafe(JaiminIsBoxCom):
    _name_re = r'\.cafe(?:/manga/read)?/([^/]+)/'
    _content_str = '{}/{}/'
    _chapters_selector = '.content .last .x-btn'  # TODO

    def get_archive_name(self) -> str:
        return 'archive_{}'.format(self._chapter_index())

    def get_chapter_index(self) -> str:
        return str(self._chapter_index())

    def get_cover(self) -> str:
        return self._get_cover_from_content('.entry-content img')


main = HentaiCafe
