import xml.etree.ElementTree as ET
from collections import Counter

# Simple AI-based classification rules
FAILURE_PATTERNS = {
    "Element not found": ["ElementNotFound", "NoSuchElement", "locator"],
    "Timeout issue": ["Timeout", "waiting", "timed out"],
    "Browser issue": ["SessionNotCreated", "WebDriverException"],
    "Data issue": ["CSV", "invalid", "ValueError"],
    "Application issue": ["500", "404", "not reachable"]
}

def classify_failure(message):
    for category, keywords in FAILURE_PATTERNS.items():
        for keyword in keywords:
            if keyword.lower() in message.lower():
                return category
    return "Unknown issue"

def analyze_robot_results(xml_path="results/output.xml"):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    failures = []

    for test in root.iter("test"):
        status = test.find("status")
        if status is not None and status.attrib.get("status") == "FAIL":
            failure_message = status.text or ""
            failures.append(classify_failure(failure_message))

    summary = Counter(failures)

    print("\n🤖 AI-BASED TEST FAILURE ANALYSIS")
    print("=" * 40)

    if not summary:
        print("✅ All tests passed. No failures detected.")
        return

    for issue, count in summary.items():
        print(f"❌ {count} failure(s) due to: {issue}")

    print("\n🧠 AI Recommendation:")
    if "Element not found" in summary:
        print("- Review UI locators. Possible UI changes detected.")
    if "Timeout issue" in summary:
        print("- Increase wait times or check application performance.")
    if "Browser issue" in summary:
        print("- Verify browser/driver compatibility.")
    if "Data issue" in summary:
        print("- Validate test data inputs.")
    if "Application issue" in summary:
        print("- Check application server health.")

    print("\n📌 This analysis helps testers focus on root causes instead of reading raw logs.")

if __name__ == "__main__":
    analyze_robot_results()
