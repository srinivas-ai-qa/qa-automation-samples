from locust import HttpUser, between, task


class PostsUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task(3)
    def list_posts(self):
        self.client.get("/posts", name="/posts")

    @task(1)
    def read_post(self):
        self.client.get("/posts/1", name="/posts/[id]")
