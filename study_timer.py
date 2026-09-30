import json
import math
import time
from datetime import date
from pathlib import Path


BREAK_SECONDS = 5 * 60
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


def get_study_duration_seconds():
	while True:
		try:
			study_seconds = float(input("Study time in seconds: "))
		except ValueError:
			print("Enter a number greater than zero.")
			continue

		if not math.isfinite(study_seconds) or study_seconds <= 0:
			print("Enter a number greater than zero.")
			continue

		return math.ceil(study_seconds)


def countdown(duration_seconds):
	end_time = time.monotonic() + duration_seconds

	while True:
		seconds_remaining = max(0, math.ceil(end_time - time.monotonic()))
		minutes, seconds = divmod(seconds_remaining, 60)
		print(f"\rTime remaining: {minutes:02d}:{seconds:02d}", end="", flush=True)

		if seconds_remaining == 0:
			break

		time.sleep(max(0, min(1, end_time - time.monotonic())))

	print()


def start_focus_session():
	name = input("Session name: ").strip()
	if not name:
		print("Session name cannot be empty.")
		return

	study_seconds = get_study_duration_seconds()
	study_minutes = round(study_seconds / 60, 1)
	input("Press Enter to start the study timer...")
	session_date = date.today().isoformat()

	countdown(study_seconds)

	sessions = load_sessions()
	sessions.append({
		"name": name,
		"minutes": study_minutes,
		"date": session_date,
	})
	save_sessions(sessions)
	print("Session saved.")

	print("Break time!")
	countdown(BREAK_SECONDS)
	print("Break complete!")


def print_summary(sessions):
	if not sessions:
		print("No focus sessions logged today")
		return

	totals = {}
	for session in sessions:
		name = session["name"]
		totals[name] = totals.get(name, 0) + session["minutes"]

	for name, minutes in totals.items():
		print(f"{name}: {minutes:.1f} min")

	print(f"Total: {sum(totals.values()):.1f} min")


def main():
	while True:
		print("\n1. Start a focus session")
		print("2. Show today's summary")
		print("3. Quit")

		choice = input("Choose an option: ").strip()
		if choice == "1":
			start_focus_session()
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
