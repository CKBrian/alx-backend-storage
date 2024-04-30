# Redis Project Tasks and Usage

This document provides an overview of the tasks involved in the Redis project and how to use the implemented functionality.

## Tasks

### Task 1: Reading from Redis and recovering original type
**Objective:** Create a `get` method to retrieve data from Redis and convert it back to the original format.

- **Implementation:** Implement a `get` method in the `Cache` class that takes a key string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format. If the key does not exist, conserve the original Redis `get` behavior. Additionally, implement two new methods, `get_str` and `get_int`, that automatically parameterize `Cache.get` with the correct conversion function.
- **Usage:** Use the `get` method to retrieve data from Redis and specify a conversion function if necessary.

### Task 2: Incrementing values
**Objective:** Implement a system to count how many times methods of the `Cache` class are called.

- **Implementation:** Implement a `count_calls` decorator above the `Cache` class that takes a single method `Callable` argument and returns a `Callable`. Use the qualified name of the method as the key for counting calls. Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.
- **Usage:** Decorate `Cache.store` with `count_calls` to count the number of times it's called.

### Task 3: Storing lists
**Objective:** Define a `call_history` decorator to store the history of inputs and outputs for a particular function.

- **Implementation:** Implement a `call_history` decorator above the `Cache` class that stores the history of inputs and outputs for a particular function in Redis. Use the decorated function's qualified name to create input and output list keys. Use `rpush` to append the input arguments and store the output using `rpush` in the output list.
- **Usage:** Decorate `Cache.store` with `call_history` to store the history of its inputs and outputs.

### Task 4: Retrieving lists
**Objective:** Implement a replay function to display the history of calls of a particular function.

- **Implementation:** Implement a replay function to display the history of calls of a particular function using keys generated in previous tasks. Familiarize yourself with Redis commands like `RPUSH`, `LPUSH`, and `LRANGE`.
- **Usage:** Use the replay function to display the history of calls of a specific function.

## Usage

1. **Installation:**
   - Ensure you have Redis installed on your system (`sudo apt-get -y install redis-server`).
   - Install the `redis` Python package (`pip3 install redis`).

2. **Project Setup:**
   - Clone the project repository to your local machine.

3. **Task Implementation:**
   - Implement each task as described in the project specifications.
   - Follow the provided requirements and guidelines for coding style, documentation, and type annotations.

4. **Testing:**
   - Test each implemented task to ensure correctness and functionality.
   - Use sample data and scenarios to verify the behavior of each task.

5. **Documentation:**
   - Ensure that all modules, classes, functions, and methods are properly documented.
   - Write meaningful documentation explaining the purpose and usage of each component.

6. **Usage in Applications:**
   - Integrate the implemented functionality into your applications as needed.
   - Utilize Redis for caching, counting calls, storing lists, and retrieving history.

By following these steps, you can successfully complete the Redis project tasks and utilize the implemented functionality in your Python applications.

