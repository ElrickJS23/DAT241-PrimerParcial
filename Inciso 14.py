from mpi4py import MPI
import numpy as np

def multiplica_fila(fila, B):
    return np.dot(fila, B)

def main():
    comm = MPI.COMM_WORLD
    procesador = comm.Get_rank()
    cantidad = comm.Get_size()

    # Tamano matriz
    n = 4

    if procesador == 0:
        A = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]], dtype=int)

        B = np.array([[16, 15, 14, 13],
                      [12, 11, 10, 9],
                      [8, 7, 6, 5],
                      [4, 3, 2, 1]], dtype=int)

        C = np.zeros((n, n), dtype=int)

        for i in range(1, cantidad):
            comm.Send([B, MPI.INT], dest=i, tag=0)

        for i in range(1, cantidad):
            comm.Send([A[i], MPI.INT], dest=i, tag=1)

        C[0] = multiplica_fila(A[0], B)

        for i in range(1, cantidad):
            comm.Recv([C[i], MPI.INT], source=i, tag=2)

        print("Resultado de la multiplicación de matrices C:")
        print(C)

    else:
        B = np.zeros((n, n), dtype=int)
        comm.Recv([B, MPI.INT], source=0, tag=0)

        fila = np.zeros(n, dtype=int)
        comm.Recv([fila, MPI.INT], source=0, tag=1)

        resultado = multiplica_fila(fila, B)

        comm.Send([resultado, MPI.INT], dest=0, tag=2)

if __name__ == "__main__":
    main()
