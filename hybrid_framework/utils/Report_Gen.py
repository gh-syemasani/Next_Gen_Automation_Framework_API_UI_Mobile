from datetime import datetime
import os



def generate_report(start_time, end_time, test_name="Test Execution", context="General"):
    """Generates a simple execution report in reports/ directory."""
    duration = end_time - start_time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("reports", exist_ok=True)
    report_file = os.path.join("reports", f"report_{timestamp}.txt")

    with open(report_file, "w") as f:
        f.write(f"Execution Report - {test_name}\n")
        f.write(f"Context: {context}\n")
        f.write(f"Start Time: {start_time}\n")
        f.write(f"End Time: {end_time}\n")
        f.write(f"Duration: {duration}\n")

    print(f"Report generated: {report_file}")


start_time_feature = {}
start_time_scenario = {}

def before_feature(context, feature):
    start_time_feature[feature.name] = datetime.now()
    print(f"\n[BEFORE FEATURE] {feature.name}")

def after_feature(context, feature):
    end_time = datetime.now()
    print(f"[AFTER FEATURE] {feature.name}")
    generate_report(start_time_feature[feature.name], end_time, test_name=feature.name, context="Feature")

def before_scenario(context, scenario):
    start_time_scenario[scenario.name] = datetime.now()
    print(f"\n  [BEFORE SCENARIO] {scenario.name}")

def after_scenario(context, scenario):
    end_time = datetime.now()
    print(f"  [AFTER SCENARIO] {scenario.name}")
    generate_report(start_time_scenario[scenario.name], end_time, test_name=scenario.name, context="Scenario")