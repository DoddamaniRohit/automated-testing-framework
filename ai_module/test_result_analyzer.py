import os
import xml.etree.ElementTree as ET
from collections import defaultdict

# AI-style failure pattern knowledge base
FAILURE_PATTERNS = {
    "Assertion failure": [
        "should have been",
        "but was",
        "assert",
        "comparison failed"
    ],
    "Element not found": [
        "element",
        "locator",
        "nosuchelement",
        "not found"
    ],
    "Timeout issue": [
        "timeout",
        "waiting",
        "timed out"
    ],
    "Browser issue": [
        "webdriver",
        "session",
        "browser"
    ],
    "Data issue": [
        "csv",
        "invalid",
        "valueerror"
    ],
    "Application issue": [
        "404",
        "500",
        "not reachable"
    ]
}


def classify_failure(message):
    message = message.lower()
    for category, keywords in FAILURE_PATTERNS.items():
        for keyword in keywords:
            if keyword in message:
                return category
    return "Unknown issue"

def identify_application(test_name):
    """
    AI logic to identify which application failed
    """
    test_name = test_name.lower()

    if "grocery" in test_name or "cart" in test_name or "login" in test_name:
        return "Grocery Application"

    return "Student Management Application"

def find_output_xml():
    """
    Intelligently locate Robot Framework output.xml
    """
    possible_paths = [
        "results/output.xml",   # CI path
        "output.xml"            # Local path
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        "Robot Framework output.xml not found. Please run tests first."
    )

def analyze_robot_results(xml_path=None):
    if not xml_path:
        xml_path = find_output_xml()

    tree = ET.parse(xml_path)
    root = tree.getroot()   # ✅ THIS LINE WAS MISSING

    analysis = defaultdict(lambda: defaultdict(int))

    for test in root.iter("test"):
        test_name = test.attrib.get("name", "")
        status = test.find("status")

        if status is not None and status.attrib.get("status") == "FAIL":
            failure_message = status.text or ""
            app = identify_application(test_name)
            issue = classify_failure(failure_message)
            analysis[app][issue] += 1

    print("\n🤖 AI-BASED TEST FAILURE ANALYSIS")
    print("=" * 40)

    if not analysis:
        print("✅ All tests passed. No failures detected.")
        return

    for app, issues in analysis.items():
        print(f"\n📌 Application: {app}")
        for issue, count in issues.items():
            print(f"❌ {count} failure(s) due to: {issue}")

    print("\n🧠 AI Recommendations:")
    for app, issues in analysis.items():
        if "Assertion failure" in issues:
            print(f"- Review expected vs actual behavior in {app}")
        if "Element not found" in issues:
            print(f"- Review UI locators in {app}")
        if "Timeout issue" in issues:
            print(f"- Improve waits or performance checks in {app}")
        if "Browser issue" in issues:
            print(f"- Verify browser stability in {app}")
        if "Data issue" in issues:
            print(f"- Validate test data used in {app}")
        if "Application issue" in issues:
            print(f"- Check server availability for {app}")

    print("\n📊 AI-assisted analysis reduces manual debugging effort.")


    analysis = defaultdict(lambda: defaultdict(int))

    for test in root.iter("test"):
        test_name = test.attrib.get("name", "")
        status = test.find("status")

        if status is not None and status.attrib.get("status") == "FAIL":
            failure_message = status.text or ""
            app = identify_application(test_name)
            issue = classify_failure(failure_message)
            analysis[app][issue] += 1

    print("\n🤖 AI-BASED TEST FAILURE ANALYSIS")
    print("=" * 40)

    if not analysis:
        print("✅ All tests passed. No failures detected.")
        return

    for app, issues in analysis.items():
        print(f"\n📌 Application: {app}")
        for issue, count in issues.items():
            print(f"❌ {count} failure(s) due to: {issue}")

    print("\n🧠 AI Recommendations:")
    for app, issues in analysis.items():
        if "Element not found" in issues:
            print(f"- Review UI locators in {app}")
        if "Timeout issue" in issues:
            print(f"- Improve waits or performance checks in {app}")
        if "Browser issue" in issues:
            print(f"- Verify browser stability in {app}")
        if "Data issue" in issues:
            print(f"- Validate test data used in {app}")
        if "Application issue" in issues:
            print(f"- Check server availability for {app}")

    print("\n📊 AI-assisted analysis reduces manual debugging effort.")

if __name__ == "__main__":
    analyze_robot_results()
