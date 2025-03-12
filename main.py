import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def time_function(func, *args, **kwargs):
    start_time = time.time()  
    result = func(*args, **kwargs)  
    end_time = time.time() 
    execution_time = end_time - start_time  
    print(f"Execution Time: {execution_time:.6f} seconds")
    return result 

def multiply(a, b):
    logging.info(f"Multiplication: {a} * {b}")
    
    try:
        result = a * b
    except NameError:
        logging.error("All the variables should be defined.")
    except IndexError:
        logging.error("Calculation problem")
    else:
        logging.debug(f"Result: {result}")
        return result  

logging.info("The program started")

time_function(multiply, 10, 5)
time_function(multiply, 4, 6)
time_function(multiply, 8, 7)

logging.warning("This is a warning")
logging.info("The program ended")