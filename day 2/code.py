#!/usr/bin/env python3
"""
Small interactive script for greeting the user and showing coffee recommendations.

Usage: Run the script and follow prompts.
"""

def main():
	try:
		name = input("Enter your name: ").strip()
	except EOFError:
		# If run non-interactively, fallback
		name = "Guest"

	if not name:
		name = "Guest"

	print(f"\nHello, {name}! Welcome to Brew Haven.\n")

	recommendations = [
		"Espresso",
		"Cappuccino",
		"Latte",
		"Americano",
		"Mocha",
		"Macchiato",
	]

	print("Today's recommendations:")
	for i, item in enumerate(recommendations, start=1):
		print(f"{i}. {item}")

	try:
		choice = input("\nPick a number to see a fun fact about that drink (or press Enter to exit): ").strip()
	except EOFError:
		choice = ""

	if choice.isdigit():
		idx = int(choice)
		if 1 <= idx <= len(recommendations):
			facts = {
				1: "Espresso is the base for many coffee drinks and is made by forcing hot water through finely-ground coffee.",
				2: "Cappuccino traditionally has equal parts espresso, steamed milk, and milk foam.",
				3: "Latte contains more steamed milk than a cappuccino, giving it a creamier texture.",
				4: "Americano is made by diluting espresso with hot water, creating a similar strength to drip coffee.",
				5: "Mocha is a chocolate-flavored variant of a latte, often topped with whipped cream.",
				6: "Macchiato means 'stained' in Italian — a shot of espresso 'stained' with a small amount of milk or foam.",
			}
			print(f"\n{recommendations[idx-1]}: {facts[idx]}\n")
		else:
			print("Number out of range. Goodbye.\n")
	else:
		print("Goodbye.\n")


if __name__ == "__main__":
	main()

