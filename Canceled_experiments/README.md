# Monthly Experiment Churn Rate Calculation

## Overview

This SQL script calculates the **monthly churn rate** of experiments, defined as the ratio of canceled experiments to active experiments within a given month. The output provides churn rates for January, February, and March 2024.

## Assumptions

The query assumes the existence of an `experiments` table with at least the following columns:
- `id`: Unique identifier for each experiment.
- `experiment_start`: Start date of the experiment.
- `experiment_end`: End date of the experiment (nullable if the experiment is ongoing).

## Logic and Steps

The query consists of multiple Common Table Expressions (CTEs) to structure the logic in a readable and maintainable way:

### 1. `months`
Defines the first and last day of each target month:
- January 2024
- February 2024
- March 2024

### 2. `cross_join`
Creates a Cartesian product between each experiment and each of the target months. This allows evaluating each experiment in the context of each month.

### 3. `status`
Determines whether an experiment was:
- **Active** during the month (`is_active = 1`) — if it started before the month and did not end before the month started.
- **Canceled** during the month (`is_canceled = 1`) — if it ended within the current month.

### 4. `status_aggregate`
Aggregates the number of active and canceled experiments for each month.

### 5. Final SELECT
Calculates the churn rate as:

