from pornhub_api import PornhubApi
import random


class CornAPI:

    def __init__(self):
        self.api = PornhubApi()

    def search_for_randomcorn(self):
        try:
            tags = random.sample(self.api.video.tags('f').tags, 5)
            category = random.choice(self.api.video.categories().categories)
            data = self.api.search.search(
                ordering="mostviewed",
                tags=tags,
                category=category
            )
        except ValueError:
            return None

        if len(data.videos) == 0:
            return None
        return data.videos[0].url

    def search_for_mostviewed_corn(self):
        data = self.api.search.search(
            ordering="mostviewed"
        )
        if len(data.videos) == 0:
            return None
        return data.videos[0].url

    def search_for_corn(self, query, period):
        try:
            data = self.api.search.search(
                query,
                ordering="mostviewed",
                period=period
            )
        except ValueError:
            return None

        if len(data.videos) == 0:
            return None
        return data.videos[0].url
