"""
Simple Get Request with TaskSet.
Calling from Another Class.
"""

from locust import TaskSet, constant, task, HttpUser


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)
