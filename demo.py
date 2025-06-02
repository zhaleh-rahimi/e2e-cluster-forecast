# demo.py
import subprocess

examples = [
    ('regression', 'synthetic'),
    ('xgboost', 'synthetic'),
    ('lstm', 'synthetic'),
    ('cluster_forecast', 'synthetic')
]

for model, data in examples:
    print(f"\n--- Running model: {model} on {data} data ---")
    subprocess.run(['python', 'main.py', '--model', model, '--data', data])
