# VK Getter

Very simple and pythonic way to extract data from [VK](https://vk.com).

## Getting started

Install package via pip

```
pip install vk_getter
```

Use your access token, and get posts from any public group. You can get token [here](https://vkhost.github.io/).

```python
from vk_getter import VKGetter

getter = VKGetter("TOKEN")

# get 200 latest posts from https://www.vk.com/vk
posts = getter.get_posts("vk", 200) 

# get 150 posts with offset of 50
posts = getter.get_posts("lol", 150, 50)
```

You can specify different settings:

```python
posts = getter.get_latest_posts("https://www.vk.com/vk",
                                count=120,
				offset=20,
                                pinned=False,
                                allow_no_attachments=False,
                                ads=False,
                                copyright=False)
```

All posts are retrieved as a Python dataclasses, but can also be returned as dicts.

```python
posts = getter.get_latest_posts(group_domain="vk",
                                count=1,
                                as_dict=True)
# posts[0] = 
#     {
#         "id": 1320761,
#         "date": "15.09.2022",
#         "time": "14:15:11",
#         "text": "...",
#         "attachments": {
#             "photo": [],
#             "video": [
#                 "..."
#             ],
#             "audio": [],
#             "other": []
#         },
#         "comments": 858,
#         "likes": 1150,
#         "reposts": 371,
#         "views": 518953
#     }

```

## Attachments

You can download gathered attachments to your local system.

```python
from vk_getter import VKGetter
from vk_getter.utils import download, download_all

getter = VKGetter("TOKEN")
posts = getter.get_posts("lol", 150)

# download all of the 4 types
path = "lol"
download_all(posts, path)

# or specify one
download(posts, "photo", path)
download(posts, "video", path)
download(posts, "audio", path)
download(posts, "other", path)
```

Or you can extract them as links.

```python
from vk_getter import VKGetter
from vk_getter.utils import extract, extract_all

getter = VKGetter("TOKEN")
posts = getter.get_posts("lol", 150)

# extract all of the 4 types
photos, videos, audios, others = extract_all(posts)

# or specify one
photos = extract(posts, "photo")
videos = extract(posts, "video")
audios = extract(posts, "audio")
others = extract(posts, "other")
```

`*Note:` do NOT use `as_dict` in the get_posts method.

---
