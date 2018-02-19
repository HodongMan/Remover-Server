from json import dumps
from django.utils import timezone
from django.test import TestCase, Client

from ..models import Category, Board, Comment, Like

class LikeTestCase(TestCase):

    def setUp(self):

        self._category = Category.objects.create(
            title = "고민 상담"
        )
        self._board1 = Board.objects.create(
            category_id = self._category,
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )
        self._board2 = Board.objects.create(
            category_id = self._category,
            user = "jhd9206@gmail.com",
            name = "hodongGod",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        Like.objects.create(
            board_id = self._board1,
            user = "hodonggod@net.com",
        )
        Like.objects.create(
            board_id = self._board1,
            user = "hodonggod2@net.com",
        )
        Like.objects.create(
            board_id = self._board2,
            user = "hodonggod3@net.com",
        )
        Like.objects.create(
            board_id = self._board2,
            user = "hodonggod4@net.com",
        )

    def test_get_list_like_object(self):

        like_list = Like.objects.all()

        self.assertEqual(like_list[0].user, "hodonggod@net.com")
        self.assertEqual(like_list[1].user, "hodonggod2@net.com")
        self.assertEqual(like_list[2].user, "hodonggod3@net.com")
        self.assertEqual(like_list[3].user, "hodonggod4@net.com")

    def test_get_retrieve_like_object(self):

        like_object1 = Like.objects.get(pk=1)
        like_object2 = Like.objects.get(pk=2)
        like_object3 = Like.objects.get(pk=3)
        like_object4 = Like.objects.get(pk=4)

        self.assertEqual(like_object1.user, "hodonggod@net.com")
        self.assertEqual(like_object2.user, "hodonggod2@net.com")
        self.assertEqual(like_object3.user, "hodonggod3@net.com")
        self.assertEqual(like_object4.user, "hodonggod4@net.com")

    def test_create_like_object(self):

        Like.objects.create(
            board_id = self._board2,
            user = "hodonggod5@net.com",
        )
        like_object = Like.objects.get(pk=5)
        
        self.assertEqual(like_object.user, "hodonggod5@net.com")

    def test_update_like_object(self):

        update_like = Like.objects.get(pk=3)
        update_like.user = "godhodong@naver.com"
        update_like.save()

        like_object = Like.objects.get(pk=3)

        self.assertEqual(update_like.user, like_object.user)

    def test_delete_like_object(self):

        delete_like = Like.objects.get(pk=1)
        delete_like.delete()
        like_list = Like.objects.all()

        self.assertEqual(len(like_list), 3)
        self.assertNotEqual(delete_like, like_list[0])

class LikeHttpTestCase(TestCase):

    def setUp(self):

        category = Category.objects.create(
            title = "고민 상담"
        )
        board1 = Board.objects.create(
            category_id = category,
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )
        board2 = Board.objects.create(
            category_id = category,
            user = "jhd9206@gmail.com",
            name = "hodongGod",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        Like.objects.create(
            board_id = board1,
            user = "hodonggod@net.com",
        )
        Like.objects.create(
            board_id = board1,
            user = "hodonggod2@net.com",
        )
        Like.objects.create(
            board_id = board2,
            user = "hodonggod3@net.com",
        )
        Like.objects.create(
            board_id = board2,
            user = "hodonggod4@net.com",
        )
        self._client = Client()

    def test_http_get_list_like(self):

        http_response = self._client.get("/api/board/like/")
        self.assertEqual(http_response.status_code, 200)

    def test_http_get_retrieve_like(self):

        http_response1 = self._client.get("/api/board/like/1/")
        http_response2 = self._client.get("/api/board/like/2/")
        http_response3 = self._client.get("/api/board/like/3/")
        http_response4 = self._client.get("/api/board/like/4/")

        self.assertEqual(http_response1.status_code, 200)
        self.assertEqual(http_response2.status_code, 200)
        self.assertEqual(http_response3.status_code, 200)
        self.assertEqual(http_response4.status_code, 200)

    def test_http_post_create_like(self):

        http_response = self._client.post("/api/board/like/", {
            "board_id" : 2,
            "user" : "hodonggod2@net.com",
        })
        self.assertEqual(http_response.status_code, 201)

    def test_http_put_update_like(self):

        http_response = self._client.put("/api/board/like/1/", dumps({
            "board_id" : 1,
            "user" : "hodonggod2@net.com",
        }), content_type="application/json")
        self.assertEqual(http_response.status_code, 200)

    def test_http_delete_like(self):

        http_response = self._client.delete("/api/board/like/2/")
        self.assertEqual(http_response.status_code, 204)