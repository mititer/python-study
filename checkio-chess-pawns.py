pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
pawns = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
pawns = {"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}

def check_pawns(pawns):
    pawn_list = []
    unsafe_pawns = []
    safe_pawns = []
    # decode to position
    for pawn in pawns:
        print("handling "+str(pawn))
        file, rank = pawn[0], int(pawn[1])
        pawn_list.append((rank, file))
    print(pawn_list)

    for pawn in pawn_list:
        ok_flag = False
        rank, file = pawn[0], pawn[1]
        print("checking "+file+str(rank))

        if rank == 1:
            unsafe_pawns.append(pawn)
            continue

        chk_rank = rank - 1
        chk_file1 = chr(ord(file)+1)
        if(chk_file1 > 'h'):
            chk_file1 = False
        chk_file2 = chr(ord(file)-1)
        if(chk_file2 < 'a'):
            chk_file2 = False

        print("file="+file+", chk_file1="+str(chk_file1)+", chk_file2="+str(chk_file2))

        for one_pawn in pawn_list:
            if chk_file1:
                print("checking 1: "+chk_file1+str(chk_rank)+" with "+str(one_pawn))
                if (chk_rank, chk_file1) == one_pawn:
                    print("found: pawn="+str(pawn)+" protected by "+str((chk_file1, chk_rank)))
                    safe_pawns.append(pawn)
                    ok_flag = True
                    break
            if chk_file2:
                print("checking 2: "+chk_file2+str(chk_rank)+str(one_pawn))
                if (chk_rank, chk_file2) == one_pawn:
                    print("found: pawn="+str(pawn)+" protected by "+str((chk_file2, chk_rank)))
                    safe_pawns.append(pawn)
                    ok_flag = True
                    break
        if not ok_flag:
            unsafe_pawns.append(pawn)

    print("unsafe: "+str(unsafe_pawns))
    print("safe: "+str(safe_pawns))
    return len(safe_pawns)

print(check_pawns(pawns))