"""
Multiple Tasks under a Class.
Simple Get Requests.
Calling from Another Class.
"""


from locust import HttpUser, TaskSet, constant, task


class GetJPetStore(TaskSet):

    @task
    def get_homepage(self):
        res = self.client.get('/')
        print(res.status_code)

    @task
    def get_catalog(self):
        res = self.client.get('/actions/Catalog.action')
        print(res.status_code)


class MyLoadTest(HttpUser):
    host = 'https://petstore.octoperf.com'
    tasks = [GetJPetStore]
    wait_time = constant(3)
