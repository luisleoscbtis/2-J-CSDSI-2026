def plants_and_zombies(lawn, zombies):
    shooters = {}
    for r, row in enumerate(lawn):
        for c, ch in enumerate(row):
            if ch == 'S':
                shooters[(r, c)] = 'S'
            elif '0' <= ch <= '9':
                shooters[(r, c)] = int(ch)

    active = []
    zombie_queue = sorted(zombies, key=lambda z: z[0])
    total_zombies = len(zombie_queue)
    move = 0

    while move <= 10000:
        # Phase 1a: mover zombis existentes a la izquierda
        for z in active:
            z[2] -= 1

        # Phase 1b: spawnear zombis de este turno (no se mueven en su turno de spawn)
        for z in zombie_queue:
            zi, zrow, zhp = z
            if zi == move:
                active.append([zhp, zrow, len(lawn[zrow]) - 1])

        # Phase 1c: zombis que caen sobre un tirador lo destruyen
        to_del = [k for k in shooters
                  if any(z[1] == k[0] and z[2] == k[1] for z in active)]
        for k in to_del:
            del shooters[k]

        # Phase 1d: brecha — zombi llegó a col <= 0
        for zh, zr, zc in active:
            if zc <= 0:
                return move + 1

        # Phase 2: disparos
        def first_right(r, c):
            best = None
            for z in active:
                if z[1] == r and z[2] > c:
                    if best is None or z[2] < best[2]: best = z
            return best

        def first_diag_up(r, c):
            best = None
            for z in active:
                dc = z[2]-c; dr = r-z[1]
                if dc > 0 and dr > 0 and dc == dr:
                    if best is None or dc < (best[2]-c): best = z
            return best

        def first_diag_down(r, c):
            best = None
            for z in active:
                dc = z[2]-c; dr = z[1]-r
                if dc > 0 and dr > 0 and dc == dr:
                    if best is None or dc < (best[2]-c): best = z
            return best

        def damage(z):
            if z not in active: return
            z[0] -= 1
            if z[0] <= 0: active.remove(z)

        for (sr, sc), val in list(shooters.items()):
            if val == 'S': continue
            for _ in range(val):
                t = first_right(sr, sc)
                if t is None or t not in active: break
                damage(t)

        s_shooters = sorted([(r,c) for (r,c),v in shooters.items() if v=='S'],
                            key=lambda x: (-x[1], x[0]))
        for sr, sc in s_shooters:
            for fn in [first_right, first_diag_up, first_diag_down]:
                t = fn(sr, sc)
                if t is not None and t in active and t[0] > 0:
                    damage(t)

        if not active and all(z[0] <= move for z in zombie_queue):
            return None

        move += 1
    return None