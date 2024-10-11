import multiprocessing as mp 
 
def leibniz(start, end): 
    partial_sum = 0.0 
    for k in range(start, end): 
        partial_sum += ((-1)**k) / (2*k + 1) 
    return partial_sum 
 
if name == "__main__": 
    n_terms = 1000000  
    n_processes = mp.cpu_count()   
    chunk_size = n_terms // n_processes 
 
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(n_processes)] 
     
    with mp.Pool(processes=n_processes) as pool: 
        results = pool.starmap(leibniz, ranges) 
     
    pi_approx = 4 * sum(results) 
     
    print(f"Valor de PI con {n_terms} términos: {pi_approx}")
print(f"Se usaron: {n_processes} procesadores")
