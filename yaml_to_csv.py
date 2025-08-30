#!/usr/bin/env python3
"""
Convert YAML files in yaml_v1/ directory to CSV format based on the schema.
"""

import yaml
import csv
import os
from pathlib import Path
import sys

def extract_yaml_data(yaml_path):
    """Extract relevant data from a single YAML file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data:
        return None
    
    # Extract metadata
    metadata = data.get('metadata', {})
    
    # Extract problem statement
    problem = data.get('problem_statement', {})
    
    # Extract methodology
    methodology = data.get('methodology', {})
    
    # Extract evaluation
    evaluation = data.get('evaluation', {})
    
    # Extract results analysis
    results = data.get('results_analysis', {})
    
    # Extract contributions
    contributions = data.get('contributions', {})
    
    # Process lists for CSV format
    def list_to_str(lst):
        if lst and isinstance(lst, list):
            return ' | '.join([str(item) for item in lst])
        return ''
    
    # Process tasks (take first task if multiple)
    tasks = data.get('tasks', [])
    task_name = ''
    task_overview = ''
    if tasks and len(tasks) > 0:
        first_task = tasks[0]
        task_name = first_task.get('task_name', '')
        task_overview = first_task.get('task_overview', '')
    
    # Process datasets (combine all dataset names)
    datasets = data.get('datasets', [])
    dataset_names = []
    for ds in datasets:
        if 'dataset_name' in ds:
            dataset_names.append(ds['dataset_name'])
    
    # Extract narrative understanding aspects
    narrative_aspects = list_to_str(data.get('narrative_understanding_aspects', []))
    
    # Extract keywords
    keywords = list_to_str(data.get('keywords', []))
    
    row = {
        'filename': os.path.basename(yaml_path),
        'title': metadata.get('title', ''),
        'authors': list_to_str(metadata.get('authors', [])),
        'year': metadata.get('year', ''),
        'venue': metadata.get('venue', ''),
        'paper_url': metadata.get('paper_url', ''),
        'background': problem.get('background', ''),
        'gap_or_challenge': problem.get('gap_or_challenge', ''),
        'research_objective': problem.get('research_objective', ''),
        'significance': problem.get('significance', ''),
        'task_name': task_name,
        'task_overview': task_overview,
        'method_name': methodology.get('method_name', ''),
        'approach_type': methodology.get('approach_type', ''),
        'core_technique': methodology.get('core_technique', ''),
        'base_models': list_to_str(methodology.get('base_models', [])),
        'key_innovations': list_to_str(methodology.get('key_innovations', [])),
        'datasets': list_to_str(dataset_names),
        'evaluation_strategy': evaluation.get('evaluation_strategy', ''),
        'main_results': evaluation.get('main_results', ''),
        'metrics_used': list_to_str(evaluation.get('metrics_used', [])),
        'key_findings': list_to_str(results.get('key_findings', [])),
        'ablation_summary': results.get('ablation_summary', ''),
        'main_contributions': list_to_str(contributions.get('main_contributions', [])),
        'limitations': list_to_str(contributions.get('limitations', [])),
        'narrative_understanding_aspects': narrative_aspects,
        'keywords': keywords,
        'notes': data.get('notes', '')
    }
    
    return row

def main():
    # Set up paths
    yaml_dir = Path('yaml_v1')
    output_csv = 'papers_summary.csv'
    
    if not yaml_dir.exists():
        print(f"Error: Directory {yaml_dir} does not exist")
        sys.exit(1)
    
    # Get all YAML files (excluding the schema file)
    yaml_files = sorted([f for f in yaml_dir.glob('*.yaml') 
                         if f.name != 'summarization_scheme_v1.yaml'])
    
    if not yaml_files:
        print("No YAML files found to process")
        sys.exit(1)
    
    print(f"Found {len(yaml_files)} YAML files to process")
    
    # Process all YAML files
    all_rows = []
    for yaml_file in yaml_files:
        print(f"Processing: {yaml_file.name}")
        try:
            row = extract_yaml_data(yaml_file)
            if row:
                all_rows.append(row)
        except Exception as e:
            print(f"  Error processing {yaml_file.name}: {e}")
            continue
    
    if not all_rows:
        print("No data extracted from YAML files")
        sys.exit(1)
    
    # Write to CSV
    print(f"\nWriting {len(all_rows)} entries to {output_csv}")
    
    # Define fieldnames (order of columns)
    fieldnames = [
        'filename', 'title', 'authors', 'year', 'venue', 'paper_url',
        'background', 'gap_or_challenge', 'research_objective', 'significance',
        'task_name', 'task_overview', 'method_name', 'approach_type',
        'core_technique', 'base_models', 'key_innovations', 'datasets',
        'evaluation_strategy', 'main_results', 'metrics_used',
        'key_findings', 'ablation_summary', 'main_contributions', 'limitations',
        'narrative_understanding_aspects', 'keywords', 'notes'
    ]
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print(f"Successfully created {output_csv}")
    print(f"Total papers processed: {len(all_rows)}")

if __name__ == '__main__':
    main()