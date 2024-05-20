import os
import time
import psutil

class UniqueInt:
    def __init__(self):
        self.unique_integers = set()

    def read_next_item_from_file(self, line):
        try:
            number = int(line.strip())
            return number
        except ValueError:
            return None

    def process_file(self, input_file_path, output_file_path):
        start_time = time.time()
        process = psutil.Process(os.getpid())

        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if not line or len(line.split()) != 1:
                    continue

                number = self.read_next_item_from_file(line)
                if number is not None and -1023 <= number <= 1023:
                    self.unique_integers.add(number)

        sorted_unique_integers = self.custom_sort(list(self.unique_integers))

        with open(output_file_path, 'w') as output_file:
            for number in sorted_unique_integers:
                output_file.write(f"{number}\n")

        end_time = time.time()
        memory_usage = process.memory_info().rss

        print(f"Memory Usage: {memory_usage} bytes")
        print(f"Runtime: {end_time - start_time} seconds")

    def custom_sort(self, numbers):
        # Implementing a simple bubble sort for demonstration
        n = len(numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers


if __name__ == "__main__":
    
    base_dir = 'C:\\Users\\HP\\Desktop\\UniqueInt\\dsa\\hw01'
    sample_inputs_dir = os.path.join(base_dir, 'sample_inputs')
    sample_results_dir = os.path.join(base_dir, 'sample_results')

    unique_int_processor = UniqueInt()

    for input_filename in os.listdir(sample_inputs_dir):
        if input_filename.endswith('.txt'):
            input_filepath = os.path.join(sample_inputs_dir, input_filename)
            output_filepath = os.path.join(sample_results_dir, f"{input_filename}_results.txt")
            unique_int_processor.process_file(input_filepath, output_filepath)