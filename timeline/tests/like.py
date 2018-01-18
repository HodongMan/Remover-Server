from json import dumps
from django.test import TestCase, Client

from ..models import Board, Comment, Like

class LikeTestCase(TestCase):

    def setUp(self):

        board_result = Board.objects.create(
            email = "arshavin3@naver.com",
            name = "hodong",
            title = "테스트에 관하여",
            description = "테스트란 어떤 걸까",
        )

        Like.objects.create(
            board_id = board_result,
            email = "arshavin3@naver.com"
        )

        Like.objects.create(
            board_id = board_result,
            email = "jhd9206@gmail.com"
        )
        self._board = board_result

    def test_get_list_like_object(self):

        like_list = Like.objects.all()

        self.assertEqual(len(like_list), 2)
        self.assertEqual(like_list[1].email, "arshavin3@naver.com")
        self.assertEqual(like_list[0].email, "jhd9206@gmail.com")

    def test_get_retrieve_like_object(self):

        like_object1 = Like.objects.get(pk=1)
        like_object2 = Like.objects.get(pk=2)

        self.assertEqual(like_object1.email, "arshavin3@naver.com")
        self.assertEqual(like_object2.email, "jhd9206@gmail.com")

    def test_create_like_object(self):

        like_object = Like.objects.create(
            board_id = self._board,
            email = "hodongman@github.com",)        
        like_list = Like.objects.all()

        self.assertEqual(len(like_list), 3)
        self.assertEqual(like_list[0].email, like_object.email)
        self.assertEqual(like_list[0].email, "hodongman@github.com")

    def test_update_like_object(self):

        like_object = Like.objects.get(pk=1)
        
        like_object.email = "wenger@arsenal.com"
        like_object.save()

        like_list = Like.objects.all()
        self.assertEqual(like_object.email, like_list[1].email)
        self.assertEqual(like_list[1].email, "wenger@arsenal.com")

    def test_delete_like_object(self):

        like_object = Like.objects.get(pk=2)

        like_object.delete()

        like_list = Like.objects.all()
        self.assertEqual(len(like_list), 1)
        self.assertEqual(like_list[0].id, 1)


class LikeHttpTestCase(TestCase):

    def setUp(self):

        board_result = Board.objects.create(
            email = "arshavin3@naver.com",
            name = "hodong",
            title = "테스트에 관하여",
            description = "테스트란 어떤 걸까",
        )

        Like.objects.create(
            board_id = board_result,
            email = "arshavin3@naver.com"
        )

        Like.objects.create(
            board_id = board_result,
            email = "jhd9206@gmail.com"
        )
        self._client = Client()

    def test_http_get_list_like(self):

        http_result = self._client.get("/api/timeline/like/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_get_retireve_like(self):

        http_result1 = self._client.get("/api/timeline/like/1/")
        http_result2 = self._client.get("/api/timeline/like/2/")

        self.assertEqual(http_result1.status_code, 200)
        self.assertEqual(http_result2.status_code, 200)

    def test_http_post_create_like(self):

        http_result = self._client.post("/api/timeline/like/", {
            "board_id" : 1,
            "email" : "그럼난뭐하지@닷.컴",
        })

        self.assertEqual(http_result.status_code, 201)
    
    def test_http_put_update_like(self):

        http_result = self._client.put("/api/timeline/like/2/", dumps({
              "board_id" : 1,
              "email" : "Ozil@arsenal.com",
        }), content_type="application/json")

        self.assertEqual(http_result.status_code, 200)

    def test_http_delete_like(self):

        http_result = self._client.delete("/api/timeline/like/1/")
        self.assertEqual(http_result.status_code, 204)