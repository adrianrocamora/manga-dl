from .senmanga_com import SenMangaCom


class RawSenmangaCom(SenMangaCom):

    def get_archive_name(self) -> str:
        return self.get_chapter_index()

    def get_chapter_index(self):
        ch = self.chapter
        re = r'\.com/[^/]+/([^/]+)'
        return self.re.search(re, ch)


main = RawSenmangaCom
