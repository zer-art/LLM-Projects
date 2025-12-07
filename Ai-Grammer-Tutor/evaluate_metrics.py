"""
Evaluation script for AI Grammar Tutor
Generates metrics for resume/portfolio documentation
"""

import time
import json
from datetime import datetime
from src.utils import GrammarChecker

# Test dataset with grammar errors and correct sentences
test_cases = [
    # Grammar errors
    {
        "input": "He go to school every day.",
        "has_error": True,
        "category": "Subject-verb agreement",
    },
    {
        "input": "She don't like pizza.",
        "has_error": True,
        "category": "Subject-verb agreement",
    },
    {
        "input": "I seen that movie yesterday.",
        "has_error": True,
        "category": "Verb tense",
    },
    {
        "input": "Their going to the park.",
        "has_error": True,
        "category": "Homophone confusion",
    },
    {
        "input": "Me and him went to the store.",
        "has_error": True,
        "category": "Pronoun case",
    },
    {
        "input": "The dog wagged it's tail.",
        "has_error": True,
        "category": "Apostrophe misuse",
    },
    {
        "input": "I could of helped you.",
        "has_error": True,
        "category": "Modal verb error",
    },
    {
        "input": "Between you and I, this is wrong.",
        "has_error": True,
        "category": "Pronoun case",
    },
    {
        "input": "There is three apples on the table.",
        "has_error": True,
        "category": "Subject-verb agreement",
    },
    {
        "input": "Your the best friend ever.",
        "has_error": True,
        "category": "Homophone confusion",
    },
    # Correct sentences
    {
        "input": "She goes to school every day.",
        "has_error": False,
        "category": "Correct",
    },
    {"input": "They are going to the park.", "has_error": False, "category": "Correct"},
    {
        "input": "I have seen that movie before.",
        "has_error": False,
        "category": "Correct",
    },
    {
        "input": "The weather is beautiful today.",
        "has_error": False,
        "category": "Correct",
    },
    {
        "input": "We should have studied more.",
        "has_error": False,
        "category": "Correct",
    },
]


def evaluate_correction_detection(response, has_error):
    """Check if the model correctly identifies errors or correct sentences"""
    response_lower = response.lower()

    # Keywords indicating error detection
    error_indicators = [
        "incorrect",
        "mistake",
        "error",
        "should be",
        "correct version",
        "grammar rule",
        "corrected",
        "wrong",
        "fix",
    ]

    # Keywords indicating correct sentence recognition
    correct_indicators = [
        "correct",
        "great job",
        "well done",
        "perfect",
        "no mistakes",
        "good",
        "excellent",
        "right",
    ]

    if has_error:
        # Should detect error
        return any(indicator in response_lower for indicator in error_indicators)
    else:
        # Should recognize correctness
        return any(indicator in response_lower for indicator in correct_indicators)


def measure_response_time(text):
    """Measure API response time"""
    start_time = time.time()
    checker = GrammarChecker(text)
    result = checker.check_grammar()
    end_time = time.time()
    return end_time - start_time, result


def evaluate_response_quality(response):
    """Score response quality based on structure and completeness"""
    score = 0
    response_lower = response.lower()

    # Check for explanation (+25 points)
    if any(word in response_lower for word in ["because", "rule", "should", "reason"]):
        score += 25

    # Check for examples (+25 points)
    if "example" in response_lower or ":" in response:
        score += 25

    # Check for correction provided (+25 points)
    if any(
        word in response_lower for word in ["correct version", "should be", "change to"]
    ):
        score += 25

    # Check for encouragement (+25 points)
    if any(
        word in response_lower
        for word in ["good", "great", "well done", "keep", "practice"]
    ):
        score += 25

    return score


def run_evaluation():
    """Run full evaluation and generate metrics"""
    print("=" * 60)
    print("AI Grammar Tutor - Metrics Evaluation")
    print("=" * 60)

    results = {
        "timestamp": datetime.now().isoformat(),
        "total_tests": len(test_cases),
        "correct_detections": 0,
        "response_times": [],
        "quality_scores": [],
        "category_accuracy": {},
        "test_details": [],
    }

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}/{len(test_cases)}: {test['category']}")
        print(f"Input: {test['input'][:50]}...")

        # Measure response time and get result
        response_time, response = measure_response_time(test["input"])
        results["response_times"].append(response_time)

        # Evaluate detection accuracy
        is_correct = evaluate_correction_detection(response, test["has_error"])
        if is_correct:
            results["correct_detections"] += 1

        # Evaluate response quality
        quality_score = evaluate_response_quality(response)
        results["quality_scores"].append(quality_score)

        # Track by category
        category = test["category"]
        if category not in results["category_accuracy"]:
            results["category_accuracy"][category] = {"total": 0, "correct": 0}
        results["category_accuracy"][category]["total"] += 1
        if is_correct:
            results["category_accuracy"][category]["correct"] += 1

        # Store details
        results["test_details"].append(
            {
                "input": test["input"],
                "category": category,
                "has_error": test["has_error"],
                "detected_correctly": is_correct,
                "response_time": response_time,
                "quality_score": quality_score,
                "response_preview": response[:200] + "...",
            }
        )

        print(f"✓ Detection: {'Correct' if is_correct else 'Incorrect'}")
        print(f"✓ Response time: {response_time:.2f}s")
        print(f"✓ Quality score: {quality_score}/100")

    # Calculate summary metrics
    accuracy = (results["correct_detections"] / results["total_tests"]) * 100
    avg_response_time = sum(results["response_times"]) / len(results["response_times"])
    avg_quality = sum(results["quality_scores"]) / len(results["quality_scores"])

    # Category-wise accuracy
    category_stats = {}
    for cat, stats in results["category_accuracy"].items():
        category_stats[cat] = (stats["correct"] / stats["total"]) * 100

    # Print summary
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    print(f"Overall Accuracy: {accuracy:.1f}%")
    print(f"Average Response Time: {avg_response_time:.2f}s")
    print(f"Average Quality Score: {avg_quality:.1f}/100")
    print(f"\nCategory-wise Accuracy:")
    for cat, acc in category_stats.items():
        print(f"  - {cat}: {acc:.1f}%")

    # Save results
    results["summary"] = {
        "accuracy": accuracy,
        "avg_response_time": avg_response_time,
        "avg_quality_score": avg_quality,
        "category_accuracy": category_stats,
    }

    with open("evaluation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Results saved to evaluation_results.json")

    return results


if __name__ == "__main__":
    try:
        results = run_evaluation()
        print("\n✓ Evaluation completed successfully!")
    except Exception as e:
        print(f"\n✗ Error during evaluation: {str(e)}")
        raise
