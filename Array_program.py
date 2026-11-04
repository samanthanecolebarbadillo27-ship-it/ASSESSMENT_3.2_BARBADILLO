def main():
    word = input("Enter your last name: ").strip().upper() or "BARBADILLO"
    letters = [ch for ch in word if ch.isalpha()]

    array = []                      # Step 2: create an empty array
    print("\nAdding the letters:")
    for ch in letters:              # Step 3: append each letter
        array.append(ch)
    print("Index:", *range(len(array)), sep="  ")
    print("Value:", *array, sep="  ")

    print("\nRemoving the letters:")
    while len(array) != 0:          # Step 4 & 6: check if empty / repeat
        print("pop ->", array.pop())  # Step 5: remove last element and display
    print("Array is now empty")


if __name__ == "__main__":
    main()