import time

def algorithm(problem_size):
    # Start the algorithm
    work = 1
    for x in range(problem_size):
        work += 5
        work -= 5
    # End of algorithm

def time_algorithm(problem_size):
    start_time = time.perf_counter()
    algorithm(problem_size)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    while True:
        print(f"\n{'Problem Size':<15}\t{'Seconds':<10}")
        print("-" * 15 + "\t" + "-" * 10)

        # Initial problem size
        size = 1_000_000

        # Run 4 iterations
        for _ in range(4):
            # Time the algorithm multiple times and take average
            total_time = 0
            runs = 3
            for _ in range(runs):
                total_time += time_algorithm(size)
            avg_time = total_time / runs

            # Print results with proper alignment
            print(f"{size:,}\t\t{avg_time:.4f}")

            # Triple the size for next iteration
            size *= 3

        # Ask user if they want to run the program again or exit
        user_input = input("\nPress 'x' to exit or any other key to run again: ").strip().lower()
        if user_input == 'x':
            break

if __name__ == "__main__":
    main()