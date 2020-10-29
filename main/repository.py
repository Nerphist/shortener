from typing import Optional

from main.models import ShortenedUrl


def get_or_create_url(url: str) -> (ShortenedUrl, bool):
    url, created = ShortenedUrl.objects.get_or_create(url=url)
    return url, created


def get_url_by_id(url_id: int) -> Optional[ShortenedUrl]:
    return ShortenedUrl.objects.filter(id=url_id).first()


def increment_clicks(url_model: ShortenedUrl):
    url_model.clicks_count += 1
    url_model.save()
