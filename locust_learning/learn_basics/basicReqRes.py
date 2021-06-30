"""
Multiple tasks within one Class.
GET & POST Requests
"""
from locust import HttpUser, task, constant


class MyReqRes(HttpUser):

    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("api/users?page=2")
        print(res.status_code)
        print(res.elapsed)

    @task
    def create_user(self):
        res = self.client.post("api/users", data='''
        {name: "morpheus", job: "leader"}
        ''')
        print(res.status_code)
        print(res.elapsed)
