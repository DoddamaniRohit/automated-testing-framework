import xml.etree.ElementTree as ET
from collections import defaultdict
import os


FAILURE_PATTERNS = {
    "Assertion failure": {
        "patterns": [
            "should have been", "but was", "should be", "expected", "actual",
            "assert", "assertionerror", "comparison failed",
            "does not match", "not equal", "!=", "mismatch"
        ],
        "description": "The expected result defined in the test did not match the actual application behavior.",
        "ai_explanation": "This usually happens when application logic changes but test expectations are not updated.",
        "recommendation": [
            "Re-check expected vs actual values",
            "Confirm UI text or API response",
            "Update assertions if application behavior is correct"
        ]
    },

    "Element not found": {
        "patterns": [
            "no such element", "unable to locate", "element not found",
            "element not visible", "element not interactable",
            "stale element", "invalid selector"
        ],
        "description": "The required UI element could not be located or interacted with.",
        "ai_explanation": "This typically occurs due to UI changes, incorrect locators, or timing issues.",
        "recommendation": [
            "Verify XPath / CSS selector",
            "Add explicit waits",
            "Check if element is inside iframe or dynamic UI"
        ]
    },

    "Timeout issue": {
        "patterns": [
            "timeout", "timed out", "waited", "page load timeout"
        ],
        "description": "The application took longer than expected to respond.",
        "ai_explanation": "Slow network, backend delay, or missing synchronization can cause this.",
        "recommendation": [
            "Increase explicit wait duration",
            "Avoid hard-coded sleeps",
            "Optimize page load performance"
        ]
    },

    "Browser / Driver crash": {
        "patterns": [
            "session not created", "chrome instance exited",
            "webdriverexception", "process unexpectedly closed"
        ],
        "description": "Browser or WebDriver crashed during execution.",
        "ai_explanation": "Common in CI pipelines due to missing display or driver mismatch.",
        "recommendation": [
            "Run browser in headless mode",
            "Use Xvfb in CI",
            "Ensure Chrome & Driver versions match"
        ]
    },

    "Data issue": {
        "patterns": [
            "csv", "null", "none", "missing value",
            "valueerror", "typeerror", "keyerror"
        ],
        "description": "Invalid or missing test data caused the failure.",
        "ai_explanation": "Incorrect input data leads to unpredictable application behavior.",
        "recommendation": [
            "Validate CSV / test data before execution",
            "Add boundary checks",
            "Handle null or empty values gracefully"
        ]
    }
}


def classify_failure(message: str):
    message = message.lower()
    for category, data in FAILURE_PATTERNS.items():
        for pattern in data["patterns"]:
            if pattern in message:
                return category, pattern
    return "Unknown issue", None


def identify_application(test_name: str):
    name = test_name.lower()
    if "grocery" in name or "cart" in name or "login" in name:
        return "Grocery Application"
    return "Student Management Application"


def find_output_xml():
    paths = ["results/output.xml", "output.xml"]
    for p in paths:
        if os.path.exists(p):
            return p
    raise FileNotFoundError("output.xml not found. Run Robot tests first.")


def analyze_robot_results():
    xml_path = find_output_xml()
    tree = ET.parse(xml_path)
    root = tree.getroot()

    failures = defaultdict(list)

    for test in root.iter("test"):
        status = test.find("status")
        if status is not None and status.attrib.get("status") == "FAIL":
            test_name = test.attrib.get("name", "Unknown Test")
            message = status.text or ""

            app = identify_application(test_name)
            category, matched_pattern = classify_failure(message)

            failures[app].append((test_name, category, matched_pattern, message))

    print("\n AI-BASED TEST FAILURE ANALYSIS")
    print("=" * 60)

    if not failures:
        print(" All tests passed. No failures detected.")
        return

    for app, items in failures.items():
        print(f"\n Application: {app}")
        print("-" * 60)

        for test_name, category, pattern, message in items:
            print(f"\n Test Case: {test_name}")
            print(f" Failure Category: {category}")

            if pattern:
                print(f" Detected Pattern: '{pattern}'")

            if category in FAILURE_PATTERNS:
                info = FAILURE_PATTERNS[category]
                print(f" Meaning: {info['description']}")
                print(f" AI Insight: {info['ai_explanation']}")
                print(" Recommended Fixes:")
                for rec in info["recommendation"]:
                    print(f"   - {rec}")
            else:
                print(" Meaning: Unclassified failure")
                print(" Recommendation: Review logs manually")

    print("\n AI-assisted analysis reduces manual debugging effort.")
    print("=" * 60)


if __name__ == "__main__":
    analyze_robot_results()
