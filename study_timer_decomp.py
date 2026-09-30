import json
import math
from datetime import date
from pathlib import Path


LOG_FILE = Path(__file__).with_name("focus_log.json")


def load_sessions():
	try:
		log_contents = LOG_FILE.read_text(encoding="utf-8")
	except FileNotFoundError:
		return []

	if not log_contents.strip():
		return []

	return json.loads(log_contents)


def save_sessions(sessions):
	LOG_FILE.write_text(json.dumps(sessions, indent=2) + "\n", encoding="utf-8")


def record_session():
	name = input("Session name: ").strip()
	if not name:
		print("Session name cannot be empty.")
		return

	while True:
		try:
			minutes = float(input("Minutes studied: "))
		except ValueError:
			print("Enter a number greater than zero.")
			continue

		if not math.isfinite(minutes) or minutes <= 0:
			print("Enter a number greater than zero.")
			continue
		break

	sessions = load_sessions()
	sessions.append({
		"name": name,
		"minutes": minutes,
		"date": date.today().isoformat(),
	})
	save_sessions(sessions)
	print("Session saved.")


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
			record_session()
		elif choice == "2":
			today = date.today().isoformat()
			todays_sessions = [
				session for session in load_sessions()
				if session.get("date") == today
			]
			print_summary(todays_sessions)
		elif choice == "3":
			break
		else:
			print("Not a valid choice")


if __name__ == "__main__":
	main()
