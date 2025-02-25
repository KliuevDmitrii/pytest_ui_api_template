from api.BoardApi import BoardApi

def test_get_boards():
    api = BoardApi()
    board_list = api.get_all_boards_by_org_id("63ff33f90a2c921d9db739f2")
    print(board_list)

    assert len(board_list) == 0

def test_create_board():
    api = BoardApi()
    org_id = "63ff33f90a2c921d9db739f2"
    board_list_before = api.get_all_boards_by_org_id(org_id)
    resp = api.create_board(org_id, "Test board")
    board_list_after = api.get_all_boards_by_org_id(org_id)

    assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board():
    api = BoardApi()
    org_id = "63ff33f90a2c921d9db739f2"
    board_list_before = api.get_all_boards_by_org_id(org_id)
    board_id = board_list_before[0]["id"]

    resp = api.delete_board_by_id(board_id)
    print(resp)

    board_list_after = api.get_all_boards_by_org_id(org_id)

    assert len(board_list_before) - len(board_list_after) == 1