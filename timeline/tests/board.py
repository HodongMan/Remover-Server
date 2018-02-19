# -*- coding: utf-8 -*-

from json import dumps
from django.test import TestCase, Client

from ..models import Board

class BoardTestCase(TestCase):

    def setUp(self):

        Board.objects.create(
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )

        Board.objects.create(
            user = "jhd9206@gmail.com",
            name = "hodongGod",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )

    def test_get_list_board_object(self):

        board_list = Board.objects.all()
        
        self.assertEqual(len(board_list), 2)
        self.assertEqual(board_list[0].name, "hodongGod")
        self.assertEqual(board_list[1].user, "arshavin3@naver.com")

    def test_get_retrieve_board_object(self):

        board_list1 = Board.objects.get(pk=1)
        board_list2 = Board.objects.get(pk=2)

        self.assertEqual(board_list1.name, "hodong")
        self.assertEqual(board_list2.description, "테스트는 해야 하는 것인가에 대하여 어렵구만")

    def test_create_board_object(self):

        new_board = Board.objects.create(
            user = "hodongGod@naver.com",
            name = "장호동",\
            description = "출근길 1시간 40분 너무한거 아니냐",
        )

        get_new_board = Board.objects.get(pk=3)

        self.assertEqual(new_board.description, get_new_board.description)

    def test_update_board_object(self):

        update_board = Board.objects.get(pk=2)
        update_board.views += 1
        update_board.save()

        self.assertEqual(update_board.views, 1)
        self.assertEqual(update_board.user, "jhd9206@gmail.com")

    def test_delete_board_object(self):

        delete_board = Board.objects.get(pk=1)
        delete_board.delete()

        board_list = Board.objects.all()

        self.assertEqual(len(board_list), 1)
        self.assertEqual(board_list[0].name, "hodongGod")

class BoardHttpTestCase(TestCase):

    def setUp(self):
        
        Board.objects.create(
            user = "arshavin3@naver.com",
            name = "hodong",
            description = "테스트란 어떤 걸까",
        )

        Board.objects.create(
            user = "jhd9206@gmail.com",
            name = "hodongGod",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        self.test_client = Client()

    def test_http_get_list_board(self):

        http_result = self.test_client.get("/api/timeline/")
        
        self.assertEqual(http_result.status_code, 200)
    
    def test_http_get_retrieve_board(self):

        http_result = self.test_client.get("/api/timeline/1/")
        http_404_result = self.test_client.get("/api/timeline/3/")

        self.assertEqual(http_result.status_code, 200)
        self.assertEqual(http_404_result.status_code, 404)

    def test_http_get_list_board_by_user(self):

        http_result = self.test_client.get("/api/timeline/search/user/jhd9206@gmail.com/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_post_create_board(self):

        http_result = self.test_client.post("/api/timeline/", {
            "user" : "hodongGod@naver.com",
            "name" : "Arsenal",
            "description" : "그들은 우승 하고 싶은 생각이 있긴 한가",
        })

        self.assertEqual(http_result.status_code, 201)

    
    def test_http_put_update_board(self):

        http_result = self.test_client.put("/api/timeline/1/", dumps({
            "user" : "hodongGod@naver.com",
            "name" : "Arsenal",
            "description" : "그들은 우승 하고 싶은 생각이 있긴 한가",
            "views" : 2,
        }), content_type="application/json")

        self.assertEqual(http_result.status_code, 200)
    

    def test_http_delete_board(self):

        http_result = self.test_client.delete("/api/timeline/1/")

        self.assertEqual(http_result.status_code, 204)
