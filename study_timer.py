import math
import time


BREAK_SECONDS = 5 * 60


def get_study_duration_seconds():
	while True:
		try:
			study_minutes = float(input("Study time in minutes: "))
		except ValueError:
			print("Enter a number greater than zero.")
			continue

		if not math.isfinite(study_minutes) or study_minutes <= 0:
			print("Enter a number greater than zero.")
			continue

		return math.ceil(study_minutes * 60)


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


def main():
	study_seconds = get_study_duration_seconds()
	input("Press Enter to start the study timer...")

	countdown(study_seconds)
	print("Break time!")
	countdown(BREAK_SECONDS)
	print("Break complete!")


if __name__ == "__main__":
	main()
