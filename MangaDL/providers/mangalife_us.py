from MangaDL.provider import Provider
from .helpers.std import Std


class MangaLifeUs(Provider, Std):
    img_selector = '.image-container .CurImage'

    def get_archive_name(self) -> str:
        idx = self.get_chapter_index().split('-')
        return 'vol_{:0>2}-{:0>3}'.format(*idx)

    def get_chapter_index(self) -> str:
        selector = r'-chapter-(\d+).+(?:-index-(\d+))?'
        chapter = self.re.search(selector, self.chapter).groups()
        return '{}-{}'.format(
            1 if chapter[1] is None else chapter[1],  # todo: maybe 0 ?
            chapter[0]
        )

    def get_main_content(self):
        return self._get_content('{}/manga/{}')

    def get_manga_name(self) -> str:
        uri = self.get_url()
        test = uri.find('.us/read-online/') > 0
        if test:
            uri = self.html_fromstring(uri, 'a.list-link', 0).get('href')
        return self.re.search(r'(?:\.us)?/manga/([^/]+)', uri).group(1)

    def get_chapters(self):
        return self._elements('.chapter-list a.list-group-item')

    def get_files(self):
        url = self.chapter
        parser = self.html_fromstring(url, '.mainWrapper', 0)
        pages = parser.cssselect('select.PageSelect')[0].cssselect('option + option')
        images = self._images_helper(parser, self.img_selector)
        for page in pages:
            page_url = self.re.sub(r'(.+page-)\d+(.+)', r'\1{}\2', url)
            parser = self.html_fromstring(page_url.format(page.get('value')))
            images += self._images_helper(parser, self.img_selector)
        return images

    def get_cover(self) -> str:
        return self._cover_from_content('.leftImage img')


main = MangaLifeUs