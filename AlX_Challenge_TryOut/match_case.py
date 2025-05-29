"""
Great question!

### `case _ if condition:` explained

In Python’s **`match-case`** (introduced in Python 3.10), the syntax:

```python
case _ if condition:
```

means:

* **`_`** is a **wildcard pattern** — it matches **anything**.
* The **`if condition`** is a **guard clause** — it lets you filter the match based on a condition.

---

### Think of it like this:

When you write:

```python
match guess:
    case _ if guess == secret_number:
        print("You got it!")
```

It means:

> “For **any value** of `guess`, if `guess == secret_number`, then run this block.”

---

### Why use `_`?

Because `match-case` is primarily used for **pattern matching** (like matching exact values or structure). If you don’t care about the actual pattern but want to test a condition, you use `_` as a **placeholder**.

---

### Summary:

| Syntax            | Meaning                                        |
| ----------------- | ---------------------------------------------- |
| `case 5:`         | Match if the value is exactly `5`              |
| `case _:`         | Match anything (default case)                  |
| `case _ if cond:` | Match anything **only if** condition is `True` |

---

Let me know if you'd like examples with other data types (like dictionaries or lists)!

"""


from random import randint

def play_game():
    secret_number = randint(1, 10)
    guess_count = 0

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input())
            guess_count += 1

            match guess:
                case _ if guess == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {guess_count} tries!")
                    break
                case _ if guess > secret_number:
                    print("Nope, your guess is a bit high. Give it another shot!")
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("Please enter a valid number.")

# Game loop
while True:
    play_game()
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
