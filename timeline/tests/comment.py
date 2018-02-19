# -*- coding: utf-8 -*-

from json import dumps
from django.test import TestCase, Client

from ..models import Comment, Board

class CommentTestCase(TestCase):

    def setUp(self):

        board_result = Board.objects.create(
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )

        Comment.objects.create(
            board_id = board_result,
            user = "wenger@arshenal.com",
            name = "Wenger",
            description = "호동 산체스 대체자로 올래?",
        )

        Comment.objects.create(
            board_id = board_result,
            user = "펩@manchestercity.com",
            name = "펩",
            description = "아게로 팔건데 호동 올래?",
        )

        self.board_result = board_result

    def test_get_list_comment_object(self):

        comment_list = Comment.objects.all()

        self.assertEqual(len(comment_list), 2)
        self.assertEqual(comment_list[0].name, "펩")
        self.assertEqual(comment_list[1].name, "Wenger")

    def test_get_retrieve_comment_object(self):

        comment_list1 = Comment.objects.get(pk=1)
        comment_list2 = Comment.objects.get(pk=2)

        self.assertEqual(comment_list1.description, "호동 산체스 대체자로 올래?")
        self.assertEqual(comment_list2.description, "아게로 팔건데 호동 올래?")

    def test_create_comment_object(self):

        Comment.objects.create(
            board_id = self.board_result,
            user = "콘테@chelsea.com",
            name = "콘테",
            description = "모라타 튜토리얼 가능하냐",
        )

        new_comment = Comment.objects.get(pk=3)

        self.assertEqual(new_comment.description, "모라타 튜토리얼 가능하냐")

    def test_update_comment_object(self):

        update_comment = Comment.objects.get(pk=2)

        update_comment.description = "마네 팔건데 호동 올래?"
        update_comment.save()

        updated_comment = Comment.objects.get(pk=2)

        self.assertEqual(update_comment.description, updated_comment.description)
        self.assertEqual(updated_comment.description, "마네 팔건데 호동 올래?")

    def test_delete_comment_object(self):

        delete_comment = Comment.objects.get(pk=2)
        delete_comment.delete()

        comment_list = Comment.objects.all()

        self.assertEqual(len(comment_list), 1)
        self.assertNotEqual(comment_list[0].description, delete_comment.description)

class CommentHttpTestCase(TestCase):

    def setUp(self):

        board_result = Board.objects.create(
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )

        Comment.objects.create(
            board_id = board_result,
            user = "wenger@arshenal.com",
            name = "Wenger",
            description = "호동 산체스 대체자로 올래?",
        )

        Comment.objects.create(
            board_id = board_result,
            user = "펩@manchestercity.com",
            name = "펩",
            description = "아게로 팔건데 호동 올래?",
        )

        self.test_client = Client()

    def test_http_get_list_comment(self):

        http_response = self.test_client.get("/api/timeline/comment/")
        self.assertEqual(http_response.status_code, 200)

    def test_http_get_retrieve_comment(self):

        http_response1 = self.test_client.get("/api/timeline/comment/1/")
        http_response2 = self.test_client.get("/api/timeline/comment/2/")

        self.assertEqual(http_response1.status_code, 200)
        self.assertEqual(http_response2.status_code, 200)

    def test_http_post_create_comment(self):

        http_response = self.test_client.post("/api/timeline/comment/", {
            "board_id" : 1,
            "user" : "Hodong God@naver.com",
            "name" : "장호동",
            "description" : "장호동이 짱이쥬",
        })

        self.assertEqual(http_response.status_code, 201)

    def test_http_put_update_comment(self):
        
        http_response = self.test_client.put("/api/timeline/comment/1/", dumps({
            "board_id" : 1,
            "user" : "hodongGod@naver.com",
            "name" : "Arsenal",
            "description" : "그들은 우승 하고 싶은 생각이 있긴 한가",
        }), content_type="application/json")

        self.assertEqual(http_response.status_code, 200)

    def test_http_delete_comment(self):

        http_response1 = self.test_client.delete("/api/timeline/comment/1/")
        http_response2 = self.test_client.delete("/api/timeline/comment/2/")

        self.assertEqual(http_response1.status_code, 204)
        self.assertEqual(http_response2.status_code, 204)