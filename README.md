# North Yorkshire Crime & Policing Dashboard

This project analyses North Yorkshire street crime, outcomes, and stop-search activity from July 2024 to February 2026.

## Dashboard

The Power BI dashboard contains three pages:

- Overview
- Street Crime & Outcomes
- Stop Search

## Data

The raw data is stored in: data/raw/

Cleaned outputs are stored in: data/cleaned/

## Data Cleaning
The cleaning pipeline:

standardises column names
converts date fields
flags missing crime IDs and locations
deduplicates street crime records using crime_id where available
keeps ASB records without crime_id because they may represent separate incidents
deduplicates outcomes by crime_id, month, and outcome_type
keeps stop-search rows because there is no stable public event ID
creates a latest_outcomes.csv table for Power BI

ASB records are included in street crime totals but excluded from outcome matching because they do not have Crime IDs.

## Power BI Model
The dashboard uses separate tables for:

street
outcomes
latest_outcomes
search
crime_ids
Date
This avoids inflating crime counts when one crime has multiple outcome records.

The Power BI dashboard analyses North Yorkshire crime and policing activity from July 2024 to February 2026.

It includes three pages: an overview of crime trends and hotspots, a street crime and outcomes page, and a stop-search analysis page. The report tracks total crime, recorded crime, ASB incidents, latest outcomes, suspect charged rates, stop-search activity, arrests, and positive search outcomes.

## Run the Pipeline
python3 main.py
Outputs
The main cleaned files are:

street.csv
outcomes.csv
latest_outcomes.csv
search.csv