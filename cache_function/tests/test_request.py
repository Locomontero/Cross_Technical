import time
import unittest

import request

BASE_URL = 'https://jsonplaceholder.typicode.com'
POSTS_URL = BASE_URL + '/posts'


class Tests(unittest.TestCase):
    def test_cache(self):
        # First request
        self.assertGreater(_request_load_time(), 0.01)

        # Cached request
        self.assertLess(_request_load_time(), 0.01)

    def test_get_method(self):
        self.assertTrue(len(request.get(POSTS_URL)))

    def test_post_method(self):
        body = {
            'title': 'test',
            'body': 'bar',
            'userId': 1
        }
        self.assertTrue(len(request.post(POSTS_URL, data=body)))

    def test_put_method(self):
        body = {
            'id': 1,
            'title': 'test',
            'body': 'barth',
            'userId': 1
        }
        self.assertTrue(len(request.put(f'{POSTS_URL}/{body.get("id")}', data=body)))

    def test_patch_method(self):
        id = 1
        body = {
            'body': 'barth',
        }
        self.assertTrue(len(request.patch(f'{POSTS_URL}/{id}', data=body)))

    def test_delete_method(self):
        id = 1
        self.assertDictEqual(request.delete(f'{POSTS_URL}/{id}'), {})


def _request_load_time():
    """ Returns request load time """
    start = time.time()
    request.get(POSTS_URL)
    end = time.time()
    load_time = end - start
    return load_time


if __name__ == '__main__':
    unittest.main()
