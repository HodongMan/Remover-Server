from json import dumps
from django.test import TestCase, Client

from ..models import Category

class CategoryTestCase(TestCase):

    def setUp(self):

        Category.objects.create(
            title = "고민 상담"
        )
        Category.objects.create(
            title = "연애 고민"
        )
        Category.objects.create(
            title = "하소연"
        )

    def test_get_list_category_object(self):

        category_list = Category.objects.all()

        self.assertEqual(len(category_list), 3)
        self.assertEqual(category_list[0].title, "고민 상담")
        self.assertEqual(category_list[1].title, "연애 고민")
        self.assertEqual(category_list[2].title, "하소연")

    def test_get_retrieve_category_object(self):

        category_object1 = Category.objects.get(pk=1)
        category_object2 = Category.objects.get(pk=2)
        category_object3 = Category.objects.get(pk=3)

        self.assertEqual(category_object1.title, "고민 상담")
        self.assertEqual(category_object2.title, "연애 고민")
        self.assertEqual(category_object3.title, "하소연")

    def test_create_category_object(self):

        Category.objects.create(
            title = "개발"
        )
        category_object = Category.objects.get(pk=4)
        category_list = Category.objects.all()

        self.assertEqual(category_object.title, "개발")
        self.assertEqual(len(category_list), 4)
        self.assertEqual(category_list[0].title, category_object.title)

    def test_update_category_object(self):

        category_object = Category.objects.get(pk=2)
        category_object.title = "바꾼 제목"
        category_object.save()

        category_list = Category.objects.all()

        self.assertEqual(category_object.title, "바꾼 제목")
        self.assertEqual(category_list[1].title, category_object.title)

    def test_delete_category_object(self):

        category_object = Category.objects.get(pk=1)
        category_object.delete()

        category_list = Category.objects.all()

        self.assertEqual(len(category_list), 2)
        self.assertNotEqual(category_object.title, category_list[0].title)


class CategoryHttpTestCase(TestCase):

    def setUp(self):

        Category.objects.create(
            title = "고민 상담"
        )
        Category.objects.create(
            title = "연애 고민"
        )
        Category.objects.create(
            title = "하소연"
        )
        self._client = Client()

    def test_http_get_list_category(self):

        http_result = self._client.get("/api/board/category/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_get_retrieve_category(self):

        http_result1 = self._client.get("/api/board/category/1/")
        http_result2 = self._client.get("/api/board/category/2/")

        self.assertEqual(http_result1.status_code, 200)
        self.assertEqual(http_result2.status_code, 200)

    def test_http_post_create_category(self):

        http_result = self._client.post("/api/board/category/", {
            "title" : "새로운 제목"
        })
        
        self.assertEqual(http_result.status_code, 201)

    def test_http_put_update_category(self):

        http_result = self._client.put("/api/board/category/1/", dumps({
            "title" : "바뀐 제목"
        }), content_type="application/json")

        self.assertEqual(http_result.status_code, 200)

    def test_http_delete_category(self):

        http_result = self._client.delete("/api/board/category/1/")
        self.assertEqual(http_result.status_code, 204)