pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

def check_pawns(pawns):
    n = 0
    pos = []
    unsafe_pawns = []

    # decode to position
    lowerest_rank = 0
    for pawn in pawns:
        file = pawn[0]
        rank = int(pawn[1])
        if rank < lowerest_rank:
            lowerest_rank = rank
        pos.append((rank, file))
    pos = sorted(pos, key=lambda x: (x[0]))
    lowerest_rank = pos[0][0]
    print("lowest rank="+str(lowerest_rank))

    # the lowest ranks is unsafe
    for pawn in pos:
        if lowerest_rank == pawn[0]:
            unsafe_pawns.append(pawn)

    # check from top to lower rank
    safe_pawns = []
    pos = sorted(pos, key=lambda x: (x[0]), reverse=True)
    print("reversed: "+str(pos))
    for pawn in pos:
        rank = pawn[0]
        file = pawn[1]
        if rank == 1 and rank != lowerest_rank:
            unsafe_pawns.append(pawn)
            break
        chk_rank = rank - 1
        chk_file1 = False if file == 'a' else chr(ord(file) + 1)
        chk_file2 = chr(ord(file) - 1) if file == 'h' else False
        for item in pawns:
            if chk_file1:
                if (chk_rank, chk_file1) == item:
                    safe_pawns.append(pawn)
                    break
            if chk_file2:
                if (chk_rank, chk_file2) == item:
                    safe_pawns.append(pawn)
                    break
        unsafe_pawns.append(pawn)

    print("unsafe: "+str(unsafe_pawns))
    print("safe: "+str(safe_pawns))
    return len(safe_pawns)

print(check_pawns(pawns))