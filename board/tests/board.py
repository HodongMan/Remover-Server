from json import dumps
from django.utils import timezone
from django.test import TestCase, Client

from ..models import Category, Board

class BoardTestCase(TestCase):

    def setUp(self):

        self._category1 = Category.objects.create(
            title = "고민 상담"
        )
        self._category2 = Category.objects.create(
            title = "연애 고민"
        )
        Board.objects.create(
            category_id = self._category1,
            email = "arshavin3@naver.com",
            name = "hodong",
            title = "테스트에 관하여",
            description = "테스트란 어떤 걸까",
        )
        Board.objects.create(
            category_id = self._category1,
            email = "jhd9206@gmail.com",
            name = "hodongGod",
            title = "테스트는 해야 하는 것인가",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        Board.objects.create(
            category_id = self._category2,
            email = "쩌리짱@teamnexters.com",
            name = "넥터",
            title = "넥터에서 개발중",
            description = "후 넥터에서 개발하기란 참으로 어려운건지 쉬운건지",
        )
        Board.objects.create(
            category_id = self._category2,
            email = "hyeheon@nexters.com",
            name = "정해현",
            title = "CEO님짱",
            description = "둥실때문에 그는 스트레스 받아 보인다",
        )

    def test_get_list_board_object(self):

        board_list = Board.objects.all()

        self.assertEqual(len(board_list), 4)
        self.assertEqual(board_list[3].title, "테스트에 관하여")
        self.assertEqual(board_list[2].name, "hodongGod")
        self.assertEqual(board_list[1].name, "넥터")
        self.assertEqual(board_list[0].description, "둥실때문에 그는 스트레스 받아 보인다")

    def test_get_retrieve_board_object(self):

        board_object1 = Board.objects.get(pk=1)
        board_object2 = Board.objects.get(pk=2)
        board_object3 = Board.objects.get(pk=3)
        board_object4 = Board.objects.get(pk=4)

        self.assertEqual(board_object1.title, "테스트에 관하여")
        self.assertEqual(board_object2.name, "hodongGod")
        self.assertEqual(board_object3.name, "넥터")
        self.assertEqual(board_object4.description, "둥실때문에 그는 스트레스 받아 보인다")

    def test_create_board_object(self):

        board_object = Board.objects.create(
            category_id = self._category1,
            email = "test@test.com",
            name = "테스트 유저",
            title = "테스트 케이스 생성 중",
            description = "테스트를 하고 있는데 과연 이걸 하는게 맞나 싶구만",
        )

        board_list = Board.objects.all()

        self.assertEqual(len(board_list), 5)
        self.assertEqual(board_object.title, "테스트 케이스 생성 중")
        self.assertEqual(board_list[0].description, board_object.description)

    def test_update_board_object(self):

        board_object = Board.objects.get(pk=2)
        board_object.description = "바뀐 내용입니다."
        board_object.updated = timezone.now()
        board_object.save()

        board_list = Board.objects.all()

        self.assertEqual(board_object.description, "바뀐 내용입니다.")
        self.assertEqual(board_list[2].description, board_object.description)

    def test_delete_board_object(self):

        board_object = Board.objects.get(pk=4)
        board_object.delete()

        board_list = Board.objects.all()
        
        self.assertEqual(len(board_list), 3)
        self.assertNotEqual(board_list[2].description, board_object.description)

class BoardHttpTestCase(TestCase):

    def setUp(self):

        self._category1 = Category.objects.create(
            title = "고민 상담"
        )
        self._category2 = Category.objects.create(
            title = "연애 고민"
        )
        Board.objects.create(
            category_id = self._category1,
            email = "arshavin3@naver.com",
            name = "hodong",
            title = "테스트에 관하여",
            description = "테스트란 어떤 걸까",
        )
        Board.objects.create(
            category_id = self._category1,
            email = "jhd9206@gmail.com",
            name = "hodongGod",
            title = "테스트는 해야 하는 것인가",
            description = "테스트는 해야 하는 것인가에 대하여 어렵구만",
        )
        Board.objects.create(
            category_id = self._category2,
            email = "쩌리짱@teamnexters.com",
            name = "넥터",
            title = "넥터에서 개발중",
            description = "후 넥터에서 개발하기란 참으로 어려운건지 쉬운건지",
        )
        Board.objects.create(
            category_id = self._category2,
            email = "hyeheon@nexters.com",
            name = "정해현",
            title = "CEO님짱",
            description = "둥실때문에 그는 스트레스 받아 보인다",
        )
        self._client = Client()

    def test_http_get_list_board(self):

        http_result = self._client.get("/api/board/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_get_retrieve_board(self):

        http_result1 = self._client.get("/api/board/1/")
        http_result2 = self._client.get("/api/board/2/")
        http_result3 = self._client.get("/api/board/3/")
        http_result4 = self._client.get("/api/board/4/")

        self.assertEqual(http_result1.status_code, 200)
        self.assertEqual(http_result2.status_code, 200)
        self.assertEqual(http_result3.status_code, 200)
        self.assertEqual(http_result4.status_code, 200)

    def test_http_get_list_board_by_user(self):

        http_result = self._client.get("/api/board/search/user/쩌리짱@teamnexters.com/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_get_list_board_by_category(self):

        http_result = self._client.get("/api/board/search/category/1/")
        self.assertEqual(http_result.status_code, 200)

    def test_http_post_create_board(self):

        http_result = self._client.post("/api/board/", {
            "category_id" : 1,
            "email" : "djangotest@test.com",
            "name" : "django.test",
            "title" : "unittest",
            "description" : "아 테스트 코드 짜는거 은근 개귀찮네",
        })
        self.assertEqual(http_result.status_code, 201)

    def test_http_put_update_board(self):

        http_result = self._client.put("/api/board/1/", dumps({
            "category_id" : 1,
            "email" : "djangotest2@test.com",
            "name" : "django.test2",
            "title" : "unittest2",
            "description" : "아 테스트 코드 짜는거 은근 개귀찮네2",
        }), content_type="application/json")
        self.assertEqual(http_result.status_code, 200)

    def test_http_delete_board(self):

        http_result = self._client.delete("/api/board/2/")
        self.assertEqual(http_result.status_code, 204)