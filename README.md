# QB Pressure Analysis

This is a script that calculates the most pressurized quarterbacks over the past 5 years based on PFF premium data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Description: This Python script computes the most pressurized quarterbacks over the past five years utilizing PFF (Pro Football Focus) premium data. The script employs specific PFF metrics related to quarterback protection versus pressure to make the determination.

The script generates a .txt file to store the list of the most pressurized quarterbacks identified through the analysis. It serves as a valuable tool for analyzing quarterback performance under pressure and provides insights into their ability to handle challenging game situations.
## Features

- Utilizes PFF premium data for in-depth quarterback analysis.
- Utilized pandas library for data analysis
- Calculates quarterback pressure metrics over a five-year period for comprehensive insights.
- Filtered atleast 20% percent of the most thrown attempts (QB needs to throw the ball more than 20% of the most attempts)
- Outputs results to a .txt file for easy reference and analysis.
- Allows fans to analyze the best and worst pass protecting teams in the NFL
- Provides valuable information for football enthusiasts, analysts, and professionals interested in team protection performance metrics.

## Installation

Provide instructions on how to install and set up the project locally.

```bash
# Clone the repository
git clone https://github.com/chukse/QB-Pressure-Analysis.git

# Navigate to the project directory
cd QB-Pressure-Analysis

# Install dependencies (if needed)
pip install pandas
pip install os-sys
