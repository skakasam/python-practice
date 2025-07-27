"""Hello Python"""

from common.project import Project, Subject


if __name__ == "__main__":
    print(
        Project(
            "Taking Python to Production",
            Subject("Setup development environment with VSCode"),
            Subject("Learn Python programming, and build real world projects"),
            Subject("Improve code quality using docstrings, testing, & type hinting"),
            Subject("Version, package, and publish Python applications"),
            Subject("Learn git workflow with GitHub and CI/CD with GitHub Actions"),
        )
    )
