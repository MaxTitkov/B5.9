import time

class TimeThis:
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		pass

	def __call__(self, num_runs=10):
		def decorator(function):
			def time_scaler(param):
				avg_time=0
				for _ in range(num_runs):
					t0 = time.time()
					result = function(param)
					t1 = time.time()
					avg_time += (t1 - t0)
				avg_time /= num_runs
				print(f"Количество запусков: {num_runs}\nСреднее время выполнения: {avg_time}")				
			return time_scaler
		return decorator


with TimeThis() as timeit:
	@timeit(num_runs=20)
	def fib(n):
		fib =[0]
		for i in range(1, n+1):
			if i < 3:
				fib.append(i)
			else:
				fib.append(fib[i-1]+fib[i-2])
		return fib[n]
fib(100)
