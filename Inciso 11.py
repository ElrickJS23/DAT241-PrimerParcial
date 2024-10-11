from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

n = 10
if rank == 0:
    vec1 = np.random.randint(1, 10, size=n)
    vec2 = np.random.randint(1, 10, size=n)

vec3 = np.zeros(n, dtype=int)
vec4 = np.zeros(n, dtype=int)

# El procesador 0 envia los elementos segun posicion
if rank == 0:
    for i in range(n):
        if i % 2 == 0:
            if size > 1:
                comm.Send([vec1[i] + vec2[i], MPI.INT32_T], dest=1, tag=1)
            else:
                vec3[i] = vec1[i] + vec2[i]
        else:
            if size > 2:
                comm.Send([vec1[i] + vec2[i], MPI.INT32_T], dest=2, tag=2)
            else:
                vec4[i] = vec1[i] + vec2[i]

# Procesador 1 recibe los pares
elif rank == 1:
    for i in range(n // 2):
        result = np.zeros(1, dtype=int)
        comm.Recv([result, MPI.INT32_T], source=0, tag=1)
        vec3[2 * i] = result

# Procesador 2 recibe los impares
elif rank == 2:
    for i in range(n // 2):
        result = np.zeros(1, dtype=int)
        comm.Recv([result, MPI.INT32_T], source=0, tag=2)
        vec4[2 * i + 1] = result

if rank == 0:
    if size > 1:
        for i in range(n // 2):
            result = np.zeros(1, dtype=int)
            comm.Recv([result, MPI.INT32_T], source=1, tag=1)
            vec3[2 * i] = result
    if size > 2:
        for i in range(n // 2):
            result = np.zeros(1, dtype=int)
            comm.Recv([result, MPI.INT32_T], source=2, tag=2)
            vec4[2 * i + 1] = result

    print("Primer vector:", vec1)
    print("Segundo vector:", vec2)
    print("Suma de vectores pares:", vec3)
    print("Suma de vectores impares:", vec4)

MPI.Finalize()
