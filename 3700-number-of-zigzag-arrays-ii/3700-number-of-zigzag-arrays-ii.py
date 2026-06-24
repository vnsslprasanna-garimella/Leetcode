class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        size = 2 * m

        # Transition matrix
        T = [[0] * size for _ in range(size)]

        # U'[y] = sum(D[x]) for x < y
        for y in range(m):
            for x in range(y):
                T[y][m + x] = 1

        # D'[y] = sum(U[x]) for x > y
        for y in range(m):
            for x in range(y + 1, m):
                T[m + y][x] = 1

        def mat_mul(A, B):
            nsz = len(A)
            C = [[0] * nsz for _ in range(nsz)]

            for i in range(nsz):
                for k in range(nsz):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]
                    for j in range(nsz):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            nsz = len(M)

            R = [[0] * nsz for _ in range(nsz)]
            for i in range(nsz):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        def mat_vec_mul(M, v):
            nsz = len(M)
            res = [0] * nsz

            for i in range(nsz):
                s = 0
                row = M[i]
                for j in range(nsz):
                    if row[j]:
                        s = (s + row[j] * v[j]) % MOD
                res[i] = s

            return res

        # Length = 2 states
        state = [0] * size

        # U2[v] = number of x < v
        for v in range(m):
            state[v] = v

        # D2[v] = number of x > v
        for v in range(m):
            state[m + v] = m - 1 - v

        if n == 2:
            return sum(state) % MOD

        P = mat_pow(T, n - 2)
        final_state = mat_vec_mul(P, state)

        return sum(final_state) % MOD