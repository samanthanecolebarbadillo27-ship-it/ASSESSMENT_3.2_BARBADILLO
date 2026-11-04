
from collections import deque
queue = deque()

def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    queue = deque()                 # Step 2: create empty queue

    print("\nAdding the letters (front is the first letter added):")
    for ch in word:
        if ch.isalpha():
            queue.append(ch)        # Step 3: append
            print(f"append({ch}) -> {' '.join(queue)}")

    print("\nRemoving the letters:")
    while len(queue) != 0:          # Step 4 & 6
        print("popleft ->", queue.popleft())  # Step 5: remove front, display
    print("Queue is now empty")


if __name__ == "__main__":
    main()