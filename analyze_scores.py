import csv
from collections import defaultdict
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "students.csv"


def load_students():
    with DATA_FILE.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def main():
    students = load_students()
    scores = [int(student["score"]) for student in students]
    department_scores = defaultdict(list)

    for student in students:
        department_scores[student["department"]].append(int(student["score"]))

    print(f"학생 수: {len(students)}명")
    print(f"평균 점수: {sum(scores) / len(scores):.1f}점")
    print(f"최고 점수: {max(scores)}점")
    print(f"최저 점수: {min(scores)}점")
    print(f"80점 이상 학생 수: {sum(score >= 80 for score in scores)}명")
    print("학과별 평균:")

    for department in sorted(department_scores):
        department_average = sum(department_scores[department]) / len(
            department_scores[department]
        )
        print(f"- {department}: {department_average:.1f}점")


if __name__ == "__main__":
    main()
