import requests
class Post:

    def __init__(self):
        self.endpoint = "https://api.npoint.io/0b58960888cf476332b3"
        self.blog_posts = self.get_posts()


    def get_posts(self):
        with requests.get(self.endpoint) as response:
            response.raise_for_status()
            return  response.json()

    def post_by_id(self, id):
        for x in self.blog_posts:
            if x['id'] == int(id):
                return self.blog_posts[self.blog_posts.index(x)]

