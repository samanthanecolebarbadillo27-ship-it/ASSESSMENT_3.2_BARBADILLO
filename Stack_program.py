def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    stack = []                      # Step 2: create empty stack

    print("\nAdding the letters (top is the last letter added):")
    for ch in word:
        if ch.isalpha():
            stack.append(ch)        # Step 3: append
            print(f"Append ({ch}) -> {' '.join(stack)}")

    print("\nRemoving the letters:")
    while len(stack) != 0:          # Step 4 & 6: check if empty / repeat
        print("pop ->", stack.pop())  # Step 5: pop top and display
    print("Stack is now empty")


if __name__ == "__main__":
    main()
