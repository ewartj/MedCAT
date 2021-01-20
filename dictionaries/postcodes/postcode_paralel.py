import multiprocessing
import os
all_processes = ("postcode1.py","postcode2.py","postcode3.py","postcode4.py","postcode5.py")

def execute(process):
    os.system(f"python {process}")

process_pool = multiprocessing.Pool(processes = 5)                                                        
process_pool.map(execute, all_processes)