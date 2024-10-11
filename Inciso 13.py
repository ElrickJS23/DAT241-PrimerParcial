from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

user_input = input("Enter a string: ")
words = user_input.split()
length = len(words)

if rank == 0:
    
    for i in range(length):
        if i % 2 == 0:  
            if size > 1:
                comm.Send([words[i], MPI.CHAR], dest=1, tag=1)
        else:  
            if size > 2:
                comm.Send([words[i], MPI.CHAR], dest=2, tag=2)

    print(words)

elif rank == 1:
    word = comm.recv(source=0)
    print(f"Processor {rank} received: {word}")
    print("1")

elif rank == 2:
    word = comm.recv(source=0)
    print(f"Processor {rank} received: {word}")
    print("2")


