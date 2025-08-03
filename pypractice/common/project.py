"""Subject Module"""


class Subject:
    """Subject Class"""

    def __init__(self, name: str, *topics: str):
        self._name: str = name
        self._topics: list[str] = []
        self.add_topics(*topics)

    @property
    def name(self) -> str:
        return self._name

    @property
    def topics(self) -> tuple[str, ...]:
        return tuple(self._topics)

    def add_topics(self, *topics_to_add: str) -> None:
        for topic in topics_to_add:
            if topic not in self._topics:
                self._topics.append(topic)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Subject):
            return False
        return self.name == other.name

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        topics_str = ""
        if self._topics:
            topics_str = "\n".join(
                [
                    f"    Topic {idx + 1}. {topic}"
                    for idx, topic in enumerate(self._topics)
                ]
            )

        subject_str = f"{self._name}\n{topics_str}" if topics_str else self._name
        return subject_str


class Project:
    """Project Class"""

    def __init__(self, name: str, *subjects: Subject):
        self._name: str = name
        self._subjects: list[Subject] = []
        self.add_subjects(*subjects)

    @property
    def name(self) -> str:
        return self._name

    @property
    def subjects(self) -> tuple[Subject, ...]:
        return tuple(self._subjects)

    def add_subjects(self, *subjects_to_add: Subject) -> None:
        for subject in subjects_to_add:
            if subject not in self._subjects:
                self._subjects.append(subject)

    def __str__(self) -> str:
        subjects_str = ""
        if self._subjects:
            subjects_str = "\n".join(
                [
                    f"  Subject {idx + 1}. {subject}"
                    for idx, subject in enumerate(self._subjects)
                ]
            )

        project_str = f"{self._name}\n{subjects_str}" if subjects_str else self._name
        return project_str


def create_project(project_details_ref: str) -> Project:
    with open(file=project_details_ref, mode="r", encoding="UTF-8") as in_stream:
        project_name = None
        project_subj = []

        for line in in_stream.readlines():
            cleansed_line = line.rstrip()
            if cleansed_line.startswith("PROJECT:"):
                project_name = line.rstrip().split(":")[1]
            elif cleansed_line.startswith("SUBJECT:"):
                project_subj.append(line.rstrip().split(":")[1])

    if project_name and project_subj:
        project = Project(project_name)
        project.add_subjects(*project_subj)
    else:
        raise ValueError("Unable to create a Project based on the reference file!")

    return project
