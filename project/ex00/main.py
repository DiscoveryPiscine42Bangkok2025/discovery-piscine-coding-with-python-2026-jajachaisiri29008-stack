from checkmate import is_in_check

board = [
    list("....Q..."),
    list("........"),
    list("........"),
    list("....K..."),
    list("........"),
    list("........"),
    list("........"),
    list("........")
]

if is_in_check(board):
    print("Success")
else:
    print("Fail")
