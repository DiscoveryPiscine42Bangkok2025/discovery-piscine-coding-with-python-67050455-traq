def checkmate(board: str):
    rows = board.splitlines()
    size = len(rows)

    king_pos = None
    for r in range(size):
        for c in range(len(rows[r])):
            if rows[r][c] == 'K':
                king_pos = (r, c)
    if not king_pos:
        print("Error.")
        return
    
    kr, kc = king_pos

    for dr , dc in [(-1, -1), (-1, 1)]:
        r , c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < len(rows[r]):
            if rows[r][c] == 'R':
                print("Success")
                return
            
    def check_direction(dr, dc , threats):
        r, c = kr, kc
        while True:
            r += dr
            c += dc
            if r < 0 or c < 0 or r >= size or c >= len(rows[r]):
                return False
            piece = rows[r][c]
            if piece != ".":
                return piece in threats
            
    for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        if check_direction(dr, dc, ["B", "Q"]):
            print("Success")
            return

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        if check_direction(dr, dc, ["R", "Q"]):
            print("Success")
            return

    print("Fail")