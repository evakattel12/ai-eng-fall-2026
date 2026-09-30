def print_summary(sessions):
	if not sessions:
		print("No focus sessions logged today")
		return

	totals = {}
	for session in sessions:
		name = session["name"]
		totals[name] = totals.get(name, 0) + session["minutes"]

	for name, minutes in totals.items():
		print(f"{name}: {minutes} min")

	print(f"Total: {sum(totals.values())} min")


def main():
	while True:
		print("1. Start a focus session")
		print("2. Show today's summary")
		print("3. Quit")

		choice = input("Choose an option: ")
		if choice == "1":
			print("Focus session placeholder.")
		elif choice == "2":
			print("Today's summary placeholder.")
		elif choice == "3":
			break
		else:
			print("Not a valid choice")


if __name__ == "__main__":
	main()
