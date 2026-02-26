rom datetime import datetime, timedelta

class Assignment:
    def __init__(self, title, due_date, estimated_hours):
        self.title = title
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.estimated_hours = estimated_hours


class StudySession:
    def __init__(self, date, duration):
        self.date = date
        self.duration = duration
        self.status = "Planned"

    def mark_complete(self):
        self.status = "Completed"


class StudyScheduler:
    def generate_schedule(self, assignment):
        today = datetime.today()
        days_available = (assignment.due_date - today).days

        if days_available <= 0:
            print("Due date has passed or is today.")
            return []

        hours_per_day = assignment.estimated_hours / days_available
        schedule = []

        for i in range(days_available):
            session_date = today + timedelta(days=i+1)
            schedule.append(StudySession(session_date.date(), round(hours_per_day, 2)))

        return schedule


if __name__ == "__main__":
    title = input("Enter assignment title: ")
    due = input("Enter due date (YYYY-MM-DD): ")
    hours = float(input("Enter estimated study hours: "))

    assignment = Assignment(title, due, hours)
    scheduler = StudyScheduler()
    sessions = scheduler.generate_schedule(assignment)

    print("\nGenerated Study Schedule:")
    for session in sessions:
        print(f"Date: {session.date} | Hours: {session.duration} | Status: {session.status}")
