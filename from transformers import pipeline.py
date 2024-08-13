from transformers import pipeline

classifier = pipeline("sentiment-analysis")

results = classifier(["What the fuck!"])
for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")